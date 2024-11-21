
import WhatsAppAPI  # Error: No existe un módulo llamado WhatsAppAPI

def iniciar_sesion(usuario, contraseña):
    if usuario == "admin" and contraseña == "12345":
        print("Inicio de sesión exitoso!")
    else:
        print("Error en el inicio de sesión")
        return False
