import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

def initialize_firestore():
    cred = credentials.Certificate('firebase_credentials.json')
    firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://prueba-01-chatbot-default-rtdb.firebaseio.com'
    })
    return db

def guardar_cita(nombre, documento_identidad, num_celular, email, servicio_cita, eps_remitente, estado=None):
    ref = db.reference('/citas')

    nueva_cita_ref = ref.push()

    nueva_cita_ref.set({
        'nombre': nombre,
        'documento_identidad': documento_identidad,
        'num_celular': num_celular,
        'email': email,
        'servicio_cita': servicio_cita,
        'eps_remitente':eps_remitente,
        'estado':estado
    })

    return nueva_cita_ref.key


def guardar_service(nombre_service, horas_disponibles):
    ref = db.reference('/services')

    nuevo_service_ref = ref.push()

    nuevo_service_ref.set({
        'nombre_service': nombre_service,
        'horas_disponibles': horas_disponibles,
    })

    return nuevo_service_ref.key
