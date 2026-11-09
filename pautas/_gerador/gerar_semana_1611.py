"""Artes da semana de 16/11/2026 (1 carrossel educativo e 4 stories) no padrão visual da HL.

Reaproveita os componentes de gerar.py (mesmo CSS, fontes e tipos de tela).
O reel da semana tem gerador próprio em pautas/2026-11-17_reel-pix-pago-aguardando/.

Uso:  python3 -I pautas/_gerador/gerar_semana_1611.py     (gera os HTML em pautas/<post>/slides/)
      python3 -I pautas/_gerador/render.py 2026-11-1 /tmp/png   (PNG fora do repo, até a aprovação)

Marcação de texto: **palavra** = ciano (uma por título), ~texto~ = comentário esmaecido,
^texto^ = destaque ciano dentro de bloco de código.
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import gerar as g  # noqa: E402
from gerar_semana_0911 import capa_dado  # noqa: E402

RAIZ = g.RAIZ

# 1) Educativo (qua 18/11, 18h): Pix contestado e a trilha da venda. Público: lojas virtuais e PMEs que vendem por Pix.
T = 8
FONTES_MED = "Fontes: Tecnoblog (02/02/2026), Finsiders Brasil (27/01/2026)"
POSTS = {
    "2026-11-18_carrossel-pix-contestado-prova-da-venda": [
        capa_dado(1, T, "11 dias", "prazo que o BC espera para devolver um Pix contestado · MED 2.0",
                  "Cliente contestou um **Pix**. Seu sistema prova a venda?", "Desliza: 5 registros pra guardar", 190),
        g.contexto(2, T, "O MED 2.0 segue o **caminho** do dinheiro.",
                   "Desde 2 de fevereiro de 2026, o MED 2.0 é obrigatório no Pix. Ele rastreia o caminho do dinheiro, e o Banco Central espera a devolução em até 11 dias depois da contestação.\n\nVale para fraude, golpe, coerção ou erro da instituição. Desacordo comercial não entra.\n\nDurante a análise, o valor pode ficar bloqueado nas contas envolvidas. Por isso, eu deixo a trilha da venda pronta antes.",
                   FONTES_MED + ", Transfeera (25/02/2026)"),
        g.teste(3, T, "01", "O **pedido** e tudo que foi vendido.",
                "O que o cliente comprou, por quanto e quando. É o começo da trilha.",
                "pedido.criado", ["pedido ........... 2087", "itens ............ 2", "valor ........... R$ 240,00", "criado em ....... ^14:02^"]),
        g.teste(4, T, "02", "A **cobrança** que gerou o Pix.",
                "O txid amarra a cobrança ao pedido. Sem ele, o Pix cai solto no extrato.",
                "cobranca.criada", ["txid ............ ^a91f…c20^", "pedido ........... 2087", "valor ........... R$ 240,00", "expira em ....... 14:32"]),
        g.teste(5, T, "03", "O **Pix** que chegou.",
                "O identificador de ponta a ponta e a hora exata ficam guardados, sem depender do extrato.",
                "pix.recebido", ["end_to_end ..... E00000000…e5f", "txid ............ a91f…c20", "pagador ......... Ana M.", "recebido às ..... ^14:05^"]),
        g.teste(6, T, "04", "A **entrega** que fecha a venda.",
                "Venda de produto tem entrega. O rastreio e a data ficam presos ao mesmo pedido.",
                "entrega.confirmada", ["pedido ........... 2087", "enviado ......... 16/11", "entregue ........ ^18/11^", "rastreio ........ guardado"]),
        g.teste(7, T, "05", "O **atendimento** com data e hora.",
                "Cliente perguntou, loja respondeu. A conversa fica registrada no pedido, não só no celular de alguém.",
                "contato.registrado", ["pedido ........... 2087", "cliente perguntou . ^09:12^", "loja respondeu ... 09:20"]),
        g.fluxo(8, T, "Os 5 registros pra **salvar**.",
                [("pedido.criado", "o que foi vendido"), ("cobranca.criada", "txid ligado ao pedido"), ("pix.recebido", "end_to_end e hora"),
                 ("entrega.confirmada", "rastreio guardado"), ("contato.registrado", "conversa com data e hora")],
                "Link na bio", "Exemplos ilustrativos. Não é consultoria jurídica."),
    ],
}

# 2) Stories (seg 16/11 e qua 18/11, 12h30; qui 19/11 já tem os stories do case da Fernanda)
STORIES = {
    "2026-11-16_stories-interacao": [
        g.story("Seu Pix foi pago e o pedido ficou **aguardando**?", "Vota aí embaixo.", "Pedido 2087",
                ["pix.recebido ........ ok", "pedido.status ....... ^aguardando^"], "enquete"),
        g.story("Amanhã, 18h: 3 **motivos** de um Pix pago continuar aguardando.", "Ativa o lembrete.", "", [], "contagem"),
        g.story("Em quantos dias o BC espera **devolver** um Pix contestado por fraude?", "Quiz. A resposta está no post de hoje, 18h.", "", [], "quiz"),
        g.story("Qual a sua maior dúvida sobre **Pix** na loja?", "Cobrança, conciliação, devolução? Conta na caixinha.", "Dúvida do dia",
                ["cobrança", "conciliação", "^devolução^"], "pergunta"),
    ],
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
