from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Функция для проверки наличия аккаунта по никнейму
def osint_search_nick(username):
    results = []
    sites = {
        "GitHub": f"https://github.com/{username}",
        "Telegram": f"https://t.me/{username}",
        "Steam": f"https://steamcommunity.com/id/{username}"
    }
    
    for site_name, url in sites.items():
        try:
            r = requests.get(url, timeout=3)
            if r.status_code == 200:
                results.append({"site": site_name, "url": url, "status": "Найден"})
        except Exception:
            pass
            
    return results

@app.route('/', methods=['GET', 'POST'])
def home():
    results = None
    query = ""
    if request.method == 'POST':
        query = request.form.get('query', '').strip()
        if query:
            clean_nick = query.replace('@', '')
            results = osint_search_nick(clean_nick)
            
    return render_template('index.html', results=results, query=query)

if __name__ == '__main__':
    app.run(debug=True)