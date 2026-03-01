from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    context = {
        "name": "ReyZ4YouXGod",
        "role": "Python Enthusiast & Developer",
        "bio": "Code is my language, logic is my art. Coffee in, code out.",
        "whatsapp": "6281260512743", # Ganti nomor WA
        "telegram": "Reyz4YouXGod",  # Ganti user Tele
        "github": "Reyz4YouXGod",    # Ganti user Github
        "instagram": "reyz4you_xgod", # Ganti user IG
        "projects": [
            {"title": "Automated Scraper", "tech": "Python", "desc": "Bot pengambil data otomatis."},
            {"title": "Telegram Bot AI", "tech": "API, Python", "desc": "Bot pintar asisten pribadi."},
            {"title": "System Monitor", "tech": "Flask", "desc": "Dashboard monitoring server."}
        ]
    }
    return render_template('index.html', **context)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
