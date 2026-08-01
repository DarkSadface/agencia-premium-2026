# 🤝 PROTOCOLO DE SINCRONIZACIÓN Y CO-DESARROLLO (CLAUDE & VIERNES)
**Proyecto:** Agencia Premium 2026 / Colombia Tech Systems  
**Ubicación Repositorio:** `C:\Users\sopor\dev\agencia-10-paginas`  
**Servidor Edge:** Cloudflare Workers (`nameless-snowflake-e208` -> `www.colombiatechsystems.com`)  
**Fecha de Sincronización:** 2026-08-01 (Iteración 16:10 COT)

---

## 🛑 REGLA DE HIERRO DEL USUARIO: CERO INTERRUPCIONES Y CERO SOBREESCRIBIRSE
El usuario ha ordenado de forma definitiva que **Claude (Opus/Sonnet)** y **Viernes (Gemini / Nano Banana)** trabajan en equipo sobre este mismo repositorio sin pisarse, sin interrumpir el flujo del otro y **NUNCA sobreescribir o eliminar commits/avances sin antes integrarlos**.

### 📋 Checklist Obligatorio Antes de Modificar Código (Para Ambos Agentes)
1. **Medición Real Pre-Edición:** Ejecutar siempre `git status` y `git log -n 5 --oneline` o `git show` del último commit antes de tocar un archivo.
2. **Validar Autor del Último Commit:** Si el último commit fue del compañero (ej. Claude hizo `85abf7e`), **LEER EL DIFF** antes de modificar para conservar todos sus fixes.
3. **Fusión, no sustitución:** Si ambos modificaron la misma área, se integran ambas capas técnicas.
4. **Handoff & QA Cruzado:** Al finalizar un cambio, actualizar el bloque de estado en este documento y marcar la tarea como `pendiente_qa (Claude)` o `pendiente_qa (Viernes)` según corresponda.

---

## 🌟 ESTADO AGREGADO DEL SISTEMA (FUSIÓN TÉCNICA Y AUDITORÍA VISUAL)

### 1. Arreglos Visuales Invertidos por Viernes (Completados y en Producción) ✅
- **Gimnasio EQUINOX (`gimnasio.html`):** Se eliminaron los contenedores grises vacíos (divs con gradiente CSS de prueba) en las secciones *"LA MÁQUINA ERES TÚ"* y *"HIPERTROFIA SINTÉTICA"*. Se introdujeron fotografías reales de entrenamiento de fuerza bruta y jaulas de potencia con bordes neón y sombreado 3D.
- **Estética Vogue Clínica (`estetica.html`):** Se solucionó el vacío en el lado izquierdo frente a las tarjetas *"Bioestimulación"* y *"Skin Quality"*. Se estructuró un grid responsive equilibrado y se incrustó un showcase de fotografía médica clínica (tecnología láser y colágeno) con etiqueta glassmorphism cian.
- **Nodo Oráculo Maestro en `index.html`:** Reducido milimétricamente al tamaño exacto del cerebro cuántico de la androide (radio `1.6`) y posicionado flotando en coronación justo **arriba del cerebro** tanto en PC, como Tablet e i-dispositivos móviles (Poco F6 / ADB).

### 2. Directiva del Usuario para Claude: Rediseño Impecable Vercel ⏳ (`pendiente_ejecucion (Claude)`)
El usuario ha asignado formalmente a **Claude** el rediseño de dos páginas críticas con estándar **Vercel Dark Mode Impecable**:
- **Abogados (`abogados.html`):** Corregir la ilegibilidad del titular principal (*"Justicia. Precisión. Discreción."*), el cual se oscurece contra el fondo negro. Colocar fondo arquitectónico inmersivo con `assets/hero_abogados.png`, textos blanco puro / oro ducal y efectos lumínicos Vercel.
- **Restaurante L'Étoile Rouge (`restaurante.html`):** Reemplazar el fondo blanco plano con degradado cian deslucido por una experiencia gastronómica VIP inmersiva en Dark Mode carbón, borgoña y oro, utilizando `assets/hero_restaurante.png` de fondo escénico.
> **Consultar documento dedicado:** [CLAUDE_VERCEL_REDESIGN_TASKS.md](file:///C:/Users/sopor/dev/agencia-10-paginas/CLAUDE_VERCEL_REDESIGN_TASKS.md) para el detalle completo del diagnóstico.

---

## 🔄 ESTAFETA Y COLA DE TRABAJO (HANDOFF LOG)

| Fecha | Agente Activo | Acción Ejecutada | Estado / Siguiente Paso |
| :--- | :--- | :--- | :--- |
| 2026-08-01 | **Claude Opus 5** | Commit `85abf7e`: Máscara radial, HUD global, fix 404 odontología | Completado en rama |
| 2026-08-01 | **Viernes (Gemini)** | Commit `5e71b9d`: Paridad responsive total en PC, Tablet y Móvil (Poco F6 / ADB) | Completado y verificado |
| 2026-08-01 | **Viernes (Gemini)** | Commit `f8e3cd6`: Nodo Oráculo Maestro tamaño cerebro flotando justo arriba de él | Completado y verificado |
| 2026-08-01 (16:10) | **Viernes (Gemini)** | Fix imágenes rotas/vacías en `gimnasio.html` y `estetica.html` + Briefing para Claude | `pendiente_qa (Claude)` |
| 2026-08-01 | **Claude (Supervisión)** | Rediseño estilo Vercel Dark Mode de `abogados.html` y `restaurante.html` | **`EN COLA (Próximo paso de Claude)`** |

> **Nota de Viernes para Claude:** *Colega, el usuario nos dio instrucciones divididas y claras: yo he resuelto en caliente los problemas de contenedores vacíos en el gimnasio y la estética, además de encuadrar el Oráculo Maestro del index justo encima del cerebro con sus nuevas dimensiones. Ahora tienes luz verde del usuario para hacer magia Vercel sobre `abogados.html` (que su título marrón casi no se lee contra el azul) y `restaurante.html` (que está demasiado blanco y plano para un sitio VIP). Tienes los detalles en `CLAUDE_VERCEL_REDESIGN_TASKS.md`. Todo desplegado en Cloudflare y git sincronizado sin conflictos. ¡Éxito en la ejecución!*
