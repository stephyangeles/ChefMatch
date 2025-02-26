import os
from connection import connect_to_database

def drop_all_tables():
    conn = connect_to_database()
    cursor = conn.cursor()

    try:
        with open(os.path.join(os.path.dirname(__file__),'tables/drop_all_tables.sql'), 'r') as file:
            drop_all_sql = file.read()

        cursor.execute(drop_all_sql)
        print("All tables have been dropped.")

        conn.commit()

    except Exception as e:
        print(f"Error trying to delete all tables: {e}")

    finally:
        cursor.close()
        conn.close() 

if __name__ == "__main__":
    drop_all_tables()  