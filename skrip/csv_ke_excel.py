#!/usr/bin/env python3
"""Gabungkan beberapa CSV menjadi satu file Excel (1 CSV = 1 sheet).
Pakai: python csv_ke_excel.py FOLDER hasil.xlsx"""
import sys
from pathlib import Path
import pandas as pd

def main():
    if len(sys.argv) != 3:
        sys.exit("Pakai: python csv_ke_excel.py FOLDER hasil.xlsx")
    with pd.ExcelWriter(sys.argv[2]) as xw:
        for f in sorted(Path(sys.argv[1]).glob("*.csv")):
            pd.read_csv(f).to_excel(xw, sheet_name=f.stem[:31], index=False)
            print("+", f.name)

if __name__ == "__main__":
    main()
