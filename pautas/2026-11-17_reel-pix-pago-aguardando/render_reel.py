"""Renderiza reel.html em MP4 (1080x1920, 30 fps, 15 s, sem áudio) e a capa em PNG.

Uso: python3 -I pautas/2026-11-17_reel-pix-pago-aguardando/render_reel.py <pasta-de-saida> [--audio voz.mp3] [t1 t2 ...]
Com tempos extras (em segundos), só salva stills desses instantes (QA) e não gera o MP4.
Com --audio, junta a locução (normalizada em -16 LUFS) ao vídeo.
Requer: playwright com chromium e ffmpeg. Saída fora do repo até a aprovação.
"""
import pathlib
import shutil
import subprocess
import sys

from playwright.sync_api import sync_playwright

AQUI = pathlib.Path(__file__).resolve().parent
args = sys.argv[1:]
audio = None
if "--audio" in args:
    i = args.index("--audio")
    audio = args[i + 1]
    del args[i:i + 2]
saida = pathlib.Path(args[0])
stills = [float(x) for x in args[1:]]
FPS, DUR = 30, 16.0
saida.mkdir(parents=True, exist_ok=True)

with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={"width": 1080, "height": 1920})
    pg.goto("file://" + str(AQUI / "reel.html"))
    pg.evaluate("document.fonts.ready")
    pg.wait_for_timeout(400)
    if stills:
        for t in stills:
            pg.evaluate(f"seek({t})")
            pg.screenshot(path=str(saida / f"still_{t:05.2f}.png"))
    else:
        pg.evaluate("seek(1.5)")
        pg.screenshot(path=str(saida / "capa-reel.png"))
        frames = saida / "_frames"
        shutil.rmtree(frames, ignore_errors=True)
        frames.mkdir()
        for i in range(int(DUR * FPS)):
            pg.evaluate(f"seek({i / FPS:.4f})")
            pg.screenshot(path=str(frames / f"f{i:05d}.jpg"), type="jpeg", quality=92)
    b.close()

if not stills:
    mp4 = saida / "reel_pix-pago-aguardando_9x16.mp4"
    cmd = ["ffmpeg", "-y", "-v", "error", "-framerate", str(FPS), "-i", str(saida / "_frames" / "f%05d.jpg")]
    if audio:
        cmd += ["-i", audio, "-af", "loudnorm=I=-16:TP=-1.5:LRA=11,apad", "-c:a", "aac", "-b:a", "192k", "-t", str(DUR)]
    cmd += ["-c:v", "libx264", "-preset", "slow", "-crf", "18", "-pix_fmt", "yuv420p", "-movflags", "+faststart", str(mp4)]
    subprocess.run(cmd, check=True)
    shutil.rmtree(saida / "_frames")
    print("mp4 ok")
