# otomasi-kantor

Skrip Python kecil untuk pekerjaan administrasi yang berulang.

| Skrip | Fungsi |
|---|---|
| `rapikan_nama_file.py` | Standarkan nama file (mode simulasi dulu) |
| `gabung_pdf.py` | Gabung banyak PDF jadi satu |
| `csv_ke_excel.py` | Gabung CSV ke satu Excel multi-sheet |

## Instalasi
```bash
pip install -r requirements.txt
```

## Contoh
```bash
python skrip/rapikan_nama_file.py ./dokumen            # simulasi
python skrip/rapikan_nama_file.py ./dokumen --jalankan # eksekusi
python skrip/gabung_pdf.py ./scan gabungan.pdf
python skrip/csv_ke_excel.py ./data laporan.xlsx
```
Lisensi: MIT
