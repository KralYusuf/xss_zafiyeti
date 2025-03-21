from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import os
import bleach  # HTML içeriğini temizlemek için kullanılır
import subprocess

app = Flask(__name__)

# Veritabanı dosyası oluşturma
def init_db():
    conn = sqlite3.connect('comments.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS comments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            comment TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Flask 2.0+ sürümlerinde before_first_request kullanımdan kaldırıldı
# Bu işlevi ana kod bloğunda çağıracağız

# Ana sayfa - yorumları görüntüleme ve form
@app.route('/')
def index():
    conn = sqlite3.connect('comments.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM comments')
    comments = cursor.fetchall()
    conn.close()
    return render_template('index.html', comments=comments, app_version="fixed")

# Yorum ekleme işlemi
@app.route('/add_comment', methods=['POST'])
def add_comment():
    # Kullanıcı girdilerini alıyoruz
    name = request.form['name']
    comment = request.form['comment']
    
    # XSS Koruması: Kullanıcı girdisini temizliyoruz
    # bleach kütüphanesi HTML kodlarını temizliyor
    clean_name = bleach.clean(name)
    clean_comment = bleach.clean(comment)
    
    conn = sqlite3.connect('comments.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO comments (name, comment) VALUES (?, ?)', 
                  (clean_name, clean_comment))
    conn.commit()
    conn.close()
    
    return redirect(url_for('index'))

# Tüm yorumları temizleme (test için)
@app.route('/clear_comments', methods=['POST'])
def clear_comments():
    conn = sqlite3.connect('comments.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM comments')
    conn.commit()
    conn.close()
    return redirect(url_for('index'))

# Güvenlik açığı olan versiyona geçiş
@app.route('/switch_to_vulnerable')
def switch_to_vulnerable():
    import subprocess
    # Güvenlik açığı olan versiyonu başlat
    subprocess.Popen(['python', 'vulnerable_xss_app.py'])
    # Replit ortamında 5000 portuna yönlendir
    return redirect('https://5000-{}')  # Otomatik olarak Replit için oluşturulacak URL

if __name__ == '__main__':
    if not os.path.exists('comments.db'):
        init_db()
    app.run(host='0.0.0.0', port=5001, debug=True)
