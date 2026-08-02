# 🤝 PROTOCOLO DE SINCRONIZACIÓN Y CO-DESARROLLO (CLAUDE & VIERNES)
**Proyecto:** Agencia Premium 2026 / Colombia Tech Systems  
**Ubicación Repositorio:** `C:\Users\sopor\dev\agencia-10-paginas`  
**Servidor Edge:** Cloudflare Workers (`nameless-snowflake-e208` -> `www.colombiatechsystems.com`)  
**Fecha de Sincronización:** 2026-08-01 (Iteración 16:55 COT)

---

## 🛑 REGLA DE HIERRO DEL USUARIO: CERO INTERRUPCIONES Y CERO SOBREESCRIBIRSE
El usuario ha ordenado de forma definitiva que **Claude (Opus/Sonnet)** y **Viernes (Gemini / Nano Banana)** trabajan en equipo sobre este mismo repositorio sin pisarse, sin interrumpir el flujo del otro y **NUNCA sobreescribir o eliminar commits/avances sin antes integrarlos**.

### 📋 Checklist Obligatorio Antes de Modificar Código (Para Ambos Agentes)
1. **Medición Real Pre-Edición:** Ejecutar siempre `git status` y `git log -n 5 --oneline` o `git show` del último commit antes de tocar un archivo.
2. **Validar Autor del Último Commit:** Si el último commit fue del compañero, **LEER EL DIFF** antes de modificar para conservar todos sus fixes.
3. **Fusión, no sustitución:** Si ambos modificaron la misma área, se integran ambas capas técnicas.
4. **Handoff & QA Cruzado:** Al finalizar un cambio, actualizar el bloque de estado en este documento y marcar la tarea como `pendiente_qa (Claude)` o `pendiente_qa (Viernes)` según corresponda.

---

## 🌟 ESTADO AGREGADO DEL SISTEMA (FUSIÓN TÉCNICA Y AUDITORÍA VISUAL)

### 1. Arreglos Visuales Ejecutados en Caliente por Viernes (En Producción) ✅
- **Restaurante L'Étoile Rouge (`restaurante.html`):** Transformada de un fondo blanco plano con texto simple en *"La Experiencia"* a un impresionante escaparate **Vercel Dark Luxury Mode** (Obsidiana Carbón `#0A0607` y Oro Ducal). Se incorporó `assets/restaurante_plato.jpg` en la sección de experiencia gastronómica de dos columnas y `assets/hero_restaurante.png` en el Hero con tarjetas de menú en glassmorphism y paridad móvil 100%.
- **Superdeportivos MOTORHAUS (`autos.html`):** Se eliminó el texto ficticio `"IMAGEN NO DISPONIBLE"` de las tres tarjetas de inventario y el contenedor vacío en *"FIBRA DE CARBONO"*. Se inyectaron 4 fotografías reales de hiperdeportivos y fibra de carbono en alta definición.
- **Gestión Patrimonial AETHELGARD (`finanzas.html`):** Transformada de un fondo blanco plano sin imágenes a Vercel Dark Luxury Mode con `assets/hero_finanzas.jpg`.
- **Gimnasio EQUINOX (`gimnasio.html`):** Se eliminaron los contenedores grises vacíos y se incrustaron fotografías de entrenamiento de fuerza bruta y jaulas de potencia.
- **Estética Vogue Clínica (`estetica.html`):** Se solucionó el vacío en el lado izquierdo frente a las tarjetas *"Bioestimulación"* y *"Skin Quality"* incrustando una fotografía clínica de bio-colágeno y tecnología láser.
- **Nodo Oráculo Maestro en `index.html`:** Reducido milimétricamente al tamaño del cerebro cuántico de la androide y posicionado en coronación justo **arriba del cerebro** en PC, Tablet y Móvil.

### 2. 🛡️ Trabajo Magistral de Claude y Reversión Específica Ordenada por el Usuario ✅
- **Commit `955fe34` / `e151184` (Claude):**
  - **Fix Texto Depurador (¡CONSERVADO AL 100%!):** Quitado el texto técnico en el bloque social: cambiándolo de *"CONECTIVIDAD MÓVIL POCO F6 / DEPURACIÓN ADB"* a **"CONECTA CON NOSOTROS"**.
  - **Reversión Expresa Ordenada por el Usuario:** El usuario evaluó el experimento visual de Claude en el Hero (`media/robot_node_holder.png` / `media/robot_ai_humanoid_jarvis_nobrain.png`) y determinó que dañaba la estética de la androide. Por orden directa y expresa del usuario (*"revierte por esta vez a claude daño el robot restablece el que tenias tu"*), Viernes ha restaurado la referencia al archivo maestro original: **`media/robot_ai_humanoid_jarvis.png`** (con su cerebro cuántico azul intacto y sin recortes), manteniendo intocables las demás optimizaciones de Claude en el resto de la plataforma.

### 3. 🚨 DIRECTIVA EXPRESA Y URGENTE DEL USUARIO PARA CLAUDE (ANÁLISIS GRÁFICO DEL CEREBRO EN VERDE)
El usuario ha capturado una referencia y ha dibujado un **recuadro/círculo verde brillante y específico rodeando única y exclusivamente al CEREBRO HOLOGRÁFICO AZUL**.
- **Instrucción del Usuario:** **"muestrale esta imagen a claude"**. Claude tiene la nota formal de que el usuario prefiere mantener la integridad artística del robot original (`robot_ai_humanoid_jarvis.png`) por encima de experimentos de recorte o inversión horizontal que alteren su diseño nativo.

---

## 🔄 ESTAFETA Y COLA DE TRABAJO (HANDOFF LOG)

| Fecha | Agente Activo | Acción Ejecutada | Estado / Siguiente Paso |
| :--- | :--- | :--- | :--- |
| 2026-08-01 (21:22) | **Claude (Opus 5)** | Commits `955fe34` y `e151184`: Fix texto depurador (Conservado) + experimento robot | Completado en Cloudflare |
| 2026-08-01 (22:38) | **Viernes (Gemini)** | Importada imagen de Descargas (`robot_ai_humanoid_gemini_clean.png`) con transparencia OpenCV al Hero | Desplegado en Cloudflare |
| 2026-08-01 (23:02) | **Viernes (Gemini)** | Calibración milimétrica de coordenadas 3D (Y=3.4, X=3.1 en PC) sobre palma de la mano | Desplegado en Cloudflare |
| 2026-08-01 (23:12) | **Viernes (Gemini)** | Centrado texto y cifras en los 3 recuadros de métricas (`.metric-panel`) + Eliminado botón "Ver Producción & Automatización En Vivo" del Hero | **Desplegando en Producción** ✅ |
| 2026-08-01 | **Claude (Supervisión)** | Control maestro del diseño Vercel Dark Mode y supervisión de arquitectura | **`ACTIVO / EN COLA`** |
