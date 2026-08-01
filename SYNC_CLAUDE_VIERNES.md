# 🤝 PROTOCOLO DE SINCRONIZACIÓN Y CO-DESARROLLO (CLAUDE & VIERNES)
**Proyecto:** Agencia Premium 2026 / Colombia Tech Systems  
**Ubicación Repositorio:** `C:\Users\sopor\dev\agencia-10-paginas`  
**Servidor Edge:** Cloudflare Workers (`nameless-snowflake-e208` -> `www.colombiatechsystems.com`)  
**Fecha de Sincronización:** 2026-08-01 (Iteración JARVIS PC Neural & Plano Holográfico)

---

## 🛑 REGLA DE HIERRO DEL USUARIO: CERO INTERRUPCIONES Y CERO SOBREESCRIBIRSE
El usuario ha ordenado de forma definitiva que **Claude (Opus/Sonnet)** y **Viernes (Gemini / Nano Banana)** trabajan en equipo sobre este mismo repositorio sin pisarse, sin interrumpir el flujo del otro y **NUNCA sobreescribir o eliminar commits/avances sin antes integrarlos**.

### 📋 Checklist Obligatorio Antes de Modificar Código (Para Ambos Agentes)
1. **Medición Real Pre-Edición:** Ejecutar siempre `git status` y `git log -n 5 --oneline` o `git show` del último commit antes de tocar un archivo.
2. **Validar Autor del Último Commit:** Si el último commit fue del compañero (ej. Claude hizo `85abf7e`), **LEER EL DIFF** antes de modificar para conservar todos sus fixes.
3. **Fusión, no sustitución:** Si ambos modificaron la misma área (ej. el Showcase del Robot o HUD), se integran ambas capas técnicas.
4. **Handoff & QA Cruzado:** Al finalizar un cambio, actualizar el bloque de estado en este documento y marcar la tarea como `pendiente_qa (Claude)` o `pendiente_qa (Viernes)` según corresponda.

---

## 🌟 ESTADO AGREGADO DEL SISTEMA (FUSIÓN TÉCNICA Y ARQUITECTURA NEURONAL VERIFICADA)
En la iteración actual (2026-08-01 14:45), se ejecutaron y verificaron los siguientes avances en estricto cumplimiento del diseño JARVIS PC y las instrucciones del usuario:

### 1. Paridad Total de Diseño y Cohesión en PC, Tablet y Móvil ✅
- **Algoritmo de Alineación Cuántica (`alignNodeWithRobot`):** Se creó un sistema dinámico en Three.js que calcula el ancho de la pantalla y adapta la posición y escala de la constelación en tiempo real:
  - **PC / Escritorio (`>= 1100px`):** Posiciona el nodo central en `X=4.2, Y=1.8, Z=-0.5` con escala `1.0`, abrazando exactamente el cerebro y mano en el lado derecho del monitor.
  - **Tablet (`650px - 1100px`):** Traslación automática a `X=-0.6, Y=-0.2` con escala `0.85`, garantizando que al cambiar el layout a vista apilada, el nodo central siga encerrando exactamente el cerebro y mano del androide centrado en la base.
  - **Móvil / Poco F6 / Smartphones (`< 650px`):** Traslación a `X=-0.35, Y=-0.9` con escala `0.65`, adaptando perfectamente la esfera reticular a las proporciones de pantallas móviles sin saturar la vista.
- **Responsive Fluido con `clamp()`:** Todas las tipografías del HUD, botones, métricas y tarjetas de showroom B2B se escalan mediante funciones fluidas de CSS, eliminando desbordamientos de texto, márgenes indebidos o scroll horizontal en tablet y móvil.

### 2. Nodo Central Oráculo Maestro ENCERRANDO EL CEREBRO Y LA MANO DEL ROBOT ✅
- **Esfera de Dyson Neuronal (Radio 4.6, Detalle 3):** Envuelve, custodia y encierra completamente tanto el cerebro cuántico resplandeciente como la mano cibernética que lo soporta en los 3 formatos de dispositivo (PC, Tablet y Móvil), manteniendo una transparencia del 55% para una nitidez visual impecable de los elementos ocultos en el interior de la esfera.

### 3. Emblema 'JARVIS' en Brazo de Titanio (Cero Textos Invertidos o AETHER) ✅
- **Insignia Oficial Tono JARVIS:** El hexágono cian con núcleo esmeralda y el texto **JARVIS** relucen al derecho en la placa de titanio del hombro del androide (`media/robot_ai_humanoid_jarvis.png`), mostrándose con fidelidad 100% nativa sin transformaciones de espejo.

---

## 🔄 ESTAFETA Y COLA DE TRABAJO (HANDOFF LOG)

| Fecha | Agente Activo | Acción Ejecutada | Estado / Siguiente Paso |
| :--- | :--- | :--- | :--- |
| 2026-08-01 | **Claude Opus 5** | Commit `85abf7e`: Máscara radial, HUD global, fix 404 odontología | Completado en rama |
| 2026-08-01 | **Viernes (Gemini)** | Commit `2bf98ef`: Contorno desvanecido y Nodos Icosaedro Wireframe | Completado y verificado |
| 2026-08-01 | **Viernes (Gemini)** | Commit `9bcfb10`: Robot en borde derecho exacto + silueta PNG transparente | Completado y verificado |
| 2026-08-01 | **Viernes (Gemini)** | Commit `4a630dd`: Limpieza absoluta de texto (cero NOC, Fable 5, iniciar.bat) | Completado y verificado |
| 2026-08-01 | **Viernes (Gemini)** | Commit `9d21e90`: Emblema 'JARVIS' en hombro de titanio pre-rotado hacia la izquierda | Completado y verificado |
| 2026-08-01 (14:45) | **Viernes (Gemini)** | Paridad de diseño 100% verificada para PC, Tablet y Móvil (Poco F6 / ADB) con nodo encerrando mano y cerebro | `pendiente_qa (Claude)` |

> **Nota de Viernes para Claude:** *Colega, he implementado paridad total de diseño y alineación para **PC, Tablet y Móvil**. Antes, al reducir la pantalla, el robot bajaba al centro pero la constelación 3D se quedaba desalineada en el cielo del lienzo. Implementé la función `alignNodeWithRobot(w, h)` que ajusta matemáticamente la posición y escala de la esfera del Oráculo Maestro (`X, Y, scale`) en los breakpoints de PC, Tablet y Smartphone (incluyendo el Poco F6 del usuario). Así aseguramos que en **todos los dispositivos** la página se ve con idéntica elegancia y el nodo central **siempre queda encerrando exactamente el cerebro y la mano del robot**. Propagado en el Edge de Cloudflare y ramas de Git. Queda en `pendiente_qa (Claude)`.*
