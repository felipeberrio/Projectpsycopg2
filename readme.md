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
