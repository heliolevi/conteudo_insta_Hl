import html, pathlib
OUT = pathlib.Path('/home/claude/work/slides')
TOTAL = 8

CSS = """
@font-face{font-family:'Lexend Exa';font-weight:500;src:url(fonts/lexend-exa-latin-500-normal.woff2)}
@font-face{font-family:'Manrope';font-weight:400;src:url(fonts/manrope-latin-400-normal.woff2)}
@font-face{font-family:'Manrope';font-weight:600;src:url(fonts/manrope-latin-600-normal.woff2)}
@font-face{font-family:'JetBrains Mono';font-weight:400;src:url(fonts/jetbrains-mono-latin-400-normal.woff2)}
@font-face{font-family:'JetBrains Mono';font-weight:500;src:url(fonts/jetbrains-mono-latin-500-normal.woff2)}
:root{--abyss:#030714;--bg:#050b1c;--deep:#0a1e43;--cobalt:#1963a6;--azure:#1aa0c5;--cyan:#22c3e6;--foam:#dbeaf3;--ink:#e8f1f8;--muted:#8fa8c4;--line:#17315c}
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:1080px;height:1350px;background:var(--bg);color:var(--ink);font-family:'Manrope',sans-serif;overflow:hidden}
.slide{position:relative;width:1080px;height:1350px;background:var(--bg)}
.mare{position:absolute;inset:0;background:
  radial-gradient(ellipse 900px 700px at 110% -5%, rgba(34,195,230,.38), transparent 60%),
  radial-gradient(ellipse 1000px 800px at 85% 25%, rgba(26,160,197,.30), transparent 62%),
  radial-gradient(ellipse 1200px 900px at 20% 80%, rgba(25,99,166,.55), transparent 65%),
  radial-gradient(ellipse 900px 700px at -10% 100%, rgba(10,30,67,1), transparent 70%),
  linear-gradient(160deg,#0a1e43 0%,#050b1c 55%,#030714 100%)}
.grao{position:absolute;inset:0;opacity:.32;mix-blend-mode:overlay;background-image:url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='300' height='300'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='.9' numOctaves='2' stitchTiles='stitch'/><feColorMatrix values='0 0 0 0 1  0 0 0 0 1  0 0 0 0 1  0 0 0 1.2 -.1'/></filter><rect width='300' height='300' filter='url(%23n)'/></svg>")}
.top{position:absolute;left:80px;right:80px;top:84px;display:flex;justify-content:space-between;align-items:center;font-family:'JetBrains Mono';font-weight:500;font-size:26px;letter-spacing:.08em;text-transform:uppercase;color:var(--muted)}
.foot{position:absolute;left:80px;right:80px;bottom:72px;display:flex;justify-content:space-between;align-items:center;border-top:1px solid var(--line);padding-top:28px}
.sig{display:flex;align-items:center;gap:16px;font-family:'Lexend Exa';font-weight:500;font-size:26px;letter-spacing:.04em;text-transform:lowercase;color:var(--foam)}
.node{width:14px;height:14px;border-radius:50%;background:var(--cyan);box-shadow:0 0 14px 3px rgba(34,195,230,.65)}
.url{font-family:'JetBrains Mono';font-weight:500;font-size:24px;letter-spacing:.08em;color:var(--muted)}
.body{position:absolute;left:80px;right:80px;top:200px}
.num{font-family:'JetBrains Mono';font-weight:500;font-size:40px;letter-spacing:.08em;color:var(--muted);margin-bottom:28px}
h1,h2{font-family:'Lexend Exa';font-weight:500;letter-spacing:.01em;line-height:1.16;color:var(--foam)}
h1{font-size:92px}
h2{font-size:68px}
.c{color:var(--cyan)}
p{font-size:38px;line-height:1.45;color:var(--ink);margin-top:36px;max-width:880px}
.fonte{font-family:'JetBrains Mono';font-size:26px;letter-spacing:.04em;color:var(--muted);margin-top:28px}
.log{margin-top:44px;border:1px solid var(--line);border-radius:14px;background:var(--abyss);padding:36px 40px;font-family:'JetBrains Mono';font-size:30px;line-height:1.55;color:var(--ink);white-space:pre}
.log .k{color:var(--muted)}
.log .t{display:block;color:var(--muted);letter-spacing:.08em;font-size:24px;margin-bottom:14px;text-transform:uppercase}
.duo{display:flex;gap:24px;margin-top:44px}
.duo .card{flex:1;border:1px solid var(--line);border-radius:14px;background:var(--abyss);padding:32px 34px;font-family:'JetBrains Mono';font-size:28px;line-height:1.6}
.duo .card .t{display:block;color:var(--muted);letter-spacing:.08em;font-size:23px;margin-bottom:14px;text-transform:uppercase}
.tags{display:flex;gap:16px;margin-top:44px}
.tag{border:1px solid var(--line);border-radius:4px;background:var(--abyss);padding:12px 22px;font-family:'JetBrains Mono';font-weight:500;font-size:26px;letter-spacing:.08em;text-transform:uppercase;color:var(--muted)}
.check{margin-top:36px;display:flex;flex-direction:column;gap:22px}
.check div{display:flex;align-items:center;gap:26px;font-size:36px;line-height:1.3}
.box{flex:none;width:34px;height:34px;border:2px solid var(--muted);border-radius:4px}
.cta{margin-top:48px;border:1px solid var(--line);border-radius:14px;background:var(--abyss);padding:32px 40px;font-family:'JetBrains Mono';font-weight:500;font-size:34px;letter-spacing:.08em;text-transform:uppercase;color:var(--foam)}
.cta .c{color:var(--cyan)}
"""

def page(inner, mare=False):
    bg = '<div class="mare"></div><div class="grao"></div>' if mare else ''
    return f"""<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><style>{CSS}</style></head><body><div class="slide">{bg}{inner}</div></body></html>"""

def chrome(n, eyebrow):
    return f"""<div class="top"><span>{eyebrow}</span><span>{n:02d}/{TOTAL:02d}</span></div>
<div class="foot"><div class="sig"><span class="node"></span>hélio levi</div><div class="url">hl.build</div></div>"""

def log(title, lines):
    return f'<div class="log"><span class="t">{title}</span>{lines}</div>'

slides = []

# 1 capa
slides.append(page(f"""{chrome(1,'PRA QUEM RECEBE POR PIX')}
<div class="body" style="top:300px"><h1>5 sinais de que você ainda concilia <span class="c">Pix</span> na&nbsp;mão</h1>
<p style="font-family:'JetBrains Mono';font-size:30px;letter-spacing:.08em;color:var(--muted);margin-top:64px">DESLIZA →</p></div>""", mare=True))

# 2 segunda capa
slides.append(page(f"""{chrome(2,'PRA QUEM RECEBE POR PIX')}
<div class="body"><h2>O Pix cai na hora. A <span class="c">conferência</span> não.</h2>
<p>No comércio, o QR Code dinâmico foi de 5% das transações em 2021 para 40% em 2025. Quem integra a API do Pix opera em tempo real. Quem não integra depende de processo manual.</p>
<p class="fonte">FONTE: BANCO CENTRAL, RELATÓRIO DE GESTÃO DO PIX 2023-2025</p>
<p style="margin-top:44px">Em 6 telas, 5 sinais. O quinto passa batido.</p></div>"""))

# 3 sinal 1
slides.append(page(f"""{chrome(3,'PRA QUEM RECEBE POR PIX')}
<div class="body"><div class="num">01</div><h2>Você abre o app do banco pra saber <span class="c">quem pagou</span></h2>
<p>Se a venda só fecha quando você lembra de conferir o extrato, o seu caixa depende da sua memória.</p>
{log('// ilustrativo', '<span class="k">{</span>\n  <span class="k">"pedido":</span> "#1042",\n  <span class="k">"valor":</span> "150.00",\n  <span class="k">"status":</span> "CONCLUIDA"\n<span class="k">}</span>')}</div>"""))

# 4 sinal 2
slides.append(page(f"""{chrome(4,'PRA QUEM RECEBE POR PIX')}
<div class="body"><div class="num">02</div><h2>Entra um valor e <span class="c">ninguém sabe</span> de quê</h2>
<p>O cliente paga e não avisa o pedido. Você cruza valor, hora e nome. Com uma cobrança por pedido, cada Pix já chega identificado.</p>
<div class="duo"><div class="card"><span class="t">// extrato</span>R$ 150,00<br>14:32<br>João S.</div><div class="card"><span class="t">// pedidos</span>#1042 R$ 150,00<br>#1043 R$ 150,00<br>quem é quem?</div></div></div>"""))

# 5 sinal 3
slides.append(page(f"""{chrome(5,'PRA QUEM RECEBE POR PIX')}
<div class="body"><div class="num">03</div><h2>Cobrança de mensalidade é <span class="c">mensagem</span> no WhatsApp</h2>
<p>Todo mês você lembra o cliente de pagar. No Pix Automático o cliente autoriza uma vez e a cobrança recorrente acontece sozinha.</p>
{log('// ilustrativo','<span class="k">autorização:</span> 1x pelo cliente\n<span class="k">próxima cobrança:</span> 05/11\n<span class="k">valor:</span> R$ 89,90')}</div>"""))

# 6 sinal 4
slides.append(page(f"""{chrome(6,'PRA QUEM RECEBE POR PIX')}
<div class="body"><div class="num">04</div><h2>O fechamento do mês é uma <span class="c">planilha</span> com 3 abas</h2>
<p>Extrato de um lado, vendas do outro, e você cruzando. Cada fórmula quebrada é uma venda sem dono.</p>
<div class="tags"><span class="tag">extrato</span><span class="tag">vendas</span><span class="tag">ajustes</span></div>
{log('// ilustrativo','=SOMASE(B2:B900; A2:A900; D2)\n<span class="k">→</span> #REF!')}</div>"""))

# 7 sinal 5 (pico)
slides.append(page(f"""{chrome(7,'PRA QUEM RECEBE POR PIX')}
<div class="body"><div class="num">05</div><h2>Ninguém sabe <span class="c">quando</span> o erro aconteceu</h2>
<p>Sem registro de cada evento, o erro vira discussão de memória. Quando o sistema grava cada pagamento, dá pra auditar: data, valor e origem.</p>
{log('// ilustrativo','<span class="k">14:32:07</span>  pix.recebido   #1042  150.00\n<span class="k">14:32:07</span>  pedido.pago    #1042\n<span class="k">14:32:08</span>  nota.emitida   #1042')}</div>"""))

# 8 fechamento
slides.append(page(f"""{chrome(8,'SALVA PRA CONSULTAR')}
<div class="body"><h2>Marcou 2 ou mais? Dá pra <span class="c">automatizar</span></h2>
<div class="check">
<div><span class="box"></span>Confiro o extrato pra saber quem pagou</div>
<div><span class="box"></span>Pix chega sem identificação</div>
<div><span class="box"></span>Mensalidade cobrada na mão</div>
<div><span class="box"></span>Fechamento em planilha</div>
<div><span class="box"></span>Não sei quando o erro aconteceu</div>
</div>
<div class="cta">Quer ver como eu monto isso?<br><span class="c">Link na bio</span></div></div>"""))

for i,s in enumerate(slides,1):
    (OUT/f'slide-{i:02d}.html').write_text(s, encoding='utf-8')
print(len(slides),'slides')
