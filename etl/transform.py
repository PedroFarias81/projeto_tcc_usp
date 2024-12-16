import pandas as pd
from etl.load import *

def create_new_table(database_path: str, sql_script: str, table_name: str):
    """
    _summary_
    """
    conn = create_connection(database_path)

    setup_sql_script = read_sql_script(sql_script)
    states_table = pd.read_sql(setup_sql_script, conn)

    #Salvar consulta na base de dados
    save_to_database(table_name, states_table, conn)

def transform_raw_data(table_name: str, database_path: str):
    """
    _summary_
    """
    create_new_table(database_path, "scripts/setup_refined_data.sql", table_name)