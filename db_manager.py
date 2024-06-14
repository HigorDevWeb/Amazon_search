import sqlite3

def init_db():
    conn = sqlite3.connect('amazon_products.db')
    c = conn.cursor()
    c.execute('''
              CREATE TABLE IF NOT EXISTS products (
                  id INTEGER PRIMARY KEY AUTOINCREMENT,
                  title TEXT,
                  price TEXT,
                  link TEXT,
                  image TEXT
              )
              ''')
    return conn, c

def insert_data_into_db(conn, c, title, price, link, img):
    c.execute('INSERT INTO products (title, price, link, image) VALUES (?,?,?,?)', (title, price, link, img))
    conn.commit()
