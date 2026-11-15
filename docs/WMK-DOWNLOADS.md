# WMK Photo Studio — Downloads públicos

## Para usuários Windows 10/11 (64 bits)

1. Acesse https://github.com/WalneyNF/WMK-Photo-Studio/releases
2. Abra a versão **WMK Photo Studio — Prévia Windows** mais recente.
3. Em **Assets**, baixe **WMK-Photo-Studio-Windows-x64.zip**.
4. Descompacte o arquivo numa pasta local.
5. Execute **WMK-Photo-Studio.exe**.

A versão é **experimental**, o executável não é assinado digitalmente e alguns recursos podem falhar. Use cópias de imagens importantes. Não desative proteções do Windows para executar o arquivo.

## Para os responsáveis pelo projeto

A compilação automática usa o workflow `.github/workflows/wmk-windows.yml`. Após testes básicos e `cargo build --release`, o fluxo cria um GitHub Release pré-lançamento público e anexa o ZIP.

- A publicação só ocorre quando as etapas anteriores terminam com sucesso.
- O release usa tag por número da execução + SHA para evitar sobrescritas.
- Caso não haja release, inspecione a execução no GitHub Actions.
- O repositório precisa permitir **Actions → Workflow permissions → Read and write permissions** para o GITHUB_TOKEN publicar um release.
- O workflow possui `permissions: contents: write`, mas regras da organização ou do repositório podem restringir essa permissão.
- Não há assinatura Authenticode; o Windows pode exibir alertas de reputação.
- O workflow não realiza automaticamente uma instalação completa e não garante compatibilidade em todos os computadores.

## Licenciamento e créditos

Código base PhotoCraft (MIT OR Apache-2.0). Preservados `LICENSE-MIT`, `LICENSE-APACHE`, `NOTICE` e `ATTRIBUTION.md`.

WMK Photo Studio: Walney Moreira Klein — walneyk@hotmail.com.
