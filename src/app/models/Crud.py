import sqlite3
import datetime

# Create your models here.


class Crud:
    @classmethod
    def findAll(cls):
        table_name = cls._meta.db_table

        query_columns = f"PRAGMA table_info({ table_name })"
        with sqlite3.connect('src/data/bmt_db.sqlite3') as connection:
            cursor = connection.cursor()
            cursor.execute(query_columns)
            columns = [column[1] for column in cursor.fetchall()]

        query = f"SELECT * FROM { table_name } "

        with sqlite3.connect('src/data/bmt_db.sqlite3') as connection:
            cursor = connection.cursor()
            cursor.execute(query)
            rows = cursor.fetchall()

            if rows:
                result = []
                for row in rows:
                    row_dict = {column: value for column, value in zip(columns, row)}
                    result.append(row_dict)
                return result

        return None 


    @classmethod
    def findOne(cls, data):
        table_name = cls._meta.db_table
        key, value = next(iter(data.items()))

        query = f"SELECT * FROM { table_name } WHERE {key} = ?"

        with sqlite3.connect('src/data/bmt_db.sqlite3') as connection:
            cursor = connection.cursor()
            cursor.execute(query, (value,))
            row = cursor.fetchone()

            if row: 
                return cls(*row)
            
        return None

    @classmethod
    def create(cls, data):
        table_name = cls._meta.db_table
        columns = ", ".join(data.keys())
        placeholders = ", ".join(["?" for _ in data.values()])
        values = tuple(data.values())


        query = f"INSERT INTO { table_name } ({ columns }) VALUES ({ placeholders })"

        with sqlite3.connect('src/data/bmt_db.sqlite3') as connection:
            cursor = connection.cursor()
            cursor.execute(query, values)

    
    @classmethod
    def update(cls, data, where):     
        table_name = cls._meta.db_table
        set_data = ""
        set_condition = ""

        for key, value in data.items():
            set_data += f"{key} = '{value}', "

        if set_data.endswith(", "): set_data = set_data[:-2]

        for key, value in where.items():
            set_condition += f"{key} = '{value}' AND "

        if set_condition.endswith("AND "): set_condition = set_condition[:-4]
            

        query = f"UPDATE {table_name} SET {set_data} WHERE {set_condition}"

        with sqlite3.connect('src/data/bmt_db.sqlite3') as connection:
            cursor = connection.cursor()
            cursor.execute(query)


    @classmethod
    def destroy(cls, where):
        table_name = cls._meta.db_table
        key, value = next(iter(where.items()))

        
        query = f"DELETE FROM { table_name } WHERE { key } = { value }"

        with sqlite3.connect('src/data/bmt_db.sqlite3') as connection:
            cursor = connection.cursor()
            cursor.execute(query)




    @classmethod
    def find_orders_with_dependances_by_user(cls, where):
        set_condition = ""

        for key, value in where.items():
            set_condition = f"{key} = {value}"

        query = """
            SELECT o.id AS order_id, o.command_date, d.id AS drink_id, d.name AS drink_name, 
                   t.id AS topping_id, t.name AS topping_name
            FROM app_order o
            JOIN app_order_drink od ON o.id = od.order_id
            JOIN app_drink d ON od.drink_id = d.id
            LEFT JOIN app_drink_topping dt ON d.id = dt.drink_id
            LEFT JOIN app_topping t ON dt.topping_id = t.id
            WHERE {where_condition}
            ORDER BY o.command_date DESC;
        """.format(where_condition=set_condition)

        # Exécution de la requête SQL
        with sqlite3.connect('src/data/bmt_db.sqlite3') as connection:
            cursor = connection.cursor()
            cursor.execute(query)
            rows = cursor.fetchall()

        return rows


    @classmethod
    def create_order_with_cart(cls, command_date, state, total, user_id, cart):
        # Insérez la commande
        order_query = """
            INSERT INTO app_order (command_date, state, total_order, user_id, num_order) 
            VALUES (?, ?, ?, ?, ?)
        """
        # Concaténation de l'ID de la commande et de la date de commande pour former le numéro de commande
        num_order = f"{cls.get_last_order_id() + 1}-{datetime.date.today().strftime('%Y%m%d')}"

        order_values = (command_date, state, total, user_id, num_order)
        order_id = cls._execute_query(order_query, order_values)

        # Ajoutez chaque boisson du panier à la commande
        for item in cart:
            drink_id = item['id']
            toppings = item.get('toppings', [])  # Liste des garnitures associées à la boisson
            sugar_quantity = item.get('sugar')

            # Insérez la boisson dans la commande
            order_drink_query = """
                INSERT INTO app_order_drink (order_id, drink_id, sugar_quantity)
                VALUES (?, ?, ?)
            """
            order_drink_values = (order_id, drink_id, sugar_quantity)
            cls._execute_query(order_drink_query, order_drink_values)

            # Ajoutez les garnitures associées à la boisson
            for topping_id in toppings:
                # Insérez la garniture associée à la boisson
                drink_topping_query = """
                    INSERT INTO app_drink_topping (drink_id, topping_id)
                    VALUES (?, ?)
                """
                drink_topping_values = (drink_id, topping_id)
                cls._execute_query(drink_topping_query, drink_topping_values)

        return order_id

    @staticmethod
    def _execute_query(query, values=None):
        with sqlite3.connect('src/data/bmt_db.sqlite3') as connection:
            cursor = connection.cursor()
            if values:
                cursor.execute(query, values)
            else:
                cursor.execute(query)
            connection.commit()
            return cursor.lastrowid

    @staticmethod
    def get_last_order_id():
        with sqlite3.connect('src/data/bmt_db.sqlite3') as connection:
            cursor = connection.cursor()
            cursor.execute("SELECT MAX(id) FROM app_order")
            last_order_id = cursor.fetchone()[0]
            return last_order_id if last_order_id else 0
