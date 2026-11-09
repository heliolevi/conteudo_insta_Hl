# Carrossel educativo: Cliente contestou um Pix. Seu sistema prova a venda?

- Status: **rascunho, aguardando aprovação do Hélio** (nada agendado; artes fora de `midia/`)
- Pilar: Ensina | Público: lojas virtuais e PMEs que vendem por Pix (primário do perfil) | Formato: carrossel 8 telas, 1080×1350
- Fórmula: checklist de 5 registros ("o que guardar"). Meta principal: **salvamentos** (a tela 8 é a lista para guardar) e **envios** ("manda pra quem atende o financeiro da loja")
- Por que agora: o MED 2.0 do Pix virou regra obrigatória em 02/02/2026 e é um dos temas que o nicho busca ("Pix contestado", "devolução de Pix"). A semana de 16/11 antecede a Black Friday (27/11). O relatório de 09/11 mostra educativos com alcance de 11 a 21 pessoas e 0 salvamentos nas peças de 10h; este vai às 18h para separar horário de tema.
- Gatilhos: número específico na capa (11 dias), aversão à perda (valor bloqueado e venda sem prova), checklist final para salvar, pico-fim (tela 7, o atendimento), identificação ("já recebi um Pix contestado")
- CTA único: link na bio
- Horário: **quarta 18/11, 18h (Fortaleza)**. Ver `Horário`.

## Fatos conferidos (09/11/2026) e como citar

- O MED 2.0 passou a ser obrigatório para as instituições do Pix em 2 de fevereiro de 2026; o BC deu tolerância regulatória até 10/05 (Resolução BCB nº 546). Fontes: Finsiders Brasil (27/01/2026, atualizada em 02/02/2026) e Tecnoblog (02/02/2026).
- O MED 2.0 rastreia o caminho do dinheiro, e o BC espera a devolução em até 11 dias depois da contestação. Fontes: Tecnoblog e Finsiders Brasil (as duas dizem "espera" ou "será possível"; a legenda usa "espera").
- O MED vale para fraude, golpe, coerção e erro operacional da instituição. Desacordo comercial, arrependimento de compra e erro de digitação de chave não entram. Fonte: Transfeera (25/02/2026, fonte secundária de uma fintech).
- Após acionar o MED, há bloqueio cautelar de valores nas contas envolvidas durante a análise. Fonte: Transfeera. **Pendente:** não abri o texto da Resolução BCB nº 493 (regulamento do MED). Os dados vêm das reportagens e do blog. Se quiser o primário, abrir bcb.gov.br (Resolução BCB nº 493) antes de publicar.
- Os 5 registros e os valores nas telas são **exemplos ilustrativos** (pedido 2087, txid, horários). Não são regra do BC nem dado de cliente.

## Confirmar com o Hélio antes de aprovar

1. A frase "eu deixo a trilha da venda pronta" (tela 2) e a tela 8 dizem que eu monto esses 5 registros. Se o Payments API não registra esses 5 eventos hoje, troco por "eu montaria" para não afirmar o que não é fato.
2. A lista de 5 registros é uma sugestão de boa prática, não uma exigência do BC. A arte não diz que é obrigação; a legenda também não.

## Telas

| # | Texto na arte | Alt text |
|---|---|---|
| 1 | Cliente contestou um **Pix**. Seu sistema prova a venda? Número "11 dias" com o rótulo "prazo que o BC espera para devolver um Pix contestado · MED 2.0". Desliza: 5 registros pra guardar | Capa azul-escura com o título "Cliente contestou um Pix. Seu sistema prova a venda?" e o número 11 dias |
| 2 | O MED 2.0 segue o **caminho** do dinheiro. Obrigatório desde 02/02/2026, devolução esperada em até 11 dias, vale para fraude, golpe, coerção ou erro da instituição, desacordo comercial não entra, valor pode ficar bloqueado na análise. Fontes: Tecnoblog, Finsiders Brasil, Transfeera | Texto explicando o MED 2.0 do Pix, o prazo de 11 dias e quando ele vale |
| 3 | 01. O **pedido** e tudo que foi vendido. Bloco pedido.criado (pedido 2087, itens 2, valor R$ 240,00, criado 14:02) | Bloco de exemplo com o pedido 2087, dois itens, valor de 240 reais e hora de criação |
| 4 | 02. A **cobrança** que gerou o Pix. Bloco cobranca.criada (txid, pedido 2087, valor, expira 14:32) | Bloco de exemplo com o txid ligado ao pedido 2087 e a hora em que a cobrança expira |
| 5 | 03. O **Pix** que chegou. Bloco pix.recebido (end_to_end, txid, pagador Ana M., recebido às 14:05) | Bloco de exemplo com o identificador do Pix, o txid e a hora em que o Pix foi recebido |
| 6 | 04. A **entrega** que fecha a venda. Bloco entrega.confirmada (enviado 16/11, entregue 18/11, rastreio guardado) | Bloco de exemplo com as datas de envio e entrega do pedido 2087 |
| 7 | 05. O **atendimento** com data e hora. Bloco contato.registrado (cliente perguntou 09:12, loja respondeu 09:20) | Bloco de exemplo com a pergunta do cliente e a resposta da loja, com horários |
| 8 | Os 5 registros pra **salvar**. pedido.criado, cobranca.criada, pix.recebido, entrega.confirmada, contato.registrado. Link na bio. Exemplos ilustrativos, não é consultoria jurídica | Lista com cinco registros e botão link na bio |

## Legenda

Cliente contestou um Pix. Seu sistema prova que a venda foi real?

Desde 2 de fevereiro de 2026, o MED 2.0 é obrigatório no Pix. Ele rastreia o caminho do dinheiro, e o Banco Central espera a devolução em até 11 dias depois da contestação. Durante a análise, o valor pode ficar bloqueado nas contas envolvidas.

Nos slides eu mostro os 5 registros que eu deixo prontos em cada venda por Pix: pedido, cobrança com txid, Pix recebido, entrega e atendimento. Os exemplos são ilustrativos e não são consultoria jurídica.

Salva a lista e manda pra quem atende o financeiro da loja. Quer que eu olhe o seu fluxo? Link na bio.

Fontes: Tecnoblog (02/02/2026), Finsiders Brasil (27/01/2026) e Transfeera (25/02/2026).

#pix #medpix #lojavirtual #pequenasempresas #hlbuild

## Primeiro comentário (fixar)

Fontes: https://tecnoblog.net/noticias/pix-novas-regras-facilitam-devolucao-de-dinheiro-em-caso-de-fraude , https://finsidersbrasil.com.br/pagamentos/pix/novo-med-do-pix-passa-a-ser-obrigatorio-mas-instituicoes-terao-um-respiro/ e https://transfeera.com/blog/med-pix-2-0/ . Regra oficial: Resolução BCB nº 493, no site do Banco Central.

## Horário (getBestTimeToPostByNetwork, Instagram, America/Fortaleza, 16 a 20/11)

- Valores por hora do Metricool na quarta: 10h = 6.506 (maior pico da semana), 11h = 6.063, 12h = 5.774, 18h = 4.869 (segundo pico), 19h = 3.992.
- Escolhido: **quarta 18/11, 18h**. Motivos: (1) está na janela B2B de 18h–20h do perfil; (2) na conta, as peças da noite alcançaram mais (273 e 473) que as de 10h–11h (11 a 152, 5 conteúdos), então este é o teste de horário contra o educativo de 11/11 e a prova de 13/11, ambos às 10h; (3) o reel de terça fica a um dia de distância, sem canibalizar. Se o Hélio preferir seguir o pico do Metricool (10h), troco; a perda é o teste.
- O quiz de story (qua 12h30) leva quem já segue para o post das 18h.
- Sexta 20/11 é feriado nacional (Dia da Consciência Negra), sem feed.

## Respostas prontas

- "Se o cliente se arrepender, entra no MED?" → Pelas fontes, desacordo comercial e arrependimento de compra não entram no MED; ele vale para fraude, golpe, coerção e erro da instituição. Pro seu caso, confirma com o seu banco.
- "Posso perder o dinheiro?" → Durante a análise, o valor pode ficar bloqueado nas contas envolvidas. Quem decide é o banco. Confirma o seu caso com ele ou com um advogado.
- "Serve pra MEI?" → Qualquer um que recebe por Pix pode ter uma contestação. Os 5 registros ajudam a responder rápido, mas não é consultoria jurídica.
- "Quanto custa montar isso?" → Depende do que você já usa. Chama pelo link da bio que eu olho o seu caso.

## O que medir depois (relatório de 23/11)

Alcance (comparar com os educativos de 10h: 19, 21 e 11 em 02 a 06/11, e os de 11 e 13/11), salvamentos por alcance (meta 2%; só avaliar com alcance acima de 100), envios por alcance (meta 1%), comentários. Registrar se o horário das 18h repete o desempenho noturno.

## Regenerar as artes

`python3 -I pautas/_gerador/gerar_semana_1611.py && python3 -I pautas/_gerador/render.py 2026-11-18 <pasta-de-saida>`
