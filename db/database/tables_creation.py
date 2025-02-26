import os
from connection import connect_to_database

SQL_DIRECTORY = "db/tables/"
EXCLUDED_FILES = ["drop_all_tables.sql"]

SQL_FILES_IN_ORDER = [
    "users.sql",
    "specialty.sql",
    "chefs.sql",
    "reservations.sql",
    "general_ledger.sql"
]

def get_sql_files():
    """
    Obtiene los archivos SQL en el orden específico, excluyendo los definidos en EXCLUDED_FILES.

    :return: Lista de archivos SQL filtrados y ordenados.
    """
    # Filtrar los archivos .sql excluyendo el drop_all_tables.sql
    sql_files = [file for file in SQL_FILES_IN_ORDER if os.path.exists(os.path.join(SQL_DIRECTORY, file))]

    return sql_files

def execute_sql_file(cur, file_path):
    """
    Ejecuta el contenido del archivo SQL en el cursor proporcionado.

    :param cur: Cursor de base de datos.
    :param file_path: Ruta del archivo SQL.
    """
    with open(file_path, "r") as sql_file:
        content = sql_file.read()
        print(f"Executing SQL from: {file_path}")
        cur.execute(content)
        print(f"Successfully executed queries from {file_path}")

def execute_all_sql_files(conn):
    """
    Ejecuta todos los archivos SQL en el directorio, excluyendo el archivo drop_all_tables.sql,
    en el orden especificado en SQL_FILES_IN_ORDER.

    :param conn: Conexión activa a la base de datos.
    """
    cur = conn.cursor()

    try:
        # Obtener los archivos SQL en el orden especificado
        sql_files = get_sql_files()
        print(sql_files)

        # Ejecutar los archivos SQL en el orden especificado
        for sql_file in sql_files:
            print(sql_file)
            file_path = os.path.join(SQL_DIRECTORY, sql_file)
            execute_sql_file(cur, file_path)

        # Confirmar los cambios después de ejecutar todos los archivos
        conn.commit()

    except Exception as e:
        print(f"❌ Error executing SQL files: {e}")
        conn.rollback()  # Deshacer cambios en caso de error
    finally:
        cur.close()

def main():
    # Obtener la conexión a la base de datos
    conn = connect_to_database()

    if conn:
        try:
            execute_all_sql_files(conn)
            print("All SQL scripts executed successfully.")
        except Exception as e:
            print(f"❌ Error executing SQL scripts: {e}")
        finally:
            conn.close()

if __name__ == "__main__":
    main()