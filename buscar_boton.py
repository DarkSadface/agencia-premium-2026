# -*- coding: utf-8 -*-
with open(r"C:\Users\sopor\dev\agencia-10-paginas\curso-agentic-ia.html", "r", encoding="utf-8") as f:
    lines = f.readlines()
for i, l in enumerate(lines):
    if "Inscribirme" in l or "290" in l or "USD" in l or "btn" in l:
        print(f"Línea {i+1}: {l.strip()}")
