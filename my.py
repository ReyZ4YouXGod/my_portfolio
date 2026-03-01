from flask import Flask, render_template

app = Flask(__name__)

# Baris ini WAJIB ada supaya Vercel bisa jalanin Flask-mu
app = app 

@app.route('/')
def home():
    context = {
        "name": "ReyZ4YouXGod",
        "role": "Python Enthusiast & Developer",
        "bio": "Code is my language, logic is my art. Coffee in, code out.",
        "whatsapp": "6281260512743",
        "telegram": "ReyZ4YouXGod",
        "github": "ReyZ4YouXGod",
        "instagram": "reyz4you_xgod",
        "projects": [
            {"title": "Automated Scraper", "tech": "Python", "desc": "Bot pengambil data otomatis."},
            {"title": "Telegram Bot AI", "tech": "API, Python", "desc": "Bot Telegram pintar."},
            {"title": "System Monitor", "tech": "Flask", "desc": "Dashboard pemantau sistem."}
        ]
    }
    return render_template('index.html', **context)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
