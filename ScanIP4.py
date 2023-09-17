import subprocess
import smtplib
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from tqdm import tqdm
from colorama import Fore, Style

# Lista de direcciones IP que deseas escanear
ips_a_escanear = ["192.168.1.1", "192.168.1.109", "10.0.0.1"]

# Función para realizar el ping
def ping(ip):
    try:
        # Ejecutar el comando ping
        subprocess.run(["ping", ip], check=True)
        return True  # Si el ping tiene éxito, devuelve True
    except subprocess.CalledProcessError:
        return False  # Si el ping falla, devuelve False

# Función para enviar un correo electrónico
def enviar_correo(ip):
    # Configuración del servidor SMTP
    servidor_smtp = "smtp.email.es"
    puerto_smtp = 465
    usuario = "usuario@usuario.es"
    contrasena = "password"

    # Crear el mensaje
    mensaje = MIMEMultipart()
    mensaje["From"] = usuario
    mensaje["To"] = "remitente@gmail.com"
    mensaje["Subject"] = "Tunel VPN caido no responde"

    cuerpo = f"La IP {ip} del tunel VPN no ha respondido después de 3 minutos."
    mensaje.attach(MIMEText(cuerpo, "plain"))

    # Conectar al servidor SMTP y enviar el correo
    try:
        servidor = smtplib.SMTP(servidor_smtp, puerto_smtp)
        servidor.starttls()
        servidor.login(usuario, contrasena)
        servidor.sendmail(usuario, "remitente@gmail.com", mensaje.as_string())
        servidor.quit()
        print(f"{Fore.GREEN}{ip} El túnel VPN está respondiendo.{Style.RESET_ALL}")  # Texto en verde
    except Exception as e:
        print(f"{Fore.RED}Error al enviar el correo electrónico: {str(e)}{Style.RESET_ALL}")  # Texto en rojo

# Bucle infinito
while True:
    for ip in tqdm(ips_a_escanear, bar_format="{l_bar}%s{bar}%s{r_bar}" % (Fore.BLUE, Fore.RESET)):
        tiempo_inicio = time.time()
        while True:
            if ping(ip):
                print(f"{Fore.GREEN}{ip} El túnel VPN está respondiendo.{Style.RESET_ALL}")  # Texto en verde
                break
            tiempo_transcurrido = time.time() - tiempo_inicio
            if tiempo_transcurrido >= 30:  # 3 minutos en segundos
                print(f"{Fore.RED}{ip} El túnel VPN no está respondiendo.{Style.RESET_ALL}")  # Texto en rojo
                enviar_correo(ip)
                break

    # Cuenta atrás de 5 minutos antes de comenzar de nuevo
    tiempo_restante = 150  # 150 segundos = 2.5 minutos
    while tiempo_restante > 0:
        print(f"Próxima ejecución en {tiempo_restante} segundos...", end="\r")
        time.sleep(1)
        tiempo_restante -= 1

    print("Iniciando nuevo ciclo...\n")
