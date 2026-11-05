#!/usr/bin/env python3
"""Gera as 9 telas do carrossel (1080x1350) do case Fernanda Oliveira, no padrão visual da HL."""
import os, sys
from playwright.sync_api import sync_playwright

ROOT = "/home/claude/case_fernanda"
HTML = f"{ROOT}/html"
OUT = f"{ROOT}/out/carrossel"
os.makedirs(HTML, exist_ok=True)
os.makedirs(OUT, exist_ok=True)
TOTAL = 9

CSS = """
@font-face{font-family:'Lexend Exa';font-weight:400;src:url(../fonts/lexend-exa-latin-400-normal.woff2) format('woff2')}
@font-face{font-family:'Lexend Exa';font-weight:500;src:url(../fonts/lexend-exa-latin-500-normal.woff2) format('woff2')}
@font-face{font-family:'Manrope';font-weight:400;src:url(../fonts/manrope-latin-400-normal.woff2) format('woff2')}
@font-face{font-family:'Manrope';font-weight:500;src:url(../fonts/manrope-latin-500-normal.woff2) format('woff2')}
@font-face{font-family:'Manrope';font-weight:600;src:url(../fonts/manrope-latin-600-normal.woff2) format('woff2')}
@font-face{font-family:'Manrope';font-weight:700;src:url(../fonts/manrope-latin-700-normal.woff2) format('woff2')}
@font-face{font-family:'JetBrains Mono';font-weight:400;src:url(../fonts/jetbrains-mono-latin-400-normal.woff2) format('woff2')}
@font-face{font-family:'JetBrains Mono';font-weight:500;src:url(../fonts/jetbrains-mono-latin-500-normal.woff2) format('woff2')}
:root{--bg:#050b1c;--surface:#091734;--surface-2:#0c1f45;--line:#17315c;--line-strong:#4a6fa3;--ink:#e8f1f8;--ink-muted:#8fa8c4;
--cyan:#22c3e6;--cyan-glow:rgba(34,195,230,.35);--ok:#3fb950;--warn:#d29922;--mark-stem:#e6e8ee;
--display:'Lexend Exa','Manrope',sans-serif;--sans:'Manrope',sans-serif;--mono:'JetBrains Mono',monospace}
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:1080px;height:1350px;background:var(--bg)}
.slide{position:relative;width:1080px;height:1350px;overflow:hidden;color:var(--ink);font-family:var(--sans);
background:
 radial-gradient(60% 46% at 90% 4%, rgba(25,99,166,.5) 0%, transparent 70%),
 radial-gradient(58% 42% at 4% 100%, rgba(25,99,166,.78) 0%, rgba(26,160,197,.22) 38%, transparent 72%),
 radial-gradient(40% 28% at 64% 58%, rgba(16,76,118,.32) 0%, transparent 70%),
 linear-gradient(170deg,#0a1e43 0%,#050b1c 42%,#030714 100%)}
.slide::after{content:"";position:absolute;inset:0;pointer-events:none;opacity:.2;mix-blend-mode:overlay;
background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='180' height='180'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='.9' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E")}
.top{position:absolute;left:80px;right:80px;top:58px;display:flex;justify-content:space-between;align-items:center;font-family:var(--mono);font-size:26px;letter-spacing:.04em;z-index:3}
.brand{display:flex;align-items:center;gap:16px;color:var(--ink)}
.dot{width:16px;height:16px;border-radius:50%;background:var(--cyan);box-shadow:0 0 14px var(--cyan-glow),0 0 4px var(--cyan-glow)}
.count{color:var(--ink-muted);letter-spacing:.1em}
.abs{position:absolute;left:80px;right:80px;z-index:2}
.eyebrow{font-family:var(--mono);font-weight:500;font-size:25px;letter-spacing:.1em;text-transform:uppercase;color:var(--ink-muted)}
.title{font-family:var(--display);font-weight:500;font-size:80px;line-height:1.13;letter-spacing:-.01em;color:var(--ink)}
.title em{font-style:normal;color:var(--cyan)}
.sub{font-family:var(--sans);font-weight:500;font-size:40px;line-height:1.38;color:var(--ink-muted)}
.cta{position:absolute;left:80px;right:80px;bottom:74px;z-index:3;display:flex;align-items:center;gap:16px;font-family:var(--mono);font-weight:500;font-size:25px;letter-spacing:.1em;text-transform:uppercase;color:var(--ink)}
.cta.muted{color:var(--ink-muted)}
.cta svg{width:34px;height:20px}
.card{background:var(--surface);border:1px solid var(--line);border-radius:14px;overflow:hidden}
.shot{border:1px solid var(--line-strong);border-radius:14px;overflow:hidden;background:#1c120d}
.shot img{display:block;width:100%}
.log{font-family:var(--mono);font-size:32px;line-height:1.75;color:var(--ink)}
.log .head{display:flex;justify-content:space-between;align-items:center;padding:16px 28px;background:var(--surface-2);border-bottom:1px solid var(--line);font-size:22px;letter-spacing:.06em;color:var(--ink-muted);text-transform:uppercase}
.log .body{padding:26px 28px;white-space:pre}
.log .c{color:var(--ink-muted)} .log .ok{color:var(--ok)} .log .warn{color:var(--warn)}
.tag{display:inline-block;padding:8px 16px;border-radius:4px;font-family:var(--mono);font-weight:500;font-size:25px;color:var(--ink-muted);box-shadow:inset 0 0 0 1px var(--line-strong)}
.row{display:flex;align-items:center;gap:30px;padding:34px 36px}
.row .n{font-family:var(--mono);font-weight:500;font-size:28px;letter-spacing:.08em;color:var(--cyan);width:56px;flex:none}
.row .t{font-family:var(--sans);font-weight:600;font-size:38px;line-height:1.25;color:var(--ink)}
.phone{border:2px solid var(--line-strong);border-radius:48px;overflow:hidden;background:#1c120d;width:340px;height:735px}
.phone img{display:block;width:100%;height:100%;object-fit:cover;object-position:top}
.pill{display:inline-flex;align-items:center;gap:12px;padding:10px 22px;border:1px solid var(--line-strong);border-radius:999px;font-family:var(--mono);font-weight:500;font-size:26px;color:var(--ink)}
.pill::before{content:"";width:14px;height:14px;border-radius:50%;background:var(--ok)}
.mark{height:auto;overflow:visible}
.mark .stem{fill:var(--mark-stem)} .mark .flow{fill:var(--cyan)}
.mark.glow .node{filter:drop-shadow(0 0 8px var(--cyan-glow)) drop-shadow(0 0 3px var(--cyan-glow))}
.lockup{display:flex;align-items:center;gap:30px}
.lockup .rule{width:1px;align-self:stretch;background:var(--line-strong);opacity:.7}
.lockup .name{font-family:var(--display);font-weight:400;font-size:46px;line-height:1.1;letter-spacing:.01em;color:var(--ink)}
.lockup .sub2{margin-top:10px;font-family:var(--mono);font-size:19px;letter-spacing:.18em;text-transform:uppercase;color:var(--cyan)}
"""

ARROW = '<svg viewBox="0 0 34 20" fill="none" stroke="#22c3e6" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M1 10h30M23 2l8 8-8 8"/></svg>'
MARK = '<svg class="mark glow" viewBox="0 0 110.25 108" style="height:{h}px" aria-label="HL"><rect class="stem" x="0" y="0" width="18" height="108" rx="3.375"/><rect class="stem" x="49.5" y="0" width="18" height="108" rx="3.375"/><rect class="flow" x="18" y="45" width="31.5" height="18"/><rect class="flow" x="67.5" y="90" width="18" height="18"/><circle class="flow node" cx="101.25" cy="99" r="9"/></svg>'


def slide(n, body, cta=None, cta_muted=False):
    cta_html = ""
    if cta:
        cls = "cta muted" if cta_muted else "cta"
        arrow = "" if cta_muted else ARROW
        cta_html = f'<div class="{cls}"><span>{cta}</span>{arrow}</div>'
    return f"""<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><style>{CSS}</style></head><body>
<div class="slide">
<div class="top"><div class="brand"><span class="dot"></span><span>hl.build</span></div><div class="count">{n:02d} / {TOTAL:02d}</div></div>
{body}
{cta_html}
</div></body></html>"""


S = {}

# 1 CAPA
S[1] = slide(1, """
<div class="abs eyebrow" style="top:150px">Case · Editora de vídeo</div>
<div class="abs title" style="top:200px;font-size:76px">Ela edita Reels para 6 marcas. Faltava um lugar para pedir <em>orçamento</em>.</div>
<div class="abs shot" style="top:700px;height:500px"><img src="../shots/d_hero.png" style="width:100%;height:100%;object-fit:cover;object-position:top"></div>
""", cta="Desliza: como eu fiz")

# 2 ANTES
S[2] = slide(2, """
<div class="abs eyebrow" style="top:150px">O antes</div>
<div class="abs title" style="top:200px;font-size:100px;line-height:1.1">Só Instagram. Sem <em>site</em>.</div>
<div class="abs sub" style="top:520px">O portfólio dela morava dentro do perfil do Instagram, sem um endereço próprio.</div>
<div class="abs card log" style="top:760px"><div class="head"><span>fernanda · portfólio</span><span>// ilustrativo</span></div><div class="body">onde ............ <span class="c">instagram</span>
site próprio .... <span class="warn">nenhum</span></div></div>
""", cta="Slide 2 de 9", cta_muted=True)

# 3 DESAFIO
S[3] = slide(3, """
<div class="abs eyebrow" style="top:150px">O desafio</div>
<div class="abs title" style="top:200px">Mostrar o trabalho e levar ao <em>WhatsApp</em>.</div>
<div class="abs" style="top:640px;display:flex;flex-direction:column;gap:22px">
 <div class="card row"><span class="n">01</span><span class="t">Mostrar os Reels logo no começo</span></div>
 <div class="card row"><span class="n">02</span><span class="t">Mostrar para quem ela já criou Reels</span></div>
 <div class="card row"><span class="n">03</span><span class="t">Pedido de orçamento em 1&nbsp;clique</span></div>
</div>
""", cta="Slide 3 de 9", cta_muted=True)

# 4 DECISAO 01
S[4] = slide(4, """
<div class="abs eyebrow" style="top:150px">Decisão 01</div>
<div class="abs title" style="top:200px">O topo mostra o que ela vende: <em>Reels</em>.</div>
<div class="abs shot" style="top:560px;height:640px"><img src="../shots/d_gallery2.png" style="width:100%;height:100%;object-fit:cover;object-position:top"></div>
""", cta="Galeria de Reels · site no ar", cta_muted=True)

# 5 DECISAO 02
S[5] = slide(5, """
<div class="abs eyebrow" style="top:150px">Decisão 02</div>
<div class="abs title" style="top:200px">Antes do pedido, vem a <em>prova</em>.</div>
<div class="abs" style="top:560px;font-family:var(--display);font-weight:500;font-size:330px;line-height:1;letter-spacing:-.03em;color:var(--ink)">6</div>
<div class="abs eyebrow" style="top:900px;color:var(--ink-muted)">Marcas em faixa contínua, logo abaixo do topo</div>
<div class="abs shot" style="top:1000px;height:200px"><img src="../shots/d_strip.png" style="width:100%;height:100%;object-fit:cover"></div>
""", cta="Faixa de prova · site no ar", cta_muted=True)

# 6 DECISAO 03
S[6] = slide(6, """
<div class="abs eyebrow" style="top:150px">Decisão 03</div>
<div class="abs title" style="top:200px;font-size:72px">3 planos, 1 clique: o pedido sai pronto no <em>WhatsApp</em>.</div>
<div class="abs" style="top:660px;display:flex;gap:16px"><span class="tag">Essencial</span><span class="tag">Impulso</span><span class="tag">Presença</span></div>
<div class="abs card log" style="top:760px;font-family:var(--sans)"><div class="head" style="font-family:var(--mono)"><span>whatsapp · mensagem pronta</span><span>// ilustrativo</span></div><div style="padding:38px 34px;font-size:42px;line-height:1.4;font-weight:500;color:var(--ink)">Olá, Fernanda! Vi o seu portfólio e quero um orçamento do plano <b style="font-weight:700">Impulso</b>.</div></div>
""", cta="Cada botão leva o plano escolhido", cta_muted=True)

# 7 CELULAR
S[7] = slide(7, """
<div class="abs eyebrow" style="top:150px">Decisão 04</div>
<div class="abs title" style="top:200px;font-size:96px">E no <em>celular</em>.</div>
<div class="phone" style="position:absolute;left:180px;top:420px;z-index:2"><img src="../shots/m_hero.png"></div>
<div class="phone" style="position:absolute;left:560px;top:420px;z-index:2"><img src="../shots/m_gallery2.png"></div>
""", cta="Versão celular · site no ar", cta_muted=True)

# 8 RESULTADO
S[8] = slide(8, """
<div class="abs eyebrow" style="top:150px">O resultado</div>
<div class="abs title" style="top:200px;font-size:96px">Entregue e no <em>ar</em>.</div>
<div class="abs card log" style="top:520px"><div class="head"><span>fernanda-landpage.vercel.app</span><span class="ok">online</span></div><div class="body">site ............ <span class="ok">no ar</span>
marcas .......... 6
planos .......... 3
orçamento ....... 1 clique</div></div>
<div class="abs sub" style="top:960px;font-size:36px">Os números de resultado eu conto aqui quando a Fernanda liberar.</div>
""", cta="Slide 8 de 9", cta_muted=True)

# 9 CTA
S[9] = slide(9, """
<div class="abs eyebrow" style="top:150px">Feito por HL</div>
<div class="abs title" style="top:200px;font-size:92px">Seu projeto é o <em>próximo</em>.</div>
<div class="abs sub" style="top:520px">Eu construo o seu site. Link na bio.</div>
<div class="abs" style="top:760px"><div class="lockup">""" + MARK.format(h=110) + """<span class="rule"></span><div><div class="name">hélio levi</div><div class="sub2">Back-end · Systems</div></div></div></div>
<div class="abs eyebrow" style="top:960px">@hl.build &nbsp;·&nbsp; case com @ffernanda.olvr</div>
""", cta="Link na bio", cta_muted=False)


def main():
    nums = [int(a) for a in sys.argv[1:]] or list(S)
    for n in nums:
        with open(f"{HTML}/slide{n}.html", "w", encoding="utf-8") as f:
            f.write(S[n])
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path="/usr/bin/google-chrome", args=["--no-sandbox", "--allow-file-access-from-files"])
        page = b.new_page(viewport={"width": 1080, "height": 1350}, device_scale_factor=1)
        for n in nums:
            page.goto(f"file://{HTML}/slide{n}.html")
            page.wait_for_load_state("networkidle")
            page.evaluate("document.fonts.ready")
            page.wait_for_timeout(500)
            page.screenshot(path=f"{OUT}/slide{n:02d}.png")
            print("ok", n)
        b.close()


if __name__ == "__main__":
    main()
