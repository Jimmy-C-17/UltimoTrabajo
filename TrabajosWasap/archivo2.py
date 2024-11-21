
def conectar_whatsapp():
    conexion = open_connection()  # Error: La función `open_connection` no está definida
    if conexion:
        print("Conexión exitosa a WhatsApp")
    else:
        print("No se pudo conectar a WhatsApp")
    return conexion
