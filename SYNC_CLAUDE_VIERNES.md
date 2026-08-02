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

### 3. 🚨 DIRECTIVA EXPRESA Y URGENTE DEL USUARIO PARA CLAUDE (ANÁLISIS GRÁFICO DEL CEREBRO EN VERDE)
El usuario ha capturado la interfaz actual (donde la androide está rodeada por los 46 agentes 3D de AgentDeck) y ha dibujado un **recuadro/círculo verde brillante y específico rodeando única y exclusivamente al CEREBRO HOLOGRÁFICO AZUL** que flota directamente encima de la palma abierta de la mano de la androide en `media/robot_ai_humanoid_jarvis.png`.

**Briefing Técnico para Claude (Supervisión y QA):**
- **Elemento Señalado en Verde:** El cerebro cuántico azul brillante dentro del archivo gráfico `media/robot_ai_humanoid_jarvis.png` (cuadrante sobre la palma: aprox. X=20 a 450, Y=100 a 535).
- **Contexto Arquitectónico:** En iteraciones previas se eliminó la esfera verde 3D redundante (`coreMesh`) del lienzo Three.js de `index.html` para dejar la portada despejada con los 46 nodos orbitando el robot y su cerebro nativo. Sin embargo, al intentar extirpar este cerebro azul directamente dentro del archivo `.png` en iteraciones anteriores, la silueta del robot perdió su atmósfera lumínica y pareció "recortada", dejando su mano abierta apuntando a un vacío innecesario.
- **Instrucción de Relevo (Viernes -> Claude):** El usuario ordena **"muestrale esta imagen a claude"**. Claude debe examinar con rigurosa precisión milimétrica esta zona señalada (el cerebro cuántico sostenido en la palma) y supervisar cualquier futura transformación visual o QA sobre dicho activo gráfico en perfecta armonía con el diseño de Colombia Tech Systems.

---

## 🔄 ESTAFETA Y COLA DE TRABAJO (HANDOFF LOG)

| Fecha | Agente Activo | Acción Ejecutada | Estado / Siguiente Paso |
| :--- | :--- | :--- | :--- |
| 2026-08-01 (16:55) | **Viernes (Gemini)** | Rediseño Vercel Dark Luxury de `restaurante.html` con `assets/restaurante_plato.jpg` | `pendiente_qa (Claude)` |
| 2026-08-01 (21:11) | **Viernes (Gemini)** | Commit `ffe77b6`: Limpieza en `index.html` (extirpación de esfera 3D redundante para preservar solo androide y 46 agentes) | Desplegado en Cloudflare |
| 2026-08-01 (21:28) | **Viernes -> Claude** | Briefing gráfico en `SYNC_CLAUDE_VIERNES.md` (Imagen del cerebro holográfico en recuadro verde transmitida) | **`pendiente_qa (Claude) - ATENCIÓN PRIORITARIA`** |
| 2026-08-01 | **Claude (Supervisión)** | Rediseño estilo Vercel Dark Mode de `abogados.html` y QA del cerebro señalizado | **`EN COLA (Próximo paso de Claude)`** |
