
def enviar_mensaje(contacto, mensaje):
    if contacto == "" or mensaje == None:  # Error: `mensaje == None` no es la forma ideal de verificar strings vacíos
        print("Contacto o mensaje inválido")
        return False
    
    print(f"Enviando mensaje a {contacto}: {mensaje}")
    enviar = send_message(contacto, mensaje)  # Error: La función `send_message` no existe
    if enviar:
        print("Mensaje enviado con éxito")
    else:
        print("Error al enviar el mensaje")
