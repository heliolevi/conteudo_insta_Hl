# Carrossel: O caminho de um Pix em 5 eventos

- Status: **agendado no Metricool para sexta, 06/11, 10h (Fortaleza)**, a pedido do Hélio em 30/10. Artes em `midia/2026-11-06_carrossel-pix-auditavel-5-eventos/`.
- Pilar: Prova/mecânica (como eu desenho) | Público: PMEs que cobram por Pix e quem integra pagamentos | Formato: carrossel 8 telas, 1080×1350
- Fórmula: IG8 (framework "steal this"). Meta principal: **salvamentos** (tela 8 é o mapa) e **envios** (para dev ou contador)
- Gatilhos: loop aberto ("se um dos 5 falta..."), especificidade (log como imagem, assinatura da marca), pico-fim (tela 7), mapa final para salvar
- Limite de fatos: o post só afirma o que o perfil confirma (stack Node.js, Express e MongoDB da Payments API, produto próprio). Todos os registros são **ilustrativos** e estão marcados. Nenhum número de resultado.
- CTA único: link na bio

## Telas

| # | Texto na arte | Alt text |
|---|---|---|
| 1 | O caminho de um **Pix** em 5 eventos. Bloco com a trilha do pedido 1042. Desliza: o mapa completo | Capa com um registro de cinco eventos de um pedido pago por Pix |
| 2 | Um Pix sem trilha é um **palpite**. Se um dos 5 eventos falta, a conciliação vira adivinhação. Lista dos 5 eventos | Texto e lista dos cinco eventos do fluxo de cobrança |
| 3 | 01. A cobrança nasce com o **pedido**. JSON de cobranca.criada | Bloco de código com o evento cobranca.criada |
| 4 | 02. O banco avisa, o sistema **registra**. JSON de pix.recebido | Bloco de código com o evento pix.recebido |
| 5 | 03. O pedido só muda de status com **prova**. JSON de pedido.pago | Bloco de código com o evento pedido.pago |
| 6 | 04. A nota sai **amarrada** ao pagamento. JSON de nota.emitida | Bloco de código com o evento nota.emitida |
| 7 | 05. O fechamento é uma **consulta**, não uma planilha. JSON de conciliado com 1 divergência | Bloco de código mostrando uma divergência encontrada na conciliação |
| 8 | O mapa pra **salvar**. Os 5 eventos em sequência, link na bio | Mapa com os cinco eventos e botão link na bio |

## Legenda

Se um desses 5 eventos falta, a conciliação vira adivinhação.

Um Pix auditável tem trilha: cobrança criada, Pix recebido, pedido pago, nota emitida e conciliado. Nos slides eu mostro cada evento e o que ele responde sem você abrir o extrato.

Eu monto esse tipo de fluxo em Node.js, Express e MongoDB, o stack da minha Payments API. Os registros nos slides são ilustrativos.

Salva o mapa e manda pra quem ainda fecha o mês no extrato. Link na bio.

#pix #conciliacaobancaria #automacaofinanceira #desenvolvimentodesoftware #hlbuild

## Respostas prontas

- "Isso serve pra outro meio de pagamento?" → A ideia da trilha serve pra boleto e cartão também. Os nomes dos eventos mudam, o princípio não.
- "Você faz isso sob medida?" → Faço. Chama pelo link da bio e me conta como você cobra hoje.
