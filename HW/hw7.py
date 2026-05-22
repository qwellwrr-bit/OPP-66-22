import sqlite3
connect = sqlite3.connect("store.db")

cursor = connect.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(35) NOT NULL,
        price REAL NOT NULL,
        quantity INTEGER                         
)
 ''')
connect.commit()

def create_product(name,price,quantity):
    cursor.execute(
            'INSERT INTO products (name, price, quantity) VALUES (?, ?, ?)',
            (name, price, quantity)
    )
connect.commit()
print("продукт добавлен")
create_product("Lenovo",1200,13)
create_product('Iphone', 23000,10)
create_product("hw", 2000, 25)


def read_all_products():
    cursor.execute("SELECT * FROM products")
    data = cursor.fetchall()
    for i in data:
        print(i)

read_all_products()

def update_product(name, id):
    cursor.execute(
        "UPDATE products SET name = ? WHERE id = ?",
        (name, id)

    )
connect.commit()
print("продукт обнавлен")

update_product("Samsung", 1)
def delete_product(id):
    cursor.execute(
        "DELETE FROM products WHERE rowid = ?",
        (id,)
    )
    connect.commit()
    print("пользователь удален")

delete_product(1)
print("после изменений")








