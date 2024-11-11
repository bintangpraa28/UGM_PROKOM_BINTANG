from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, date

app = Flask(__name__)

# konfigurasi sqlite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///rmpasi.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# database anak
class Anak(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nama = db.Column(db.String(100), nullable=False)
    tanggal_lahir = db.Column(db.Date, nullable=False)
    umur = db.Column(db.Integer, nullable=False)  # umur bulan
    berat_badan = db.Column(db.Float, nullable=False)  # kg
    jenis_kelamin = db.Column(db.String(10), nullable=False)
    tanggal_input = db.Column(db.DateTime, default=db.func.now())

    def rekomendasi_mpasi(self):
        if self.umur < 6:
            return "ASI eksklusif, tidak diperlukan MPASI"
        if self.umur == 6:
            if 5.7 <= self.berat_badan <= 8.8:
                baby_data = Mpasi.query.filter_by(id=1).first()
                return f"MPASI lembut, seperti {baby_data.menu}. Nutrisi utama: {baby_data.nutrisi}. kalori: {baby_data.kalori} kalori. Frekuensi: {baby_data.freq}"
            elif self.berat_badan < 5.7:
                baby_data = Mpasi.query.filter_by(id=1).first()
                return f"MPASI lembut, seperti {baby_data.menu}. Nutrisi utama: {baby_data.nutrisi}. kalori: {baby_data.kalori} kalori. Frekuensi: {baby_data.freq}. Catatan: {baby_data.notes_kurang}"            
            else:
                baby_data = Mpasi.query.filter_by(id=1).first()
                return f"MPASI semi padat, seperti {baby_data.menu}. Nutrisi utama: {baby_data.nutrisi}. kalori: {baby_data.kalori} kalori. Frekuensi: {baby_data.freq}. Catatan: {baby_data.notes_lebih}"

        elif self.umur == 7:
            if 6.0 <= self.berat_badan <= 9.2:
                baby_data = Mpasi.query.filter_by(id=2).first()
                return f"MPASI lembut, seperti {baby_data.menu}. Nutrisi utama: {baby_data.nutrisi}. kalori: {baby_data.kalori} kalori. Frekuensi: {baby_data.freq}"
            elif self.berat_badan < 6:
                baby_data = Mpasi.query.filter_by(id=2).first()
                return f"MPASI lembut, seperti {baby_data.menu}. Nutrisi utama: {baby_data.nutrisi}. kalori: {baby_data.kalori} kalori. Frekuensi: {baby_data.freq}. Catatan: {baby_data.notes_kurang}"            
            else:
                baby_data = Mpasi.query.filter_by(id=2).first()
                return f"MPASI semi padat, seperti {baby_data.menu}. Nutrisi utama: {baby_data.nutrisi}. kalori: {baby_data.kalori} kalori. Frekuensi: {baby_data.freq}. Catatan: {baby_data.notes_lebih}"

        elif self.umur == 8:
            if 6.3 <= self.berat_badan <= 9.6:
                baby_data = Mpasi.query.filter_by(id=3).first()
                return f"MPASI lembut, seperti {baby_data.menu}. Nutrisi utama: {baby_data.nutrisi}. kalori: {baby_data.kalori} kalori. Frekuensi: {baby_data.freq}"
            elif self.berat_badan < 6.3:
                baby_data = Mpasi.query.filter_by(id=3).first()
                return f"MPASI lembut, seperti {baby_data.menu}. Nutrisi utama: {baby_data.nutrisi}. kalori: {baby_data.kalori} kalori. Frekuensi: {baby_data.freq}.\nCatatan: {baby_data.notes_kurang}"            
            else:
                baby_data = Mpasi.query.filter_by(id=3).first()
                return f"MPASI semi padat, seperti {baby_data.menu}. Nutrisi utama: {baby_data.nutrisi}. kalori: {baby_data.kalori} kalori. Frekuensi: {baby_data.freq}.\nCatatan: {baby_data.notes_lebih}"

        elif self.umur == 9:
            if 6.5 <= self.berat_badan <= 9.9:
                baby_data = Mpasi.query.filter_by(id=4).first()
                return f"MPASI lembut, seperti {baby_data.menu}. Nutrisi utama: {baby_data.nutrisi}. kalori: {baby_data.kalori} kalori. Frekuensi: {baby_data.freq}"
            elif self.berat_badan < 6.5:
                baby_data = Mpasi.query.filter_by(id=4).first()
                return f"MPASI lembut, seperti {baby_data.menu}. Nutrisi utama: {baby_data.nutrisi}. kalori: {baby_data.kalori} kalori. Frekuensi: {baby_data.freq}. Catatan: {baby_data.notes_kurang}"            
            else:
                baby_data = Mpasi.query.filter_by(id=4).first()
                return f"MPASI semi padat, seperti {baby_data.menu}. Nutrisi utama: {baby_data.nutrisi}. kalori: {baby_data.kalori} kalori. Frekuensi: {baby_data.freq}. Catatan: {baby_data.notes_lebih}"

        elif self.umur == 10:
            if 8.5 <= self.berat_badan <= 11:
                baby_data = Mpasi.query.filter_by(id=5).first()
                return f"MPASI lembut, seperti {baby_data.menu}. Nutrisi utama: {baby_data.nutrisi}. kalori: {baby_data.kalori} kalori. Frekuensi: {baby_data.freq}"
            elif self.berat_badan < 8.5:
                baby_data = Mpasi.query.filter_by(id=5).first()
                return f"MPASI lembut, seperti {baby_data.menu}. Nutrisi utama: {baby_data.nutrisi}. kalori: {baby_data.kalori} kalori. Frekuensi: {baby_data.freq}. Catatan: {baby_data.notes_kurang}"            
            else:
                baby_data = Mpasi.query.filter_by(id=5).first()
                return f"MPASI semi padat, seperti {baby_data.menu}. Nutrisi utama: {baby_data.nutrisi}. kalori: {baby_data.kalori} kalori. Frekuensi: {baby_data.freq}. Catatan: {baby_data.notes_lebih}"


        elif self.umur == 11:
            if 6.9 <= self.berat_badan <= 10.5:
                baby_data = Mpasi.query.filter_by(id=6).first()
                return f"MPASI lembut, seperti {baby_data.menu}. Nutrisi utama: {baby_data.nutrisi}. kalori: {baby_data.kalori} kalori. Frekuensi: {baby_data.freq}"
            elif self.berat_badan < 6.9:
                baby_data = Mpasi.query.filter_by(id=6).first()
                return f"MPASI lembut, seperti {baby_data.menu}. Nutrisi utama: {baby_data.nutrisi}. kalori: {baby_data.kalori} kalori. Frekuensi: {baby_data.freq}. Catatan: {baby_data.notes_kurang}"            
            else:
                baby_data = Mpasi.query.filter_by(id=6).first()
                return f"MPASI semi padat, seperti {baby_data.menu}. Nutrisi utama: {baby_data.nutrisi}. kalori: {baby_data.kalori} kalori. Frekuensi: {baby_data.freq}. Catatan: {baby_data.notes_lebih}"

        elif self.umur == 12:
            if 7.0 <= self.berat_badan <= 10.8:
                baby_data = Mpasi.query.filter_by(id=7).first()
                return f"MPASI lembut, seperti {baby_data.menu}. Nutrisi utama: {baby_data.nutrisi}. kalori: {baby_data.kalori} kalori. Frekuensi: {baby_data.freq}"
            elif self.berat_badan < 7.0:
                baby_data = Mpasi.query.filter_by(id=7).first()
                return f"MPASI lembut, seperti {baby_data.menu}. Nutrisi utama: {baby_data.nutrisi}. kalori: {baby_data.kalori} kalori. Frekuensi: {baby_data.freq}. Catatan: {baby_data.notes_kurang}"            
            else:
                baby_data = Mpasi.query.filter_by(id=7).first()
                return f"MPASI semi padat, seperti {baby_data.menu}. Nutrisi utama: {baby_data.nutrisi}. kalori: {baby_data.kalori} kalori. Frekuensi: {baby_data.freq}. Catatan: {baby_data.notes_lebih}"

        elif self.umur == 13:
            if 7.7 <= self.berat_badan <= 11:
                baby_data = Mpasi.query.filter_by(id=8).first()
                return f"MPASI lembut, seperti {baby_data.menu}. Nutrisi utama: {baby_data.nutrisi}. kalori: {baby_data.kalori} kalori. Frekuensi: {baby_data.freq}"
            elif self.berat_badan <7.7:
                baby_data = Mpasi.query.filter_by(id=8).first()
                return f"MPASI lembut, seperti {baby_data.menu}. Nutrisi utama: {baby_data.nutrisi}. kalori: {baby_data.kalori} kalori. Frekuensi: {baby_data.freq}. Catatan: {baby_data.notes_kurang}"            
            else:
                baby_data = Mpasi.query.filter_by(id=8).first()
                return f"MPASI semi padat, seperti {baby_data.menu}. Nutrisi utama: {baby_data.nutrisi}. kalori: {baby_data.kalori} kalori. Frekuensi: {baby_data.freq}. Catatan: {baby_data.notes_lebih}"

        elif self.umur == 14:
            if 7.4 <= self.berat_badan <= 12.6:
                baby_data = Mpasi.query.filter_by(id=9).first()
                return f"MPASI lembut, seperti {baby_data.menu}. Nutrisi utama: {baby_data.nutrisi}. kalori: {baby_data.kalori} kalori. Frekuensi: {baby_data.freq}"
            if self.berat_badan < 7.4:
                baby_data = Mpasi.query.filter_by(id=9).first()
                return f"MPASI lembut, seperti {baby_data.menu}. Nutrisi utama: {baby_data.nutrisi}. kalori: {baby_data.kalori} kalori. Frekuensi: {baby_data.freq}. Catatan: {baby_data.notes_kurang}"            
            else:
                baby_data = Mpasi.query.filter_by(id=9).first()
                return f"MPASI semi padat, seperti {baby_data.menu}. Nutrisi utama: {baby_data.nutrisi}. kalori: {baby_data.kalori} kalori. Frekuensi: {baby_data.freq}. Catatan: {baby_data.notes_lebih}"

        elif self.umur == 15:
            if 7.6 <= self.berat_badan <= 11.5:
                baby_data = Mpasi.query.filter_by(id=10).first()
                return f"MPASI lembut, seperti {baby_data.menu}. Nutrisi utama: {baby_data.nutrisi}. kalori: {baby_data.kalori} kalori. Frekuensi: {baby_data.freq}"
            elif self.berat_badan < 7.6:
                baby_data = Mpasi.query.filter_by(id=10).first()
                return f"MPASI lembut, seperti {baby_data.menu}. Nutrisi utama: {baby_data.nutrisi}. kalori: {baby_data.kalori} kalori. Frekuensi: {baby_data.freq}. Catatan: {baby_data.notes_kurang}"            
            else:
                baby_data = Mpasi.query.filter_by(id=10).first()
                return f"MPASI semi padat, seperti {baby_data.menu}. Nutrisi utama: {baby_data.nutrisi}. kalori: {baby_data.kalori} kalori. Frekuensi: {baby_data.freq}. Catatan: {baby_data.notes_lebih}"            

        elif self.umur == 16:
            if 7.7 <= self.berat_badan <= 11.1:
                baby_data = Mpasi.query.filter_by(id=11).first()
                return f"MPASI lembut, seperti {baby_data.menu}. Nutrisi utama: {baby_data.nutrisi}. kalori: {baby_data.kalori} kalori. Frekuensi: {baby_data.freq}"
            elif self.berat_badan < 7.7:
                baby_data = Mpasi.query.filter_by(id=11).first()
                return f"MPASI lembut, seperti {baby_data.menu}. Nutrisi utama: {baby_data.nutrisi}. kalori: {baby_data.kalori} kalori. Frekuensi: {baby_data.freq}. Catatan: {baby_data.notes_kurang}"            
            else:
                baby_data = Mpasi.query.filter_by(id=11).first()
                return f"MPASI semi padat, seperti {baby_data.menu}. Nutrisi utama: {baby_data.nutrisi}. kalori: {baby_data.kalori} kalori. Frekuensi: {baby_data.freq}. Catatan: {baby_data.notes_lebih}"            

        elif self.umur == 17:
            if 7.9 <= self.berat_badan <= 12.0:
                baby_data = Mpasi.query.filter_by(id=12).first()
                return f"MPASI lembut, seperti {baby_data.menu}. Nutrisi utama: {baby_data.nutrisi}. kalori: {baby_data.kalori} kalori. Frekuensi: {baby_data.freq}"
            elif self.berat_badan < 7.9:
                baby_data = Mpasi.query.filter_by(id=12).first()
                return f"MPASI lembut, seperti {baby_data.menu}. Nutrisi utama: {baby_data.nutrisi}. kalori: {baby_data.kalori} kalori. Frekuensi: {baby_data.freq}. Catatan: {baby_data.notes_kurang}"            
            else:
                baby_data = Mpasi.query.filter_by(id=12).first()
                return f"MPASI semi padat, seperti {baby_data.menu}. Nutrisi utama: {baby_data.nutrisi}. kalori: {baby_data.kalori} kalori. Frekuensi: {baby_data.freq}. Catatan: {baby_data.notes_lebih}"

        elif self.umur == 18:
            if 8.1 <= self.berat_badan <= 12.2:
                baby_data = Mpasi.query.filter_by(id=13).first()
                return f"MPASI lembut, seperti {baby_data.menu}. Nutrisi utama: {baby_data.nutrisi}. kalori: {baby_data.kalori} kalori. Frekuensi: {baby_data.freq}"
            elif self.berat_badan < 8.1:
                baby_data = Mpasi.query.filter_by(id=13).first()
                return f"MPASI lembut, seperti {baby_data.menu}. Nutrisi utama: {baby_data.nutrisi}. kalori: {baby_data.kalori} kalori. Frekuensi: {baby_data.freq}. Catatan: {baby_data.notes_kurang}"            
            else:
                baby_data = Mpasi.query.filter_by(id=13).first()
                return f"MPASI semi padat, seperti {baby_data.menu}. Nutrisi utama: {baby_data.nutrisi}. kalori: {baby_data.kalori} kalori. Frekuensi: {baby_data.freq}. Catatan: {baby_data.notes_lebih}"

        elif self.umur == 19:
            if 8.2 <= self.berat_badan <= 12.5:
                baby_data = Mpasi.query.filter_by(id=14).first()
                return f"MPASI lembut, seperti {baby_data.menu}. Nutrisi utama: {baby_data.nutrisi}. kalori: {baby_data.kalori} kalori. Frekuensi: {baby_data.freq}"
            elif self.berat_badan < 8.2:
                baby_data = Mpasi.query.filter_by(id=14).first()
                return f"MPASI lembut, seperti {baby_data.menu}. Nutrisi utama: {baby_data.nutrisi}. kalori: {baby_data.kalori} kalori. Frekuensi: {baby_data.freq}. Catatan: {baby_data.notes_kurang}"            
            else:
                baby_data = Mpasi.query.filter_by(id=14).first()
                return f"MPASI semi padat, seperti {baby_data.menu}. Nutrisi utama: {baby_data.nutrisi}. kalori: {baby_data.kalori} kalori. Frekuensi: {baby_data.freq}. Catatan: {baby_data.notes_lebih}"

        elif self.umur == 20:
            if 8.4 <= self.berat_badan <= 12.7:
                baby_data = Mpasi.query.filter_by(id=15).first()
                return f"MPASI lembut, seperti {baby_data.menu}. Nutrisi utama: {baby_data.nutrisi}. kalori: {baby_data.kalori} kalori. Frekuensi: {baby_data.freq}"
            elif self.berat_badan < 8.4:
                baby_data = Mpasi.query.filter_by(id=15).first()
                return f"MPASI lembut, seperti {baby_data.menu}. Nutrisi utama: {baby_data.nutrisi}. kalori: {baby_data.kalori} kalori. Frekuensi: {baby_data.freq}. Catatan: {baby_data.notes_kurang}"            
            else:
                baby_data = Mpasi.query.filter_by(id=15).first()
                return f"MPASI semi padat, seperti {baby_data.menu}. Nutrisi utama: {baby_data.nutrisi}. kalori: {baby_data.kalori} kalori. Frekuensi: {baby_data.freq}. Catatan: {baby_data.notes_lebih}"

        elif self.umur == 21:
            if 8.6 <= self.berat_badan <= 12.9:
                baby_data = Mpasi.query.filter_by(id=16).first()
                return f"MPASI lembut, seperti {baby_data.menu}. Nutrisi utama: {baby_data.nutrisi}. kalori: {baby_data.kalori} kalori. Frekuensi: {baby_data.freq}"
            elif self.berat_badan < 8.6:
                baby_data = Mpasi.query.filter_by(id=16).first()
                return f"MPASI lembut, seperti {baby_data.menu}. Nutrisi utama: {baby_data.nutrisi}. kalori: {baby_data.kalori} kalori. Frekuensi: {baby_data.freq}. Catatan: {baby_data.notes_kurang}"            
            else:
                baby_data = Mpasi.query.filter_by(id=16).first()
                return f"MPASI semi padat, seperti {baby_data.menu}. Nutrisi utama: {baby_data.nutrisi}. kalori: {baby_data.kalori} kalori. Frekuensi: {baby_data.freq}. Catatan: {baby_data.notes_lebih}"

        elif self.umur == 22:
            if 8.7 <= self.berat_badan <= 12.9:
                baby_data = Mpasi.query.filter_by(id=17).first()
                return f"MPASI lembut, seperti {baby_data.menu}. Nutrisi utama: {baby_data.nutrisi}. kalori: {baby_data.kalori} kalori. Frekuensi: {baby_data.freq}"
            elif self.berat_badan < 8.7:
                baby_data = Mpasi.query.filter_by(id=17).first()
                return f"MPASI lembut, seperti {baby_data.menu}. Nutrisi utama: {baby_data.nutrisi}. kalori: {baby_data.kalori} kalori. Frekuensi: {baby_data.freq}. Catatan: {baby_data.notes_kurang}"            
            else:
                baby_data = Mpasi.query.filter_by(id=17).first()
                return f"MPASI semi padat, seperti {baby_data.menu}. Nutrisi utama: {baby_data.nutrisi}. kalori: {baby_data.kalori} kalori. Frekuensi: {baby_data.freq}. Catatan: {baby_data.notes_lebih}"

        elif self.umur == 23:
            if 8.9 <= self.berat_badan <= 13.2:
                baby_data = Mpasi.query.filter_by(id=18).first()
                return f"MPASI lembut, seperti {baby_data.menu}. Nutrisi utama: {baby_data.nutrisi}. kalori: {baby_data.kalori} kalori. Frekuensi: {baby_data.freq}"
            if self.berat_badan < 8.9:
                baby_data = Mpasi.query.filter_by(id=18).first()
                return f"MPASI lembut, seperti {baby_data.menu}. Nutrisi utama: {baby_data.nutrisi}. kalori: {baby_data.kalori} kalori. Frekuensi: {baby_data.freq}. Catatan: {baby_data.notes_kurang}"            
            else:
                baby_data = Mpasi.query.filter_by(id=18).first()
                return f"MPASI semi padat, seperti {baby_data.menu}. Nutrisi utama: {baby_data.nutrisi}. kalori: {baby_data.kalori} kalori. Frekuensi: {baby_data.freq}. Catatan: {baby_data.notes_lebih}"
        elif 24 <= self.umur < 72:
            return "Umur ASI berakhir, anak disarankan berhenti minum ASI dan beralih ke makanan keluarga"
        else:
            return "Umur sudah enam tahun keatas, anak sudah bisa makan makanan dewasa"

#database mpasi
class Mpasi(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    umur = db.Column(db.Integer, nullable=False)
    berat_min = db.Column(db.Float, nullable=False)
    berat_max = db.Column(db.Float, nullable=False)
    menu = db.Column(db.Text, nullable=False)
    nutrisi = db.Column(db.Text, nullable=False)
    kalori = db.Column(db.Integer, nullable=False)
    freq = db.Column(db.String(50), nullable=False)
    notes_lebih = db.Column(db.Text, nullable=True)
    notes_kurang = db.Column(db.Text, nullable=True)
    
#input database mpasi
data = [
    Mpasi(
        umur=6, 
        berat_min=5.7, 
        berat_max=8.8,
        menu='Puree dari buah (pisang, alpukat, apel), sayuran (wortel, labu, kentang), dan bubur beras yang dihaluskan',
        nutrisi='Karbohidrat, vitamin A dan C, lemak sehat dari alpukat', 
        kalori=200, 
        freq='2-3 kali makan per hari',
        notes_kurang='Jika berat badan bayi kurang: Mulai dengan 2-3 kali makan per hari dengan 2-3 sendok makan per porsi dengan tambahan 1-2 kali snack sehat. Kalori tinggi, lemak sehat, zat besi, dan vitamin A',
        notes_lebih='Jika Berat Badan Bayi Lebih: 2-3 kali makan per hari, 2-3 sendok makan per porsi. Serat, vitamin, dan mineral tanpa tambahan lemak atau kalori yang tinggi.'
    ),
    Mpasi(
        umur=7, 
        berat_min=6.0, 
        berat_max=9.2,
        menu='Puree lebih bervariasi (kentang dengan daging atau ikan), bubur kacang hijau, bubur nasi dicampur sayuran',
        nutrisi='Protein hewani, serat, zat besi', 
        kalori=200, 
        freq='3 kali makan utama per hari',
        notes_kurang='Jika berat badan bayi kurang: 3 kali makan utama per hari dan 2 snack dengan 3-4 sendok makan per porsi. Tinggi kalori, lemak sehat, protein hewani, zat besi, dan vitamin A untuk mendukung pertambahan berat badan.',
        notes_lebih='Jika Berat Badan Bayi Lebih: 3 kali makan per hari dengan sesuai kebutuhan bayi, tidak perlu terlalu banyak. Serat, protein tanpa lemak, vitamin, dan mineral untuk menjaga kesehatan dan perkembangan bayi tanpa kelebihan kalori.'
    ),
    Mpasi(
        umur=8,
        berat_min=6.3,
        berat_max=9.6,
        menu='Bubur lebih kental, mulai mengenalkan kuning telur, tahu, dan tempe yang dilumatkan, buah potong lembut (pisang, pepaya)',
        nutrisi='Protein, vitamin D, kalsium, serat',
        kalori=250,
        freq='3 kali makan per hari',
        notes_kurang='Jika Berat Badan Bayi Kurang: 3 kali makan utama dan 2 snack bergizi. Dengan 4 sendok makan per porsi. Tinggi kalori, protein, zat besi, dan lemak sehat untuk meningkatkan berat badan.',
        notes_lebih='Jika Berat Badan Bayi Lebih: 3 kali makan utama per hari dengan 1 snack ringan. Dengan 4 sendok makan per porsi. Serat, protein rendah lemak, vitamin, dan mineral untuk mendukung pertumbuhan tanpa kelebihan kalori.'
    ),
    Mpasi(
        umur=9,
        berat_min=6.5,
        berat_max=9.9,
        menu='Nasi lembek atau bubur kental dengan potongan kecil sayur, daging cincang, atau ikan',
        nutrisi='Zat besi, protein, vitamin B kompleks', 
        kalori=300,
        freq='3 kali makan per hari',
        notes_kurang='Jika Berat Badan Bayi Kurang: 3 kali makan per hari dan 1-2 snack dengan porsi 5 sendok makan per porsi. Protein, kalori, zat besi, lemak sehat.',
        notes_lebih='Jika Berat Badan Bayi Lebih: 3 kali makan per hari dengan 3-5 sendok makan per porsi. Vitamin, serat, dan mineral tanpa tambahan kalori berlebih.'
    ),
    Mpasi(
        umur=10, 
        berat_min=8.5,
        berat_max=11.0,
        menu='Bubur kental atau nasi lembek dengan lebih banyak variasi, telur utuh (dengan putihnya), buah potong.',
        nutrisi='Protein tambahan, kolin (penting untuk perkembangan otak).',
        kalori=300,
        freq='3 kali makan per hari',
        notes_kurang='Jika Berat Badan Bayi Kurang: 3 kali makan dengan 5 sendok makan per porsi dan 1-2 snack. Kalori tinggi, lemak sehat, protein.',
        notes_lebih='Jika Berat Badan Bayi Lebih: 3 kali makan dengan 4-5 sendok makan per porsi. Serat tinggi dan vitamin tanpa tambahan kalori berlebih.'
    ),
    Mpasi(
        umur=11, 
        berat_min=6.9,
        berat_max=10.5,
        menu='Nasi lembek atau nasi tim dengan lauk lengkap (Ayam, Tahu, sayuran), produk susu seperti yogurt.',
        nutrisi='Kalsium, Protein, Vitamin D.',
        kalori=350,
        freq='3 kali makan per hari',
        notes_kurang='Jika Berat Badan Bayi Kurang: 3 kali makan per hari dengan 5-6 sendok makan per porsi, serta 1-2 snack sehat. Protein, lemak sehat, kalori tinggi.',
        notes_lebih='Jika Berat Badan Bayi Lebih: Tetap 3 kali makan per hari dengan 5-6 sendok makan per porsi. Serat, vitamin, mineral tanpa tambahan kalori berlebih.'
    ),
    Mpasi(
        umur=12,
        berat_min=7.7,
        berat_max=10.8,
        menu='Nasi lembek atau nasi tim, lauk variatif (ikan, daging, tempe, sayur cincang), produk susu lainnya (keju).',
        nutrisi='Kalsium, Protein, Zat Besi, Lemak sehat.',
        kalori=400,
        freq='3 kali makan per hari',
        notes_kurang='Jika Berat Badan Bayi Kurang: 3 kali makan dengan 6-7 sendok makan per porsi dan 1-2 snack sehat. Kalori tinggi, protein, lemak sehat.',
        notes_lebih='Jika Berat Badan Bayi Lebih: 3 kali makan per hari dengan 6 sendok makan per porsi. Serat dan vitamin tanpa tambahan kalori tinggi.'
    ),
    Mpasi(
        umur=13, berat_min=8.3, berat_max=11.0,
        menu='Nasi lembek atau nasi biasa dengan lauk (Ayam, ikan, Tahu, Tempe), sayuran yang dimasak (Wortel, bayam), dan buah potong (pepaya, pisang).',
        nutrisi='Protein (ayam, tahu), vitamin A dan C (sayuran), karbohidrat, serat.', 
        kalori=450,
        freq='3 kali makan per hari + 1-2 camilan',
        notes_kurang='Jika Berat Badan Bayi Kurang: 3 kali makan dengan 6-7 sendok makan per porsi, 1-2 kali snack sehat.',
        notes_lebih='Sama, yaitu 3 kali makan per hari dengan 6-7 sendok makan per porsi. Serat, vitamin, tanpa tambahan kalori berlebih.'
    ),
    Mpasi(
        umur=14,
        berat_min=8.1,
        berat_max=12.6,
        menu='Makanan keluarga yang diadaptasi (nasi lembut, sayuran matang, potongan kecil daging atau ayam, telur rebus, buah potong).',
        nutrisi='Protein (daging, telur), serat (sayuran), karbohidrat, lemak sehat.',
        kalori=450,
        freq='3 kali makan per hari + 1-2 camilan',
        notes_kurang='Jika Berat Badan Bayi Kurang: 3 kali makan per hari dengan 7-8 sendok makan per porsi dan 1-2 kali snack. Protein, kalori, lemak sehat.',
        notes_lebih='Tetap 3 kali makan per hari dengan 7 sendok makan per porsi. Vitamin, serat, mineral tanpa tambahan kalori berlebih.'
    ),
    Mpasi(
        umur=15,
        berat_min=8.3,
        berat_max=11.5,
        menu='Nasi biasa dengan lauk keluarga (ikan, daging cincang, atau ayam), telur, potongan buah, sayuran yang bisa dikunyah (brokoli, kentang).',
        nutrisi='Protein, zat besi, vitamin D, kalsium (dari produk susu).',
        kalori=500,
        freq='3 kali makan utama + 1-2 camilan',
        notes_kurang='Jika Berat Badan Bayi Kurang: 3 kali makan per hari dengan 7-8 sendok makan per porsi, serta 1-2 kali snack sehat. Protein, kalori, lemak sehat.',
        notes_lebih='Tetap 3 kali makan per hari dengan 7-8 sendok makan per porsi. Vitamin, serat, tanpa kalori berlebih.'
    ),
    Mpasi(
        umur=16, berat_min=8.4, berat_max=13.1,
        menu='Makanan keluarga (nasi atau roti gandum, lauk seperti tempe, ikan, daging sapi), sayuran cincang, dan  cemilan buah atau yogurt.',
        nutrisi='Protein,serat,zat besi,vitamin B kompleks,kalsium.',
        kalori=500,
        freq='3 kali makan utama + 2 cemilan',
        notes_kurang='jika Berat Badan Bayi Kurang: 3 kali makan per hari dengan 8-9 sendok makan per porsi dan 1-2 kali snack sehat.protein,kalori tinggi,lemak sehat.',
        notes_lebih='Tetap 3 kali makan per hari dengan 8 sendok makan per porsi.vitamin,serat,mineral tanpa tambahan kalori.'),
    Mpasi(
        umur=17,
        berat_min=8.6,
        berat_max=12.0, 
        menu='Makanan keluarga dengan porsi lebih lengkap,nasi biasa,potongan ikan atau ayam,tahu atau tempe,sayuran(brokoli,wortel),buah potong(apel,pisang,jeruk).',
        nutrisi='Protein,serat (sayuran),zat besi,vitamin C (buah),kalsium.',
        kalori=500, 
        freq='3 kali makan utama + 2 cemilan',
        notes_kurang='jika Berat Badan Bayi Kurang: 3 kali makan per hari dengan 8-9 sendok makan per porsi dan 1-2 kali snack sehat.protein,kalori tinggi,lemak sehat.',
        notes_lebih='Tetap 3 kali makan per hari dengan 8 sendok makan per porsi.vitamin,serat,mineral tanpa tambahan kalori.'),
    Mpasi(
        umur=18,
        berat_min=8.1,
        berat_max=12.2,
        menu='Nasi dengan lauk keluarga (ikan, ayam, tahu, tempe), sayuran (bayam (bayam, brokoli), buah potong (apel, jeruk, pepaya), produk susu.',
        nutrisi='Protein, zat besi, kalsium, serat, vitamin C.',
        kalori=550,
        freq='3 kali makan utama + 2 camilan per hari',
        notes_kurang='Jika Berat Badan Bayi Kurang: 3 kali makan dengan 8-9 sendok makan per porsi, serta 1-2 snack sehat. Kalori tinggi, lemak sehat, protein.',
        notes_lebih='Jika Berat Badan Bayi Lebih: 3 kali makan dengan 8-9 sendok makan per porsi. Serat, vitamin, tanpa tambahan kalori berlebih.'),
    Mpasi(
        umur=19,
        berat_min=8.2,
        berat_max=12.5,
        menu='Nasi biasa dengan variasi lauk (ikan, daging cincang, tempe), sayuran matang, buah segar, pasta atau roti gandum.',
        nutrisi='Protein, zat besi, kalsium, serat, lemak sehat, karbohidrat.',
        kalori=550,
        freq='3 kali makan utama + 2 camilan per hari', 
        notes_kurang='Jika Berat Badan Bayi Kurang: 3 kali makan dengan 9-10 sendok makan per porsi. Serat, vitamin, mineral.',
        notes_lebih='Jika Berat Badan Bayi Lebih: 3 kali makan dengan 8-9 sendok makan per porsi. Serat, vitamin, mineral.'),
    Mpasi(
        umur=20,
        berat_min=8.4,
        berat_max=12.7,
        menu='Nasi biasa dengan lauk (ikan, daging, atau tempe), kacang-kacangan lunak, sayuran bertekstur yang bisa dikunyah (bayam buncis), produk susu seperti yogurt atau keju.',
        nutrisi='Kalsium, protein, vitamin A (sayur berdaun hijau), karbohidrat',
        kalori=550,
        freq='3 kali makan utama + 2 camilan per hari',
        notes_kurang='Jika Berat Badan Bayi Kurang: 3 kali makan dengan 10-12 sendok makan per porsi, serta 1-2 snack sehat. Kalori tinggi, lemak sehat, protein.',
        notes_lebih='Jika Berat Badan Bayi Lebih: 3 kali makan dengan 10 sendok makan per porsi. Serat, vitamin, mineral tanpa tambahan kalori tinggi.'),
    Mpasi(
        umur=21,
        berat_min=8.6,
        berat_max=12.9,
        menu='Variasi menu keluarga (nasi, roti gandum, pasta lembut), lauk seperti daging sapi atau ayam cincang, telur, sayuran cincang, buah potong, dan camilan sehat (buah, yogurt).',
        nutrisi='Vitamin B kompleks, kalsium, protein, karbohidrat.',
        kalori=600, 
        freq='3 kali makan utama + 2 camilan per hari',
        notes_kurang='Jika Berat Badan Bayi Kurang: 3 kali makan dengan 10-12 sendok makan per porsi, serta 1-2 snack sehat. Kalori tinggi, lemak sehat, protein.',
        notes_lebih='Jika Berat Badan Bayi Lebih: 3 kali makan dengan 10 sendok makan per porsi. Serat, vitamin, tanpa tambahan kalori berlebih.'),
    Mpasi(
        umur=22,
        berat_min=8.7,
        berat_max=12.9,
        menu='Nasi dan lauk keluarga (ikan, tempe, daging sapi), sup sayuran, potongan kecil sayur dan buah segar, pasta atau mie sesekali sebagai variasi, produk susu.',
        nutrisi='Protein, zat besi, lemak sehat, karbohidrat.',
        kalori=650,
        freq='3 kali makan utama + 2 camilan per hari',
        notes_kurang='Jika Berat Badan Bayi Kurang: 3 kali makan dengan 10-12 sendok makan per porsi, serta 1-2 snack sehat. Kalori tinggi, lemak sehat, protein.',
        notes_lebih='Jika Berat Badan Bayi Lebih: 3 kali makan dengan 10-11 sendok makan per porsi. Serat, vitamin, mineral tanpa tambahan kalori tinggi.'),
    Mpasi(
        umur=23,
        berat_min=8.9,
        berat_max=13.2,
        menu='Menu keluarga penuh dengan prosi sesuai (nasi, lauk daging, ikan, telur, sayur matang, buah potong), dan tambahan susu atau yogurt.', 
        nutrisi='Seimbang (karbohidrat, protein, lemak sehat, vitamin, mineral).', 
        kalori=700,
        freq='3 kali makan utama + 2 camilan per hari',
        notes_kurang='Jika Berat Badan Bayi Kurang: 3 kali makan dengan 10-12 sendok makan per porsi, serta 1-2 snack sehat. Kalori tinggi, lemak sehat, protein.',
        notes_lebih='Jika Berat Badan Bayi Lebih: 3 kali makan dengan 10-11 sendok makan per porsi. Serat, vitamin, mineral tanpa tambahan kalori berlebih.')
]

with app.app_context():
    db.session.add_all(data)
    db.session.commit()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        nama = request.form['nama']
        tanggal_lahir = request.form['tanggal_lahir']
        berat_badan = float(request.form['berat_badan'])
        jenis_kelamin = request.form['jenis_kelamin']

        # ubah tanggal lahir mjd umur
        tanggal_lahir = datetime.strptime(tanggal_lahir, '%Y-%m-%d').date()

        # hitung umur anak dalam bulan
        today = date.today()
        umur = (today.year - tanggal_lahir.year) * 12 + today.month - tanggal_lahir.month

        # simpan data anak ke db
        anak = Anak(nama=nama, tanggal_lahir=tanggal_lahir, umur=umur, berat_badan=berat_badan, jenis_kelamin=jenis_kelamin)
        db.session.add(anak)
        db.session.commit()

        # Get MPASI recommendation
        rekomendasi = anak.rekomendasi_mpasi()
        return render_template('result.html', rekomendasi=rekomendasi, anak=anak)
    return render_template('index.html')

@app.route('/daftar')
def daftar_anak():
    anak_list = Anak.query.all()
    return render_template('daftar_anak.html', anak_list=anak_list)

@app.route('/rekomendasi/<int:anak_id>')
def rekomendasi(anak_id):
    anak = Anak.query.get_or_404(anak_id)
    rekomendasi = anak.rekomendasi_mpasi()
    return render_template('result.html', rekomendasi=rekomendasi, anak=anak)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
