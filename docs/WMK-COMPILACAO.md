# Compilação e identidade visual WMK

## Windows portátil

Execute **Actions > WMK Windows Portable > Run workflow**. O build usa `windows-2022`, Rust MSVC e `cargo build --locked --release`. Após concluir com sucesso, o ZIP fica em **Artifacts** na execução.

O workflow baixa o catálogo `craft-i18n` antes de compilar e exige `pt-br/photocraft.tsv`. Traduções são incorporadas no build, mas definir português como padrão do usuário ainda é uma tarefa separada.

## Logo e ícones

O arquivo `assets/wmk-brand/wmk-photo-studio.svg` é uma **versão vetorial simplificada** que acompanha a identidade azul/ciano aprovada. Durante o build Windows, o workflow cria PNGs para a janela e ICO para o executável; esses arquivos são gerados temporariamente no runner. O material visual é uma adaptação para distribuição técnica, não uma cópia pixel a pixel da arte apresentada no chat.

O núcleo ainda mantém caminhos históricos chamados `photocraft`. A renomeação interna deve ser feita com testes em uma mudança futura para evitar quebrar imports e empacotamento.

## Sobre erros de compilação

- O workflow atual depende de bibliotecas Git externas e pode falhar se revisões deixarem de existir ou necessitarem autenticação.
- A geração de ícones requer Node.js/npm e Sharp, instalados no runner.
- Compilação Windows de Rust pode consumir muito tempo e armazenamento. Ajustar cache, timeouts e dependências caso falhe.
- Artefatos de teste são **não assinados**; não são instaladores certificados.

## Próximos testes

Verificar inicialização, nome e ícones em Explorer/barra de tarefas, abertura de JPG/PNG, operações com camadas, salvamento `.pcraft`, abertura e reabertura PSD, idioma e CLI.

**Fork:** Walney Moreira Klein — walneyk@hotmail.com. Direitos e créditos originais mantidos.
