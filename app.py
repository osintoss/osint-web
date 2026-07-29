from flask import Flask, render_template, request
import urllib.parse
import re

app = Flask(__name__)

def clean_phone(phone_str):
    """Очищает номер телефона, оставляя только цифры и +"""
    return re.sub(r'[^\d+]', '', phone_str)

@app.route('/', methods=['GET', 'POST'])
def index():
    results = []
    query = ""
    search_type = "general"

    if request.method == 'POST':
        query = request.form.get('query', '').strip()
        search_type = request.form.get('search_type', 'general')

        if query:
            encoded_query = urllib.parse.quote(query)

            if search_type == 'phone':
                phone_clean = clean_phone(query)
                results = [
                    {"title": "Точное совпадение номера (Google)", "url": f"https://www.google.com/search?q=%22{phone_clean}%22", "status": "Exact"},
                    {"title": "Поиск формата без кодов (Google)", "url": f"https://www.google.com/search?q={phone_clean}", "status": "Search"},
                    {"title": "Проверка в Telegram (t.me)", "url": f"https://t.me/{phone_clean}", "status": "Telegram"},
                    {"title": "Поиск совпадений в соцсетях", "url": f"https://www.google.com/search?q=%22{phone_clean}%22+site:facebook.com+OR+site:instagram.com", "status": "Social"},
                    {"title": "Поиск совпадений в объявлениях и на форумах", "url": f"https://www.google.com/search?q=%22{phone_clean}%22+filetype:txt+OR+filetype:log", "status": "Leaks"}
                ]

            elif search_type == 'name':
                results = [
                    {"title": "Точное совпадение ФИО (Google)", "url": f"https://www.google.com/search?q=%22{encoded_query}%22", "status": "Exact"},
                    {"title": "Поиск профилей Facebook", "url": f"https://www.google.com/search?q=site:facebook.com+%22{encoded_query}%22", "status": "Facebook"},
                    {"title": "Поиск профилей LinkedIn", "url": f"https://www.google.com/search?q=site:linkedin.com/in/+%22{encoded_query}%22", "status": "LinkedIn"},
                    {"title": "Упоминания в документах (PDF, DOC)", "url": f"https://www.google.com/search?q=%22{encoded_query}%22+filetype:pdf+OR+filetype:doc", "status": "Docs"}
                ]

            else:
                # Стандартный поиск (по никнейму/почте)
                results = [
                    {"title": "Google Search", "url": f"https://www.google.com/search?q={encoded_query}", "status": "Search"},
                    {"title": "GitHub Profile", "url": f"https://github.com/{query}", "status": "Code"},
                    {"title": "Telegram Check", "url": f"https://t.me/{query}", "status": "Social"}
                ]

    return render_template('index.html', results=results, query=query, search_type=search_type)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
