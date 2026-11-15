# Identidade WMK Photo Studio — implantação

## Implementado no fork (versão de código, pendente de build)

- Executável Windows com os metadados WMK em `apps/photocraft/build.rs`.
- Ícones da janela, do executável e da barra superior gerados no runner Windows a partir de `assets/wmk-brand/wmk-photo-studio.svg`.
- Título da janela e título do documento editado alterados para **WMK Photo Studio**.
- Mensagens de carregamento e título das duas versões Web em português e com marca WMK.
- Diálogo **Sobre WMK Photo Studio** com créditos WMK e menção explícita à origem PhotoCraft / ArtCraft.
- Menu Ajuda apontando para repositório, issues e downloads do fork; mantidos links separados para a comunidade e o ArtCraft original.
- Seleção do tipo nativo no diálogo Abrir/Salvar rotulada `WMK Photo Studio (.pcraft)`, sem alterar o formato nativo.
- Testes de títulos atualizados para a nova marca.
- Verificação automática de atualizações do upstream desativada até existir um mecanismo seguro de atualizações exclusivo do fork.

## Mantidos intencionalmente (compatibilidade)

- Nomes de crates `photocraft-*` e módulos Rust;
- IDs e comandos usados por CLI, MCP e automações;
- Extensão `.pcraft`, diretórios de estado legados e configurações persistidas;
- Dependências do repositório original, atribuições e licenças MIT/Apache;
- Identificadores de ícones e aplicativos Linux, ainda vinculados aos instaladores e arquivos `.desktop` originais;
- Arquivos `.icns` e recursos dos instaladores macOS/Linux até existir build específico e testes dessas plataformas.

Alterar estes itens globalmente agora pode quebrar os projetos existentes e a compatibilidade dos documentos.

## Atenção à arte

O SVG atualmente versionado no GitHub é uma **versão vetorial simplificada** baseada na logo gerada e aprovada na conversa. Ainda não é a mesma imagem original pixel a pixel. A geração de PNG e ICO ocorre no workflow Windows. Para aplicar a arte exata em Windows, Linux e macOS serão necessários recursos raster/vetoriais definitivos e testes nas plataformas.

## Critérios de aceitação

1. Action Windows x64 verde (incluindo `cargo build --locked --release`).
2. ZIP baixável em Releases, com `WMK-Photo-Studio.exe`.
3. Janela e barra de tarefas exibem marca WMK.
4. Abrir imagem PNG/JPG, salvar `.pcraft`, fechar e reabrir.
5. Diálogo Sobre e menus Ajuda com links WMK.
6. Ausência de tentativa de instalar uma atualização do upstream sobre a versão WMK.
7. Verificação de compatibilidade e créditos originais.

**Importante:** documentação de implementação não significa que esses testes já foram executados.

Walney Moreira Klein — walneyk@hotmail.com
