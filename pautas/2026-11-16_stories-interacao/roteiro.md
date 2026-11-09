# Stories de interação (semana de 16/11)

- Status: **rascunho, aguardando aprovação do Hélio**. Quando aprovados, entram no Metricool como lembrete (publicação manual): o Instagram não aceita figurinhas (enquete, quiz, caixa de perguntas, contagem) via agendamento, então o Hélio cola a figurinha na hora. Artes 1080×1920, fora de `midia/` até a aprovação.
- Objetivo: **conversa e relação**, não alcance. Story serve para quem já segue e prioriza quem responde e manda DM. Cada resposta também vira dado do público (demografia indisponível abaixo de 100 seguidores).
- Zona segura: topo 150 px e base 250 px livres. A figurinha vai no terço do meio e de baixo.
- Dias: segunda 16/11, quarta 18/11 (novos, aqui) e quinta 19/11 (já agendados: os 2 stories do case da Fernanda, 12h30 e 12h32). Total: 3 dias de story na semana.
- Horário: 12h30 (Fortaleza). O Metricool aponta 11h–14h como faixa de stories; 12h = 4.994 (seg), 5.774 (qua), 5.730 (qui).
- O Metricool não devolveu nenhum dado de story desde 26/10. Anotar à mão os resultados (voto da enquete, acertos do quiz, caixinhas) em `aprendizados.md`.

## Sequência

| Dia e hora | Arte | Figurinha a colar | Por que |
|---|---|---|---|
| Seg 16/11, 12h30 | story-01: "Seu Pix foi pago e o pedido ficou aguardando?" | **Enquete** (2 opções): "Já aconteceu comigo" / "Nunca vi" | Mede quantos conhecem o problema e prepara o reel de terça |
| Seg 16/11, 12h32 | story-02: "Amanhã, 18h: 3 motivos de um Pix pago continuar aguardando." | **Contagem regressiva** até ter 17/11, 18h, nome "3 motivos do Pix" | Quem ativa o lembrete recebe o aviso do reel |
| Qua 18/11, 12h30 | story-03: "Em quantos dias o BC espera devolver um Pix contestado por fraude?" | **Quiz**: 3 dias / **11 dias** (correta) / 30 dias | Leva para o carrossel das 18h; fonte: Tecnoblog e Finsiders Brasil |
| Qua 18/11, 12h32 | story-04: "Qual a sua maior dúvida sobre Pix na loja?" | **Caixa de perguntas** ("Cobrança, conciliação, devolução?") | As respostas viram pauta e abrem DM |
| Qui 19/11, 12h30 e 12h32 | (já agendado) case da Fernanda | (nenhuma) | Divulga o carrossel de prova das 10h |

## Como usar as respostas

- Enquete: anotar o % por opção em `aprendizados.md`. Se a maioria votar "Já aconteceu comigo", o tema do reel acerta uma dor real.
- Quiz: quem erra recebe a explicação na resposta; o post das 18h traz a fonte.
- Caixa de perguntas: responder em story (print do texto, sem nome) e transformar as 3 respostas mais repetidas em carrossel. Dado de cliente real nunca entra no repo público.
- Quem responder por DM é lead morno: responder com uma pergunta, não com proposta.

## Respostas-modelo para DM

- Votou "Já aconteceu comigo" → "Com o Pix pago e o pedido parado? Hoje você confere na mão ou o sistema avisa quando isso acontece?"
- Respondeu a caixa de perguntas → "Obrigado por contar. Hoje esse processo é manual do começo ao fim ou tem alguma parte automática?"
- Pediu "o fluxo" → "Me conta como você cobra e como recebe hoje. Com isso eu te digo o que eu olharia primeiro."

## Alt text

- story-01: Pergunta "Seu Pix foi pago e o pedido ficou aguardando?" com um bloco de exemplo que mostra Pix recebido ok e pedido aguardando.
- story-02: Texto "Amanhã, 18h: 3 motivos de um Pix pago continuar aguardando" sobre fundo azul-escuro.
- story-03: Pergunta sobre em quantos dias o Banco Central espera devolver um Pix contestado por fraude.
- story-04: Pergunta "Qual a sua maior dúvida sobre Pix na loja?" com um bloco de exemplo listando cobrança, conciliação e devolução.

## Regenerar as artes

`python3 -I pautas/_gerador/gerar_semana_1611.py && python3 -I pautas/_gerador/render.py 2026-11-16 <pasta-de-saida>`
