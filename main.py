from flask import Flask, request
from firebase_service import guardar_cita

app = Flask(__name__)

@app.route('/api/citas', methods=['POST'])
def crear_cita():
    datos_cita = request.get_json()
    hora = datos_cita['hora']
    nombre = datos_cita['nombre']
    documento_identidad = datos_cita['documento_identidad']
    num_celular = datos_cita['num_celular']
    email = datos_cita['email']
    servicio_cita = datos_cita['servicio_cita']
    eps_remitente = datos_cita['eps_remitente']
    
    id_cita = guardar_cita(hora, nombre, documento_identidad, num_celular, email, servicio_cita, eps_remitente)

    return {'mensaje': 'Cita creada correctamente', 'id_cita': id_cita}

if __name__ == '__main__':
    app.run()
