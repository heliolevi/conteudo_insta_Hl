"""Gera reel.html: reel de 16 s (1080x1920, 30 fps) "3 motivos para um Pix pago continuar aguardando".

Sem áudio: todo o texto está na tela (o reel funciona no mudo). Animação determinística:
seek(t) posiciona tudo no instante t (sem CSS transitions).
Uso:  python3 -I pautas/2026-11-17_reel-pix-pago-aguardando/gerar_reel.py
      python3 -I pautas/2026-11-17_reel-pix-pago-aguardando/render_reel.py <pasta-de-saida>
"""
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
.pill{position:absolute;left:70px;top:1440px;z-index:6;opacity:0}
.step{font-family:"JetBrains Mono",monospace;font-weight:600;font-size:40px;letter-spacing:.08em;color:var(--cobalt);margin-bottom:22px}
"""


def painel(tag, linhas):
    """Bloco de log com linhas digitadas: cada linha = (instante de início, texto com ^destaque^)."""
    rows = "".join(f'<div class="ln" data-s="{s}" data-raw="{r}"></div>' for s, r in linhas)
    return (f'<div class="panel r" style="margin-top:56px"><div class="tag mono" style="display:flex;justify-content:space-between;'
            f'margin-bottom:18px;font-size:26px"><span>{tag}</span><span class="i" style="text-transform:none;color:#7f98b6">// ilustrativo</span></div>'
            f'{rows}</div>')


BODY = f"""
<div class="slide story" id="root">
 <div class="mare"></div><div class="grain"></div>
 <div class="brand"><span class="node"></span><span>hl.build</span></div>

 <!-- A: gancho (0 a 2,9 s) e loop (15,7 a 16 s) -->
 <div class="sc" id="A"><div class="wrap" style="top:470px">
   <div class="lab">Pix pago. Pedido parado.</div>
   <div class="big" style="font-size:400px;margin-top:40px">3</div>
   <div class="t1" style="font-size:66px;margin-top:30px">motivos para um Pix pago continuar <span class="cy">aguardando</span>.</div>
   {painel("Pedido 2087", [(0.0, "pix.recebido ........ ok"), (0.2, "pedido.status ....... ^aguardando^")])}
 </div></div>

 <!-- B: 01 -->
 <div class="sc" id="B"><div class="wrap" style="top:640px">
   <div class="step">01</div>
   <h2 class="t1" style="font-size:84px">O aviso não <span class="cy">chegou</span>.</h2>
   {painel("Webhook do Pix", [(3.3, "POST /webhook/pix"), (3.9, "resposta ....... ^504 timeout^"), (4.7, "pedido ........... aguardando")])}
 </div></div>

 <!-- C: 02 -->
 <div class="sc" id="C"><div class="wrap" style="top:640px">
   <div class="step">02</div>
   <h2 class="t1" style="font-size:84px">O aviso veio sem <span class="cy">pedido</span>.</h2>
   {painel("pix.recebido", [(6.5, "valor ........... R$ 240,00"), (7.1, "txid ............. ^vazio^"), (7.9, "pedido ........... não achado")])}
 </div></div>

 <!-- D: 03 -->
 <div class="sc" id="D"><div class="wrap" style="top:640px">
   <div class="step">03</div>
   <h2 class="t1" style="font-size:84px">Deu erro e <span class="cy">ninguém</span> viu.</h2>
   {painel("Fila de eventos", [(9.8, "erro ............. gravado"), (10.4, "alerta ........... ^nenhum^"), (11.1, "reprocesso ....... ^nenhum^")])}
 </div></div>

 <!-- E: solução -->
 <div class="sc" id="E"><div class="wrap" style="top:560px">
   <h2 class="t1" style="font-size:72px">Registrar, tentar de novo e <span class="cy">conciliar</span> pelo txid.</h2>
   {painel("Evento do Pix", [(12.9, "evento ........... registrado"), (13.3, "tentativa 1 ...... falhou"), (13.7, "tentativa 2 ...... ok"), (14.1, "pedido ........... ^pago^")])}
 </div></div>

 <div class="pill" id="pill">
   <div class="cta" style="height:104px;font-size:30px"><span>Manda pra quem cuida da loja</span></div>
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
const lines=[...document.querySelectorAll('.ln')];
function seek(t){
  // A: gancho (0 a 2,9 s) e retorno do loop (15,7 a 16 s)
  const a1=cl((2.9-t)/.3), a2=cl((t-15.7)/.3);
  $('A').style.opacity=(t<3.1?a1:a2).toFixed(3);
  $('A').style.transform=`scale(${(1.05-0.05*cl(t/2.6)).toFixed(4)})`;
  win($('B'),t,2.85,6.4,.3,.3);
  win($('C'),t,6.05,9.9,.3,.3);
  win($('D'),t,9.5,12.9,.3,.3);
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
"""

HTML = (f'<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>reel pix pago aguardando</title>'
        f'<style>{CSS}</style></head><body>{BODY}<script>{JS}</script></body></html>')

if __name__ == "__main__":
    (AQUI / "reel.html").write_text(HTML, encoding="utf-8")
    print("reel.html ok")
