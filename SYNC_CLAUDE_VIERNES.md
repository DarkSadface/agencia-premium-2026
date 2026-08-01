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
2. **Validar Autor del Último Commit:** Si el último commit fue del compañero (ej. Claude hizo `85abf7e`), **LEER EL DIFF** antes de modificar para conservar todos sus fixes (ej. bugs resueltos, mejoras de accesibilidad o estilos).
3. **Fusión, no sustitución:** Si ambos modificaron la misma área (ej. el Showcase del Robot o HUD), se integran ambas capas técnicas.
4. **Handoff & QA Cruzado:** Al finalizar un cambio, actualizar el bloque de estado en este documento y marcar la tarea como `pendiente_qa (Claude)` o `pendiente_qa (Viernes)` según corresponda.

---

## 🌟 ESTADO AGREGADO DEL SISTEMA (FUSIÓN TÉCNICA Y MEJORA NEURONAL VERIFICADA)
En la iteración actual (2026-08-01 13:21), se ejecutaron y verificaron los siguientes avances en estricto cumplimiento del diseño JARVIS PC:

### 1. Alineación Total al Flanco Derecho (Recuadro Verde del Usuario) ✅
- **Desplazamiento del Universo AgentDeck 3D (`constellationGroup`):** Se agrupó el núcleo central, los anillos de energía y los 46 agentes en `constellationGroup.position.x = 8.2`. Esto mueve toda la red neuronal interactiva **hacia la mitad derecha de la pantalla**, despejando el lado izquierdo para que el título gigante "COLOMBIA TECH SYSTEMS" brille con legibilidad absoluta y sin obstrucciones 3D de fondo.
- **Coexistencia Holográfica con el Robot:** El androide (`max-width: 680px`) habita en la misma zona del recuadro derecho junto al Oráculo Maestro, logrando una ilusión de que la red sináptica emerge directamente de la palma y el cerebro neuronal de la IA.

### 2. Robot en el Mismo Plano que AgentDeck 3D & Mirada Invertida ✅
- **Orientación Corregida:** Aplicado `transform: scaleX(-1)` para que el robot mire de izquierda a derecha en dirección hacia el centro y los títulos principales.
- **Desvanecimiento Total del Contorno (Fusión Holográfica):** Combinado `mix-blend-mode: screen;` con una **máscara radial multi-parada suave** (`radial-gradient(circle at 48% 50%, #000 30%, rgba(0,0,0,0.7) 55%, rgba(0,0,0,0.2) 76%, transparent 88%)`). Todos los píxeles oscuros y bordes desaparecen por completo.
- **Píldora HUD Flotante:** La placa de estado reposa flotando en el perímetro inferior como un elemento HUD sin cortar la imagen.

### 3. Nodos con la Exacta Misma Forma que el Nodo Central (Icosaedro Wireframe) ✅
- Todos los 46 nodos de los agentes en el motor Three.js pasaron de ser esferas simples a **Icosaedros Wireframe rotativos** (`IcosahedronGeometry(0.58, 2)` con `wireframe: true`), exactamente la misma forma geométrica del Núcleo Oráculo Maestro.

### 4. Animación Viva de Red Neuronal Estilo JARVIS PC ✅
- **Oscilación Biológica / Neuronal Individual:** Cada agente tiene su propia velocidad, fase y trayectoria senoidal 3D en lugar de rotar rígidamente en círculo.
- **Preservación de Fixes de Claude:** Conservado 100% el fix de 404 en el portafolio de Odontología (`assets/hero_odontologia.png`), las scanlines globales `body::after` y la accesibilidad `@media (prefers-reduced-motion: reduce)`.

---

## 🔄 ESTAFETA Y COLA DE TRABAJO (HANDOFF LOG)

| Fecha | Agente Activo | Acción Ejecutada | Estado / Siguiente Paso |
| :--- | :--- | :--- | :--- |
| 2026-08-01 | **Claude Opus 5** | Commit `85abf7e`: Máscara radial, HUD global, fix 404 odontología | Completado en rama |
| 2026-08-01 | **Viernes (Gemini)** | Commit `7233c7e`: Fusión total + protocolo de colaboración | Completado y verificado |
| 2026-08-01 | **Viernes (Gemini)** | Commit `2bf98ef`: Contorno desvanecido (mix-blend-mode) y Nodos Icosaedro Wireframe | Completado y verificado |
| 2026-08-01 (13:21) | **Viernes (Gemini)** | Alineación a la derecha del Robot y AgentDeck 3D (Despejando título izquierdo) | `pendiente_qa (Claude)` |

> **Nota de Viernes para Claude:** *Colega, el usuario solicitó alinear la red AgentDeck 3D y el Robot hacia la mitad derecha de la pantalla (zona recuadro verde de su captura), liberando de ruido visual el título gigante de la izquierda. He encapsulado las mallas neuronales en un `constellationGroup` trasladado a X=+8.2 en desktop, logrando que el robot y el Oráculo Maestro cohabiten milimétricamente en el lado derecho del lienzo. Queda en `pendiente_qa (Claude)` para tu próxima auditoría técnica.*
