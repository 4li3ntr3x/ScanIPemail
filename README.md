# ScanIPemail 🔍✉️

> Utilidad en Python para monitorear túneles VPN mediante ping y alertar por email cuando un host deja de responder.

## 📋 Descripción

Script en Python que monitorea continuamente una lista de direcciones IP. Si alguna no responde al ping dentro de un tiempo límite, envía una notificación por correo electrónico vía SMTP de Outlook.

Ideal para **administradores de redes y VPN** que necesitan saber al instante cuando un túnel o dispositivo cae.

## 🚀 Características

| Característica | Descripción |
|---|---|
| ✅ Monitoreo continuo | Bucle infinito con ciclos programados |
| ⏱️ Timeout configurable | Define cuánto esperar antes de alertar |
| 📧 Alerta por email | Notificaciones vía Outlook SMTP |
| 🏷️ Nombres amigables | Asocia IPs con nombres legibles (ScanIP8) |
| 🎨 Output coloreado | Feedback visual con `colorama` |
| 📊 Barra de progreso | Indicador visual con `tqdm` |

## 📁 Archivos

| Archivo | Descripción |
|---|---|
| `ScanIP8.py` ✅ | Versión completa con nombres amigables y 4 IPs |
| `ScanIP4.py` | Versión básica con 3 IPs (sin nombres) |
| `sendEmail.py` | Módulo simple de envío de email |

## ⚙️ Cómo funciona

```
                    ┌─────────────┐
                    │  Lista de   │
                    │    IPs      │
                    └──────┬──────┘
                           │
                           ▼
                    ┌─────────────┐
                    │   Ping a    │
                    │   cada IP   │
                    └──────┬──────┘
                           │
               ┌───────────┴───────────┐
               ▼                       ▼
        ┌─────────────┐       ┌─────────────┐
        │  Responde   │       │ No responde │
        │   (OK) ✅   │       │  (Timeout)  │
        └──────┬──────┘       └──────┬──────┘
               │                     │
               │                     ▼
               │            ┌─────────────┐
               │            │  Enviar     │
               │            │  email      │
               │            └──────┬──────┘
               │                     │
               └──────┬──────────────┘
                      ▼
             ┌──────────────┐
             │  Esperar 2.5 │
             │  min y repetir│
             └──────────────┘
```

## 🔧 Requisitos

```bash
pip install tqdm colorama
```

## 🚦 Uso

```bash
python ScanIP8.py
```

### Personalizar IPs

Editar las listas en el script:

```python
ips_a_escanear = ["192.168.1.1", "192.168.1.109", "10.0.0.1", "192.168.1.80"]

ips_nombres_amigables = {
    "192.168.1.1": "Router Principal",
    "192.168.1.109": "Portatil",
    "10.0.0.1": "Otro Dispositivo",
    "192.168.1.80": "Movil"
}
```

### Configurar alertas email

```python
remitente = "tu_correo@hotmail.com"
destinatario = "alerta@tudominio.com"
contrasena = "tu_contraseña"
```

> ⚠️ Usar variables de entorno o un archivo `.env` para no exponer credenciales.

## ⏱️ Timing

| Parámetro | ScanIP4 | ScanIP8 |
|---|---|---|
| Timeout por IP | ~30 seg | ~30 seg |
| Espera entre ciclos | ~2.5 min | ~2.5 min |

## 📸 Ejemplo de salida

```
⠋ Escaneando: 100%|████████████████████|
✅ Router Principal (192.168.1.1) El túnel VPN está respondiendo.
✅ Portatil (192.168.1.109) El túnel VPN está respondiendo.
❌ Otro Dispositivo (10.0.0.1) El túnel VPN no está respondiendo.
📧 Correo electrónico enviado para la IP 10.0.0.1.
✅ Movil (192.168.1.80) El túnel VPN está respondiendo.
⏳ Próxima ejecución en 150 segundos...
```

## 📌 Pendientes / Mejoras

- [ ] Mover credenciales a variables de entorno
- [ ] Soporte para múltiples destinatarios
- [ ] Logging a archivo
- [ ] Configuración vía archivo YAML/JSON
- [ ] Notificaciones vía Telegram/Discord además de email
- [ ] Dockerizar

---

<p align="center">
  <sub>Hecho por <a href="https://github.com/4li3ntr3x">4li3ntr3x</a></sub>
</p>
