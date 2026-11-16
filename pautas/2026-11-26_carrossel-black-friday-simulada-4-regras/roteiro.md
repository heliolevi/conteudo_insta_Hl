# Carrossel de prova: Black Friday simulada, as 4 regras que deixaram 3 Pix na mão

- Status: **rascunho, aguardando aprovação do Hélio** (nada agendado; artes fora de `midia/`)
- Pilar: Trabalho / prova (**prova própria**, simulação em código; não é cliente) | Público: lojas virtuais e PMEs que vendem por Pix | Formato: carrossel 8 telas, 1080×1350
- Fórmula: framework de 4 regras com resultado calculado. Meta principal: **salvamentos** (a tela 8 é a lista de 4 regras) e **envios** ("manda pra quem fecha o caixa")
- Por que agora: Black Friday cai em 27/11 (sexta), e o carrossel sai na quinta, véspera. Segue o reel de terça (mesmo resultado, mais detalhe). O relatório de 16/11 mostra que prova concreta alcançou 205 a 473 pessoas; o perfil não tem cliente real autorizado para o nicho, então a prova é um código que roda.
- Gatilhos: resultado no título (3 de 500), as 4 regras numeradas (loop aberto na capa), código/log como imagem (assinatura da marca), honestidade na tela 2 (premissas), checklist final para salvar, identificação ("já conferi Pix na mão")
- CTA único: link na bio
- Horário: **quinta 26/11, 10h (Fortaleza)**. Ver `Horário`.

## Premissa e o que o carrossel afirma

Todos os números das telas vêm de `pautas/2026-11-24_reel-black-friday-simulada/resultado.json`, gerado por `simular.py` (semente 2711), e o gerador `gerar_semana_2311.py` lê o JSON, sem digitar número à mão. É uma **simulação com dados fictícios** e taxas de falha que eu defini (2% de avisos perdidos, 3% duplicados, 3% de Pix sem txid). A tela 2 diz isso, a tela 7 repete ("Em loja real o número muda") e todos os blocos levam `// ilustrativo`. O carrossel não afirma que o Payments API ou qualquer produto meu faz isso em produção: ele mostra a lógica de um conciliador. **Se o Hélio quiser ligar à Payments API ("é assim que ela trata"), precisa confirmar antes; a arte atual não faz essa afirmação.**
Resultado da execução: 500 pedidos; 468 baixados por txid; 12 avisos em dobro ignorados; 17 Pix sem txid casados por valor e horário (janela de 30 min, uma única cobrança candidata); 12 avisos perdidos recuperados pela varredura; 3 na fila de conferência (2 cobranças do mesmo valor pendentes ao mesmo tempo); 497 baixados sozinhos (0,6% na mão).
Nenhum dado de mercado nas telas.

## Telas

| # | Texto na arte | Alt text |
|---|---|---|
| 1 | Simulei uma **Black Friday**. 500 Pix, 3 para conferir na mão. Bloco "Simulação · 500 pedidos": pedidos 500, baixados sozinhos 497, pra conferir 3. Desliza: as 4 regras que fizeram isso | Capa azul-escura com o título "Simulei uma Black Friday. 500 Pix, 3 para conferir na mão." e um bloco com os números da simulação |
| 2 | Dado **fictício**. Premissas minhas. Não é loja nem cliente real; 3 falhas; as taxas são minhas. Bloco "Premissas": aviso perdido 2%, aviso duplicado 3%, Pix sem txid 3% | Texto avisando que os dados são fictícios e um bloco com as três taxas de falha usadas |
| 3 | 01. Baixar **uma vez** só. 12 avisos em dobro ignorados. Bloco: 00:51:45 T1011 baixado / em dobro: ignorado | Bloco de exemplo em que o mesmo aviso do txid T1011 chega duas vezes e o segundo é ignorado |
| 4 | 02. Sem txid, **valor e horário**. 17 casados. Bloco: Pix sem txid R$ 299,90, 1 cobrança pendente, casado: pedido 1286 | Bloco de exemplo em que um Pix de 299,90 sem txid é casado com o pedido 1286 por valor e horário |
| 5 | 03. Aviso perdido? **Varredura**. 12 recuperados. Bloco: txid T1058 sem aviso, extrato R$ 249,90 às 21:56, baixado pela varredura | Bloco de exemplo em que a varredura do extrato baixa o txid T1058, que não teve aviso |
| 6 | 04. O que **não casa** vai pra fila. 3 na fila. Bloco: Pix sem txid R$ 299,90 às 12:11, 2 cobranças pendentes, ambíguo: fila de conferência | Bloco de exemplo em que um Pix de 299,90 tem duas cobranças candidatas e vai para a fila de conferência |
| 7 | 500 Pix. **3** na mão. Bloco "Resultado": baixa por txid 468, valor + horário 17, varredura 12, fila na mão 3. Simulação com dados fictícios e premissas minhas | Bloco com o resultado da simulação: 468 baixas por txid, 17 por valor e horário, 12 pela varredura e 3 na fila |
| 8 | As 4 regras pra **salvar**: baixar uma vez só, sem txid: valor e horário, aviso perdido: varredura, dúvida vai pra fila. Botão "Link na bio" | Lista de verificação com as 4 regras e botão Link na bio |

## Legenda

Simulei uma Black Friday de 500 Pix. A simulação deixou 3 para eu conferir na mão.

Não é loja nem cliente real: é um script com dados fictícios e três falhas que acontecem: aviso de pagamento em dobro, Pix que chega sem txid e aviso que não chega. As taxas de falha são premissas minhas (2%, 3% e 3%). Em loja real o resultado muda.

As 4 regras que fizeram isso:
1. Baixar uma vez só
2. Sem txid, casar por valor e horário
3. Aviso perdido? Varredura no fim do dia
4. Dúvida vai pra uma fila, com o motivo

Salva as 4 regras e manda pra quem fecha o caixa da loja. Quer isso no seu fluxo? Link na bio.

Simulação ilustrativa, semente 2711. Os registros nos slides são exemplos.

#pix #conciliacaobancaria #blackfriday2026 #automacaofinanceira #hlbuild

## Primeiro comentário (fixar)

Txid é o identificador da cobrança Pix. Varredura é consultar os Pix recebidos pelo banco em um período e comparar com o que o sistema já baixou. Quantos Pix você confere na mão num dia de promoção? Me conta aqui.

## Horário (getBestTimeToPostByNetwork, Instagram, America/Fortaleza, 23 a 27/11)

- Valores por hora do Metricool na quinta: 10h = 6.275 (segundo maior valor de seg a sex), 12h = 5.730, 18h = 5.078 (segundo pico), 19h = 4.124.
- Escolhido: **quinta 26/11, 10h**. Motivos: (1) é a janela 10h–12h do público B2B e véspera de Black Friday, quando quem tem loja olha o caixa de manhã; (2) o relatório de 16/11 diz que 10h não é confirmado nem descartado pela conta (6 a 153 de alcance, tema diferente a cada vez), então o teste fica limpo: mesmo horário que o carrossel da semana anterior, mas com prova no lugar de explicação; (3) o story de divulgação sai às 12h30. Com n=5 e temas diferentes, é hipótese.
- Sexta 27/11 (Black Friday) fica sem feed: quem vende está operando.

## Respostas prontas

- "Isso é de uma loja real?" → Não. É uma simulação com dados fictícios que eu rodei em código, com taxas de falha que eu defini. Serve pra mostrar a ordem das regras.
- "Posso ver o código?" → O script está no repositório do perfil, na pasta desta pauta. É um exemplo de lógica, não é produto pronto.
- "E se tiver dois Pix do mesmo valor ao mesmo tempo?" → É o caso da regra 4: o sistema não chuta, joga na fila com o motivo.
- "Quanto custa?" → Depende do que você já usa. Chama pelo link da bio que eu olho o seu caso.

## O que medir depois (relatório de 30/11)

Alcance (contra 8,0 de média dos carrosséis de 09/11 a 15/11 e a mediana de 13 dos 5 carrosséis de Pix/NF-e/BF), salvamentos por alcance (meta 2%), envios por alcance (meta 1%), comentários, seguidores atribuídos a post.

## Regenerar

`python3 -I pautas/2026-11-24_reel-black-friday-simulada/simular.py` (gera `resultado.json`), depois
`python3 -I pautas/_gerador/gerar_semana_2311.py` e `python3 -I pautas/_gerador/render.py 2026-11-26 <pasta-de-saida>` (PNG fora do repo até a aprovação).
