<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>OSINT Multi-Search Engine</title>
    <style>
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background-color: #0f172a; color: #f8fafc; padding: 40px; display: flex; justify-content: center; }
        .container { max-width: 650px; width: 100%; background: #1e293b; padding: 30px; border-radius: 12px; box-shadow: 0 10px 25px rgba(0,0,0,0.5); }
        h1 { text-align: center; color: #38bdf8; margin-bottom: 25px; }
        .search-box { display: flex; flex-direction: column; gap: 12px; margin-bottom: 25px; }
        .input-group { display: flex; gap: 10px; }
        select, input[type="text"] { padding: 12px; border-radius: 6px; border: 1px solid #334155; background: #0f172a; color: #fff; font-size: 16px; outline: none; }
        select { cursor: pointer; color: #38bdf8; font-weight: bold; }
        input[type="text"] { flex: 1; }
        button { padding: 12px 24px; border: none; background: #0284c7; color: white; border-radius: 6px; font-weight: bold; cursor: pointer; font-size: 16px; transition: 0.2s; }
        button:hover { background: #0369a1; }
        .card { background: #334155; padding: 12px 16px; border-radius: 6px; margin-bottom: 10px; display: flex; justify-content: space-between; align-items: center; }
        .card a { color: #38bdf8; text-decoration: none; word-break: break-all; font-weight: 500; }
        .card a:hover { text-decoration: underline; }
        .status { background: #22c55e; color: #000; padding: 4px 8px; border-radius: 4px; font-size: 12px; font-weight: bold; }
    </style>
</head>
<body>
    <div class="container">
        <h1>OSINT Search Tool</h1>
        <form method="POST" class="search-box">
            <div class="input-group">
                <select name="search_type">
                    <option value="general" {% if search_type == 'general' %}selected{% endif %}>Ник / Email</option>
                    <option value="phone" {% if search_type == 'phone' %}selected{% endif %}>Телефон</option>
                    <option value="name" {% if search_type == 'name' %}selected{% endif %}>ФИО</option>
                    <option value="photo" {% if search_type == 'photo' %}selected{% endif %}>Поиск Фото</option>
                </select>
                <input type="text" name="query" placeholder="Введите данные..." value="{{ query }}" required>
            </div>
            <button type="submit">Искать OSINT</button>
        </form>

        {% if results %}
            <div>
                {% for item in results %}
                    <div class="card">
                        <a href="{{ item.url }}" target="_blank">{{ item.title }}</a>
                        <span class="status">{{ item.status }}</span>
                    </div>
                {% endfor %}
            </div>
        {% endif %}
    </div>
</body>
</html>
