import sqlite3

def create_db():
# читаємо файл зі скриптом для створення БД
    with open('d:/GOIT/THEORY/commit/first_project/example_sql/salary.sql', 'r') as f:
        sql = f.read()

# створюємо з'єднання з БД (якщо файлу з БД немає, він буде створений)
    with sqlite3.connect('d:/GOIT/THEORY/commit/first_project/example_sql/salary.sql') as con:
        cur = con.cursor()
# виконуємо скрипт із файлу, який створить таблиці в БД
        cur.executescript(sql)

if __name__ == "__main__":
    create_db()
