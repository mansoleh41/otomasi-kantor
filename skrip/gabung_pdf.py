#!/usr/bin/env python3
"""Gabungkan banyak PDF jadi satu (urut nama). Pakai: python gabung_pdf.py FOLDER hasil.pdf"""
import sys
from pathlib import Path
from pypdf import PdfWriter

def main():
    if len(sys.argv) != 3:
        sys.exit("Pakai: python gabung_pdf.py FOLDER hasil.pdf")
    w = PdfWriter()
    berkas = sorted(Path(sys.argv[1]).glob("*.pdf"))
    if not berkas:
        sys.exit("Tidak ada PDF di folder.")
    for f in berkas:
        w.append(str(f))
        print("+", f.name)
    with open(sys.argv[2], "wb") as out:
        w.write(out)
    print("Selesai ->", sys.argv[2])

if __name__ == "__main__":
    main()
