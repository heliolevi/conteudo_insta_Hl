"""Artes da semana de 23/11/2026 (2 carrosséis e 5 stories) no padrão visual da HL.

Reaproveita os componentes de gerar.py (mesmo CSS, fontes e tipos de tela). Os números do carrossel de prova vêm de
pautas/2026-11-24_reel-black-friday-simulada/resultado.json (saída de simular.py); nada é digitado à mão.
O reel da semana tem gerador próprio em pautas/2026-11-24_reel-black-friday-simulada/.

Uso:  python3 -I pautas/_gerador/gerar_semana_2311.py     (gera os HTML em pautas/<post>/slides/)
      python3 -I pautas/_gerador/render.py 2026-11-2 /tmp/png   (PNG fora do repo, até a aprovação)

Marcação de texto: **palavra** = ciano (uma por título), ~texto~ = comentário esmaecido,
^texto^ = destaque ciano dentro de bloco de código.
"""
import datetime
import json
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import gerar as g  # noqa: E402
from gerar_semana_0911 import capa_dado  # noqa: E402

RAIZ = g.RAIZ
SIM = json.loads((RAIZ / "pautas/2026-11-24_reel-black-friday-simulada/resultado.json").read_text(encoding="utf-8"))
C, A = SIM["contagem"], SIM["amostras"]


def brl(v):
    return f"R$ {v:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


# dias entre a data de publicação do educativo (qua 25/11) e a vigência da cobrança híbrida (01/02/2027)
DIAS = (datetime.date(2027, 2, 1) - datetime.date(2026, 11, 25)).days
assert DIAS == 68, DIAS
sem_txid = C["casado_valor_hora"] + C["fila_ambiguo"] + C["fila_sem_candidato"]

POSTS = {}

# 1) Educativo (qua 25/11, 18h): cobrança híbrida (Resolução BCB 587). Público: PMEs que cobram por boleto e Pix.
T = 8
FONTE_RES = "Fonte: Banco Central, Resolução BCB nº 587 (18/09/2026)"
POSTS["2026-11-25_carrossel-boleto-qr-pix-cobranca-hibrida"] = [
    capa_dado(1, T, f"{DIAS} dias", "até 01/02/2027 · cobrança híbrida",
              "Boleto e **Pix** na mesma cobrança. Seu sistema dá baixa uma vez só?", "Desliza: 4 perguntas pra guardar", 215),
    g.contexto(2, T, "Uma cobrança, dois **jeitos** de pagar.",
               "A Resolução BCB 587 criou a cobrança híbrida: o boleto e o Pix Cobrança com vencimento na mesma cobrança. Vale a partir de 1º de fevereiro de 2027.\n\nA oferta é facultativa para a instituição de quem recebe. Nem todo banco vai ter.",
               FONTE_RES + ", art. 11-AA e art. 5º"),
    g.dois_cartoes(3, T, "Pagou por um, o **outro** não vale.",
                   "Se o cliente paga pelo boleto, o Pix da mesma cobrança precisa ser cancelado. Se o Pix cair mesmo assim, a instituição devolve tudo ao pagador em até 24 horas, com recursos próprios.",
                   [("Pagou o boleto", "O Pix Cobrança é cancelado."), ("Pix pago depois", "Devolução integral em até 24 h.")],
                   FONTE_RES + ", art. 11-AA §7º e art. 41-A §3º"),
    g.teste(4, T, "01", "A cobrança tem um **identificador** só?",
            "Boleto e Pix precisam apontar para a mesma cobrança no seu sistema. Sem isso, os dois avisos viram dois pagamentos.",
            "cobranca", ["cobranca ........... 7731", "boleto ............ linha digitável", "pix (txid) ........ ^mesma cobrança^"]),
    g.teste(5, T, "02", "A baixa roda **uma vez**?",
            "Se os dois avisos chegarem, só um baixa a cobrança. O segundo é registrado e ignorado, não somado.",
            "Dois avisos, uma baixa", ["cobranca 7731  boleto ... ^baixada^", "cobranca 7731  pix ..... ignorado", "caixa ................ 1 pagamento"]),
    g.teste(6, T, "03", "Um Pix **a mais** vira alerta?",
            "Na norma, a devolução ao pagador é da instituição, em até 24 horas. Ao seu sistema cabe registrar o Pix a mais e avisar o financeiro.",
            "pix.recebido", ["cobranca ........... 7731", "situação ........... já paga (boleto)", "^alerta: pagamento a mais^"]),
    g.contexto(7, T, "Seu banco vai **oferecer**?",
               "A oferta é facultativa, e a instituição que emite o boleto precisa ser a mesma que recebe o Pix. Pergunte ao seu banco ou plataforma se vai ter e quando, antes de mexer no sistema.",
               FONTE_RES + ", art. 11-AA §4º e §5º",
               g.painel("Cobrança híbrida", ["oferta ........... ^facultativa^", "emissor do boleto = recebedor do Pix"])),
    g.fecho(8, T, "4 perguntas pra levar ao seu **fornecedor**.",
            ["Um identificador para boleto e Pix", "Baixa uma vez só", "Pix a mais vira alerta", "Meu banco oferece? Quando?"],
            "Link na bio", "Não é consultoria jurídica. Confirme na Resolução BCB 587."),
]

# 2) Prova (qui 26/11, 10h): Black Friday simulada. Dados fictícios; números lidos de resultado.json
T = 8
POSTS["2026-11-26_carrossel-black-friday-simulada-4-regras"] = [
    g.capa_log(1, T, "Simulei uma **Black Friday**. 500 Pix, 3 para conferir na mão.", "Simulação · 500 pedidos",
               [f"pedidos ............ {SIM['pedidos']}", f"baixados sozinhos .. {SIM['automaticos']}", f"pra conferir ....... ^{SIM['fila_na_mao']}^"],
               "Desliza: as 4 regras que fizeram isso"),
    g.contexto(2, T, "Dado **fictício**. Premissas minhas.",
               "Não é loja nem cliente real. Rodei um script com 500 pedidos pagos por Pix e três falhas que acontecem: aviso perdido, aviso duplicado e Pix sem txid.\n\nAs taxas são minhas. Com outras, o resultado muda.",
               "Simulação ilustrativa, semente 2711",
               g.painel("Premissas", [f"aviso perdido ...... {int(SIM['premissas']['perdido'] * 100)}%",
                                      f"aviso duplicado .... {int(SIM['premissas']['duplicado'] * 100)}%",
                                      f"Pix sem txid ....... {int(SIM['premissas']['sem_txid'] * 100)}%"])),
    g.teste(3, T, "01", "Baixar **uma vez** só.",
            f"O mesmo aviso pode chegar duas vezes. Se baixar duas, o caixa conta o Pix em dobro. Na simulação, {C['duplicado_ignorado']} avisos em dobro foram ignorados.",
            "Regra 1", [f"{A['duplicado']['hora']}  {A['duplicado']['txid']}  baixado",
                        f"{A['duplicado']['hora']}  {A['duplicado']['txid']}  ^em dobro: ignorado^"]),
    g.teste(4, T, "02", "Sem txid, **valor e horário**.",
            f"Quando o cliente paga pela chave, o Pix chega sem txid. Busco uma cobrança pendente com o mesmo valor, criada nos 30 minutos anteriores. Achando uma só, eu baixo. Na simulação: {C['casado_valor_hora']}.",
            "Regra 2", [f"Pix sem txid  {brl(A['casado']['valor'])}", "cobranças pendentes (30 min) ... 1", f"^casado: pedido {A['casado']['pedido']}^"]),
    g.teste(5, T, "03", "Aviso perdido? **Varredura**.",
            f"Nem todo aviso chega. No fim do dia, o sistema consulta os Pix recebidos e baixa o que ficou sem baixa. Na simulação: {C['varredura']}.",
            "Regra 3", [f"txid {A['varredura']['txid']} ... sem aviso", f"extrato ... {brl(A['varredura']['valor'])} às {A['varredura']['hora'][:5]}", "^baixado pela varredura^"]),
    g.teste(6, T, "04", "O que **não casa** vai pra fila.",
            f"Com 2 cobranças do mesmo valor, eu não chuto. O Pix vai para a fila com o motivo, e você decide. Na simulação: {C['fila_ambiguo'] + C['fila_sem_candidato']}.",
            "Regra 4", [f"Pix sem txid  {brl(A['ambiguo']['valor'])} às {A['ambiguo']['hora'][:5]}", f"cobranças pendentes (30 min) ... {A['ambiguo']['candidatos']}", "^ambíguo: fila de conferência^"]),
    g.contexto(7, T, f"500 Pix. **{SIM['fila_na_mao']}** na mão.",
               f"Na mão, seriam {SIM['pedidos']} conferências. Com as 4 regras, a simulação deixou {SIM['fila_na_mao']} ({str(SIM['pct_na_mao']).replace('.', ',')}%).\n\nEm loja real o número muda. O que não muda é a ordem: baixar uma vez, casar, varrer e separar a dúvida.",
               "Simulação com dados fictícios e premissas minhas",
               g.painel("Resultado", [f"baixa por txid ........ {C['baixa_txid']}", f"valor + horário ........ {C['casado_valor_hora']}", f"varredura ............. {C['varredura']}",
                                      f"fila na mão ........... ^{SIM['fila_na_mao']}^"])),
    g.fecho(8, T, "As 4 regras pra **salvar**.",
            ["Baixar uma vez só", "Sem txid: valor e horário", "Aviso perdido: varredura", "Dúvida vai pra fila"],
            "Link na bio", "Simulação ilustrativa. Quer isso no seu fluxo?"),
]

# 3) Stories (seg 23/11, qua 25/11 e qui 26/11, 12h30 e 12h32)
STORIES = {
    "2026-11-23_stories-interacao": [
        g.story("Sexta é **Black Friday**. Você confere o Pix na mão?", "Vota aí embaixo.", "Pix do dia",
                ["14:02  entrou R$ 149,90", "^?^      de qual pedido?"], "enquete"),
        g.story("Amanhã, 12h: eu simulei uma **Black Friday** de 500 Pix.", "Ativa o lembrete.", "", [], "contagem"),
        g.story("Boleto pago e o Pix da mesma cobrança também caiu. Quem **devolve**?", "Quiz. Regra de 02/2027. A resposta está no post das 18h.", "", [], "quiz"),
        g.story("Qual a sua maior **dúvida** em cobrar por Pix e boleto?", "Conta na caixinha.", "Dúvida do dia",
                ["boleto", "pix", "^baixa^"], "pergunta"),
        g.story(f"Saiu: as 4 regras que deixaram **{SIM['fila_na_mao']}** Pix na mão.", "Carrossel novo no feed.", "Simulação",
                [f"pedidos ......... {SIM['pedidos']}", f"fila na mão ..... ^{SIM['fila_na_mao']}^"], "link"),
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
