"""Gerador das artes da semana de 02/11/2026 (carrosséis e stories) no padrão visual da HL.

Uso:  python3 -I pautas/_gerador/gerar.py     (gera os HTML em pautas/<post>/slides/)
      python3 -I pautas/_gerador/render.py    (renderiza os PNG em midia/<post>/)

Marcação de texto: **palavra** = ciano (uma por título), ~texto~ = comentário esmaecido,
^texto^ = destaque ciano dentro de bloco de código.
"""
import html
import pathlib
import re

RAIZ = pathlib.Path(__file__).resolve().parents[2]
FONTES = "../../_gerador/fonts"

CSS = """
@font-face{font-family:"Lexend Exa";src:url("FONTES/LexendExa.ttf");font-weight:100 900}
@font-face{font-family:"Manrope";src:url("FONTES/Manrope.ttf");font-weight:200 800}
@font-face{font-family:"JetBrains Mono";src:url("FONTES/JetBrainsMono.ttf");font-weight:100 800}
:root{--bg:#050b1c;--abyss:#030714;--deep:#0a1e43;--cobalt:#1963a6;--azure:#1aa0c5;--cyan:#22c3e6;
--foam:#dbeaf3;--ink:#e8f1f8;--muted:#8fa8c4;--line:#17315c;--surface:#08142e}
*{box-sizing:border-box;margin:0;padding:0}
html,body{background:#000}
.slide{position:relative;width:1080px;overflow:hidden;background:var(--bg);color:var(--ink);font-family:"Manrope",sans-serif}
.slide.feed{height:1350px}.slide.story{height:1920px}
.cy{color:var(--cyan)}.c{color:#6f89aa}.k{color:var(--cyan)}
.mono{font-family:"JetBrains Mono",monospace;font-weight:500;letter-spacing:.08em;text-transform:uppercase;color:var(--muted)}

.mare{position:absolute;inset:-40px;background:
 radial-gradient(900px 760px at 8% 98%,rgba(25,99,166,.95) 0%,rgba(25,99,166,0) 62%),
 radial-gradient(760px 640px at 100% 6%,rgba(10,30,67,1) 0%,rgba(10,30,67,0) 68%),
 radial-gradient(560px 460px at 62% 58%,rgba(26,160,197,.30) 0%,rgba(26,160,197,0) 72%),
 radial-gradient(700px 520px at 20% 30%,rgba(10,30,67,.9) 0%,rgba(10,30,67,0) 70%),#050b1c}
.slide.story .mare{background:
 radial-gradient(1100px 900px at 0% 100%,rgba(25,99,166,.95) 0%,rgba(25,99,166,0) 62%),
 radial-gradient(900px 760px at 100% 0%,rgba(10,30,67,1) 0%,rgba(10,30,67,0) 68%),
 radial-gradient(700px 560px at 70% 52%,rgba(26,160,197,.26) 0%,rgba(26,160,197,0) 72%),#050b1c}
.grain{position:absolute;inset:0;opacity:.11;mix-blend-mode:overlay;pointer-events:none;
 background-image:url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='260' height='260'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='.9' numOctaves='2' stitchTiles='stitch'/><feColorMatrix values='0 0 0 0 1  0 0 0 0 1  0 0 0 0 1  0 0 0 .9 0'/></filter><rect width='100%' height='100%' filter='url(%23n)'/></svg>")}
.onda{position:absolute;left:0;right:0;bottom:0;height:210px;pointer-events:none;
 -webkit-mask-image:linear-gradient(to top,#000 0%,#000 35%,transparent 100%)}
.onda .dots{position:absolute;inset:0;background:radial-gradient(circle,rgba(143,168,196,.42) 1.3px,transparent 1.8px) 0 0/28px 28px}
.onda svg{position:absolute;inset:0;width:100%;height:100%}

.top{position:absolute;left:80px;right:80px;top:62px;display:flex;align-items:center;justify-content:space-between;z-index:4}
.slide.story .top{top:170px}
.top .l{display:flex;align-items:center;gap:16px;font-family:"JetBrains Mono",monospace;font-weight:500;font-size:26px;letter-spacing:.04em;color:var(--foam)}
.top .r{font-family:"JetBrains Mono",monospace;font-weight:500;font-size:26px;letter-spacing:.08em;color:var(--muted)}
.node{width:14px;height:14px;border-radius:50%;background:var(--cyan);box-shadow:0 0 16px rgba(34,195,230,.85)}

.col{position:absolute;left:80px;right:80px;top:150px;bottom:150px;display:flex;flex-direction:column;z-index:3}
.slide.story .col{top:300px;bottom:330px}
.num{font-family:"Lexend Exa",sans-serif;font-weight:500;font-size:124px;line-height:1;color:var(--cobalt);margin-bottom:22px}
.h{font-family:"Lexend Exa",sans-serif;font-weight:500;letter-spacing:-.012em;color:var(--foam);font-size:72px;line-height:1.1;margin-bottom:36px}
.h.xl{font-size:90px;line-height:1.07}
.slide.story .h{font-size:100px;line-height:1.06}
.p{font-size:41px;line-height:1.38;font-weight:500;color:var(--foam);opacity:.94;margin-bottom:42px}
.p.s{font-size:34px;color:var(--muted);opacity:1}
.src{font-family:"JetBrains Mono",monospace;font-weight:500;font-size:24px;letter-spacing:.06em;text-transform:uppercase;color:#7f98b6;line-height:1.55;margin-top:auto}
.spacer{flex:1}

.panel{border:1px solid var(--line);border-radius:14px;background:var(--surface);padding:26px 32px}
.panel .tag{display:flex;justify-content:space-between;margin-bottom:16px;font-size:25px}
.panel .tag .i{color:#7f98b6;text-transform:none;letter-spacing:.02em}
.code{font-family:"JetBrains Mono",monospace;font-weight:500;font-size:32px;line-height:1.5;color:var(--foam);white-space:pre}

.bignum{font-family:"Lexend Exa",sans-serif;font-weight:500;font-size:470px;line-height:.9;color:var(--foam);letter-spacing:-.045em}
.biglab{font-size:30px;margin-top:10px}
.hint{display:flex;align-items:center;gap:14px;font-size:27px;color:var(--ink)}
.hint .a{color:var(--cyan)}

.tl{display:flex;flex-direction:column;gap:46px;margin:14px 0 52px}
.tl .row{display:flex;gap:34px;align-items:baseline}
.tl .d{font-family:"JetBrains Mono",monospace;font-weight:600;font-size:34px;letter-spacing:.04em;color:var(--cyan);width:268px;flex:none}
.tl .t{font-size:42px;font-weight:600;line-height:1.28;color:var(--ink)}
.tl .t small{display:block;font-size:27px;font-weight:500;color:var(--muted);margin-top:4px}

.chk{display:flex;flex-direction:column;gap:4px;margin-bottom:26px}
.chk .row{display:flex;align-items:center;gap:28px;height:90px}
.chk svg{flex:none;width:50px;height:50px}
.chk span{font-size:40px;font-weight:700;line-height:1.25;color:var(--ink)}
.cta{display:inline-flex;align-self:flex-start;height:96px;padding:0 44px;align-items:center;gap:18px;border-radius:8px;background:var(--cyan);color:var(--abyss);font-family:"JetBrains Mono",monospace;font-weight:700;font-size:30px;letter-spacing:.08em;text-transform:uppercase}
.note{font-size:28px;font-weight:500;line-height:1.4;color:var(--muted);margin-top:26px}
.lock{margin-top:auto}
.lock .n{font-family:"Lexend Exa",sans-serif;font-weight:500;font-size:32px;color:var(--foam);text-transform:lowercase}
.lock .t{margin-top:8px;color:var(--cyan);font-size:22px}
.two{display:flex;flex-direction:column;gap:26px;margin-bottom:38px}
.two .panel{padding:30px 34px}
.two .tt{font-family:"Lexend Exa",sans-serif;font-weight:500;font-size:46px;color:var(--foam);margin-bottom:10px}
.two .dd{font-size:36px;line-height:1.36;color:var(--muted);font-weight:500}
.flow{display:flex;flex-direction:column;gap:0;margin-bottom:34px}
.flow .st{display:flex;align-items:center;gap:26px;height:96px}
.flow .st .dot{width:20px;height:20px;border-radius:50%;border:2px solid var(--azure);flex:none;position:relative}
.flow .st .dot.on{background:var(--cyan);border-color:var(--cyan);box-shadow:0 0 14px rgba(34,195,230,.7)}
.flow .st .nm{font-family:"JetBrains Mono",monospace;font-weight:600;font-size:36px;color:var(--foam)}
.flow .st .q{font-size:29px;color:var(--muted);font-weight:500;margin-left:auto}
.stk{flex:1;display:flex;align-items:flex-end;justify-content:center;padding-bottom:6px}
"""


def esc(s):
    return html.escape(s, quote=False)


def rich(s):
    s = esc(s)
    s = re.sub(r"\*\*(.+?)\*\*", r'<span class="cy">\1</span>', s)
    s = re.sub(r"~(.+?)~", r'<span class="c">\1</span>', s)
    s = re.sub(r"\^(.+?)\^", r'<span class="k">\1</span>', s)
    return s.replace("\n", "<br>")


def onda():
    paths = ""
    for k in range(7):
        d = ""
        for x in range(0, 1081, 18):
            import math
            y = 96 + k * 15 + math.sin(x / 95 + k * 0.65) * 17
            d += ("M" if x == 0 else " L") + f"{x} {y:.1f}"
        paths += f'<path d="{d}" fill="none" stroke="#1963a6" stroke-opacity="{0.55 - k * 0.05:.2f}" stroke-width="1.3"/>'
    return f'<div class="onda"><div class="dots"></div><svg viewBox="0 0 1080 210" preserveAspectRatio="none">{paths}</svg></div>'


ONDA = onda()


def top(n, total):
    return (f'<div class="top"><div class="l"><span class="node"></span><span>hl.build</span></div>'
            f'<div class="r">{n:02d} / {total:02d}</div></div>')


def painel(tag, linhas):
    code = "<br>".join(rich(l) for l in linhas)
    tam = 38 if len(linhas) <= 2 else (36 if len(linhas) <= 4 else 32)
    return (f'<div class="panel"><div class="tag mono"><span>{esc(tag)}</span><span class="i">// ilustrativo</span></div>'
            f'<div class="code" style="font-size:{tam}px">{code}</div></div>')


def pagina(titulo, inner, fundo="onda", story=False):
    bg = '<div class="mare"></div><div class="grain"></div>' if fundo == "mare" else ONDA
    cls = "story" if story else "feed"
    css = CSS.replace("FONTES", FONTES)
    return (f'<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>{esc(titulo)}</title>'
            f'<style>{css}</style></head><body><div class="slide {cls}">{bg}{inner}</div></body></html>')


# ---------- tipos de tela ----------
def capa_num(n, t, num, label, h, hint):
    inner = top(n, t) + (
        f'<div class="col"><h1 class="h xl">{rich(h)}</h1><div class="spacer"></div>'
        f'<div class="bignum">{esc(num)}</div><div class="mono biglab">{esc(label)}</div><div class="spacer"></div>'
        f'<div class="hint"><span class="mono" style="color:var(--ink)">{esc(hint)}</span><span class="a">→</span></div></div>')
    return pagina("capa", inner, "mare")


def capa_log(n, t, h, tag, linhas, hint):
    inner = top(n, t) + (
        f'<div class="col"><h1 class="h xl">{rich(h)}</h1><div class="spacer"></div>{painel(tag, linhas)}<div class="spacer"></div>'
        f'<div class="hint"><span class="mono" style="color:var(--ink)">{esc(hint)}</span><span class="a">→</span></div></div>')
    return pagina("capa", inner, "mare")


def contexto(n, t, h, p, fonte, extra=""):
    inner = top(n, t) + (
        f'<div class="col"><h2 class="h">{rich(h)}</h2><p class="p">{rich(p)}</p>{extra}'
        f'<div class="src">{rich(fonte)}</div></div>')
    return pagina("contexto", inner)


def teste(n, t, num, h, p, tag, linhas, fonte=""):
    src = f'<div class="src">{rich(fonte)}</div>' if fonte else ""
    inner = top(n, t) + (
        f'<div class="col"><div class="num">{num}</div><h2 class="h">{rich(h)}</h2><p class="p">{rich(p)}</p>'
        f'{painel(tag, linhas)}{src}</div>')
    return pagina("teste", inner)


def dois_cartoes(n, t, h, p, cartoes, fonte):
    cards = "".join(f'<div class="panel"><div class="tt">{esc(a)}</div><div class="dd">{rich(b)}</div></div>' for a, b in cartoes)
    inner = top(n, t) + (
        f'<div class="col"><h2 class="h">{rich(h)}</h2><p class="p">{rich(p)}</p><div class="two">{cards}</div>'
        f'<div class="src">{rich(fonte)}</div></div>')
    return pagina("cartoes", inner)


def linha_tempo(n, t, h, linhas, nota, fonte):
    rows = "".join(
        f'<div class="row"><div class="d">{esc(d)}</div><div class="t">{rich(x)}</div></div>' for d, x in linhas)
    inner = top(n, t) + (
        f'<div class="col"><h2 class="h">{rich(h)}</h2><div class="tl">{rows}</div><p class="p s">{rich(nota)}</p>'
        f'<div class="src">{rich(fonte)}</div></div>')
    return pagina("linha-do-tempo", inner)


CHECK = ('<svg viewBox="0 0 52 52"><circle cx="26" cy="26" r="24" fill="none" stroke="#1963a6" stroke-width="1.5"/>'
         '<path d="M15 27 L23 35 L38 18" fill="none" stroke="#1aa0c5" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/></svg>')


def fecho(n, t, h, itens, botao, nota):
    rows = "".join(f'<div class="row">{CHECK}<span>{esc(i)}</span></div>' for i in itens)
    inner = top(n, t) + (
        f'<div class="col"><h2 class="h">{rich(h)}</h2><div class="chk">{rows}</div>'
        f'<div class="cta"><span>{esc(botao)}</span><span>→</span></div><p class="note">{esc(nota)}</p>'
        f'<div class="lock"><div class="n">hélio levi</div><div class="mono t">Back-end · Systems</div></div></div>')
    return pagina("fecho", inner, "mare")


def fluxo(n, t, h, etapas, botao, nota):
    rows = "".join(
        f'<div class="st"><span class="dot on"></span><span class="nm">{esc(a)}</span><span class="q">{esc(b)}</span></div>'
        for a, b in etapas)
    inner = top(n, t) + (
        f'<div class="col"><h2 class="h">{rich(h)}</h2><div class="flow">{rows}</div>'
        f'<div class="cta"><span>{esc(botao)}</span><span>→</span></div><p class="note">{esc(nota)}</p>'
        f'<div class="lock"><div class="n">hélio levi</div><div class="mono t">Back-end · Systems</div></div></div>')
    return pagina("fluxo", inner, "mare")


def story(h, sub, tag, linhas, dica):
    bloco = painel(tag, linhas) if linhas else ""
    inner = (f'<div class="top"><div class="l"><span class="node"></span><span>hl.build</span></div>'
             f'<div class="r">{esc(dica)}</div></div>'
             f'<div class="col"><h1 class="h">{rich(h)}</h1><p class="p s">{rich(sub)}</p>{bloco}<div class="stk"></div></div>')
    return pagina("story", inner, "mare", story=True)


# ---------- conteúdo ----------
POSTS = {}

# 1) Black Friday (seg 02/11, 10h) -- IG5 listicle, meta: salvamentos
T = 8
POSTS["2026-11-02_carrossel-black-friday-checkout"] = [
    capa_num(1, T, "25", "dias até 27/11", "Seu checkout aguenta a **Black Friday**?", "Desliza: 5 testes que eu faria hoje"),
    contexto(2, T, "O dia não muda de data. O **checkout** precisa estar pronto.",
             "A Black Friday cai em 27 de novembro. O tráfego da data pode multiplicar o volume normal várias vezes, e um site que segura o dia comum pode cair no pico.\n\n5 testes, um por tela. O último fecha o caixa.",
             "Fontes: Central do Varejo, Trendtrack (2026)",
             '<div class="bignum" style="font-size:230px;color:var(--cobalt);margin:0 0 24px">27/11</div>'),
    teste(3, T, "01", "O Pix chega **identificado**?",
          "Cada cobrança nasce com o número do pedido. Sem isso, no dia de pico você cruza valor e hora no extrato.",
          "Cobrança", ["{", '  "pedido": 1042,', '  "valor": 150.00,', '  "status": "ATIVA"', "}"]),
    teste(4, T, "02", "O **estoque** fala com a loja?",
          "Quem vende no site e na loja física precisa de estoque sincronizado. Senão, um canal vende o que o outro já esgotou.",
          "Estoque", ["sku 8841", "loja  estoque: 1", "site  estoque: 1", "~venda no site baixa nos dois canais~", "loja  estoque: 0", "site  estoque: 0"],
          "Fonte: Linx Commerce, via Central do Varejo"),
    teste(5, T, "03", "O site aguenta o dia de **pico**?",
          "Teste com mais gente do que o dia comum. O que segura o normal pode cair quando o tráfego multiplica.",
          "Plano de teste (exemplo)", ["dia comum .......... 1x", "teste 1 ............ 2x", "teste 2 ............ 5x", "^meta: sem erro e sem fila^"]),
    teste(6, T, "04", "Quando um pagamento falha, alguém **sabe**?",
          "Sem alerta, a falha vira reclamação do cliente. Com registro e aviso, você vê na hora o que quebrou.",
          "Registro de eventos",
          ["14:02:11  pix.recebido    ok", "14:02:12  pedido.pago     ok", "^14:02:12  nota.emitida   FALHA^", "14:02:12  alerta.enviado financeiro"]),
    teste(7, T, "05", "Na segunda-feira, quem **concilia**?",
          "Depois do pico vem a conferência de Pix, pedido e nota. Quando o sistema registra cada evento, a lista de divergências sai pronta.",
          "Conciliação diária",
          ["pedidos pagos  = pix recebidos   ok", "notas emitidas = pedidos pagos   ok", "^divergências   = lista pronta^"]),
    fecho(8, T, "Faltam 25 dias. Dá tempo de **testar**.",
          ["Pix identificado por pedido", "Estoque sincronizado", "Teste de pico feito", "Alerta de falha ligado", "Conciliação pronta"],
          "Link na bio", "Salva pra conferir na semana da Black Friday."),
]

# 2) Nota fiscal IBS/CBS (qua 04/11, 10h) -- IG7 myth-buster, meta: compartilhamentos
T = 7
POSTS["2026-11-04_carrossel-nota-autorizada-nao-e-nota-certa"] = [
    capa_log(1, T, "Sua nota foi **autorizada**. Isso não quer dizer que está certa.", "NF-e modelo 55",
             ["status ............ AUTORIZADA", "grupo IBS/CBS ..... ^ausente^", "obrigação .......... ^mantida^"],
             "Desliza: o que mudou na nota"),
    contexto(2, T, "A rejeição foi **suspensa**. A obrigação, não.",
             "Desde 3 de agosto de 2026, a NF-e e a NFC-e de quem está no Lucro Presumido ou Real precisam trazer IBS e CBS. A rejeição automática da nota sem esses campos foi suspensa em 31 de julho, sem nova data.",
             "Fontes: Ato Conjunto RFB/CGIBS nº 4/2026, Ato Técnico Conjunto CGIBS/RFB nº 1/2026",
             painel("Situação da NF-e", ["campos IBS/CBS ... ^obrigatórios^", "rejeição automática ... ^suspensa^"])),
    dois_cartoes(3, T, "Autorizada não é **regular**.",
                 "A nota segue sendo autorizada, por enquanto. Mas em 6 de agosto a Receita e o Comitê Gestor do IBS disseram que o dever de informar IBS e CBS continua.",
                 [("Autorizada", "O sistema aceitou o arquivo."), ("Regular", "Os campos obrigatórios estão preenchidos.")],
                 "Fonte: Baguete, 02/09/2026"),
    teste(4, T, "", "Cada produto precisa de um **código**.",
          "O cadastro de produtos e serviços precisa trazer o CST-IBS/CBS (Código de Situação Tributária) e o cClassTrib (Código de Classificação Tributária).",
          "Cadastro de produto", ["produto 8841", "cst_ibs_cbs ........ ^[preencher]^", "cclasstrib ......... ^[preencher]^", "~definido com o contador~"],
          "Fonte: Baguete, 02/09/2026").replace('<div class="num"></div>', ""),
    teste(5, T, "", "Quem valida é o seu **sistema**.",
          "Se a rejeição não vem do governo, ela precisa vir do seu sistema: bloquear a emissão quando faltar campo e registrar cada nota.",
          "Emissão de nota", ["emitir_nota(pedido 1042)", "falha: cst_ibs_cbs ausente", "emissão bloqueada", "pendência criada no painel"]).replace('<div class="num"></div>', ""),
    linha_tempo(6, T, "O calendário das **ondas**.",
                [("03/08/2026", "NF-e e NFC-e"), ("01/10/2026", "NFS-e e NFCom"), ("01/12/2026", "Plataformas digitais"), ("01/01/2027", "Simples Nacional")],
                "NFS-e sem IBS/CBS não é rejeitada pelo sistema nacional até 31/12/2026, mas pode virar desconformidade.",
                "Fontes: Contmatic, Contábeis (2026)"),
    fecho(7, T, "A rejeição pode voltar por novo ato. Seu sistema precisa estar **pronto**.",
          ["Cadastro com CST e cClassTrib", "Validação antes de emitir", "Registro de cada nota", "Contador e sistema alinhados"],
          "Link na bio", "Não é consultoria tributária. Confirme o seu caso com o contador."),
]

# 3) Pix auditável (sex 06/11, 10h) -- IG8 framework, meta: salvamentos
T = 8
POSTS["2026-11-06_carrossel-pix-auditavel-5-eventos"] = [
    capa_log(1, T, "O caminho de um **Pix** em 5 eventos.", "Trilha do pedido 1042",
             ["14:02:10  cobranca.criada", "14:02:11  pix.recebido", "14:02:12  pedido.pago", "14:02:12  nota.emitida", "14:02:13  conciliado"],
             "Desliza: o mapa completo"),
    contexto(2, T, "Um Pix sem trilha é um **palpite**.",
             "Quando cada etapa vira um evento registrado, você responde sem abrir o extrato: quem pagou, quando e por quê.\n\nSe um dos 5 eventos falta, a conciliação vira adivinhação.",
             "Eventos de exemplo, em Node.js, Express e MongoDB",
             painel("Os 5 eventos", ["cobranca.criada", "pix.recebido", "pedido.pago", "nota.emitida", "conciliado"])),
    teste(3, T, "01", "A cobrança nasce com o **pedido**.",
          "Pedido, valor e validade já na criação. Sem isso, o Pix chega sem dono.",
          "cobranca.criada", ["{", '  "evento": "cobranca.criada",', '  "pedido": 1042,', '  "valor": 150.00', "}"]),
    teste(4, T, "02", "O banco avisa, o sistema **registra**.",
          "O recebimento chega por notificação e é gravado com horário e valor. Nada de abrir o app pra conferir.",
          "pix.recebido", ["{", '  "evento": "pix.recebido",', '  "pedido": 1042,', '  "valor": 150.00,', '  "hora": "14:02:11"', "}"]),
    teste(5, T, "03", "O pedido só muda de status com **prova**.",
          "O status vira PAGO porque existe um recebimento registrado, não porque alguém avisou no WhatsApp.",
          "pedido.pago", ["{", '  "evento": "pedido.pago",', '  "pedido": 1042,', '  "motivo": "pix.recebido"', "}"]),
    teste(6, T, "04", "A nota sai **amarrada** ao pagamento.",
          "Quem emite guarda o vínculo com o pedido e com o Pix. Depois fica fácil explicar cada nota.",
          "nota.emitida", ["{", '  "evento": "nota.emitida",', '  "pedido": 1042,', '  "vinculo": "pix.recebido"', "}"]),
    teste(7, T, "05", "O fechamento é uma **consulta**, não uma planilha.",
          "Com os quatro eventos, o sistema cruza tudo e mostra só o que não bateu.",
          "conciliado", ["{", '  "divergencias": 1,', '  "pedido": 1049,', '  "falta": "nota.emitida"', "}"]),
    fluxo(8, T, "O mapa pra **salvar**.",
          [("cobranca.criada", "nasce com o pedido"), ("pix.recebido", "chega com hora e valor"), ("pedido.pago", "muda com prova"),
           ("nota.emitida", "vinculada ao Pix"), ("conciliado", "só mostra o que não bateu")],
          "Link na bio", "Registros ilustrativos."),
]

# 4) Stories de interação (seg, qua, sex)
STORIES = {
    "2026-11-02_stories-interacao": [
        story("Como você confere o **Pix** hoje?", "Vota aí embaixo.", "Extrato",
              ["14:02  entrou R$ 150,00", "^?^      de qual pedido?"], "enquete"),
        story("Qual é a maior **dor** pra receber dos seus clientes?", "Responde na caixa aqui embaixo.", "Cobrança",
              ["cobrança enviada ... ok", "pagamento ......... ^?^"], "pergunta"),
        story("Qual % das planilhas de empresas reais auditadas tinha **erro**?", "Auditorias de campo desde 1995 (Panko).", "", [], "quiz"),
        story("Quer que eu olhe o seu **fluxo** de cobrança?", "Toca no link e vê como eu trabalho.", "", [], "link"),
    ]
}

if __name__ == "__main__":
    for pasta, telas in POSTS.items():
        d = RAIZ / "pautas" / pasta / "slides"
        d.mkdir(parents=True, exist_ok=True)
        for i, h in enumerate(telas, 1):
            (d / f"slide-{i:02d}.html").write_text(h, encoding="utf-8")
        print(pasta, len(telas), "telas")
    for pasta, telas in STORIES.items():
        d = RAIZ / "pautas" / pasta / "slides"
        d.mkdir(parents=True, exist_ok=True)
        for i, h in enumerate(telas, 1):
            (d / f"story-{i:02d}.html").write_text(h, encoding="utf-8")
        print(pasta, len(telas), "stories")
