import psycopg2

host = "ec2-35-170-21-76.compute-1.amazonaws.com"
database = "df3vmel3o67tkn"
user = "nsukfugnsofdhk"
password = "a77f19d1a782e1547662653f2091e798fb110a7d3e1f8bba590c3c20afa08b50"
port = 5432

cur = None

try:
  conn = psycopg2.connect(host=host,
                          database=database,
                          user=user,
                          password=password,
                          port=port)
  cur = conn.cursor()

  cur.execute("CREATE TABLE products(id SERIAL PRIMARY KEY)");
  conn.commit()

except Exception as error:
  print(error)

finally:
  if cur is not None:
    cur.close()
  if conn is not None:
    conn.close()
