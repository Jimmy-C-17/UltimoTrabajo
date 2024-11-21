
# Eliminar el módulo inexistente
def iniciar_sesion(usuario, contraseña):
    # Verificar si los parámetros son válidos
    if not usuario or not contraseña:
        print("Usuario o contraseña no pueden estar vacíos.")
        return False

    # Autenticación básica
    if usuario == "admin" and contraseña == "12345":
        print("Inicio de sesión exitoso!")
        return True  # Devolver un indicador de éxito
    else:
        print("Usuario o contraseña incorrectos.")
        return False
