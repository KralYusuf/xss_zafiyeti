from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import os
import bleach  # Güvenli moddayken kullanılacak

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
    
    # Modu belirle
    app_version = "fixed" if secure_mode else "vulnerable"
    return render_template('index.html', comments=comments, app_version=app_version)

# Yorum ekleme işlemi
@app.route('/add_comment', methods=['POST'])
def add_comment():
    name = request.form['name']
    comment = request.form['comment']
    
    if secure_mode:
        # Güvenli mod: XSS koruması aktif (Bleach kütüphanesi ile)
        name = bleach.clean(name)
        comment = bleach.clean(comment)
    else:
        # Açıklı mod: XSS Güvenlik Açığı - Kullanıcı girdisi doğrudan veritabanına kaydediliyor
        # ve filtreleme olmadan görüntüleniyor
        pass
    
    conn = sqlite3.connect('comments.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO comments (name, comment) VALUES (?, ?)', (name, comment))
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

# Düzeltilmiş versiyona geçiş
# Mod değiştirici değişken
secure_mode = False

@app.route('/switch_mode')
def switch_mode():
    global secure_mode
    secure_mode = not secure_mode
    return redirect(url_for('index'))

if __name__ == '__main__':
    if not os.path.exists('comments.db'):
        init_db()
    app.run(host='0.0.0.0', port=5000, debug=True)
