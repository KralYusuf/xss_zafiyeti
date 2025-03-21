import sqlite3
import os

# Mevcut veritabanını sil (eğer varsa)
if os.path.exists('comments.db'):
    os.remove('comments.db')
    print("Eski veritabanı silindi.")

# Yeni veritabanı oluştur
conn = sqlite3.connect('comments.db')
cursor = conn.cursor()

# Yorumlar tablosunu oluştur
cursor.execute('''
CREATE TABLE comments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    comment TEXT NOT NULL
)
''')

# Örnek yorumlar ekle
sample_comments = [
    ('Ali', 'Bu web sitesi harika!'),
    ('Ayşe', 'Yeni özellikler çok iyi olmuş.')
]

cursor.executemany('INSERT INTO comments (name, comment) VALUES (?, ?)', sample_comments)

# Değişiklikleri kaydet ve bağlantıyı kapat
conn.commit()
conn.close()

print("Veritabanı başarıyla kuruldu ve örnek yorumlar eklendi.")
print("Toplam {} yorum eklendi.".format(len(sample_comments)))
