# WMK Photo Studio — Conversão de fotos em lote

Esta primeira ferramenta WMK aproveita o comando convert do PhotoCraft CLI. Não precisa de bibliotecas Python extras e **simula por padrão**, preservando os originais.

## Requisitos

- Python 3.10+.
- WMK-Photo-Studio-CLI.exe (disponível quando o build GitHub Actions terminar com sucesso) ou photocraft-cli.exe em compilações locais.
- Duas pastas diferentes para entrada e saída.

## Simular no PowerShell

    py -3 wmk-tools/processar_fotos.py --entrada "D:\Fotos\Originais" --saida "D:\Fotos\WebP" --cli ".\WMK-Photo-Studio-CLI.exe" --formato webp --qualidade 85

## Executar de verdade, com relatório JSON

    py -3 wmk-tools/processar_fotos.py --entrada "D:\Fotos\Originais" --saida "D:\Fotos\WebP" --cli ".\WMK-Photo-Studio-CLI.exe" --formato webp --qualidade 85 --executar --relatorio "D:\Fotos\resultado.json"

## Segurança

- Impede pastas de saída iguais, contidas na entrada ou acima da entrada.
- Impede sobrescrever arquivos de saída existentes.
- Impede colisões entre nomes de arquivos com extensões diferentes.
- Não altera os arquivos de entrada.
- Processa apenas a pasta informada (sem recursão).
- Registra erros por imagem quando o relatório é solicitado.

Executar os testes:

    py -3 -m unittest discover -s wmk-tools -p "test_*.py" -v

Próximas etapas: receitas de filtros, pré-visualização, presets JSON e interface gráfica.
