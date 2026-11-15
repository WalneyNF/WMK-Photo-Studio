# WMK Photo Studio — Roadmap próprio (15/11/2026)

Este plano complementa o ROADMAP.md original do PhotoCraft. Diferenciar sempre funcionalidades herdadas de recursos novos e efetivamente testados.

| Prioridade | Recurso | Situação no fork WMK | Critério para conclusão |
|---|---|---|---|
| P0 | README pt-BR e identidade visual | Publicado | Conferir visual e créditos |
| P0 | EXE Windows pelo Actions | Em validação | Build verde + EXE inicia em Windows |
| P0 | Logo no EXE, janela e pacote | Em validação | Conferir ícones reais na barra de tarefas |
| P0 | Tradução pt-BR no build | Em validação | Catálogo incorporado e idioma selecionável |
| P0 | Segurança ao salvar e abrir PSD | Parcial no motor original | Testes de regressão sem corrupção |
| P1 | Conversão segura em lote via CLI | Script inicial publicado | Testes + fotos reais + relatório |
| P1 | Painéis móveis e layouts JSON | Base existente | Presets WMK e testes de persistência |
| P1 | Laboratório de fotografia | Base existente | Antes/Depois e presets WMK |
| P1 | GPU modesta e fallback CPU | Base existente | Testes com GPU 2 GB e render CPU |
| P1 | Tradução integral e mensagens internas | Pendente | Medição 100%, revisão humana |
| P2 | Catálogo de projetos SQLite | Pendente | Miniaturas, pesquisa e backups |
| P2 | Remoção de fundo e restauração | Parcial no motor original | Comparações e modo opcional IA |
| P2 | Agente IA: Groq, Ollama e MCP | Estrutura MCP existente | Planejamento, validação, autorização e execução |
| P2 | Pipeline visual por nós | Pendente | JSON versionado, validação, salvar/abrir |
| P3 | Game Assets: sprites, tiles, atlas | Pendente | Exportações para Godot e Unity |
| P3 | Plugins e API externa | Parcial no motor original | Contrato público, segurança, testes |

## Ordem de execução

1. **Fundação:** obter ZIP Windows funcional, tradução incorporada e ícones WMK; validar PSD e salvamento.
2. **Fotografia:** UI Antes/Depois, ajustes não destrutivos, filtros favoritos e presets.
3. **Automação:** receitas JSON versionadas e executor seguro usando comandos existentes.
4. **IA:** linguagem natural vira plano validado, prévia e aprovação antes de alterar documentos.
5. **Criatividade:** biblioteca de projetos, texturas, sprites e atlas.

## Requisitos de arquitetura

- Preservar o motor Rust, IDs de comando, licenças MIT/Apache e créditos.
- Priorizar CPU/GPU de baixo consumo; limitar memória, registrar erros e oferecer modo seguro.
- Não sobrescrever arquivos sem confirmação; sempre permitir backup e recuperação.
- Nunca embutir chaves de IA no código, logs ou executáveis.
- Nenhum envio de fotografias à nuvem sem consentimento explícito.
- Separar recursos existentes, planejados e validados em todos os manuais.

Walney Moreira Klein — walneyk@hotmail.com
