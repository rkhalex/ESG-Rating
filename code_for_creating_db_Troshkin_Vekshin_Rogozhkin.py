import sqlite3

conn = sqlite3.connect('data.db')
cur = conn.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS my_table (url TEXT, text TEXT)''')
url_dict = {'url1': 'text1', 'url2': 'text2'} #Вставляем словарь

for key, value in url_dict.items():
    cur.execute("INSERT INTO my_table (key, value) VALUES (?, ?)", (key, value))

conn.commit()
