# Reel: Simulei uma Black Friday de 500 Pix

- Status: **rascunho, aguardando aprovação do Hélio** (nada agendado; vídeo e capa fora de `midia/`)
- Pilar: Trabalho / prova (prova própria, não cliente) | Público: lojas virtuais e PMEs que vendem por Pix | Formato: reel 9:16, 16,0 s, 1080×1920, 30 fps, **sem áudio** (todo o texto está na tela; funciona no mudo)
- Por que agora: o relatório de 16/11 mostra que prova concreta alcançou 205 a 473 pessoas e as explicações de Pix ficaram entre 6 e 126; o reel de 10/11 (número parado no quadro 1) alcançou 26 e os 4 reels da conta têm 72% a 80% de pulo. Este reel abre **com movimento desde 0,0 s** (contador de 0 a 500 e log rodando) e usa um resultado calculado em código. Hipótese, n pequeno.
- Gatilhos: movimento e número no quadro 1, pergunta que aponta para o espectador ("quantos você confere na mão?"), três viradas curtas (01, 02, 03), resultado contraintuitivo no fim (3 de 500), identificação (loja que fecha o caixa), loop (o último quadro volta ao 500)
- Sinais do Instagram: tempo assistido (16 s, texto queimado), envios por alcance ("manda pra quem fecha o caixa"), comentários (a pessoa conta quantos Pix confere por dia)
- CTA único: link na bio
- Horário: **terça 24/11, 12h (Fortaleza)**. Ver `Horário`.

## Premissa e o que o vídeo afirma

É uma **simulação com dados fictícios**, e o vídeo diz isso na tela o tempo todo ("SIMULAÇÃO · DADOS FICTÍCIOS" fixo e "// ilustrativo" em cada bloco). Os números vêm de `simular.py` (semente 2711), que gera 500 pedidos pagos por Pix e injeta três falhas com taxas que **eu defini**: 2% de avisos perdidos, 3% duplicados, 3% de Pix sem txid. Resultado da execução: 468 baixas por txid, 12 avisos em dobro ignorados, 17 Pix sem txid casados por valor e horário, 12 avisos perdidos recuperados pela varredura, 3 na fila de conferência (0,6%).
Com outras taxas ou outra semente o resultado muda, e a legenda diz isso. O vídeo não afirma resultado de loja real nem de cliente. Nenhum dado de mercado na tela.

## Roteiro (texto na tela)

| Tempo | Tela |
|---|---|
| 0,0 a 2,9 s | Gancho: contador sobe de 0 a **500** em 2,5 s com o log `pix.recebido T1xxx ok` rodando · "Pix em um dia. Quantos você confere **na mão**?" · rótulo "Black Friday simulada" |
| 2,9 a 6,2 s | 01 · **12** avisos vieram em **dobro**. Bloco "Regra 1: baixar uma vez": T1011 baixado, depois "em dobro: ignorado" |
| 6,2 a 9,7 s | 02 · **20** Pix vieram sem **txid**. Bloco "Regra 2: valor e horário": Pix sem txid R$ 299,90, 1 cobrança pendente, "casado: pedido 1286" |
| 9,7 a 12,7 s | 03 · **12** avisos **sumiram**. Bloco "Regra 3: varredura": txid T1058 sem aviso, extrato R$ 249,90, "baixado pela varredura" |
| 12,7 a 15,7 s | Resultado: "Sobraram **3** para conferir na mão." Bloco "Fim do dia": 500 pedidos, 497 baixados sozinhos, 3 na fila. CTA sobreposto a partir de 14,4 s: MANDA PRA QUEM FECHA O CAIXA · Link na bio. |
| 15,7 a 16,0 s | Loop: volta ao quadro 1 (já com 500) |

Área segura: nada importante nos 250 px de cima e de baixo nem nos 130 px da direita. O rótulo "SIMULAÇÃO · DADOS FICTÍCIOS" fica a 1570 px.

## Áudio

Sem áudio por padrão. Opcional: locução (ElevenLabs) ou música da biblioteca do Instagram em volume baixo; com locução eu reajusto o tempo das cenas à voz. Texto sugerido, uma frase por arquivo:

```
Quinhentos Pix em um dia de Black Friday. Quantos você confere na mão?
Doze avisos vieram em dobro.
Vinte Pix vieram sem txid.
Doze avisos sumiram.
Sobraram três para conferir na mão. Manda pra quem fecha o caixa.
```

## Legenda

Black Friday simulada: 500 Pix num dia. Sobraram 3 para eu conferir na mão.

Rodei uma simulação com dados fictícios, com três falhas que acontecem: aviso de pagamento em dobro, Pix sem txid e aviso que não chega. O sistema baixa uma vez só, casa por valor e horário quando falta o txid, varre o extrato no fim do dia e joga o que for dúvida numa fila.

As taxas de falha são premissas minhas (2%, 3% e 3%). Em loja real o resultado muda. A ordem das regras é que serve.

Manda pra quem fecha o caixa da loja. Quer isso no seu fluxo? Link na bio.

Dado de mercado: o Pix respondeu por 50,8% dos pedidos das lojas da Nuvemshop entre agosto e 22/10/2026 (Central do Varejo, 09/11/2026).

#pix #blackfriday2026 #conciliacaobancaria #lojavirtual #hlbuild

## Primeiro comentário (fixar)

As 4 regras detalhadas estão no carrossel de quinta (26/11). Quantos Pix você confere na mão num dia de promoção? Me conta aqui.

## Descrição da capa / alt text

Capa azul-escura com o rótulo "Black Friday simulada", o número 500 e a pergunta "Pix em um dia. Quantos você confere na mão?", acima de um bloco que mostra o log de Pix recebidos. O vídeo mostra três falhas simuladas (aviso em dobro, Pix sem txid e aviso perdido) e termina com 497 de 500 pedidos baixados sozinhos e 3 na fila de conferência. Todos os registros são exemplos fictícios.

## Horário (getBestTimeToPostByNetwork, Instagram, America/Fortaleza, 23 a 27/11)

- Valores por hora do Metricool na terça: 10h = 4.942 (pico), 12h = 4.656, 18h = 4.788 (segundo pico), 19h = 3.984.
- Escolhido: **terça 24/11, 12h**. Motivos: (1) fica na janela 10h–12h do público B2B do perfil, a 6% do pico do Metricool; (2) é um horário que a conta ainda não testou com reel em dia útil, e o relatório de 16/11 mostra que 10h–11h (6 a 153), 14h35 (380), 18h (26), 19h (276) e 23h31 (473) não ordenam o alcance, então o objetivo é ter mais um ponto, não confirmar uma tese; (3) véspera de Black Friday: quem tem loja está online e abre o Instagram no almoço. Com n=5 e temas diferentes, é hipótese.
- O story de lembrete (seg 23/11, 12h32, contagem regressiva) prepara a audiência atual.

## Respostas prontas

- "Isso é de uma loja real?" → Não. É uma simulação com dados fictícios que eu rodei em código, com taxas de falha que eu defini. Serve pra mostrar a ordem das regras, não o resultado de uma loja.
- "O que é txid?" → É o identificador da cobrança Pix. Quando o Pix chega com ele, o sistema sabe de qual pedido é.
- "Como funciona a varredura?" → No fim do dia o sistema consulta os Pix recebidos pelo banco e baixa os que ficaram sem aviso. Os detalhes estão no carrossel de quinta.
- "Quanto custa?" → Depende do que você já usa. Chama pelo link da bio que eu olho o seu caso.

## O que medir depois (relatório de 30/11)

Alcance (contra 26 do reel de 10/11, 380 do Shalom e, se aprovado, o reel de 17/11), % de views acima de 3 s (meta: mais de 65%), taxa de pulo (meta: abaixo de 35%), tempo médio assistido ÷ 16 s (meta: 50%), envios por alcance (meta 1%), comentários com a quantidade de Pix que a pessoa confere.

## Regenerar

`python3 -I pautas/2026-11-24_reel-black-friday-simulada/simular.py` (gera `resultado.json`)
`python3 -I pautas/2026-11-24_reel-black-friday-simulada/gerar_reel.py && python3 -I pautas/2026-11-24_reel-black-friday-simulada/render_reel.py <pasta-de-saida>`

Requer playwright com chromium e ffmpeg. A capa sai como `capa-reel.png` na mesma pasta de saída (quadro de 2,4 s).
