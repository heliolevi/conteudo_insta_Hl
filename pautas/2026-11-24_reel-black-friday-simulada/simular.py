"""Simulação de uma Black Friday com 500 pedidos pagos por Pix (dados 100% fictícios).

Serve de base para o reel de 24/11 e para o carrossel de 26/11. Nada aqui é dado de cliente.
As taxas abaixo são PREMISSAS minhas, não medição de loja real:
  2% dos avisos (webhook) se perdem, 3% chegam duplicados, 3% dos Pix chegam sem txid
  (cliente pagou digitando a chave, sem usar a cobrança do sistema).
Mudar a semente muda os números; a semente fica fixa para o post ser reproduzível.

Uso: python3 -I pautas/2026-11-24_reel-black-friday-simulada/simular.py   (grava resultado.json ao lado)
"""
import json
import pathlib
import random

SEMENTE = 2711
N = 500
P_PERDIDO, P_SEM_TXID, P_DUPLICADO = 0.02, 0.03, 0.03
JANELA_S = 30 * 60  # casamento por valor: só cobranças criadas nos 30 min anteriores
PRECOS = [49.90, 79.90, 99.90, 129.90, 149.90, 199.90, 249.90, 299.90]
# peso de cada hora do dia (pico à noite e no começo da manhã da promoção)
PESO_HORA = [3, 2, 1, 1, 1, 2, 3, 4, 5, 6, 6, 6, 7, 6, 6, 6, 7, 8, 9, 10, 12, 12, 9, 5]

rng = random.Random(SEMENTE)


def hhmmss(s):
    return f"{int(s // 3600):02d}:{int(s % 3600 // 60):02d}:{int(s % 60):02d}"


# 1) pedidos e cobranças
pedidos = []
for i in range(1, N + 1):
    h = rng.choices(range(24), weights=PESO_HORA)[0]
    criada = h * 3600 + rng.randrange(0, 3600)
    pago = criada + rng.randrange(20, 600)  # o cliente paga entre 20 s e 10 min depois
    pedidos.append({"pedido": 1000 + i, "txid": f"T{1000 + i}", "valor": rng.choice(PRECOS), "criada": criada, "pago": pago})

# 2) avisos recebidos pelo sistema (o que o banco/plataforma manda)
avisos, extrato = [], []
for p in pedidos:
    u = rng.random()
    tipo = "ok"
    if u < P_PERDIDO:
        tipo = "perdido"
    elif u < P_PERDIDO + P_SEM_TXID:
        tipo = "sem_txid"
    elif u < P_PERDIDO + P_SEM_TXID + P_DUPLICADO:
        tipo = "duplicado"
    p["tipo"] = tipo
    # o extrato do banco sempre tem o Pix; o txid só existe se o cliente pagou pela cobrança
    extrato.append({"pedido": p["pedido"], "txid": None if tipo == "sem_txid" else p["txid"], "valor": p["valor"], "pago": p["pago"]})
    if tipo == "perdido":
        continue
    avisos.append({"txid": None if tipo == "sem_txid" else p["txid"], "valor": p["valor"], "hora": p["pago"], "origem": p["pedido"]})
    if tipo == "duplicado":
        avisos.append({"txid": p["txid"], "valor": p["valor"], "hora": p["pago"] + rng.randrange(1, 40), "origem": p["pedido"]})
avisos.sort(key=lambda a: a["hora"])

# 3) o conciliador
baixados = {}      # pedido -> como foi baixado
fila = []          # o que sobrou para olhar na mão
cont = {"avisos": len(avisos), "baixa_txid": 0, "duplicado_ignorado": 0, "casado_valor_hora": 0, "fila_ambiguo": 0, "fila_sem_candidato": 0, "varredura": 0}
amostras = {}
por_txid = {p["txid"]: p for p in pedidos}

for a in avisos:
    if a["txid"]:
        p = por_txid[a["txid"]]
        if p["pedido"] in baixados:
            cont["duplicado_ignorado"] += 1
            amostras.setdefault("duplicado", {"txid": a["txid"], "valor": a["valor"], "hora": hhmmss(a["hora"]), "pedido": p["pedido"]})
        else:
            baixados[p["pedido"]] = "txid"
            cont["baixa_txid"] += 1
    else:
        cand = [p for p in pedidos if p["pedido"] not in baixados and p["valor"] == a["valor"]
                and 0 <= a["hora"] - p["criada"] <= JANELA_S]
        if len(cand) == 1:
            baixados[cand[0]["pedido"]] = "valor_hora"
            cont["casado_valor_hora"] += 1
            amostras.setdefault("casado", {"valor": a["valor"], "hora": hhmmss(a["hora"]), "pedido": cand[0]["pedido"]})
        elif len(cand) > 1:
            cont["fila_ambiguo"] += 1
            fila.append({"motivo": "ambiguo", "valor": a["valor"], "hora": hhmmss(a["hora"]), "candidatos": len(cand)})
            amostras.setdefault("ambiguo", {"valor": a["valor"], "hora": hhmmss(a["hora"]), "candidatos": len(cand)})
        else:
            cont["fila_sem_candidato"] += 1
            fila.append({"motivo": "sem_candidato", "valor": a["valor"], "hora": hhmmss(a["hora"]), "candidatos": 0})

# varredura no fim do dia: consulta o extrato (Pix recebidos por período) e baixa o que tem txid e ficou sem baixa
for e in extrato:
    if e["txid"] and e["pedido"] not in baixados:
        baixados[e["pedido"]] = "varredura"
        cont["varredura"] += 1
        amostras.setdefault("varredura", {"txid": e["txid"], "valor": e["valor"], "hora": hhmmss(e["pago"]), "pedido": e["pedido"]})

auto = len(baixados)
res = {
    "semente": SEMENTE, "pedidos": N,
    "premissas": {"perdido": P_PERDIDO, "sem_txid": P_SEM_TXID, "duplicado": P_DUPLICADO, "janela_min": JANELA_S // 60},
    "contagem": cont,
    "automaticos": auto,
    "fila_na_mao": len(fila),
    "pedidos_sem_baixa_no_fim": N - auto,
    "pct_na_mao": round(100 * len(fila) / N, 1),
    "amostras": amostras,
    "fila": fila,
}
# conferência: cada pedido ou foi baixado ou está na fila
assert auto + len(fila) == N, (auto, len(fila))
caminho = pathlib.Path(__file__).resolve().parent / "resultado.json"
caminho.write_text(json.dumps(res, ensure_ascii=False, indent=2), encoding="utf-8")
print(json.dumps({k: v for k, v in res.items() if k != "fila"}, ensure_ascii=False, indent=2))
