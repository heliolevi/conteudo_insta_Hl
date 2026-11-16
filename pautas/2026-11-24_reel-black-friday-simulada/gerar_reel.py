"""Gera reel.html: reel de 16 s (1080x1920, 30 fps) "Simulei uma Black Friday de 500 Pix". Números lidos de resultado.json.

Sem áudio: todo o texto está na tela (o reel funciona no mudo). Animação determinística:
seek(t) posiciona tudo no instante t (sem CSS transitions).
Uso:  python3 -I pautas/2026-11-24_reel-black-friday-simulada/gerar_reel.py
      python3 -I pautas/2026-11-24_reel-black-friday-simulada/render_reel.py <pasta-de-saida>
"""
import json
import pathlib
import sys

AQUI = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI.parent / "_gerador"))
import gerar as g  # noqa: E402

CSS = g.CSS.replace("FONTES", "../_gerador/fonts") + """
html,body{width:1080px;height:1920px;overflow:hidden}
.slide.story{width:1080px;height:1920px}
.wrap{position:absolute;left:70px;width:880px;z-index:3}
.brand{position:absolute;left:70px;top:270px;z-index:5;display:flex;align-items:center;gap:16px;
 font-family:"JetBrains Mono",monospace;font-weight:500;font-size:28px;letter-spacing:.04em;color:var(--foam)}
.sc{position:absolute;inset:0;opacity:0}
.lab{font-family:"JetBrains Mono",monospace;font-weight:600;font-size:34px;letter-spacing:.08em;text-transform:uppercase;color:var(--muted)}
.big{font-family:"Lexend Exa",sans-serif;font-weight:500;color:var(--foam);letter-spacing:-.045em;line-height:.9}
.t1{font-family:"Lexend Exa",sans-serif;font-weight:500;color:var(--foam);line-height:1.12;letter-spacing:-.012em}
.ln{min-height:60px;font-family:"JetBrains Mono",monospace;font-weight:500;font-size:38px;line-height:1.55;color:var(--foam);white-space:pre}
.panel.r{padding:30px 34px}
.cur{display:inline-block;width:.6em;height:1em;background:var(--cyan);vertical-align:-.12em;margin-left:2px}
.pill{position:absolute;left:70px;top:1300px;z-index:6;opacity:0}
.step{font-family:"JetBrains Mono",monospace;font-weight:600;font-size:40px;letter-spacing:.08em;color:var(--cobalt);margin-bottom:22px}
"""


def painel(tag, linhas):
    """Bloco de log com linhas digitadas: cada linha = (instante de início, texto com ^destaque^)."""
    rows = "".join(f'<div class="ln" data-s="{s}" data-raw="{r}"></div>' for s, r in linhas)
    return (f'<div class="panel r" style="margin-top:56px"><div class="tag mono" style="display:flex;justify-content:space-between;'
            f'margin-bottom:18px;font-size:26px"><span>{tag}</span><span class="i" style="text-transform:none;color:#7f98b6">// ilustrativo</span></div>'
            f'{rows}</div>')


SIM = json.loads((AQUI / "resultado.json").read_text(encoding="utf-8"))
C, A = SIM["contagem"], SIM["amostras"]
SEM_TXID = C["casado_valor_hora"] + C["fila_ambiguo"] + C["fila_sem_candidato"]


def brl(v):
    return f"R$ {v:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


BODY = f"""
<div class="slide story" id="root">
 <div class="mare"></div><div class="grain"></div>
 <div class="brand"><span class="node"></span><span>hl.build</span></div>
 <div class="sim">SIMULAÇÃO · DADOS FICTÍCIOS</div>

 <!-- A: gancho com movimento desde 0,0 s (contador 0 a 500 e log rodando) e loop (15,7 a 16 s) -->
 <div class="sc" id="A"><div class="wrap" style="top:430px">
   <div class="lab">Black Friday simulada</div>
   <div class="big" id="cnt" style="font-size:400px;margin-top:36px">0</div>
   <div class="t1" style="font-size:62px;margin-top:26px">Pix em um dia. Quantos você confere <span class="cy">na mão</span>?</div>
   <div class="panel r" style="margin-top:54px"><div class="tag mono" style="display:flex;justify-content:space-between;margin-bottom:14px;font-size:26px"><span>pix.recebido</span><span class="i" style="text-transform:none;color:#7f98b6">// ilustrativo</span></div>
   <div class="ln" id="lg0"></div><div class="ln" id="lg1"></div><div class="ln" id="lg2"></div></div>
 </div></div>

 <!-- B: avisos em dobro -->
 <div class="sc" id="B"><div class="wrap" style="top:620px">
   <div class="step">01</div>
   <h2 class="t1" style="font-size:84px">{C['duplicado_ignorado']} avisos vieram em <span class="cy">dobro</span>.</h2>
   {painel("Regra 1: baixar uma vez", [(3.4, f"{A['duplicado']['hora']}  {A['duplicado']['txid']}  baixado"), (4.2, f"{A['duplicado']['hora']}  {A['duplicado']['txid']}  ^em dobro: ignorado^")])}
 </div></div>

 <!-- C: sem txid -->
 <div class="sc" id="C"><div class="wrap" style="top:620px">
   <div class="step">02</div>
   <h2 class="t1" style="font-size:84px">{SEM_TXID} Pix vieram sem <span class="cy">txid</span>.</h2>
   {painel("Regra 2: valor e horário", [(6.6, f"Pix sem txid  {brl(A['casado']['valor'])}"), (7.3, "cobranças pendentes ... 1"), (8.0, f"^casado: pedido {A['casado']['pedido']}^")])}
 </div></div>

 <!-- D: avisos perdidos -->
 <div class="sc" id="D"><div class="wrap" style="top:620px">
   <div class="step">03</div>
   <h2 class="t1" style="font-size:84px">{C['varredura']} avisos <span class="cy">sumiram</span>.</h2>
   {painel("Regra 3: varredura", [(9.8, f"txid {A['varredura']['txid']} ... sem aviso"), (10.5, f"extrato ... {brl(A['varredura']['valor'])}"), (11.2, "^baixado pela varredura^")])}
 </div></div>

 <!-- E: resultado -->
 <div class="sc" id="E"><div class="wrap" style="top:540px">
   <h2 class="t1" style="font-size:78px">Sobraram <span class="cy">{SIM['fila_na_mao']}</span> para conferir na mão.</h2>
   {painel("Fim do dia", [(12.9, f"pedidos ............ {SIM['pedidos']}"), (13.3, f"baixados sozinhos .. {SIM['automaticos']}"), (13.7, f"fila na mão ........ ^{SIM['fila_na_mao']}^")])}
 </div></div>

 <div class="pill" id="pill">
   <div class="cta" style="height:104px;font-size:30px"><span>Manda pra quem fecha o caixa</span></div>
   <div style="margin-top:26px;font-size:36px;font-weight:700;color:var(--foam)">Link na bio.</div>
 </div>
</div>
"""

JS = """
const cl=(x,a=0,b=1)=>Math.min(b,Math.max(a,x));
const ease=x=>1-Math.pow(1-x,3);
const P=(t,s,d)=>ease(cl((t-s)/d));
const $=id=>document.getElementById(id);
function win(el,t,s,e,fi=.28,fo=.28,rise=26){
  const i=cl((t-s)/fi), o=cl((e-t)/fo);
  el.style.opacity=(i*o).toFixed(3);
  el.style.transform=`translateY(${((1-ease(i))*rise).toFixed(1)}px)`;
}
function typed(raw,n){
  let out='',hi=false,c=0;
  for(const ch of raw){
    if(ch==='^'){hi=!hi;out+=hi?'<span class="k">':'</span>';continue}
    if(c>=n)break; out+=(ch==='<'?'&lt;':ch); c++;
  }
  if(hi)out+='</span>'; return out;
}
const lines=[...document.querySelectorAll('.ln[data-s]')];
const FIM=NPED;
function contador(t){
  // 0 a 2,5 s sobe de 0 a FIM; depois fica; no loop (>=15,7 s) já mostra FIM
  const n=(t>=15.7)?FIM:Math.round(FIM*ease(cl(t/2.5)));
  $('cnt').textContent=n;
  for(let k=0;k<3;k++){
    const id=1000+Math.max(1,n-(2-k));
    $('lg'+k).innerHTML=n<1?'':`pix.recebido  T${id}  <span class="k">ok</span>`;
  }
}
function seek(t){
  contador(t);
  const a1=cl((2.95-t)/.3), a2=cl((t-15.7)/.3);
  $('A').style.opacity=(t<3.2?a1:a2).toFixed(3);
  win($('B'),t,2.9,6.5,.3,.3);
  win($('C'),t,6.2,9.7,.3,.3);
  win($('D'),t,9.4,12.9,.3,.3);
  win($('E'),t,12.55,15.75,.3,.3);
  for(const el of lines){
    const s=parseFloat(el.dataset.s), k=Math.floor(Math.max(0,t-s)*44);
    const raw=el.dataset.raw, full=raw.replace(/\\^/g,'').length;
    const active=t>=s && k<full;
    el.innerHTML=typed(raw,k)+(active?'<span class="cur"></span>':'');
  }
  const p=$('pill'); const pi=P(t,14.4,.35), po=cl((15.7-t)/.3);
  p.style.opacity=(pi*po).toFixed(3); p.style.transform=`translateY(${((1-pi)*30).toFixed(1)}px)`;
}
document.fonts.ready.then(()=>seek(0));
""".replace("NPED", str(SIM["pedidos"]))

HTML = (f'<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>reel black friday simulada</title>'
        f'<style>{CSS}.sim{{position:absolute;left:70px;top:1570px;z-index:5;font-family:"JetBrains Mono",monospace;font-weight:500;font-size:26px;letter-spacing:.08em;color:var(--muted)}}</style></head><body>{BODY}<script>{JS}</script></body></html>')

if __name__ == "__main__":
    (AQUI / "reel.html").write_text(HTML, encoding="utf-8")
    print("reel.html ok")
