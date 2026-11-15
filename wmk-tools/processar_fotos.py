#!/usr/bin/env python3
"""WMK: conversao em lote segura usando o CLI PhotoCraft existente."""
import argparse
import json
import subprocess
import sys
from pathlib import Path
from datetime import datetime, timezone

EXTS = {".jpg", ".jpeg", ".png", ".webp", ".bmp", ".tif", ".tiff", ".psd", ".psb", ".pcraft"}

def planejar(entrada, saida, formato):
    origem, destino = Path(entrada).resolve(), Path(saida).resolve()
    if not origem.is_dir():
        raise ValueError("Pasta de origem inexistente")
    if origem == destino or origem in destino.parents or destino in origem.parents:
        raise ValueError("Pasta de origem e destino nao podem ser iguais ou conter uma a outra")
    usados, lista = set(), []
    for arquivo in sorted(origem.iterdir()):
        if not arquivo.is_file() or arquivo.suffix.lower() not in EXTS:
            continue
        saida_arquivo = destino / (arquivo.stem + "." + formato)
        key = str(saida_arquivo).casefold()
        if key in usados or saida_arquivo.exists():
            raise ValueError("Colisao ou arquivo de saida existente: " + str(saida_arquivo))
        usados.add(key)
        lista.append((arquivo, saida_arquivo))
    return lista

def main():
    p = argparse.ArgumentParser(description="WMK Photo Studio: conversao de imagens sem sobrescrever originais")
    p.add_argument("--entrada", required=True, type=Path)
    p.add_argument("--saida", required=True, type=Path)
    p.add_argument("--cli", required=True, type=Path)
    p.add_argument("--formato", choices=["png", "jpg", "webp", "tif"], default="webp")
    p.add_argument("--qualidade", type=int, default=85)
    p.add_argument("--executar", action="store_true", help="Sem este parametro, apenas simula")
    p.add_argument("--relatorio", type=Path)
    a = p.parse_args()
    try:
        if not 1 <= a.qualidade <= 100:
            raise ValueError("Qualidade deve ser de 1 a 100")
        plano = planejar(a.entrada, a.saida, a.formato)
        if a.executar and not a.cli.is_file():
            raise ValueError("CLI nao encontrado: " + str(a.cli))
    except (ValueError, OSError) as ex:
        print("ERRO:", ex, file=sys.stderr)
        return 2
    relatorio = {"data_utc": datetime.now(timezone.utc).isoformat(), "executado": a.executar, "arquivos": []}
    if a.executar:
        a.saida.mkdir(parents=True, exist_ok=True)
    falhas = 0
    for origem, destino in plano:
        comando = [str(a.cli.resolve()), "convert", str(origem), str(destino), "--format", a.formato]
        if a.formato in ("jpg", "webp"):
            comando += ["--quality", str(a.qualidade)]
        registro = {"origem": str(origem), "destino": str(destino), "status": "simulacao"}
        print(origem.name, "=>", destino.name)
        if a.executar:
            try:
                proc = subprocess.run(comando, capture_output=True, text=True, timeout=600, check=False)
                registro["status"] = "ok" if proc.returncode == 0 and destino.is_file() else "erro"
                registro["codigo"] = proc.returncode
                registro["erro"] = proc.stderr[-2000:]
            except (OSError, subprocess.TimeoutExpired) as ex:
                registro["status"] = "erro"
                registro["erro"] = str(ex)
            if registro["status"] != "ok":
                falhas += 1
        relatorio["arquivos"].append(registro)
    if a.relatorio:
        a.relatorio.parent.mkdir(parents=True, exist_ok=True)
        a.relatorio.write_text(json.dumps(relatorio, ensure_ascii=False, indent=2), encoding="utf-8")
    print("Total:", len(plano), "| Falhas:", falhas, "| Modo:", "executar" if a.executar else "simular")
    return 1 if falhas else 0

if __name__ == "__main__":
    sys.exit(main())
