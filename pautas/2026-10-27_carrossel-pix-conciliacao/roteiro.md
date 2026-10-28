# Carrossel: 5 sinais de que você ainda concilia Pix na mão

- Status: **aprovado pelo Hélio em 2026-10-27; agendado no Metricool para quarta, 28/10, 10h (Fortaleza)**. Artes em `midia/2026-10-27_carrossel-pix-conciliacao/`.
- Pilar: Ensina (post educativo) | Público: PMEs que recebem por Pix | Formato: carrossel 8 telas, 1080×1350
- Gatilhos: lacuna de informação e loop aberto (o quinto sinal "passa batido"), aversão à perda (o que o caixa perde ao depender de conferência manual), especificidade (cenário real do dono de PME), pico-fim (tela 7 é o sinal mais forte; a 8 é o checklist que vale o salvamento)
- CTA único: link na bio
- Horário: quarta, 28/10, 10h (Fortaleza). Escolha: primeiro dia útil disponível dentro da melhor faixa do Metricool para Instagram (quarta a sexta, 10h) e dentro da janela de 10h–12h indicada para público B2B; ~70% das views acontecem nos 3 primeiros dias, então sair no meio da semana dá 3 dias úteis de distribuição. Reavaliar com o histórico próprio da conta (4–6 semanas).
- Fonte do dado da tela 2: Banco Central, Relatório de Gestão do Pix 2023-2025, citado em https://crcma.org.br/noticias/pix-evolui-e-cobranca-automatica-fica-simples-e-segura-para-empresas-e-clientes

## Telas

| # | Texto na arte | Alt text |
|---|---|---|
| 1 | 5 sinais de que você ainda concilia **Pix** na mão. Eyebrow: PRA QUEM RECEBE POR PIX. DESLIZA → | Capa azul-escura com o título "5 sinais de que você ainda concilia Pix na mão" |
| 2 | O Pix cai na hora. A **conferência** não. No comércio, o QR Code dinâmico foi de 5% das transações em 2021 para 40% em 2025. Quem integra a API do Pix opera em tempo real. Quem não integra depende de processo manual. Fonte: Banco Central, Relatório de Gestão do Pix 2023-2025. Em 6 telas, 5 sinais. O quinto passa batido. | Texto sobre a diferença entre Pix instantâneo e conferência manual, com o dado do Banco Central |
| 3 | 01. Você abre o app do banco pra saber **quem pagou**. Se a venda só fecha quando você lembra de conferir o extrato, o seu caixa depende da sua memória. Bloco ilustrativo com pedido #1042, valor 150.00 e status CONCLUIDA. | Bloco de código de exemplo mostrando um pagamento Pix identificado pelo pedido |
| 4 | 02. Entra um valor e **ninguém sabe** de quê. O cliente paga e não avisa o pedido. Você cruza valor, hora e nome. Com uma cobrança por pedido, cada Pix já chega identificado. Comparação ilustrativa: extrato com R$ 150,00 de João S. contra dois pedidos de R$ 150,00. | Dois cartões: um extrato com um Pix de R$ 150,00 e uma lista de pedidos com dois valores iguais |
| 5 | 03. Cobrança de mensalidade é **mensagem** no WhatsApp. Todo mês você lembra o cliente de pagar. No Pix Automático o cliente autoriza uma vez e a cobrança recorrente acontece sozinha. Bloco ilustrativo: autorização 1x, próxima cobrança 05/11, R$ 89,90. | Bloco de exemplo de uma cobrança recorrente autorizada uma vez pelo cliente |
| 6 | 04. O fechamento do mês é uma **planilha** com 3 abas. Extrato de um lado, vendas do outro, e você cruzando. Cada fórmula quebrada é uma venda sem dono. Tags: extrato, vendas, ajustes. Fórmula ilustrativa com erro #REF!. | Três abas de planilha e uma fórmula SOMASE retornando o erro #REF! |
| 7 | 05. Ninguém sabe **quando** o erro aconteceu. Sem registro de cada evento, o erro vira discussão de memória. Quando o sistema grava cada pagamento, dá pra auditar: data, valor e origem. Log ilustrativo: pix.recebido, pedido.pago, nota.emitida do pedido #1042. | Registro de eventos de exemplo com horário de cada etapa do pedido #1042 |
| 8 | Marcou 2 ou mais? Dá pra **automatizar**. Checklist com os 5 sinais. Quer ver como eu monto isso? **Link na bio.** | Checklist com os cinco sinais e a chamada para o link da bio |

## Legenda

Seu Pix cai em segundos. Saber quem pagou ainda leva tempo? Veja 5 sinais de que está na hora de automatizar.

Nos slides eu mostro os cinco sinais de que a conciliação do Pix ainda está na mão: conferir o extrato, Pix sem identificação, mensalidade cobrada por mensagem, fechamento em planilha e erro sem registro.

Quando o sistema se integra à API do Pix, a cobrança nasce identificada e cada pagamento fica registrado. Dá pra auditar.

Salva pra consultar depois e manda pra quem ainda confere o Pix no extrato.

Quer ver como eu monto isso? Link na bio.

Fonte: Banco Central, Relatório de Gestão do Pix 2023-2025.

#pix #automacaofinanceira #conciliacaobancaria #pequenasempresas #hlbuild

## Primeiro comentário (fixar)

Fonte do dado da tela 2: https://crcma.org.br/noticias/pix-evolui-e-cobranca-automatica-fica-simples-e-segura-para-empresas-e-clientes

## Respostas prontas para comentários prováveis

- "Isso serve pra MEI?" → Serve. Quem recebe por Pix e confere no extrato já tem o problema, mesmo com poucas vendas. O que muda é o tamanho da solução.
- "Quanto custa?" → Depende do que você já usa e do que precisa integrar. Chama pelo link da bio que eu olho o seu caso.
- "Meu banco já faz isso?" → Alguns fazem parte. O ponto aqui é ligar o pagamento ao seu pedido e ao seu financeiro, que é o que costuma ficar na mão.

## Regenerar as artes

`python3 -I gerar.py && python3 -I render.py` (ajuste os caminhos no topo dos scripts). As artes finais só vão para `midia/` depois de aprovadas.
