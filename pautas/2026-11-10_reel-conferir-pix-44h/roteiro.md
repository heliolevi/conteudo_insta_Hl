# Reel: Conferir Pix na mão custa 44 horas por ano

- Status: **rascunho, aguardando aprovação do Hélio** (nada agendado; vídeo e capa fora de `midia/`)
- Pilar: Ensina / Prova | Público: PMEs que recebem por Pix | Formato: reel 9:16, 18,3 s, 1080×1920, 30 fps, com locução (ElevenLabs, voz Carla) sincronizada
- Por que agora: o relatório de 26/10 a 01/11 mostra que reel é o formato de maior alcance (461 e 199 contas) e que o gargalo é o gancho (só 22% e 28,3% das views passaram de 3 s, e o tempo médio foi 7,4 s e 9,7 s). Hipótese, 2 reels: número específico no quadro 1 segura mais que abertura de marca.
- Gatilhos: número específico no quadro 1, "faça a conta" (o leitor troca pelos próprios números), virada em ~55% (44 h vence uma semana de 40 h), loop (o último quadro volta ao primeiro), pico-fim (a divergência)
- Sinais do Instagram: tempo assistido (15 s, quadro 1 já com informação, duas viradas, legenda queimada, fim logo após a recompensa), envios por alcance ("manda pra quem fecha o caixa"), comentários (a pessoa responde quanto deu na conta dela)
- CTA único: link na bio
- Horário: **terça 10/11, 18h (Fortaleza)**. Ver `Horário` abaixo.

## Premissa da conta (visível no vídeo e na legenda)

10 min por dia útil × 22 dias úteis = 220 min por mês (3h40) × 12 meses = 2.640 min = **44 h por ano**. 44 h ficam acima de uma semana de trabalho de 40 h. Os 10 min por dia são um exemplo ilustrativo, marcado como tal; o leitor troca pelos números dele. Não é dado de mercado, então não leva fonte.

## Roteiro (texto na tela e locução, sincronizados com o áudio)

Tempos medidos na locução entregue (18,2 s). O vídeo foi retemporizado para cada palavra cair junto da imagem.

| Tempo | Locução | Tela |
|---|---|---|
| 0,0 a 2,9 s | "Quarenta e quatro horas por ano conferindo Pix." | Gancho: número grande já no quadro 1, zoom leve. CONFERIR PIX NA MÃO CUSTA · **44h** · por ano. |
| 2,9 a 11,2 s | "Faça a conta." (2,9) | Faça a **conta**. Bloco de log digitado linha a linha |
| | "Dez minutos por dia..." (4,2) | 10 min por dia útil |
| | "vinte e dois dias úteis..." (5,9) | × 22 dias úteis, depois = 220 min (3h40 por mês) em 7,0 |
| | "doze meses." (7,9) | × 12 meses |
| | "Quarenta e quatro horas." (9,5) | = 2.640 min = 44 h (em ciano) · "Troque pelos seus números." |
| 11,1 a 13,5 s | "Mais que uma semana de trabalho." (11,3) | Virada: barras de 40 h e 44 h crescem. Mais que uma **semana** de trabalho. |
| 13,4 a 17,95 s | "Com o Pix identificado, sobra só a divergência." (13,5) | Com o Pix identificado, sobra só a **divergência**. Bloco de conciliação, divergência em 15,5 |
| 16,45 a 17,95 s | "Manda para quem fecha o caixa." (16,5) | CTA sobreposto: MANDA PRA QUEM FECHA O CAIXA · Link na bio. |
| 17,95 a 18,3 s | | Loop: volta ao quadro 1 (44h) |

Área segura: nada importante nos 250 px de cima e de baixo nem nos 130 px da direita. Blocos de log marcados `// ilustrativo`.

## Áudio

O arquivo final leva a locução da Carla (ElevenLabs), normalizada em -16 LUFS, sem música. Para música, use faixa da biblioteca do Instagram em volume bem baixo (no agendamento, `audioConfiguration` com `audioVolume` baixo; só funciona em conta business ligada a página do Facebook). Antes, a sugestão era: áudio original do Hélio (voz lendo a conta) ou faixa da biblioteca do Instagram em volume baixo (no agendamento, `audioConfiguration` com `audioVolume` baixo; só funciona em conta business ligada a página do Facebook). Se for usar voz sintética (ElevenLabs) ou gravar a sua, o texto e a direção estão na seção **Locução** abaixo.

## Locução (ElevenLabs)

Uma frase por arquivo, nomeados na ordem (01 a 07). Voz do Brasil, masculina, firme e rápida; testar 2 ou 3 vozes com a frase 01. Os tempos são onde cada frase entra no vídeo atual (15 s); se a voz passar do tempo, ajusto o vídeo para durar mais.

**Com tags (v3)**

```
[confident, fast] Quarenta e quatro horas por ano conferindo Pix.
[calm] Faça a conta.
Dez minutos por dia... vinte e dois dias úteis... doze meses.
[building up] Quarenta e quatro horas.
[surprised, clear] Mais que uma semana de trabalho.
[warm, confident] Com o Pix identificado, sobra só a divergência.
[friendly, inspiring] Manda pra quem fecha o caixa.
```

**Sem tags (Multilingual v2)**

```
Quarenta e quatro horas por ano conferindo Pix.
Faça a conta.
Dez minutos por dia, vinte e dois dias úteis, doze meses.
Quarenta e quatro horas.
Mais que uma semana de trabalho.
Com o Pix identificado, sobra só a divergência.
Manda pra quem fecha o caixa.
```

**Direção**

| # | Entra em | Intenção | Como falar |
|---|---|---|---|
| 01 | 0,0 s | gancho | direto, sem "oi", cortando o ar; "quarenta e quatro" com ênfase |
| 02 | 3,0 s | convite | mais baixo e calmo, curta |
| 03 | 3,6 s | conta | ritmo de contagem, uma pausa curta depois de cada item |
| 04 | 6,5 s | resultado | desacelera, peso no número |
| 05 | 7,9 s | virada | surpresa contida, "semana" levemente mais forte |
| 06 | 10,9 s | solução | mais leve e aliviada, firme em "divergência" |
| 07 | 13,3 s | pedido | caloroso, acabando com sorriso, sem alongar a última sílaba |

Pronúncia: "Pix" lido "píks". Números por extenso (já estão assim). Volume da música, se houver, 18 a 22 dB abaixo da voz.

## Legenda

Conferir Pix na mão custa 44 horas por ano.

A conta é simples e você troca pelos seus números: 10 minutos por dia útil, vezes 22 dias, dá 3h40 por mês. Em 12 meses são 44 horas, mais que uma semana de trabalho de 40 horas só olhando extrato.

Quando cada Pix já chega identificado pelo pedido, sobra só a divergência pra conferir.

Manda pra quem fecha o caixa da sua empresa. Quer que eu olhe o seu fluxo? Link na bio.

Premissa da conta: 10 min por dia e 22 dias úteis por mês (exemplo ilustrativo).

#pix #automacaofinanceira #conciliacaobancaria #pequenasempresas #hlbuild

## Primeiro comentário (fixar)

A conta: 10 min × 22 dias × 12 meses = 2.640 min = 44 h. Troca pelo seu tempo e me conta nos comentários quanto deu.

## Descrição da capa / alt text

Capa azul-escura com o texto "Conferir Pix na mão custa 44h por ano". Vídeo com a conta digitada em um bloco de log, duas barras comparando 40 horas de trabalho com 44 horas conferindo Pix, e um bloco de conciliação com uma divergência.

## Horário (getBestTimeToPostByNetwork, Instagram, America/Fortaleza, 09 a 13/11)

- Valores por hora do Metricool: terça tem pico às 10h (4.942) e segundo pico às 18h (4.788); 19h cai para 3.984.
- Escolhido: **terça 18h**. Motivos: (1) reels têm mais engajamento à noite nos dados do Metricool e o alcance da conta confirma de leve (reel das 23h31 alcançou 461 contas; o das 11h22 alcançou 199; n=2, com tema diferente, é hipótese); (2) 18h–20h é janela B2B do perfil; (3) o educativo de quarta e o de sexta ocupam 10h, e assim cada formato testa um horário.
- Deixar o reel na terça dá três dias úteis de distribuição (cerca de 70% das views de um reel acontecem nos 3 primeiros dias).

## Respostas prontas

- "Quanto deu na minha conta?" → Me conta: quantos minutos por dia e quantos dias por mês? Eu faço a conta com você.
- "Serve pra MEI?" → Serve. Quem recebe por Pix e confere no extrato já tem esse custo, mesmo com poucas vendas.
- "Como identifica o Pix por pedido?" → A cobrança nasce com o número do pedido, então cada Pix já chega com dono. Chama pelo link da bio que eu olho o seu caso.

## O que medir depois (relatório de 16/11)

Alcance, % de views acima de 3 s (hoje 22% e 28,3%; meta: mais de 65%), tempo médio assistido ÷ 15 s (meta 50%), envios por alcance (meta 1%), comentários com a conta feita. Registrar se o horário das 18h repete o desempenho noturno.

## Regenerar

`python3 -I pautas/2026-11-10_reel-conferir-pix-44h/gerar_reel.py && python3 -I pautas/2026-11-10_reel-conferir-pix-44h/render_reel.py <pasta-de-saida>`
