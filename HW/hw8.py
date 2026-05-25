import sqlite3

connect = sqlite3.connect("users")
cursor = connect.cursor()

cursor.execute('''
        CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name VARCHAR (50) NOT NULL
          
)
''')
cursor.execute('''
        CREATE TABLE IF NOT EXISTS movies(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            GENRE TEXT NOT NULL


)
''')
cursor.execute('''
       CREATE TABLE IF NOT EXISTS reviews(
           id INTEGER PRIMARY KEY AUTOINCREMENT,
           user_id INTEGER NOT NULL,
           movie_id INTEGER NOT NULL,
           rating INTEGER NOT NULL,
           FOREIGN KEY(user_id) REFERENCES users(id),
           FOREIGN KEY(movie_id) REFERENCES movies(id)
)
''')
connect.commit()

users = [
    ("Айжан",),
    ("Нурсултан",),
    ("Алима",),
    ("Темирлан",),
    ("Диана",)
]
cursor.executemany("INSERT INTO users (name) VALUES(?)",users)
movies = [
    ('Гарри Поттер', 'фантастика'),
    ('Властелин колец', 'Фэнтези'),
    ('Престиж', "Детектив"),
    ('Побег из Шоушена', 'Драма'),
    ('Начало', "Триллер"),
]
cursor.executemany(
    "INSERT INTO movies (title, genre) VALUES (?, ?)",
    movies
)
reviews = [
    (1, 1, 10),
    (1, 2, 8),
    (2, 3, 9),
    (2, 4, 7),
    (3, 5, 10),
    (3, 1, 9),
    (4, 2, 6),
    (4, 3, 8),
    (5, 4, 9),
    (5, 5, 10)
]
cursor.executemany(
    "INSERT INTO reviews (user_id, movie_id, rating) VALUES (?, ?, ?)",
    reviews
)
print("Отзывы пользователей:\n")

cursor.execute("""
SELECT users.name, movies.title, reviews.rating
FROM reviews
JOIN users ON reviews.user_id = users.id
JOIN movies ON reviews.movie_id = movies.id
""")
print("\nВсе фильмы:\n")

cursor.execute("""
SELECT movies.title, reviews.rating
FROM movies
LEFT JOIN reviews ON movies.id = reviews.movie_id
""")

for row in cursor.fetchall():
    print(row)

print("\nАгрегации:\n")

cursor.execute("SELECT AVG(rating) FROM reviews")
print("Средняя оценка:", cursor.fetchone()[0])

cursor.execute("SELECT MAX(rating) FROM reviews")
print("Максимальная оценка:", cursor.fetchone()[0])

cursor.execute("SELECT MIN(rating) FROM reviews")
print("Минимальная оценка:", cursor.fetchone()[0])

connect.close()
