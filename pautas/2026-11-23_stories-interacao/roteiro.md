# Stories de interação (semana de 23/11)

- Status: **rascunho, aguardando aprovação do Hélio**. Quando aprovados, entram no Metricool como lembrete (publicação manual): o Instagram não aceita figurinhas (enquete, quiz, caixa de perguntas, contagem) via agendamento, então o Hélio cola a figurinha na hora. Artes 1080×1920, fora de `midia/` até a aprovação.
- Objetivo: **conversa e relação**, não alcance. Story serve para quem já segue e prioriza quem responde e manda DM. Cada resposta também vira dado do público (demografia indisponível abaixo de 100 seguidores; a conta tem 29).
- Zona segura: topo 150 px e base 250 px livres. A figurinha vai no terço do meio e de baixo.
- Dias: segunda 23/11, quarta 25/11 e quinta 26/11 (3 dias). Sexta 27/11 (Black Friday) fica sem story programado.
- Horário: 12h30 e 12h32 (Fortaleza). O Metricool aponta 11h–14h como faixa de stories; 12h = 4.994 (seg), 5.774 (qua), 5.730 (qui).
- O Metricool não devolve nenhum dado de story desde 26/10 (nem os de 09/11). **Anotar à mão** os resultados (voto da enquete, acertos do quiz, caixinhas) em `aprendizados.md`.

## Sequência

| Dia e hora | Arte | Figurinha a colar | Por que |
|---|---|---|---|
| Seg 23/11, 12h30 | story-01: "Sexta é Black Friday. Você confere o Pix na mão?" | **Enquete** (2 opções): "Na mão" / "O sistema avisa" | Mede quantos conferem na mão e prepara o reel de terça |
| Seg 23/11, 12h32 | story-02: "Amanhã, 12h: eu simulei uma Black Friday de 500 Pix." | **Contagem regressiva** até ter 24/11, 12h, nome "Black Friday simulada" | Quem ativa o lembrete recebe o aviso do reel |
| Qua 25/11, 12h30 | story-03: "Boleto pago e o Pix da mesma cobrança também caiu. Quem devolve?" | **Quiz**: O cliente pede ao lojista / **A instituição do recebedor, em até 24 h** (correta) / Ninguém | Leva para o carrossel das 18h; fonte: Resolução BCB 587, art. 41-A §3º (vale a partir de 01/02/2027, só para cobrança híbrida) |
| Qua 25/11, 12h32 | story-04: "Qual a sua maior dúvida em cobrar por Pix e boleto?" | **Caixa de perguntas** ("Boleto, Pix, baixa?") | As respostas viram pauta e abrem DM |
| Qui 26/11, 12h30 | story-05: "Saiu: as 4 regras que deixaram 3 Pix na mão." | **Link** para o post (ou sem figurinha) | Divulga o carrossel de prova das 10h |

## Como usar as respostas

- Enquete: anotar o % por opção em `aprendizados.md`. Se a maioria votar "Na mão", o reel acerta uma dor real.
- Quiz: quem erra recebe a explicação na resposta; o post das 18h traz a fonte.
- Caixa de perguntas: responder em story (print do texto, sem nome) e transformar as 3 respostas mais repetidas em carrossel. Dado de cliente real nunca entra no repo público.
- Quem responder por DM é lead morno: responder com uma pergunta, não com proposta.

## Respostas-modelo para DM

- Votou "Na mão" → "Hoje você confere o Pix no extrato, em planilha ou o sistema já mostra de qual pedido é?"
- Respondeu a caixa de perguntas → "Obrigado por contar. Hoje esse processo é manual do começo ao fim ou tem alguma parte automática?"
- Pediu "o fluxo" → "Me conta como você cobra e como recebe hoje. Com isso eu te digo o que eu olharia primeiro."

## Alt text

- story-01: Pergunta "Sexta é Black Friday. Você confere o Pix na mão?" com um bloco de exemplo que mostra um Pix de R$ 149,90 sem pedido identificado.
- story-02: Texto "Amanhã, 12h: eu simulei uma Black Friday de 500 Pix" sobre fundo azul-escuro.
- story-03: Pergunta sobre quem devolve quando o boleto foi pago e o Pix da mesma cobrança também caiu.
- story-04: Pergunta "Qual a sua maior dúvida em cobrar por Pix e boleto?" com um bloco de exemplo listando boleto, pix e baixa.
- story-05: Texto "Saiu: as 4 regras que deixaram 3 Pix na mão" com um bloco de exemplo da simulação (500 pedidos, 3 na fila).

## Regenerar

`python3 -I pautas/_gerador/gerar_semana_2311.py` e `python3 -I pautas/_gerador/render.py 2026-11-23 <pasta-de-saida>` (PNG fora do repo até a aprovação).
