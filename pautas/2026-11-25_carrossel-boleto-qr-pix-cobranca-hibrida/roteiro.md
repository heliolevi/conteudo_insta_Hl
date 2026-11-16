# Carrossel educativo: Boleto e Pix na mesma cobrança, 4 perguntas pro seu sistema

- Status: **rascunho, aguardando aprovação do Hélio** (nada agendado; artes fora de `midia/`)
- Pilar: Ensina | Público: PMEs que cobram por boleto e Pix (primário do perfil) | Formato: carrossel 8 telas, 1080×1350
- Fórmula: checklist de 4 perguntas (gancho de atualidade amarrado ao nicho). Meta principal: **salvamentos** (tela 8 é a lista para levar ao fornecedor) e **envios** ("manda pro seu contador ou pro dev")
- Por que agora: a Resolução BCB 587 (18/09/2026) criou a cobrança híbrida, com vigência em 01/02/2027; o relatório de 16/11 mostra que o único carrossel de gancho de atualidade (27/10) foi o carrossel de maior alcance; os educativos de Pix "conceito" ficaram entre 6 e 23. Tema novo, não repete a semana de Black Friday.
- Gatilhos: número específico na capa (68 dias), aversão à perda (pagamento em dobro, caixa errado), checklist final para salvar, identificação ("meu sistema baixa as duas vias?"), pico-fim (a última pergunta pede ação com o banco)
- CTA único: link na bio
- Horário: **quarta 25/11, 18h (Fortaleza)**. Ver `Horário`.
- **Atenção:** a capa diz "68 dias" porque conta de 25/11 até 01/02/2027. Se a data de publicação mudar, trocar o número em `gerar_semana_2311.py` (a conta é feita em código e o script falha se a data mudar sem ajuste) e renderizar de novo.

## Fatos conferidos (16/11/2026) e como citar

Fonte primária lida na íntegra: **Resolução BCB nº 587, de 18/09/2026** (bcb.gov.br, normativo publicado no DOU de 21/09/2026, seção 1, p. 195/196).
- Art. 11-AA: o Pix Cobrança pode ser apresentado de forma a permitir também o pagamento por boleto. Isso é a "cobrança híbrida". Vale só para o Pix Cobrança **com vencimento**, para boleto de cobrança comum e para boleto de cobrança dinâmico não vinculado a ativo financeiro escriturado.
- §4º: a oferta da cobrança híbrida é **facultativa** para o participante (instituição) do recebedor. §5º: ele precisa ser a mesma instituição emissora do boleto.
- §6º: a instituição deve estruturar a operação para prevenir pagamentos indevidos ou em duplicidade. §7º: se pagar pelo boleto, a instituição providencia o cancelamento do Pix Cobrança correspondente. Art. 39, V: o Pix é rejeitado se a cobrança híbrida já foi paga pelo boleto.
- Art. 41-A, §3º: se o Pix Cobrança for liquidado quando a obrigação já tinha sido paga por boleto, a instituição do recebedor devolve a totalidade ao pagador, **com recursos próprios, em até 24 horas** depois da liquidação.
- Art. 5º, I: essas regras (arts. 11-AA, 11-B, 32, 39, 40, 41-A e 78-HB, parágrafo único) entram em vigor em **1º de fevereiro de 2027**.
- **Fontes que divergem:** o Mix Vale (15/11/2026) escreve que a adoção é "obrigatória" em 01/02/2027. O texto da resolução diz facultativa (art. 11-AA, §4º), e o Correio Braziliense (09/10/2026) também. Matérias de abril de 2026 (Portal O Dia, A Tarde) falavam em "obrigatória a partir de novembro": foram superadas pela resolução. A arte segue a norma e diz "facultativa".
- A arte não diz que o seu sistema "precisa" fazer algo por lei: as 4 perguntas são **boa prática de integração** minha, e a tela 6 diz que a devolução ao pagador é da instituição.

## Telas

| # | Texto na arte | Alt text |
|---|---|---|
| 1 | Boleto e **Pix** na mesma cobrança. Seu sistema dá baixa uma vez só? Número "68 dias", rótulo "até 01/02/2027 · cobrança híbrida". Desliza: 4 perguntas pra guardar | Capa azul-escura com o título "Boleto e Pix na mesma cobrança. Seu sistema dá baixa uma vez só?" e o número 68 dias |
| 2 | Uma cobrança, dois **jeitos** de pagar. A Resolução BCB 587 criou a cobrança híbrida; vale a partir de 01/02/2027; oferta facultativa. Fonte: BC, Res. BCB 587, art. 11-AA e art. 5º | Texto explicando a cobrança híbrida de boleto e Pix e a data de 1º de fevereiro de 2027 |
| 3 | Pagou por um, o **outro** não vale. Boleto pago cancela o Pix; Pix a mais é devolvido pela instituição em até 24 h. Cartões "Pagou o boleto" e "Pix pago depois". Fonte: art. 11-AA §7º e art. 41-A §3º | Dois cartões: pagou o boleto, o Pix é cancelado; Pix pago depois, devolução integral em até 24 horas |
| 4 | 01. A cobrança tem um **identificador** só? Bloco: cobranca 7731, boleto, pix (txid) mesma cobrança | Bloco de exemplo mostrando boleto e Pix ligados à mesma cobrança 7731 |
| 5 | 02. A baixa roda **uma vez**? Bloco: boleto baixada, pix ignorado, caixa 1 pagamento | Bloco de exemplo com dois avisos e uma só baixa |
| 6 | 03. Um Pix **a mais** vira alerta? Bloco: já paga (boleto), alerta: pagamento a mais | Bloco de exemplo que mostra um Pix recebido em cobrança já paga e o alerta de pagamento a mais |
| 7 | Seu banco vai **oferecer**? Facultativa; emissor do boleto = recebedor do Pix. Fonte: art. 11-AA §4º e §5º | Texto sobre a oferta facultativa e a regra de mesma instituição |
| 8 | 4 perguntas pra levar ao seu **fornecedor**: identificador único, baixa uma vez só, Pix a mais vira alerta, meu banco oferece? Quando? Botão "Link na bio". Não é consultoria jurídica | Lista de verificação com 4 perguntas e botão Link na bio |

Os blocos de código são **exemplos ilustrativos** (cobrança 7731), não dado de cliente.

## Legenda

Em 1º de fevereiro de 2027, o mesmo boleto poderá vir com um QR Code do Pix. O seu sistema dá baixa uma vez só?

O Banco Central criou a cobrança híbrida: boleto e Pix Cobrança com vencimento na mesma cobrança. Se o cliente paga pelo boleto, o Pix é cancelado. Se o Pix cair mesmo assim, a instituição devolve tudo ao pagador em até 24 horas. A oferta é facultativa, então nem todo banco vai ter.

Nos slides eu mostro 4 perguntas para o sistema que cobra os seus clientes: identificador único, baixa uma vez só, alerta de pagamento a mais e se o seu banco vai oferecer.

Salva pra levar ao seu fornecedor e manda pro seu contador ou pro seu dev. Quer que eu olhe o seu fluxo de cobrança? Link na bio.

Não é consultoria jurídica: confirme na Resolução BCB nº 587. Os registros nos slides são ilustrativos.

Fonte: Banco Central, Resolução BCB nº 587, de 18/09/2026 (DOU de 21/09/2026), arts. 11-AA, 39, 41-A e 5º.

#pix #boleto #cobrancahibrida #automacaofinanceira #hlbuild

## Primeiro comentário (fixar)

Cobrança híbrida = a mesma cobrança com código de barras do boleto e QR Code do Pix. A norma é a Resolução BCB 587 (bcb.gov.br). Algumas matérias dizem que é obrigatória; o texto da resolução diz facultativa. Seu banco já avisou se vai oferecer? Me conta aqui.

## Horário (getBestTimeToPostByNetwork, Instagram, America/Fortaleza, 23 a 27/11)

- Valores por hora do Metricool na quarta: 10h = 6.506 (maior valor de seg a qui), 12h = 5.774, 18h = 4.869 (segundo pico), 19h = 3.992.
- Escolhido: **quarta 25/11, 18h**. Motivos: (1) 18h–20h é janela B2B do perfil e o segundo pico do Metricool na quarta; (2) continua o teste de horário do educativo iniciado em 18/11 (educativo às 18h), contra os 5 carrosséis de 10h (alcance 6 a 23), então o relatório de 30/11 compara 2 educativos às 18h; (3) o stories de quiz das 12h30 do mesmo dia leva ao post. Com n=5 e temas diferentes, é hipótese. Se o educativo de 18/11 não for aprovado, o teste fica com 1 ponto.

## Respostas prontas

- "Vai ser obrigatório?" → Pelo texto da Resolução BCB 587, a oferta é facultativa para a instituição de quem recebe. Algumas matérias dizem "obrigatória", mas a norma diz o contrário. Confirma com o seu banco.
- "Meu banco vai oferecer?" → Só ele pode dizer. Pergunta quando e se a mesma instituição vai emitir o boleto e receber o Pix, que é a regra da norma.
- "E se o cliente pagar os dois?" → Pela norma, o Pix é cancelado quando o boleto é pago. Se o Pix cair mesmo assim, a instituição devolve tudo ao pagador em até 24 horas, com recursos próprios.
- "Precisa mudar meu sistema?" → Depende de como ele recebe os avisos hoje. Chama pelo link da bio que eu olho o seu caso.

## O que medir depois (relatório de 30/11)

Alcance (contra 8,0 de média dos carrosséis de 09/11 a 15/11), salvamentos por alcance (meta 2%), envios por alcance, comentários, e a comparação com o educativo de 18/11 (se for ao ar).

## Regenerar

`python3 -I pautas/_gerador/gerar_semana_2311.py` (gera os HTML em `slides/`) e `python3 -I pautas/_gerador/render.py 2026-11-25 <pasta-de-saida>` (PNG; fora do repo até a aprovação).
