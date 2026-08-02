# 🤖 Arquitectura & Configuración del Sistema de Chatbot IA + WhatsApp Automático
**Colombia Tech Systems — Oráculo Prometeus AI v2.0-PRO**

Este documento detalla la configuración integral desplegada para automatizar la captación de leads de alto valor y soporte técnico 24/7 mediante Chatbot web y WhatsApp oficial VIP (`+57 316 684 4315`).

---

## 🌐 1. Chatbot Web Interactivo (Vercel Dark Mode)
Integrado de forma nativa y sin dependencias externas en la portada principal (`index.html`), operando a velocidad máxima en el Edge:

- **Widget Flotante:** Ubicado en la esquina inferior derecha (`🤖 Asistente IA & WhatsApp`), con pulso de actividad verde neón indicando **99.9% Uptime**.
- **Flujo de Triage Automático:**
  1. **Saludo y Clasificación:** El bot recibe al prospecto y ofrece 4 ramas principales de atención (*Desarrollo Web Vercel*, *Agentes IA & Ecosistema Prometeus*, *Automatización WhatsApp*, *Consultoría NOC*).
  2. **Captura de Datos B2B:** Al elegir una rama, el sistema solicita de forma inteligente nombre, empresa y requerimiento breve.
  3. **Compilación y Enlace WhatsApp VIP:** Con la información recibida, el bot compila un paquete de datos formateado con etiquetas (ej. `⚡ [LEAD AUTOMÁTICO CHATBOT WEB]`) y genera el botón de enlace directo para abrir WhatsApp con todo precargado.

---

## ⚙️ 2. Servidor de Automatización & Webhooks (`whatsapp_automations_server.py`)
Un servidor ligero en Python diseñado para ejecutarse localmente, en Cloudflare o en servidores VPS para gestionar respuestas automáticas 24/7 sin alucinación.

### Componentes:
- **`whatsapp_bot_config.json`**: Base de conocimiento con reglas de palabras clave (*cotizar*, *agentes*, *web*, *soporte*, *taller*, *panaderia*), prioridades y mensajes automáticos.
- **Registro en el Segundo Cerebro:** Cada lead y consulta recibida por webhook o chat es logueada automáticamente en la bóveda de Obsidian del usuario:
  - **Ruta Oficial:** `G:\Mi unidad\EL OJO DE DIOS\entrada\leads_whatsapp.md`
  - **Etiqueta de Calidad:** `pendiente_qa (Sales Closer)` para seguimiento posterior.
- **Compatibilidad Multi-Proveedor:**
  - Meta WhatsApp Business Cloud API
  - Green-API / UltraMsg
  - Twilio Webhooks

### Cómo Ejecutar el Servidor Local / Respaldo:
Desde tu consola de Windows (con PowerShell o CMD):
```cmd
cmd /c "python C:\Users\sopor\dev\agencia-10-paginas\whatsapp_automations_server.py"
```
El servidor escuchará peticiones en el puerto `8088` (`http://localhost:8088/webhook/whatsapp`).

---

## 📊 3. Sincronización con Agentes Especialistas
- Los leads con palabra clave **"cotizar"** o **"web"** se enrutan al skill `sales-closer-b2b`.
- Las alertas de **"soporte"** o **"caída"** notifican con prioridad crítica al skill `incident-responder` y `network-engineer` del NOC Prometeus.

*Despliegue verificado y optimizado para producción continua.*
