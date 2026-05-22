import sqlite3

DB = 'quises.sqlite'
conn = None
cursor = None

def open():
    global conn, cursor
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()
    # CONFIGURAR PARAMETROS DE LA DATABASE
    cursor.execute('PRAGMA foreign_key=on')

def close():
    cursor.close()
    conn.close()

def execute_query(query):
    cursor.execute(query)
    conn.commit()

def create_tables():
    open()

    tables = [
        '''CREATE TABLE IF NOT EXISTS quiz (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL);''',

        '''CREATE TABLE IF NOT EXISTS question (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        question_name TEXT NOT NULL,
        correct VARCHAR(100) NOT NULL,
        wrong1 VARCHAR(100) NOT NULL,
        wrong2 VARCHAR(100) NOT NULL,
        wrong3 VARCHAR(100) NOT NULL
        );''',

        '''CREATE TABLE IF NOT EXISTS quiz_content(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        quiz_id INTEGER NOT NULL,
        question_id INTEGER NOT NULL,
        FOREIGN KEY (quiz_id) REFERENCES quiz (id) ON DELETE CASCADE,
        FOREIGN KEY (question_id) REFERENCES question (id) ON DELETE CASCADE);''']

    for query in tables:
        execute_query(query)

    close()

def set_quises():
    quises = [
            ('Propio juego', ),
            ('¿Quién quiere ser millonario?', ),
            ('El más inteligente', )]
    open()
    cursor.executemany('INSERT INTO quiz (name) VALUES (?);', quises)
    conn.commit()
    close()

def set_question():
    questions = [
            ('¿Cuántos meses en un año tienen 28 días?', 'Todos', 'Uno', 'Ninguno','Dos'),
            ('¿Qué aspecto tendrá el acantilado verde si se cae en el Mar Rojo?', 'Mojado', 'Rojo', 'No cambiará', 'Púrpura'),
            ('¿Con qué mano es mejor mezclar el té?', 'Con una cuchara', 'Derecha', 'Izquierda', 'Cualquiera'),
            ('¿Qué no tiene longitud, profundidad, ancho, o altura pero puede medirse?', 'Tiempo', 'Estupidez', 'El mar','Aire'),
            ('¿Cuándo es posible sacar agua con una red?', 'Cuando el agua está congelada', 'Cuando no hay peces', 'Cuando los peces de colores nadan lejos', 'Cuando la red se rompe'),
            ('¿Qué es más grande que un elefante y no pesa nada?', 'La sombra de un elefante','Un globo','Un paracaídas', 'Una nube')
        ]
    open()
    cursor.executemany('''INSERT INTO question (
        question_name, correct, wrong1, wrong2, wrong3)
        VALUES (?, ?, ?, ?, ?);''', questions)
    conn.commit()
    close()

def fetch_data(query, data=None):
    open()
    if data:
        cursor.execute(query, data)
    else:
        cursor.execute(query)
    result = cursor.fetchall()
    close()
    return result
        
def show_tables():
    open()
    tables = ['quiz', 'question', 'quiz_content']
    for table in tables:
        print(f'=== TABLA: {table} ===')
        try:
            cursor.execute(f'SELECT * FROM {table}')
            data = cursor.fetchall()
            if not data:
                print('La tabla esta vacia.')
            else:
                for d in data:
                    print(d)

        except sqlite3.OperationalError as error:
            print(f'Ocurrio el siguiente error: {error}')
    close()

    
def destroy_db():
    open()
    tables = ['quiz_content', 'quiz', 'question']
    for table in tables:
        execute_query(f'DROP TABLE IF EXISTS {table}')
    close()
    print('😘')

def create_links():
    pass
