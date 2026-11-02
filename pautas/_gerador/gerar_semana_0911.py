"""Artes da semana de 09/11/2026 (2 carrosséis e 5 stories) no padrão visual da HL.

Reaproveita os componentes de gerar.py (mesmo CSS, fontes e tipos de tela).

Uso:  python3 -I pautas/_gerador/gerar_semana_0911.py     (gera os HTML em pautas/<post>/slides/)
      python3 -I pautas/_gerador/render.py 2026-11-1 /tmp/png   (PNG fora do repo, até a aprovação)

Marcação de texto: **palavra** = ciano (uma por título), ~texto~ = comentário esmaecido,
^texto^ = destaque ciano dentro de bloco de código.
"""
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import gerar as g  # noqa: E402

RAIZ = g.RAIZ


def capa_dado(n, t, num, label, h, hint, tam):
    """Capa com número grande (tamanho ajustável, para textos como '14 mil')."""
    inner = g.top(n, t) + (
        f'<div class="col"><h1 class="h xl">{g.rich(h)}</h1><div class="spacer"></div>'
        f'<div class="bignum" style="font-size:{tam}px">{g.esc(num)}</div>'
        f'<div class="mono biglab">{g.esc(label)}</div><div class="spacer"></div>'
        f'<div class="hint"><span class="mono" style="color:var(--ink)">{g.esc(hint)}</span><span class="a">→</span></div></div>')
    return g.pagina("capa", inner, "mare")


POSTS = {}

# 1) Educativo: Pix Automático (qua 11/11, 10h) -- checklist para salvar, público primário (PMEs que cobram recorrência)
T = 8
FONTE_PA = "Fonte: Celcoin, guia do Pix Automático"
POSTS["2026-11-11_carrossel-pix-automatico-5-perguntas"] = [
    capa_dado(1, T, "14 mil", "recebedores · o BC informou em ago/2026",
              "Seu sistema está pronto para o **Pix Automático**?", "Desliza: 5 perguntas pro seu sistema", 215),
    g.contexto(2, T, "O cliente autoriza **uma vez**. A cobrança chega sozinha.",
               "No 2º trimestre de 2026, o Pix Automático movimentou R$ 3,5 bilhões em 9,5 milhões de transações. O BC informou que os recebedores passaram de mil, no fim de 2025, para 14 mil.\n\n5 perguntas para o sistema que cobra os seus clientes. Uma por tela.",
               "Fonte: Finsiders Brasil (28/10/2026), com dados do Banco Central"),
    g.teste(3, T, "01", "Ele guarda a **autorização** de cada cliente?",
            "O cliente autoriza uma vez, no app do banco: recebedor, valor máximo e periodicidade. O sistema precisa guardar isso por cliente.",
            "autorizacao.criada", ["{", '  "cliente": 318,', '  "valor_maximo": 120.00,', '  "periodicidade": "mensal"', "}"],
            FONTE_PA),
    g.teste(4, T, "02", "Ele agenda na **janela** certa?",
            "A cobrança é agendada de 2 a 10 dias antes da liquidação. Fora dessa janela, o banco rejeita.",
            "cobranca.agendada", ["liquidacao ........ 07/12", "enviada ............ 30/11", "antecedencia ...... ^7 dias^"],
            FONTE_PA),
    g.teste(5, T, "03", "E se a cobrança **falhar**?",
            "O recebedor pode tentar de novo: até 3 retentativas em até 7 dias corridos após o vencimento. A regra nasce junto com a autorização.",
            "cobranca.recusada", ["motivo .............. saldo", "retentativas ........ ^até 3^", "prazo ............... 7 dias", "valor ............... o original"],
            "Fontes: documentação do Asaas e da Celcoin"),
    g.teste(6, T, "04", "O cliente cancelou. Alguém **sabe**?",
            "O pagador cancela a qualquer momento, pelo app do banco. Isso não encerra o contrato, então o sistema precisa avisar o financeiro.",
            "autorizacao.cancelada", ["cliente ............. 318", "cobrancas futuras .. ^canceladas^", "aviso ............... financeiro"],
            FONTE_PA),
    g.teste(7, T, "05", "A baixa cai no **cliente** certo?",
            "Cada Pix recebido precisa apontar para a autorização e para a fatura que ele paga. É isso que fecha o mês sem planilha.",
            "pix.recebido", ["autorizacao ......... 7731", "fatura .............. 2026-12", "baixa ............... ^automática^"]),
    g.fecho(8, T, "Alguma resposta foi **não sei**?",
            ["Guarda a autorização por cliente", "Agenda na janela certa", "Faz retentativa", "Registra o cancelamento", "Dá baixa no cliente certo"],
            "Link na bio", "Regras exatas: consulte o regulamento do Banco Central."),
]

# 2) Prova: Payments AI (sex 13/11, 10h) -- mapa para salvar, público secundário (loja virtual, fintech, software house)
T = 8
POSTS["2026-11-13_carrossel-5-checagens-pix-suspeito"] = [
    g.capa_log(1, T, "5 checagens antes de um **Pix** virar pedido pago.", "pix.recebido · pedido 2087",
               ["valor ............ R$ 1.490,00", "ticket médio ...... R$ 180,00", "checagens ........ ^3 de 5 acionadas^", "decisão ........... ^revisar^"],
               "Desliza: as 5 checagens"),
    g.contexto(2, T, "A Black Friday chega em **14 dias**.",
               "Pedido grande com Pix rápido é o cenário em que um sinal passa batido.\n\nEu construí o Payments AI, produto próprio de análise financeira e detecção de fraude. Aqui vão 5 checagens de exemplo, entre o Pix recebido e o pedido pago.",
               "Fonte da data: Central do Varejo (Black Friday em 27/11/2026)"),
    g.teste(3, T, "01", "Valor fora do **padrão**.",
            "Compare o valor com o ticket médio. Um pedido muitas vezes maior pede um segundo olhar.",
            "checagem.valor", ["ticket_medio ..... 180.00", "valor ............ 1490.00", "razao ............ ^8,3x^"]),
    g.teste(4, T, "02", "Pix em **sequência**.",
            "Vários Pix do mesmo pagador em poucos minutos mudam o risco do pedido.",
            "checagem.sequencia", ["pagador 5521", "14:02:10  pix  490.00", "14:03:25  pix  490.00", "14:05:02  pix  510.00", "^3 Pix em menos de 3 min^"]),
    g.teste(5, T, "03", "Pagador **novo**, pedido grande.",
            "Primeira compra com valor alto não prova nada. Entra como um sinal a mais na soma.",
            "checagem.historico", ["pagador 5521", "pedidos anteriores .. 0", "valor ............. 1490.00", "sinal ............. ^somar^"]),
    g.teste(6, T, "04", "O nome do titular não **bate**?",
            "Se quem pagou é diferente de quem comprou, o sistema marca. Pode ser um parente pagando, então a marca é só um aviso.",
            "checagem.titular", ["comprador ..... Ana M.", "titular pix ... Carlos M.", "sinal .......... ^nome diferente^"]),
    g.teste(7, T, "05", "O sistema **soma** os sinais e decide.",
            "Cada checagem soma pontos. Com a soma, ele libera, manda para revisão ou segura o pedido, e registra o motivo da decisão.",
            "decisao.pedido", ["sinais acionados .. 3 de 5", "decisão ........... ^revisar^", "motivo ............ valor, sequência,", "                    pagador novo"]),
    g.fluxo(8, T, "O mapa pra **salvar**.",
            [("pix.recebido", "hora e valor"), ("checagens", "5 sinais somados"), ("decisão", "liberar · revisar · segurar"),
             ("pedido.pago", "com decisão registrada"), ("registro", "motivo guardado")],
            "Link na bio", "Regras de exemplo. As reais dependem do seu negócio."),
]

# 3) Stories (seg 09/11, qua 11/11, sex 13/11)
STORIES = {
    "2026-11-09_stories-interacao": [
        g.story("Quanto tempo por dia você gasta **conferindo** Pix?", "Vota aí embaixo.", "Conferência do dia",
                ["abrir o app do banco", "cruzar com a planilha", "^achar o pedido do Pix^"], "enquete"),
        g.story("Amanhã, 18h: quantas **horas por ano** isso vira?", "Ativa o lembrete.", "", [], "contagem"),
        g.story("Quantos **recebedores** de Pix Automático o BC informou em agosto?", "Quiz. A resposta está no post de hoje.", "", [], "quiz"),
        g.story("Como você **cobra** seus clientes hoje?", "Planilha, ERP, banco, WhatsApp? Conta na caixinha.", "Cobrança do mês",
                ["lembrete no WhatsApp", "Pix ou boleto manual", "^baixa na planilha^"], "pergunta"),
        g.story("Black Friday em 14 dias. Quer que eu olhe o seu **fluxo** de pagamento?", "Toca no link e vê como eu trabalho.", "", [], "link"),
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
