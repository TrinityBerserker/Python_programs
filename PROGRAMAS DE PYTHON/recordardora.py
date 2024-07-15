import schedule
import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Configuración del correo electrónico
def send_email(subject, body):
    # Configura los detalles de tu servidor de correo electrónico
    from_email = 'tu_correo@gmail.com'
    from_password = 'tu_contraseña'
    to_email = 'destinatario@gmail.com'

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(from_email, from_password)
        text = msg.as_string()
        server.sendmail(from_email, to_email, text)
        server.quit()
        print("Email sent successfully")
    except Exception as e:
        print(f"Failed to send email: {str(e)}")

# Función para enviar recordatorio
def send_task_reminder():
    subject = "Recordatorio de Tarea"
    body = "Recuerda completar tus tareas!"
    send_email(subject, body)

# Programar el recordatorio para cada hora
schedule.every().hour.do(send_task_reminder)

# Bucle principal para ejecutar las tareas programadas
while True:
    schedule.run_pending()
    time.sleep(1)
