import psycopg2


class BDAccess:
    def __init__(self):
        print("Constructor")

    def openConnection(self):
        try:
            self.connection = psycopg2.connect(
                database="estacio",
                user="postgres",
                password="19029696",
                port=5433
            )
        except (Exception, psycopg2.Error) as error:
            if self.connection:
                print('Unexpected database error', error)

    def selectData(self):
        try:
            self.openConnection()
            cursor = self.connection.cursor()

            print('Selecting Products')
            selectQuery = "select * from products"

            cursor.execute(selectQuery)
            registers = cursor.fetchall()

        except (Exception, psycopg2.Error) as error:
            print('Unexpected database error', error)

        finally:
            if self.connection:
                cursor.close()
                self.connection.close()
                print('Conection finished')
        return registers

    def insertData(self, code, name, price):
        try:
            self.openConnection()
            cursor = self.connection.cursor()
            insertSql = "insert into products values(%s, %s, %s)"
            recordInsert = (code, name, price)
            cursor.execute(insertSql, recordInsert)
            self.connection.commit()
            count = cursor.rowcount()
            print(count, "Insertion successfully")

        except (Exception, psycopg2.Error) as error:
            print('Unexpected database error', error)

        finally:
            if self.connection:
                cursor.close()
                self.connection.close()
                print('Connection finished')

    def updateData(self, code, name, price):
        try:
            self.openConnection()
            cursor = self.connection.cursor()
            print("Registers before update")
            selectData = "select * from products where code = %s"

            cursor.execute(selectData, [code])

            record = cursor.fetchone()
            print(record)

            updateSql = "update products set name = %s, price = %s where code = %s"

            cursor.execute(updateSql, (name, price, code))
            self.connection.commit()
            select = "select * from products where code = %s"
            cursor.execute(select, [code])
            record = cursor.fetchone()
            print(record)

        except (Exception, psycopg2.Error) as error:
            print(error)

        finally:
            if self.connection:
                cursor.close()
                self.connection.close()
                print('Connection finished')

    def deleteData(self, code):
        try:
            self.openConnection()
            cursor = self.connection.cursor()
            deleteSql = "delete from products where code = %s"

            cursor.execute(deleteSql, [code])

            self.connection.commit()
            print("Register deleted Successfully")

        except (Exception, psycopg2.Error) as error:
            print('Unexpected database error', error)

        finally:
            if self.connection:
                cursor.close()
                self.connection.close()
                print('Connection finished')

