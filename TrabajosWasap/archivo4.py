
from archivo1 import iniciar_sesion
from archivo2 import conectar_whatsapp
from archivo3 import enviar_mensaje

usuario = input("Introduce tu usuario: ")
contraseña = input("Introduce tu contraseña: ")
iniciar_sesion(usuario)  # Error: La función `iniciar_sesion` requiere dos argumentos, pero solo se pasa uno

conexion = conectar_whatsapp()
if conexion:
    contacto = input("Introduce el número de contacto: ")
    mensaje = input("Introduce el mensaje a enviar: ")
    enviar_mensaje(contacto, mensaje)
