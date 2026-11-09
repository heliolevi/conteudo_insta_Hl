# Reel: 3 motivos para um Pix pago continuar "aguardando"

- Status: **rascunho, aguardando aprovação do Hélio** (nada agendado; vídeo e capa fora de `midia/`)
- Pilar: Ensina / Trabalho | Público: lojas virtuais e PMEs que vendem por Pix | Formato: reel 9:16, 16,0 s, 1080×1920, 30 fps, **sem áudio** (todo o texto está na tela; funciona no mudo)
- Por que agora: o relatório de 09/11 mostra 2 semanas sem reel e o alcance diário da conta caindo 83% (542 para 90). Reel é a porta de entrada da conta (205 e 473 de alcance nos dois reels) e o gargalo é o gancho (22% e 28,4% das views acima de 3 s). Este é o 2º reel com número no quadro 1 (o 1º é o de 10/11), para ter dois reels comparáveis. Hipótese, n pequeno.
- Gatilhos: número no quadro 1 (já com o contraste "Pix recebido ok, pedido aguardando"), loop aberto ("3 motivos"), três viradas curtas (01, 02, 03) e a solução no fim, identificação ("já aconteceu na minha loja"), fim logo depois da recompensa, loop (o último quadro volta ao primeiro)
- Sinais do Instagram: tempo assistido (16 s, quadro 1 com informação, legenda queimada), envios por alcance ("manda pra quem cuida da loja"), comentários (a pessoa conta se já aconteceu na loja dela)
- CTA único: link na bio
- Horário: **terça 17/11, 18h (Fortaleza)**. Ver `Horário`.

## Premissa e o que o vídeo afirma

Nenhum dado de mercado. O vídeo afirma só o mecanismo: quando o aviso do pagamento (webhook) falha, chega sem identificar o pedido ou dá erro sem alerta, o pedido pode ficar parado mesmo com o Pix pago. A causa real de cada caso depende do sistema, e a legenda diz isso. Todos os registros levam `// ilustrativo`.

## Roteiro (texto na tela)

| Tempo | Tela |
|---|---|
| 0,0 a 2,9 s | Gancho: "PIX PAGO. PEDIDO PARADO." · número **3** grande · "motivos para um Pix pago continuar **aguardando**." · bloco com `pix.recebido ok` e `pedido.status aguardando` já no quadro 1 |
| 2,9 a 6,2 s | 01 · O aviso não **chegou**. Bloco: POST /webhook/pix, resposta 504 timeout, pedido aguardando |
| 6,2 a 9,7 s | 02 · O aviso veio sem **pedido**. Bloco: valor R$ 240,00, txid vazio, pedido não achado |
| 9,7 a 12,7 s | 03 · Deu erro e **ninguém** viu. Bloco: erro gravado, alerta nenhum, reprocesso nenhum |
| 12,7 a 15,7 s | Solução: Registrar, tentar de novo e **conciliar** pelo txid. Bloco: evento registrado, tentativa 1 falhou, tentativa 2 ok, pedido pago. CTA sobreposto a partir de 14,4 s: MANDA PRA QUEM CUIDA DA LOJA · Link na bio. |
| 15,7 a 16,0 s | Loop: volta ao quadro 1 |

Área segura: nada importante nos 250 px de cima e de baixo nem nos 130 px da direita.

## Áudio

Sem áudio por padrão. Se quiser locução (ElevenLabs) ou música da biblioteca do Instagram em volume baixo, é opcional; com locução eu reajusto o tempo das cenas à voz. Texto sugerido para a locução (uma frase por arquivo):

```
Pix pago, pedido parado. Três motivos.
Um: o aviso não chegou.
Dois: o aviso veio sem pedido.
Três: deu erro e ninguém viu.
Registre, tente de novo e concilie pelo txid.
Manda pra quem cuida da loja.
```

## Legenda

3 motivos para um Pix pago continuar "aguardando pagamento" na sua loja.

O cliente pagou, o dinheiro caiu e o pedido segue parado. Quando isso acontece, costuma ser um destes: o aviso do pagamento (webhook) não chegou, chegou sem identificar o pedido, ou deu erro e ninguém viu.

Quando o sistema registra o aviso, tenta de novo e concilia pelo txid, o pedido muda sozinho para pago.

Manda pra quem cuida da loja virtual. Quer que eu olhe o seu fluxo de pagamento? Link na bio.

Os registros do vídeo são ilustrativos. A causa real depende do seu sistema.

#pix #lojavirtual #webhook #automacaofinanceira #hlbuild

## Primeiro comentário (fixar)

Webhook é o aviso que o banco ou a plataforma de pagamento manda para o seu sistema quando um Pix cai. Se ele falha, o pedido não muda de status. Já aconteceu na sua loja? Me conta aqui.

## Descrição da capa / alt text

Capa azul-escura com o número 3 e o texto "motivos para um Pix pago continuar aguardando", acima de um bloco de exemplo que mostra Pix recebido ok e pedido aguardando. O vídeo mostra três motivos em blocos de exemplo (aviso que não chegou, aviso sem pedido e erro sem alerta) e termina com o pedido pago depois de uma nova tentativa.

## Horário (getBestTimeToPostByNetwork, Instagram, America/Fortaleza, 16 a 20/11)

- Valores por hora do Metricool na terça: 10h = 4.942, 18h = 4.788 (segundo pico), 19h = 3.984.
- Escolhido: **terça 17/11, 18h**. Motivos: (1) mesmo horário do reel de 10/11, para os dois reels serem comparáveis; (2) 18h–20h é janela B2B do perfil, e o Metricool mostra mais engajamento de reel à noite; (3) na conta, o alcance das peças da noite foi maior (reel 23h31: 473; carrossel 19h: 273) que o das de 10h–11h (11 a 152). Com n=5 e temas diferentes, é hipótese.
- O story de lembrete (seg 16/11, 12h32, contagem regressiva) prepara a audiência atual.

## Respostas prontas

- "O que é webhook?" → É o aviso que o banco ou a plataforma de pagamento manda pro seu sistema quando o Pix cai. Se esse aviso falha, o sistema não sabe que o pedido foi pago.
- "Acontece na minha plataforma de loja?" → Pode acontecer em qualquer uma. A causa depende de como o pagamento foi ligado ao pedido. Chama pelo link da bio que eu olho o seu caso.
- "Como resolve?" → Registrar cada aviso, tentar de novo se falhar e identificar o Pix pelo pedido (txid). Aí sobra só a divergência pra conferir.
- "Quanto custa?" → Depende do que você já usa. Chama pelo link da bio.

## O que medir depois (relatório de 23/11)

Alcance (contra 205 e 473 dos reels antigos e o reel de 10/11), % de views acima de 3 s (meta: mais de 65%), tempo médio assistido ÷ 16 s (meta 50%), envios por alcance (meta 1%), comentários com "já aconteceu". Registrar o resultado das 18h do dia 10/11 e do dia 17/11.

## Regenerar

`python3 -I pautas/2026-11-17_reel-pix-pago-aguardando/gerar_reel.py && python3 -I pautas/2026-11-17_reel-pix-pago-aguardando/render_reel.py <pasta-de-saida>`

Requer playwright com chromium e ffmpeg. A capa sai como `capa-reel.png` na mesma pasta de saída.
