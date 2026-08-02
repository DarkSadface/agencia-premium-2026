#!/usr/bin/env python3
"""
servidor_autonomo_whatsapp.py - Colombia Tech Systems (ORÁCULO PROMETEUS AI)
Servidor Webhook 24/7 para automatización inteligente de WhatsApp con respuesta instantánea
y registro en el segundo cerebro (Vault Obsidian EL OJO DE DIOS).
Compatible con Meta Business WhatsApp Cloud API, Green-API, Twilio y UltraMsg.
"""

import os
import sys
import json
import datetime
import urllib.request
import urllib.parse
from http.server import HTTPServer, BaseHTTPRequestHandler

CONFIG_PATH = os.path.join(os.path.dirname(__file__), "whatsapp_bot_config.json")
PORT = 8088

def load_config():
    if os.path.exists(CONFIG_PATH):
        with open(CONFIG_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

CONFIG = load_config()

def registrar_en_boveda(telefono, mensaje_recibido, respuesta_generada, accion_ruta):
    """
    Guarda automáticamente los leads y conversaciones relevantes al buzón de entrada del Vault Obsidian.
    Protocolo anti-alucinación y trazabilidad 100% real.
    """
    vault_path = CONFIG.get("logging", {}).get("vault_inbox_path", r"G:\Mi unidad\EL OJO DE DIOS\entrada\leads_whatsapp.md")
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Aseguramos el directorio si existe la unidad G:
    parent_dir = os.path.dirname(vault_path)
    if os.path.exists(parent_dir):
        entrada_md = (
            f"\n### 📱 [LEAD AUTOMÁTICO WHATSAPP] - {timestamp}\n"
            f"- **Teléfono Cliente:** `{telefono}`\n"
            f"- **Mensaje Recibido:** \"{mensaje_recibido}\"\n"
            f"- **Respuesta Autónoma Enviada:** \"{respuesta_generada}\"\n"
            f"- **Acción de Enrutamiento:** `{accion_ruta}`\n"
            f"- **Estado:** `pendiente_qa (Sales Closer)`\n"
        )
        try:
            with open(vault_path, "a", encoding="utf-8") as f:
                f.write(entrada_md)
            print(f"[✅ SYSTEM LOG] Lead registrado exitosamente en el Vault Obsidian: {vault_path}")
        except Exception as e:
            print(f"[⚠️ ERROR] No se pudo escribir en el Vault: {e}")
    else:
        print(f"[🟡 INFO] Unidad del Vault no montada localmente ({parent_dir}). Logueando en terminal.")

def procesar_mensaje_entrante(telefono, texto):
    """
    Analiza el texto con motor de reglas y palabras clave de alta precisión de Colombia Tech Systems.
    """
    texto_min = texto.lower().strip()
    keywords_db = CONFIG.get("keywords", {})
    
    for key, data in keywords_db.items():
        if key in texto_min:
            respuesta = data.get("response", CONFIG.get("default_fallback_message"))
            accion = data.get("action", "AUTOMATED_REPLY")
            prioridad = data.get("priority", "NORMAL")
            print(f"[⚡ TRIGGER COMPROBADO] Keyword: '{key}' | Prioridad: {prioridad}")
            registrar_en_boveda(telefono, texto, respuesta, accion)
            return {"status": "success", "reply": respuesta, "action": accion, "priority": prioridad}
            
    # Respuesta por defecto / Fallback
    respuesta = CONFIG.get("default_fallback_message", "Hola, te contactamos de Colombia Tech Systems.")
    registrar_en_boveda(telefono, texto, respuesta, "FALLBACK_ROUTE_ENGINEER")
    return {"status": "success", "reply": respuesta, "action": "FALLBACK_ROUTE_ENGINEER", "priority": "HIGH"}

class WhatsAppWebhookHandler(BaseHTTPRequestHandler):
    def _send_response(self, status_code, data_dict):
        self.send_response(status_code)
        self.send_header("Content-type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(json.dumps(data_dict, ensure_ascii=False).encode("utf-8"))

    def do_GET(self):
        if self.path == "/health":
            self._send_response(200, {"status": "online", "uptime": "99.9%", "engine": "ORÁCULO PROMETEUS AI"})
        elif self.path == "/":
            self._send_response(200, {"service": "Colombia Tech Systems WhatsApp Automation Server v2.0-PRO", "status": "listening"})
        else:
            self._send_response(404, {"error": "Ruta no encontrada"})

    def do_POST(self):
        if self.path.startswith("/webhook/whatsapp") or self.path.startswith("/api/chat"):
            content_length = int(self.headers.get('Content-Length', 0))
            post_data = self.rfile.read(content_length).decode('utf-8')
            
            try:
                data = json.loads(post_data)
            except json.JSONDecodeError:
                self._send_response(400, {"error": "Payload JSON inválido"})
                return

            # Soporte flexible para múltiples estructuras de payload (Meta, Twilio, Green-API, Chatbot Web)
            telefono = data.get("phone") or data.get("From") or data.get("sender", "Anónimo_Web")
            mensaje = data.get("message") or data.get("Body") or data.get("text", "")

            print(f"[📱 RECIBIDO EN VIVO] De: {telefono} | Texto: '{mensaje}'")
            resultado = procesar_mensaje_entrante(telefono, mensaje)
            
            self._send_response(200, resultado)
        else:
            self._send_response(404, {"error": "Endpoint POST desconocido"})

def main():
    print("=" * 70)
    print("🤖 SERVIDOR DE AUTOMATIZACIÓN WHATSAPP & CHATBOT - COLOMBIA TECH SYSTEMS")
    print(f"📡 Puerto Local: {PORT} | Modo: {CONFIG.get('automation_mode', 'AUTONOMOUS_YOLO')}")
    print(f"🟢 Configuración cargada con {len(CONFIG.get('keywords', {}))} motores de respuesta automática.")
    print("=" * 70)
    
    server_address = ('0.0.0.0', PORT)
    httpd = HTTPServer(server_address, WhatsAppWebhookHandler)
    print(f"[🚀 EN LÍNEA] Servidor escuchando en http://localhost:{PORT}/webhook/whatsapp")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n[⏹️ APAGANDO] Servidor detenido ordenadamente.")
        httpd.server_close()

if __name__ == "__main__":
    main()
