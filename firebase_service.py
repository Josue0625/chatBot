import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Ruta al archivo de credenciales JSON descargado
cred = credentials.Certificate('firebase_credentials.json')

# Inicializar la aplicación de Firebase con las credenciales
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://prueba-01-chatbot-default-rtdb.firebaseio.com'
})

def guardar_cita(nombre, documento_identidad, hora, num_celular, email, servicio_cita, eps_remitente):
    ref = db.reference('/citas')

    nueva_cita_ref = ref.push()

    nueva_cita_ref.set({
        'hora': hora,
        'nombre': nombre,
        'documento_identidad': documento_identidad,
        'num_celular': num_celular,
        'email': email,
        'servicio_cita': servicio_cita,
        'eps_remitente':eps_remitente
    })

    return nueva_cita_ref.key
