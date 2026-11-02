# Carrossel de prova: 5 checagens antes de um Pix virar pedido pago (Payments AI)

- Status: **rascunho, aguardando aprovação do Hélio** (nada agendado; artes fora de `midia/`)
- Pilar: Trabalho / prova (produto próprio) | Público: lojas virtuais, fintechs e software houses (público secundário do perfil) | Formato: carrossel 8 telas, 1080×1350
- Produto: **Payments AI**, produto próprio de análise financeira e detecção de fraude (perfil). O post só afirma isso. As 5 checagens são **exemplos ilustrativos**, todos os registros levam `// ilustrativo`, e a legenda diz que as regras reais dependem do negócio. Nenhum número de resultado, nenhum dado real.
- Rodízio do portfólio: a semana de 02/11 usou a Payments API (Pix auditável, 06/11). Esta usa o Payments AI.
- Meta principal: **salvamentos** (tela 8 é o mapa) e **envios** ("manda pra quem tem loja virtual" e para o dev da loja)
- Gatilhos: data fixa (Black Friday em 14 dias), loop aberto (5 checagens), especificidade (log como imagem, assinatura da marca), pico-fim (tela 7, a decisão), mapa final para salvar
- CTA único: link na bio
- Horário: **sexta 13/11, 10h (Fortaleza)**. Ver `Horário`.

## Confirmar com o Hélio antes de aprovar

1. Posso descrever o Payments AI como "produto próprio de análise financeira e detecção de fraude" (é o que o perfil diz)? Se o produto faz outras checagens, troco os exemplos.
2. As 5 checagens são ilustrativas. Se alguma delas existir de fato no produto, posso dizer "eu uso", mas hoje a legenda não afirma isso.

## Fato conferido

- Black Friday 2026 cai em 27/11. Fonte: Central do Varejo (mesma fonte da pauta de 02/11). De 13/11 a 27/11 são 14 dias.
- Conta usada nos exemplos: R$ 1.490,00 ÷ R$ 180,00 = 8,3×; 490 + 490 + 510 = 1.490; do primeiro ao terceiro Pix, 2 min 52 s.

## Telas

| # | Texto na arte | Alt text |
|---|---|---|
| 1 | 5 checagens antes de um **Pix** virar pedido pago. Bloco: valor R$ 1.490,00, ticket médio R$ 180,00, 3 de 5 checagens acionadas, decisão revisar. Desliza: as 5 checagens | Capa com um registro de exemplo de um Pix com três de cinco checagens acionadas e decisão de revisar |
| 2 | A Black Friday chega em **14 dias**. Pedido grande com Pix rápido é o cenário em que um sinal passa batido. Eu construí o Payments AI, produto próprio de análise financeira e detecção de fraude. Fonte da data: Central do Varejo | Texto sobre a Black Friday em 14 dias e o produto Payments AI |
| 3 | 01. Valor fora do **padrão**. Bloco: ticket médio 180.00, valor 1490.00, razão 8,3x | Bloco de exemplo comparando o valor do pedido com o ticket médio |
| 4 | 02. Pix em **sequência**. Bloco: três Pix do mesmo pagador em menos de 3 min | Bloco de exemplo com três Pix do mesmo pagador em poucos minutos |
| 5 | 03. Pagador **novo**, pedido grande. Bloco: pedidos anteriores 0, valor 1490.00 | Bloco de exemplo de pagador sem pedidos anteriores com valor alto |
| 6 | 04. O nome do titular não **bate**? Bloco: comprador Ana M., titular Pix Carlos M. | Bloco de exemplo em que o nome do comprador é diferente do nome do titular do Pix |
| 7 | O sistema **soma** os sinais e decide. Bloco: 3 de 5 sinais, decisão revisar, motivo valor, sequência, pagador novo | Bloco de exemplo com a decisão de revisar e os motivos registrados |
| 8 | O mapa pra **salvar**. pix.recebido → checagens → decisão → pedido.pago → registro. Link na bio. Regras de exemplo | Mapa com cinco etapas, do Pix recebido ao registro da decisão, e botão link na bio |

## Legenda

Black Friday em 14 dias. Seu sistema segura um Pix suspeito antes de ele virar pedido pago?

Eu construí o Payments AI, produto próprio de análise financeira e detecção de fraude. Nos slides, 5 checagens de exemplo entre o Pix recebido e o pedido pago: valor fora do padrão, Pix em sequência, pagador novo com pedido grande, nome do titular diferente e a soma dos sinais que decide.

Os registros são ilustrativos. As regras reais dependem do seu negócio.

Salva o mapa e manda pra quem tem loja virtual. Quer que eu desenhe isso pro seu fluxo? Link na bio.

Fonte da data: Central do Varejo (Black Friday em 27/11/2026).

#pix #deteccaodefraude #blackfriday2026 #ecommerce #hlbuild

## Primeiro comentário (fixar)

Fonte da data da Black Friday: https://centraldovarejo.com.br/black-friday-2026-data-faturamento-e-preparacao-do-varejo/

## Horário

- Sexta tem o maior pico da semana no Metricool: 10h = 6.734 (11h = 5.952; 12h = 5.909). Está na janela B2B de 10h–12h.
- Escolhido: **sexta 13/11, 10h**. A contagem "14 dias" fica exata nesse dia; o story-05 (link) sai às 12h30 do mesmo dia.

## Respostas prontas

- "Isso é fraude de verdade?" → Aqui são regras de exemplo para mostrar a lógica. As reais dependem do negócio, do ticket e do histórico de cada loja.
- "Bloqueia o pedido?" → Depende da soma dos sinais. Pode liberar, mandar para revisão ou segurar, e o motivo fica registrado.
- "Funciona pra loja pequena?" → Funciona. O que muda é o tamanho do histórico que o sistema usa para comparar.
- "Quanto custa?" → Depende do que você já usa. Chama pelo link da bio que eu olho o seu caso.

## Regenerar as artes

`python3 -I pautas/_gerador/gerar_semana_0911.py && python3 -I pautas/_gerador/render.py 2026-11-13 <pasta-de-saida>`
