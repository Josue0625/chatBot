from flask import Blueprint, render_template, url_for, redirect, request,jsonify,flash,current_app
from .firebase_service import guardar_cita
from .firebase_service import guardar_service
from .firebase_service import initialize_firestore
db = initialize_firestore()
service_api_bp = Blueprint("service_api_bp", __name__, template_folder="templates", static_folder="static")

#Se crea el API para agregar una cita
@service_api_bp.route('/api/citas', methods=['POST'])
def crear_cita():
    datos_cita = request.get_json()
    nombre = datos_cita['nombre']
    documento_identidad = datos_cita['documento_identidad']
    num_celular = datos_cita['num_celular']
    email = datos_cita['email']
    servicio_cita = datos_cita['servicio_cita']
    eps_remitente = datos_cita['eps_remitente']
    estado = "Activo"
    
    id_cita = guardar_cita(nombre, documento_identidad, num_celular, email, servicio_cita, eps_remitente, estado)

    return {'mensaje': 'Cita creada correctamente', 'id_cita': id_cita}

#Se crea el API para agregar un servicio
@service_api_bp.route('/api/services', methods=['POST'])
def crear_service():
    datos_service = request.get_json()
    nombre_service = datos_service['nombre_service']
    horas_disponible = datos_service['horas_disponibles']
    
    
    id_service = guardar_service(nombre_service, horas_disponible)

    return {'mensaje': 'Servicio creado correctamente', 'id_service': id_service}


@service_api_bp.route('/api/consulta_cita/<documento_identidad2>/<serivicio_cita2>', methods=['GET'])
def obtener_citas_por_cedula(documento_identidad, service):
    # Obtener las citas asociadas al número de documento_identidad desde la Realtime Database
    citas_ref = db.reference('citas')
    citas_query = citas_ref.get()
    for key, value in citas_query.items():
        if value['documento_identidad'] == documento_identidad and value['servicio_cita'] == service and value['estado']!="eliminado" :
            return jsonify({"message": "¡Usted tiene sus datos registrados para el agendamiento de una cita!"}), 200

    return jsonify({"message": "No se encontraron citas para el documento de identidad especificado."}), 404 
    
@service_api_bp.route('/api/cancelar_cita', methods=['POST'])
def cancelar_cita():
    data = request.json  # Obtener los datos del cuerpo de la solicitud POST

    if 'documento_identidad' in data and 'servicio_cita' in data:
        documento_identidad = data['documento_identidad']
        service = data['servicio_cita']

        # Obtener las citas asociadas al número de documento_identidad desde la Realtime Database
        citas_ref = db.reference('citas')
        citas_query = citas_ref.get()

        for key, value in citas_query.items():
            if value['documento_identidad'] == documento_identidad and value['servicio_cita'] == service and value['estado'] != "eliminado":
                citas_query[key]['estado'] = 'eliminado'
                citas_ref.set(citas_query)
                return jsonify({"message": "Cita eliminada con éxito."}), 200
            
        return jsonify({"message": "No se encontraron citas para el documento de identidad y servicio especificados, o la cita ya está eliminada."}), 404
    else:
        return jsonify({"message": "Debe proporcionar el documento de identidad y el servicio para cancelar la cita."}), 400