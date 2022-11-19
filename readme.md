### Python & PostgreSQL - Psycopg2 Tutorial
> https://www.psycopg.org/docs/

> Proyecto de conexión a una libreria en la nube llamada psycopg2

## Proyect IDE

1. Vamos a utilizar Replit.com IDE para crear un entorno de python en la nube por lo que no tenemos que instalar modulos en el pc y preocuparnos por nuestro rendimiento, además vamos a usar Heroku servicio de entorno en la nube para nuestra base de datos Heroku Postgress

2. print('Hello World') + ctrl + enter = Hello World
Ya tenemos un entorno de python así que vamos a instalar módulos

## Heroku Postgress

3. en Heroku.com vamos a ingresas y vamos a crear una nueva aplicación, lo creamos como: proyecto-psycopg2 en USA,

4. Con el proyecto creado vamos a ir al plugin en Resourses - Add-ons - Heroku Postgres, escogemos el plan gratuito para usar bases de datos únicamente desde la nube, al hacer esto creamos nuestro entorno de postgress en la nube.

5. Damos click en el Add-ons de heroku postgress creado que nos va a llevar a: https://data.heroku.com/datastores/db85caef-e383-44c0-9aa9-aa3c57d9c93a: el panel de la base de datos creada, con el nombre que postgress nos da todo bajo los limites gratuitos, 10.000 filas y demás carateristicas de la DB.

6. Vamos a settings del panel de control de la DB y vemos en Database Credentials - View Credentials; esta documentación mantenerla lo mas seguro posible, nos dice donde se aloja la DB, que clave de acceso, nombre de la DB, etc

## Conexión entre proyecto python en Replit y DB en Heroku

Modulo prycopg2<br>
7. vamos a ir a o buscamos en Google psycopg2: https://www.psycopg.org/docs/

8. Allí vamos al link de Instalation - Quick Instalation<br>Existen 2 psycopg2: psycopg vs psycopg-binary

>psycopg-binary: Principiantes que aprenden recién a hacer conexiones entre el modulo desde python a postgress sql (usarlo enteramente desde la nube) - NUESTRO CASO
>
>psycopg2: Para usar en producción

9. Normalmente esta instalado en las librerias de postgress el modulo de prycopg2 PERO ESO SI INSTALARAMOS LOCAL y descargaramos postgress en nuestra maquina pero esta maquina de replit no lo tiene por lo que vamos a  uscar en packages de la barra de herramientas lateral izquierda: psycopg2-binary <br>ojo que sea el 2
>Manualmente se puede instal en la consola de shell power shell con: pip install psycopg2
>
>Ya tenemos instalada nuestra versión por defecto de PIP podemos verla con: pip --version
>
<br>
Replit utiliza un administrador de paquetes llamado poetry podemos verlo en files

### Configurando el main.py

10. Primero importamos el modulo descargado: <br>import psycopg2
11. Utilizamos su método connect que recive varios parametros host: database: user: password: port: que traemos desde heroku<br>Para no tener cambiarlo manual vamos a incluir una variable llamada host que tenga la url del host de la DB de heroku

host="ec2-35-170-21-76.compute-1.amazonaws.com"
database="df3vmel3o67tkn"
user="nsukfugnsofdhk"
password="a77f19d1a782e1547662653f2091e798fb110a7d3e1f8bba590c3c20afa08b50"
port=5432

psycopg2.connect(
  host=host,
  database=database,
  user=user,
  password=password,
  port=port
)

Ya tenemos los parametros principales, comprobemos la conexión<br>

12. el modulo psycopg2 va a devolver un objeto de conexión que guardaremos en una variable conn: conn = psycopg2.connect(

13. Esto puede ir mál o bien entonces vamos a hacer un try: (lo que espero que vaya bien)  y un excep: (si sale una excepción que lo ponga como error al posible error de conexión)
try:
  conn = psycopg2.connect(
    host=host,
    database=database,
    user=user,
    password=password,
    port=port
  )
  print('Correct conection')
except Exception as error:
  print(error)

14. Le damos a correr en consola y si todo va bien saldra un: Correct conection

15. Al utilizar la base de datos, vamos a usar conn para conectar pero con el metodo cursor .cur() para permitirme hacer consultas, asi que creamos cursor en una variable: cur = conn.cursor(), luego ejecutamos el servidor, y sumamos desde la DB, luego creamos la respuesta, y luego la imprimimos, 

  >cur = conn.cursor()
  >
  >cur.execute("SELECT 1 + 1")
  >  
  >result = cur.fetchone()
  >print(result)

16. Pero tambien tenemos que cerrar esta conexión y el cursor

  cur.close()
  conn.close()

17. Otra forma de cerrar es poner al final finally: donde si existe un cursor no vacio, cerrarlo. Creamos la variable fuera del try: para que el finally pueda acceder a ella:
    > cur = None
    >
    > finally:
    >   if cur is not None:
    >   cur.close()
    >   if conn is not None:
    >   conn.close()
    

18. Vamos a borrar la consulta de ejemplo que hicimos anteriormente:
  cur.execute("SELECT 1 + 1")
  result = cur.fetchone()
  print(result)
  print('Correct conection')


### Crear tabla con nuestra conexión psycopg2

19. Al crear una DB en postgress no tenemos ninguna tabla creada, podemos crear por código utilizando el cursos que tenemos con el metodo execute para ejecutar una consulta y la consulta sera crear una tabla productos y detallar lo que queremos como un id serial y que sera un primary.

  cur.execute("CREATE TABLE products(id SERIAL PRIMARY KEY)");

20. Para crear la tabla necesitamos tambien usar el metodo commit() para especificar que esa es la consulta que queremos hacer en la DB en la conexión

  conn.commit()

>Al ejecutar ya podemos ver que en heroku se nos crea la nueva tabla en la DB
>En DATACLIPS podemos hacer consultar de las DB con Create Dataclip -> y ahi vas a poner lo que necesitas consultar ej. SELECT * FROM products y nos seleccionaria todas las filas de la tabla, en este caso nada porque no tiene datos pero significa que la tabla si existe

21. Si quiero una tabla con más columnas podemos refactorizar nuestro código, usar las multiples string de python con """

    cur.execute("""
              CREATE TABLE IF NOT EXISTS users(
                id SERIAL PRIMARY KEY,
                name VARCHAR(255) NOT NULL,
                email VARCHAR(255) NOT NULL,
                password VARCHAR(255) NOT NULL
              )
              """);
  conn.commit()

>Si ejecutamos esto vamos a tener dos tablas en heroku, la nueva con nuevas columnas

22. Igualmente esta consulta que al final es un string podemos guardarla en una variable

### Insetar una fila Insert Row()

23. Vamos a borrar la variable con nuestra consultar para primeramente hacer ejecutar una consultar donde vamos a a hacer una insercion y donde le vamos a ejecutar el lenguaje SQL donde vamos a agregar una fila con valores del tipo string a cada uno de las columnas 

  cur.execute("INSERT INTO users(name, email, password) VALUES (%s, %s, %s)")

24. Despues del string voy a ingresar una tupla que coincida con los valores que espero (crear los datos de la fila)

  cur.execute("INSERT INTO users(name, email, password) VALUES (%s, %s, %s)", ("Cristian   Berrio","cristianberrio95@gmail.com","123456789"))
  
  conn.commit()

25. y podemos ejecutar el código y buscar en heroku en la dataclip en busqueda que teniamos test de SELECT * FROM users y vamos a obtener los datos anteriormemnte escritos