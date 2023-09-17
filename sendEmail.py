from email.message import EmailMessage
import smtplib

remitente = "remitente@hotmail.com"
destinatario = "destinatario@gmail.com"
mensaje = "¡Hola, mundo!"

email = EmailMessage()
email["From"] = remitente
email["To"] = destinatario
email["Subject"] = "Tunel VPN caido no responde"
email.set_content(mensaje)

smtp = smtplib.SMTP("smtp-mail.outlook.com", port=587)
smtp.starttls()
smtp.login(remitente, "password")
smtp.sendmail(remitente, destinatario, email.as_string())
smtp.quit()