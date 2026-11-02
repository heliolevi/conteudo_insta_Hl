"""Renderiza os HTML de pautas/<post>/slides/ em PNG (midia/<post>/).

Uso: python3 -I pautas/_gerador/render.py [filtro-opcional-no-nome-da-pasta] [pasta-de-saida]
Sem pasta de saida, grava em midia/ (so use depois da aprovacao). Antes da aprovacao,
passe uma pasta fora do repo (ex.: /tmp/png) para nao publicar arte nao aprovada.
Requer: playwright com chromium.
"""
import pathlib
import sys

from playwright.sync_api import sync_playwright

RAIZ = pathlib.Path(__file__).resolve().parents[2]
filtro = sys.argv[1] if len(sys.argv) > 1 else ""
BASE = pathlib.Path(sys.argv[2]) if len(sys.argv) > 2 else RAIZ / "midia"

with sync_playwright() as p:
    b = p.chromium.launch()
    for pasta in sorted((RAIZ / "pautas").glob("2026-*")):
        if filtro not in pasta.name or not (pasta / "slides").exists():
            continue
        saida = BASE / pasta.name
        saida.mkdir(parents=True, exist_ok=True)
        for h in sorted((pasta / "slides").glob("*.html")):
            story = h.name.startswith("story")
            pg = b.new_page(viewport={"width": 1080, "height": 1920 if story else 1350})
            pg.goto("file://" + str(h))
            pg.evaluate("document.fonts.ready")
            pg.wait_for_timeout(250)
            pg.locator(".slide").screenshot(path=str(saida / (h.stem + ".png")))
            pg.close()
        print(pasta.name, "ok")
    b.close()
