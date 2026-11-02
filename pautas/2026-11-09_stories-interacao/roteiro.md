# Stories de interação (semana de 09/11)

- Status: **rascunho, aguardando aprovação do Hélio**. Quando aprovados, entram no Metricool como lembrete (publicação manual): o Instagram não aceita figurinhas (enquete, quiz, caixa de perguntas, link, contagem) via agendamento, então o Hélio cola a figurinha na hora. Artes 1080×1920, fora de `midia/` até a aprovação.
- Objetivo: **conversa e relação**, não alcance. Story serve para quem já segue e prioriza quem responde e manda DM. Cada story também vira dado do público (demografia indisponível abaixo de 100 seguidores).
- Zona segura: topo 150 px e base 250 px livres. A figurinha vai no terço do meio e de baixo.
- Dias: segunda, quarta e sexta, 12h30 (Fortaleza). O Metricool aponta 11h–14h como faixa de stories; 12h = 4.994 (seg), 5.774 (qua), 5.909 (sex).

## Sequência

| Dia e hora | Arte | Figurinha a colar | Por que |
|---|---|---|---|
| Seg 09/11, 12h30 | story-01: "Quanto tempo por dia você gasta conferindo Pix?" | **Enquete** (2 opções): "Menos de 10 min" / "10 min ou mais" | Mede o público e prepara a premissa do reel (10 min por dia) |
| Seg 09/11, 12h32 | story-02: "Amanhã, 18h: quantas horas por ano isso vira?" | **Contagem regressiva** até ter 10/11, 18h, nome "A conta do Pix" | Quem ativa o lembrete recebe o aviso do reel |
| Qua 11/11, 12h30 | story-03: "Quantos recebedores de Pix Automático o BC informou em agosto?" | **Quiz**: 3 mil / **14 mil** (correta) / 40 mil | Fecha o loop do carrossel das 10h; fonte: Finsiders Brasil, com dados do BC |
| Sex 13/11, 12h30 | story-04: "Como você cobra seus clientes hoje?" | **Caixa de perguntas**: "Planilha, ERP, banco, WhatsApp?" | As respostas viram pauta e abrem DM |
| Sex 13/11, 12h32 | story-05: "Black Friday em 14 dias. Quer que eu olhe o seu fluxo de pagamento?" | **Link** para o portfólio (mesmo destino do link da bio) com o texto "Ver como eu trabalho" | CTA único; promove o carrossel das 10h |

## Como usar as respostas

- Enquete: anotar o % por opção em `aprendizados.md`. Se a maioria votar "10 min ou mais", a premissa do reel está conservadora.
- Caixa de perguntas: responder em story (print do texto, sem nome) e transformar as 3 respostas mais repetidas em carrossel. Dado de cliente real nunca entra no repo público.
- Quiz: quem erra recebe a explicação na resposta; o post das 10h tem a fonte.
- Quem responder por DM é lead morno: responder com uma pergunta, não com proposta.

## Respostas-modelo para DM

- Votou "10 min ou mais" → "Daria 44 horas por ano, mais que uma semana de trabalho. Hoje você confere no app do banco ou numa planilha?"
- Respondeu a caixa de perguntas → "Obrigado por contar. Hoje esse processo é manual do começo ao fim ou tem alguma parte automática?"
- Pediu "o fluxo" → "Me conta como você cobra e como recebe hoje. Com isso eu te digo o que eu olharia primeiro."

## Alt text

- story-01: Pergunta "Quanto tempo por dia você gasta conferindo Pix?" com um bloco de exemplo de três etapas da conferência.
- story-02: Texto "Amanhã, 18h: quantas horas por ano isso vira?" sobre fundo azul-escuro.
- story-03: Pergunta sobre quantos recebedores de Pix Automático o Banco Central informou em agosto.
- story-04: Pergunta "Como você cobra seus clientes hoje?" com um bloco de exemplo de cobrança do mês.
- story-05: Texto "Black Friday em 14 dias. Quer que eu olhe o seu fluxo de pagamento?".

## Regenerar as artes

`python3 -I pautas/_gerador/gerar_semana_0911.py && python3 -I pautas/_gerador/render.py 2026-11-09 <pasta-de-saida>`
