from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
import sqlite3

conn = sqlite3.connect('example.db')

with conn:
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            email TEXT NOT NULL
        )
    """)

c = conn.cursor()

c.execute('''CREATE TABLE mytable
             (column1 TEXT, column2 TEXT)''')

# Connect to the database
conn = sqlite3.connect('example.db')

# Create a cursor object
c = conn.cursor()

# Execute an INSERT statement
c.execute("INSERT INTO mytable (column1, column2) VALUES (?, ?)", ('value1', 'value2'))

# Commit the changes
conn.commit()

# Close the connection
conn.close()


class MyApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('My App')

        layout = QVBoxLayout()
        self.setLayout(layout)

        label = QLabel('Users')
        layout.addWidget(label)

        conn = sqlite3.connect('example.db')
        cursor = conn.cursor()

        select_query = "SELECT * FROM users"
        cursor.execute(select_query)
        results = cursor.fetchall()

        for result in results:
            label = QLabel(f"{result[0]}. {result[1]} ({result[2]})")
            layout.addWidget(label)


if __name__ == '__main__':

    app = QApplication([])
    window = MyApp()
    window.show()
    app.exec()
