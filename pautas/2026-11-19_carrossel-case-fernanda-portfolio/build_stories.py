import os
from playwright.sync_api import sync_playwright
from build_carrossel import CSS, MARK, ARROW
OUT="out/stories"; os.makedirs(OUT,exist_ok=True)
css=CSS.replace("html,body{width:1080px;height:1350px","html,body{width:1080px;height:1920px").replace(".slide{position:relative;width:1080px;height:1350px",".slide{position:relative;width:1080px;height:1920px")
def page(body): return f'<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><style>{css}</style></head><body><div class="slide">{body}</div></body></html>'
S={
1:page('''<div class="top" style="top:300px"><div class="brand"><span class="dot"></span><span>hl.build</span></div><div class="count">case novo</div></div>
<div class="abs eyebrow" style="top:420px">No feed agora</div>
<div class="abs title" style="top:480px;font-size:96px">Case novo no feed. O site da <em>Fernanda</em> no ar.</div>
<div class="abs shot" style="top:1000px;height:520px"><img src="../shots/d_hero.png" style="width:100%;height:100%;object-fit:cover;object-position:top"></div>'''),
2:page('''<div class="top" style="top:300px"><div class="brand"><span class="dot"></span><span>hl.build</span></div><div class="count"></div></div>
<div class="abs title" style="top:640px;font-size:110px">Seu projeto é o <em>próximo</em>.</div>
<div class="abs" style="top:1040px;display:flex;align-items:center;gap:18px;font-family:var(--mono);font-weight:500;font-size:34px;letter-spacing:.1em;text-transform:uppercase">Link na bio <span style="display:inline-block;width:46px">'''+ARROW.replace('<svg ','<svg style="width:46px;height:28px" ')+'''</span></div>
<div class="abs" style="top:1300px"><div class="lockup">'''+MARK.format(h=110)+'''<span class="rule"></span><div><div class="name">hélio levi</div><div class="sub2">Back-end · Systems</div></div></div></div>'''),
}
with sync_playwright() as p:
    b=p.chromium.launch(executable_path="/usr/bin/google-chrome",args=["--no-sandbox","--allow-file-access-from-files"])
    pg=b.new_page(viewport={"width":1080,"height":1920})
    for n,h in S.items():
        open(f"html/story{n}.html","w").write(h)
        pg.goto(f"file://{os.path.abspath('html')}/story{n}.html"); pg.wait_for_load_state("networkidle"); pg.wait_for_timeout(500)
        pg.screenshot(path=f"{OUT}/story-19-11-{n}.jpg",type="jpeg",quality=92)
    b.close()
