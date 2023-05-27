# auth.py : Programme d'authentification via Google Authenticator en tant que microservice
# --------------------------------------------------------
import pyotp, qrcode, pika

def creer_qr_code():
    cle = "YDDPCBFZKYDRVJL7UOFR5DAPTQHGKM64"

    uri = pyotp.totp.TOTP(cle).provisioning_uri(
        "mednaji@gmail.com",
        issuer_name="MicAuth")

    # Génération de code QR
    qrcode.make(uri).save("qr.png")

def microservice_auth():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='auth_demande')
    channel.queue_declare(queue='auth_reponse')

    def callback(ch, method, properties, code):
        print(" Le microservice authentification a reçu votre code OTP : %r"  %code)
        code = code.decode('utf-8')
        totp = pyotp.TOTP("K7R63JO2A4B6BJGIYUBGLWBAV3WHSBXQ")

        if totp.verify(code):
            print("Code : %r est Correcte" %code)
            channel.basic_publish(exchange='', routing_key='auth_reponse', body="oui")
        else:
            print("Code : %r est Incorrecte" %code)
            channel.basic_publish(exchange='', routing_key='auth_reponse', body="non")

    channel.basic_consume(queue='auth_demande', on_message_callback=callback, auto_ack=True)
    print(" [x] Microservice d'authentification prêt")
    channel.start_consuming()


if __name__ == '__main__':
    try:
        creer_qr_code()
        microservice_auth()
    except KeyboardInterrupt:
        print('Interrupted')
        quit()