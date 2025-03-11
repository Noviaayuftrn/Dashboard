## Dasbor Analisis Penyewaan Sepeda  

Proyek ini menyediakan sebuah dasbor interaktif yang dibuat menggunakan Streamlit, bertujuan untuk menganalisis dataset penggunaan sepeda. Analisis dilakukan menggunakan berbagai metode visualisasi data untuk memahami pola penyewaan sepeda berdasarkan faktor waktu dan kondisi lingkungan.  

## **Penulis**  
**Nama:** Novia Ayu Fitriana  
**Email:** a524xam376@devacademy.id  
**Cohort ID:** A524XAM376  

---

### **Metode Analisis Data yang Digunakan**  

1. **Analisis Tren Harian**  
   - Menggunakan **line plot** untuk menunjukkan tren jumlah penyewa sepeda berdasarkan hari.  
   - Tujuan: Mengidentifikasi pola mingguan atau musiman dalam penyewaan sepeda.  

2. **Analisis Tren Per Jam**  
   - Menggunakan **line plot** untuk melihat bagaimana jumlah penyewa berubah sepanjang hari.  
   - Tujuan: Mengetahui jam-jam sibuk dalam penyewaan sepeda.  

3. **Analisis Berdasarkan Kondisi Alam**  
   - Menggunakan **scatter plot dengan regresi** untuk melihat hubungan antara variabel lingkungan seperti suhu, kelembapan, dan kondisi cuaca terhadap jumlah penyewa.  
   - Tujuan: Mengidentifikasi bagaimana faktor cuaca mempengaruhi keputusan pengguna dalam menyewa sepeda.  

4. **Visualisasi Data**  
   - Menggunakan **Seaborn** dan **Matplotlib** untuk membuat grafik yang lebih informatif dan interaktif.  
   - Menambahkan **grid dan penjelasan pada setiap visualisasi** untuk membantu interpretasi data.  

---

## **Struktur Proyek**  

Proyek ini terdiri dari beberapa file dan direktori berikut:  

📂 **dashboard.py** - Script Python untuk menjalankan dasbor interaktif menggunakan Streamlit.  
📂 **data/** - Direktori yang berisi data penggunaan sepeda harian dan per jam.  
📄 **day.csv** - Data penggunaan sepeda harian.  
📄 **hour.csv** - Data penggunaan sepeda per jam.  
📄 **notebook.ipynb** - Notebook Jupyter untuk analisis mendalam dan eksplorasi data.  
📄 **README.md** - File ini yang berisi penjelasan tentang proyek.  
📄 **requirements.txt** - Daftar pustaka Python yang diperlukan untuk menjalankan proyek.  

---
## Setup Environment - Anaconda
```
conda create --name main-ds python=3.9
conda activate main-ds
pip install -r requirements.txt
```
## Setup Environment - Shell/Terminal
```
mkdir proyek_analisis_data
cd proyek_analisis_data
pipenv install
pipenv shell
pip install -r requirements.txt
```

## Run steamlit app
```
streamlit run dashboard.py
```
