import psycopg2
from faker import Faker
connection = psycopg2.connect(
    database="estacio",
    user="postgres",
    password="19029696",
    port=5433
)

print("Connection ok")

cursor = connection.cursor()
fake = Faker('pt-BR')
n = 10

for i in range(n):
    code = i + 10
    name = 'product_'+str(i+1)
    price = fake.pyfloat(
        left_digits=3, right_digits=2,
        positive=True,
        min_value=5, max_value=1000
    )
    print(price)
    print(name)

    sql = "INSERT INTO products VALUES(%s, %s, %s)"
    register = (code, name, price)
    cursor.execute(sql, register)

connection.commit()
print("Insert successfully")
connection.close()

