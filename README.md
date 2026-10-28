# conteudo_insta_hl

Conteúdo do Instagram **@hl.build** (HL). Tudo que é produzido para o perfil fica aqui.

## Estrutura

- `.insta-os/perfil.md`: perfil da marca (tom, visual, nicho, públicos, portfólio, regras)
- `marca/nicho.md`: análise e definição do nicho, com fontes
- `pautas/AAAA-MM-DD/`: pauta e peças de cada semana (legendas, roteiros, textos dos slides)
- `midia/AAAA-MM-DD/`: arte já aprovada, usada como link público no agendamento
- `relatorios/`: relatório semanal de métricas
- `aprendizados.md`: o que funcionou e o que não funcionou, para guiar as próximas pautas

## Fluxo

1. Toda segunda às 8h (Fortaleza) a rotina baixa o repo, puxa as métricas do Metricool e atualiza `relatorios/` e `aprendizados.md`.
2. Monta a pauta da semana em `pautas/` e agenda como rascunho no Metricool.
3. Nada é publicado sem aprovação. Arte só entra em `midia/` depois de aprovada.

## Regra do repositório público

Não commitar dados de clientes ou leads, pipeline de prospecção, tokens, chaves ou senhas.
