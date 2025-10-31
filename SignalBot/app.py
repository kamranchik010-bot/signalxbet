import os
from flask import Flask, render_template, send_from_directory, redirect, url_for

# Flask ilovasini yaratish
app = Flask(__name__)

# Flask-ga index.html qayerda joylashganini aytish
# Flask odatda 'templates' papkasini ishlatadi, lekin biz uni loyihaning asosiy papkasida (root) saqlaymiz.
# Shuning uchun biz 'send_from_directory' dan foydalanamiz.

@app.route('/')
def home():
    """
    Asosiy sahifa (/) so'roviga javob beradi.
    index.html faylini yuklab, brauzerga yuboradi.
    """
    try:
        # index.html faylini loyihaning asosiy katalogidan (root_path) topib yuborish
        return send_from_directory(app.root_path, 'index.html')
    except FileNotFoundError:
        # Agar index.html topilmasa, oddiy xabar qaytarish
        return "Xato: 'index.html' fayli topilmadi. Uni asosiy papkaga joylashtiring."

@app.route('/<path:filename>')
def serve_static(filename):
    """
    Boshqa statik fayllar (CSS, JS, rasm kabi) so'rovlariga javob beradi.
    Loyihangizda boshqa fayllar bo'lsa, ularni topishga yordam beradi.
    """
    # Statik fayllarni asosiy papkadan (root_path) topib yuborish
    return send_from_directory(app.root_path, filename)

@app.errorhandler(404)
def page_not_found(e):
    """
    404 (Topilmadi) xatosi yuz berganda ishlaydi.
    """
    return "Sahifa topilmadi: 404", 404

# Ilovani ishga tushirish
if __name__ == '__main__':
    # Serverni mahalliy kompyuterda ishga tushirish (host='0.0.0.0' hamma interfeysdan kirishga ruxsat beradi)
    # debug=True - kod o'zgarganda serverni avtomatik qayta yuklaydi
    app.run(host='0.0.0.0', port=5000, debug=True)
