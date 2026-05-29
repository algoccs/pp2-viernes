import sqlite3

DB = "quises.sqlite"
conn = None
cursor = None

def open():
    global conn, cursor
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()
    # parametros de config de la db
    cursor.execute('PRAGMA foreign_keys=on')

def close():
    cursor.close()
    conn.close()

def execute_query(query):
    cursor.execute(query)
    conn.commit()

def create_tables():
    tables = [
    '''CREATE TABLE IF NOT EXISTS quiz (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL);''',
  
    '''CREATE TABLE IF NOT EXISTS question (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    question_name TEXT NOT NULL,
    correct VARCHAR(100) NOT NULL,
    wrong_1 VARCHAR(10) NOT NULL,
    wrong_2 VARCHAR(10) NOT NULL,
    wrong_3 VARCHAR(10) NOT NULL);''',
    
    '''CREATE TABLE IF NOT EXISTS quiz_content (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    quiz_id INTEGER NOT NULL,
    question_id INTEGER NOT NULL,
    FOREIGN KEY (quiz_id) REFERENCES quiz (id) ON DELETE CASCADE,
    FOREIGN KEY (question_id) REFERENCES question (id) ON DELETE CASCADE);'''
    ]

    open()
    for sql in tables:
        execute_query(sql)
    close()
    print('Tablas creadas exitosamente')


def add_quises():
    quizes = [
        ('Propio juego', ),
        ('¿Quién quiere ser millonario?', ),
        ('El más inteligente', )]

    open()
    cursor.executemany('INSERT INTO quiz (name) VALUES (?);', quizes)
    conn.commit()
    close()
    print('Se ingresaron los datos de la tabla quiz!')

def add_questions():
    questions = [
    ('¿Qué se rompe si no se cae y se cae si no se rompe?', 'El día y la noche', 'Un vaso de cristal', 'Un huevo', 'Un secreto'),
    ('¿Qué es lo que puedes mantener después de dárselo a alguien?', 'Tu palabra', 'Un regalo', 'Un secreto', 'Un abrazo'),
    ('¿Qué se vuelve más húmedo cuanto más seca?', 'Una toalla', 'El aire', 'Una esponja', 'El fuego'),
    ('¿Qué objeto tiene ojos pero no puede ver?', 'Una aguja', 'Una tormenta', 'Un espejo', 'Una patata'),
    ('¿Qué tiene dientes pero nunca muerde?', 'Un peine', 'Un tiburón de juguete', 'Una cremallera', 'Un serrucho'),
    ('¿Qué sube pero nunca baja?', 'La edad', 'Un globo de helio', 'El humo', 'La marea'),
    ('¿De qué color son las cajas negras de los aviones?', 'Naranja', 'Negro', 'Blanco', 'Amarillo'),
    ('¿Qué se llena con manos y se vacía con bolsillos?', 'Los guantes', 'El dinero', 'Los pañuelos', 'La arena'),
    ('¿Qué país tiene más pirámides en el mundo?', 'Sudán', 'Egipto', 'México', 'Perú'),
    ('Si un tren eléctrico viaja hacia el norte, ¿hacia dónde va el humo?', 'Hacia ningún lado', 'Hacia el sur', 'Hacia el este', 'Hacia el oeste'),
    ('¿Qué tiene un cuello pero no tiene cabeza?', 'Una botella', 'Una jirafa', 'Una guitarra', 'Una camisa'),
    ('¿Qué invento te permite mirar directamente a través de una pared?', 'La ventana', 'El telescopio', 'Los rayos X', 'El periscopio'),
    ('¿Cuántos animales de cada especie metió Moisés en el arca?', 'Ninguno', 'Dos', 'Siete', 'Uno de cada uno'),
    ('¿Qué se compra para comer pero nunca se come?', 'El plato', 'La sopa', 'El pan', 'El menú'),
    ('¿Qué pesa más: un kilo de plumas o un kilo de plomo?', 'Pesan lo mismo', 'El kilo de plomo', 'El kilo de plumas', 'Depende del viento'),
    ('¿Qué tiene llaves pero no abre ninguna puerta?', 'Un piano', 'Un llavero', 'Un mapa', 'Un candado roto'),
    ('¿Qué puedes romper sin siquiera tocarlo o moverlo?', 'Una promesa', 'Un espejo', 'El silencio', 'Un récord'),
    ('¿Qué siempre viene pero nunca llega?', 'El mañana', 'El cartero', 'El invierno', 'El tren de las cinco'),
    ('¿De qué puedes llenar un balde para que pese menos?', 'De agujeros', 'De plumas', 'De aire caliente', 'De corcho'),
    ('¿Qué tiene patas pero no puede caminar?', 'Una mesa', 'Un ciempiés dormido', 'Un pantalón', 'Un cangrejo'),
    ('¿Qué palabra se escribe incorrectamente en todos los diccionarios?', 'Incorrectamente', 'Errónea', 'Falso', 'Ninguna'),
    ('Si estás en una carrera y adelantas al que va segundo, ¿en qué posición quedas?', 'Segundo', 'Primero', 'Tercero', 'Último'),
    ('¿Qué tiene hojas pero no es un árbol ni una planta?', 'Un libro', 'Un cuchillo', 'Una ensalada', 'Un calendario'),
    ('¿Cuál es el día más largo de la semana?', 'El miércoles', 'El domingo', 'El sábado', 'El lunes'),
    ('¿Qué es lo que entra duro y seco, pero sale blando y húmedo?', 'Un chicle', 'Un pan', 'Un fideo', 'Una esponja'),
    ('¿Qué te pertenece a ti pero los demás lo usan mucho más que tú?', 'Tu nombre', 'Tu coche', 'Tu número de teléfono', 'Tu paciencia'),
    ('¿Qué animal da saltos para caminar y se sienta para pararse?', 'El canguro', 'La rana', 'El conejo', 'El saltamontes'),
    ('¿Qué tipo de árbol puedes llevar en la mano?', 'La palma', 'El bonsái', 'El pino', 'El naranjo'),
    ('¿Qué ciudad tiene cinco letras y está en el medio de todas?', 'París', 'Madrid', 'Roma', 'Tokio'),
    ('¿Qué se hace más grande cuanta más tierra le quitas?', 'Un agujero', 'Una montaña', 'Un árbol', 'Un pozo de agua'),
    ('¿Qué tiene una cara y dos manos, pero no tiene brazos ni piernas?', 'Un reloj', 'Una moneda', 'Un espejo', 'Un fantasma'),
    ('¿Dónde se encuentra el océano Atlántico según el mapa al revés?', 'En el mismo lugar', 'En el sur', 'Abajo del Pacífico', 'A la derecha'),
    ('¿Qué entra en el agua y no se moja?', 'La sombra', 'El aceite', 'El hielo', 'Un pez con escamas'),
    ('¿Qué corre pero no tiene pies?', 'El agua', 'El viento', 'El tiempo', 'Un coche'),
    ('¿Qué número no tiene ninguna letra "O" en su nombre?', 'Cien', 'Uno', 'Dos', 'Ocho'),
    ('¿Qué se puede atrapar pero nunca se puede lanzar?', 'Un resfriado', 'Una pelota de tenis', 'Una mosca', 'Una idea'),
    ('¿Quién puede hablar todos los idiomas del mundo?', 'El eco', 'Un políglota', 'Un traductor', 'Un bebé'),
    ('¿Qué lenguaje se habla sin emitir un solo sonido?', 'El lenguaje corporal', 'El latín', 'El código Morse', 'El mimo'),
    ('¿Qué mes tiene 30 días?', 'Once meses', 'Cuatro meses', 'Seis meses', 'Todos'),
    ('¿Cuál es el instrumento musical que tiene una cuerda pero no se puede tocar?', 'La comba', 'El arco', 'El violín', 'El bajo'),
    ('¿Qué comida es sagrada para los programadores?', 'Los algoritmos con papas', 'La pizza fría', 'Los espaguetis con código', 'Las galletas de la fortuna'),
    ('¿Qué es negro cuando lo compras, rojo cuando lo usas y gris cuando lo tiras?', 'El carbón', 'El té negro', 'Un ladrillo', 'Un fósforo'),
    ('¿Cuántas manzanas crecen en un árbol de peras?', 'Ninguna', 'Dos por rama', 'Depende de la estación', 'Muchas'),
    ('¿Qué ciudad española se escribe con las mismas letras que "gira por"?', 'Parroquia', 'Girona', 'Vigo', 'Burgos'),
    ('¿Qué planta no da flores ni frutos, pero da cobijo?', 'La planta del pie', 'El musgo', 'El helecho', 'El pino'),
    ('¿Qué conductor viaja sin coche, moto ni bicicleta?', 'El de una orquesta', 'El del autobús', 'Un taxista a pie', 'El de la luz'),
    ('¿Qué es lo primero que hace una vaca cuando sale el sol?', 'Sombra', 'Comer pasto', 'Mugir', 'Caminar'),
    ('¿Qué estrella es la que está más cerca de la Tierra?', 'El Sol', 'Alfa Centauri', 'La Estrella Polar', 'Sirio'),
    ('¿Cuál es el animal que tiene más dientes?', 'El caracol', 'El tiburón blanco', 'El cocodrilo', 'El caimán'),
    ('¿Qué elemento químico pesa menos si le añades electrones?', 'Ninguno', 'El hidrógeno', 'El helio', 'El litio')
]
    open()
    cursor.executemany('''INSERT INTO question
    (question_name, correct, wrong_1, wrong_2, wrong_3)
    VALUES (?,?, ?, ?, ?);''', questions)
    conn.commit()
    close()
    print('Se ingresaron los datos de la tabla!')


def add_links(): # ESTRUCTURAR CUESTIONARIOS
    links = []

    link = input('Desea ingresar un enlace? (y/n): ')
    while link.lower() == 'y':
        quiz_id = int(input('ID del quiz: ')) 
        question_id = int(input('ID de la pregunta: ')) 

        links.append((quiz_id, question_id))
        link = input('Desea ingresar otro? (y/n): ')

    if links:
        open()
        cursor.executemany('INSERT INTO quiz_content (quiz_id, question_id) VALUES (?, ?);', links)
        conn.commit()
        close()

def destroy_db():
    tables = ['quiz_content', 'quiz', 'question']
    open()
    for table in tables:
        execute_query(f'DROP TABLE IF EXISTS {table};')
    close()
    print('😂')
        
def show_tables():
    tables = ['quiz', 'question', 'quiz_content']
    open()

    for table in tables:
        print(f'=== TABLA: {table} ===')
        try:
            cursor.execute(f'SELECT * FROM {table};')
            data = cursor.fetchall()

            if not data:
                print('La tabla esta vacia.')
            else:
                for reg in data:
                    print(reg)

        except sqlite3.DatabaseError as error:
            print('Error:', error)
    close()

def get_next_question(question_id=0, quiz_id=1):
    open()

    query = '''
        SELECT
            quiz_content.id,
            question.question_name,
            question.correct,
            question.wrong_1,
            question.wrong_2,
            question.wrong_3
        FROM quiz_content
        JOIN question ON quiz_content.question_id = question.id
        WHERE quiz_content.id > ?
        AND quiz_content.quiz_id = ?
        ORDER BY quiz_content.id
        LIMIT 1'''
    
    cursor.execute(query, [question_id, quiz_id])
    result = cursor.fetchone()
    close()
    return result

def fetch_data(query, data=None):
    open()
    if data:
        cursor.execute(query, data)
    else:
        cursor.execute(query)
    result = cursor.fetchall()
    close()

    return result

def get_quises():
    return fetch_data('SELECT * FROM quiz;')


if __name__ =='__main__':
    quiz = get_quises()


