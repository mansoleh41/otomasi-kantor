#!/usr/bin/env python3
"""Rapikan nama file dalam folder: huruf kecil, spasi -> underscore, tanpa karakter aneh.
Pakai: python rapikan_nama_file.py FOLDER [--jalankan]   (tanpa --jalankan = simulasi)"""
import argparse, re
from pathlib import Path

def bersihkan(nama: str) -> str:
    stem, dot, ext = nama.rpartition(".")
    if not dot:
        stem, ext = nama, ""
    stem = re.sub(r"[^\w\-]+", "_", stem.strip().lower()).strip("_")
    return f"{stem}.{ext.lower()}" if ext else stem

def main():
    p = argparse.ArgumentParser()
    p.add_argument("folder")
    p.add_argument("--jalankan", action="store_true", help="benar-benar mengganti nama")
    a = p.parse_args()
    for f in sorted(Path(a.folder).iterdir()):
        if not f.is_file():
            continue
        baru = f.with_name(bersihkan(f.name))
        if baru == f or baru.exists():
            continue
        print(f"{f.name}  ->  {baru.name}")
        if a.jalankan:
            f.rename(baru)

if __name__ == "__main__":
    main()
