"""Gera reel.html: reel de 18,3 s (1080x1920, 30 fps) "Conferir Pix na mão custa 44 h por ano".

A animação é determinística: seek(t) posiciona tudo no instante t (sem CSS transitions).
Uso:  python3 -I pautas/2026-11-10_reel-conferir-pix-44h/gerar_reel.py
      python3 -I pautas/2026-11-10_reel-conferir-pix-44h/render_reel.py <pasta-de-saida>
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
.sc{position:absolute;inset:0;opacity:0;will-change:auto}
.lab{font-family:"JetBrains Mono",monospace;font-weight:600;font-size:34px;letter-spacing:.08em;text-transform:uppercase;color:var(--muted)}
.big{font-family:"Lexend Exa",sans-serif;font-weight:500;color:var(--foam);letter-spacing:-.045em;line-height:.9}
.t1{font-family:"Lexend Exa",sans-serif;font-weight:500;color:var(--foam);line-height:1.1;letter-spacing:-.012em}
.ln{min-height:70px;font-family:"JetBrains Mono",monospace;font-weight:500;font-size:46px;line-height:1.5;color:var(--foam);white-space:pre}
.panel.r{padding:30px 34px}
.bar{height:60px;border-radius:8px;transform-origin:left center}
.sub{font-size:38px;font-weight:600;color:var(--muted);line-height:1.35}
.cur{display:inline-block;width:.6em;height:1em;background:var(--cyan);vertical-align:-.12em;margin-left:2px}
.pill{position:absolute;left:70px;top:1440px;z-index:6;opacity:0}
"""

BODY = """
<div class="slide story" id="root">
 <div class="mare"></div><div class="grain"></div>
 <div class="brand"><span class="node"></span><span>hl.build</span></div>

 <!-- A: gancho -->
 <div class="sc" id="A"><div class="wrap" style="top:560px">
   <div class="lab">Conferir Pix na mão custa</div>
   <div class="big" style="font-size:430px;margin-top:54px"><span id="n44">44</span><span class="cy">h</span></div>
   <div class="t1" style="font-size:84px;margin-top:40px">por ano.</div>
 </div></div>

 <!-- B: a conta -->
 <div class="sc" id="B"><div class="wrap" style="top:520px">
   <h2 class="t1" style="font-size:92px">Faça a <span class="cy">conta</span>.</h2>
   <div class="panel r" style="margin-top:60px" id="pB">
     <div class="tag mono" style="display:flex;justify-content:space-between;margin-bottom:18px;font-size:26px"><span>Conferência do Pix</span><span class="i" style="text-transform:none;color:#7f98b6">// ilustrativo</span></div>
     <div class="ln" data-s="4.15" data-raw="10 min por dia útil"></div>
     <div class="ln" data-s="5.92" data-raw="× 22 dias úteis"></div>
     <div class="ln" data-s="7.0" data-raw="= 220 min (3h40 por mês)"></div>
     <div class="ln" data-s="7.85" data-raw="× 12 meses"></div>
     <div class="ln" data-s="9.5" data-raw="= ^2.640 min = 44 h^"></div>
   </div>
   <div class="sub" id="subB" style="margin-top:44px;opacity:0">Troque pelos seus números.</div>
 </div></div>

 <!-- C: virada -->
 <div class="sc" id="C"><div class="wrap" style="top:520px">
   <h2 class="t1" style="font-size:88px">Mais que uma <span class="cy">semana</span> de trabalho.</h2>
   <div style="margin-top:90px">
     <div class="lab" style="font-size:30px">Semana de trabalho · 40 h</div>
     <div class="bar" id="b40" style="width:800px;background:#1963a6;margin-top:18px"></div>
   </div>
   <div style="margin-top:64px">
     <div class="lab" style="font-size:30px;color:var(--foam)">Conferindo Pix · 44 h</div>
     <div class="bar" id="b44" style="width:880px;background:#22c3e6;margin-top:18px"></div>
   </div>
 </div></div>

 <!-- D: solução -->
 <div class="sc" id="D"><div class="wrap" style="top:520px">
   <h2 class="t1" style="font-size:70px">Com o Pix identificado, sobra só a <span class="cy">divergência</span>.</h2>
   <div class="panel r" style="margin-top:56px">
     <div class="tag mono" style="display:flex;justify-content:space-between;margin-bottom:18px;font-size:26px"><span>Conciliação do dia</span><span class="i" style="text-transform:none;color:#7f98b6">// ilustrativo</span></div>
     <div class="ln" style="font-size:38px" data-s="14.0" data-raw="pedidos = pix recebidos     ok"></div>
     <div class="ln" style="font-size:38px" data-s="14.6" data-raw="notas = pedidos pagos       ok"></div>
     <div class="ln" style="font-size:38px" data-s="15.5" data-raw="^divergência: 1 (pedido 1049)^"></div>
   </div>
 </div></div>

 <div class="pill" id="pill">
   <div class="cta" style="height:104px;font-size:32px"><span>Manda pra quem fecha o caixa</span></div>
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
  el.style.transform=`translateY(${((1-ease(i))*rise).toFixed(1)}px) scale(${(1+(1-i)*0.012).toFixed(4)})`;
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
  // A: gancho (0 a 3) e retorno do loop (17,95 a 18,3). Tempos sincronizados com a voz (ElevenLabs).
  const a1=cl((2.95-t)/.3), a2=cl((t-17.95)/.35);
  const A=$('A'); A.style.opacity=(t<3.1?a1:a2).toFixed(3);
  A.style.transform=`scale(${(1.06-0.06*cl(t/2.6)).toFixed(4)})`;
  $("n44").textContent=44;
  // B: a conta
  win($('B'),t,2.85,11.2,.3,.3);
  // C: virada
  win($('C'),t,11.1,13.5,.3,.3);
  $('b40').style.transform=`scaleX(${P(t,11.55,.7).toFixed(3)})`;
  $('b44').style.transform=`scaleX(${P(t,12.1,.8).toFixed(3)})`;
  // D: solução
  win($('D'),t,13.35,17.95,.3,.3);
  // linhas digitadas
  for(const el of lines){
    const s=parseFloat(el.dataset.s), k=Math.floor(Math.max(0,t-s)*42);
    const raw=el.dataset.raw, full=raw.replace(/\\^/g,'').length;
    const active=t>=s && k<full;
    el.innerHTML=typed(raw,k)+(active?'<span class="cur"></span>':'');
  }
  $('subB').style.opacity=P(t,10.2,.4).toFixed(3);
  // CTA
  const p=$('pill'); const pi=P(t,16.45,.35), po=cl((17.95-t)/.3);
  p.style.opacity=(pi*po).toFixed(3); p.style.transform=`translateY(${((1-pi)*30).toFixed(1)}px)`;
}
document.fonts.ready.then(()=>seek(0));
"""

HTML = (f'<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>reel conferir pix 44h</title>'
        f'<style>{CSS}</style></head><body>{BODY}<script>{JS}</script></body></html>')

if __name__ == "__main__":
    (AQUI / "reel.html").write_text(HTML, encoding="utf-8")
    print("reel.html ok")
