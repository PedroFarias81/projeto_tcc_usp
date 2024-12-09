import pandas as pd
import sqlite3

def create_connection(db_name: str) -> sqlite3.Connection:
    """
    Função responsável por criar a conexão com banco de dados sqlite3

    Args:
        db_name (str): Nome do banco a ser criado a conexão

    Returns:
        sqlite3.Connection: Objeto de conexão do banco de dados
    """
    conn = sqlite3.connect(db_name)
    return conn

def read_sql_script(filename: str) -> str:
    """
    Função responsável por ler um script local e rodar no banco
    de dados

    Args:
        filename (str): Caminho do arquivo sql a ser lido

    Returns:
        str: string contendo o conteúdo do script sql
    """
    with open(filename, 'r') as file:
        sql_script = file.read()
    
    return sql_script

def setup_database(conn: sqlite3.Connection, sql_script: str) -> None:
    """
    Alguma Docstring
    """
    cursor = conn.cursor()
    cursor.executescript(sql_script)

def save_to_database(db_name: str, chunk: pd.DataFrame, conn: sqlite3.Connection) -> None:
    """
    Alguma docstring
    """
    chunk.to_sql(db_name, conn, if_exists='append', index=False)


if __name__ == "__main__":

    #Criando a conexão com o banco de dados
    conn = create_connection("../../database/microdata_enem_2023.db")
    db_name = "microdata_enem"

    #Configurando a conexão e criando o banco de dados do zero
    setup_sql_script = read_sql_script("../sql/setup_database.sql")
    setup_database(conn, setup_sql_script)

    #Definindo o tamanho de cada pedaço que vai ser lido do dataframe
    chunksize = 10 ** 5
    filename = '../../microdados_enem_2023/DADOS/MICRODADOS_ENEM_2023.csv'
    indice = 1

    for chunk in pd.read_csv(filename, chunksize=chunksize, sep=";", encoding="latin1", dtype=str):
        chunk.drop(
            [
                "NU_INSCRICAO", 
                "NU_ANO",
                "CO_MUNICIPIO_ESC",
                "CO_UF_ESC",
                "CO_MUNICIPIO_PROVA",
                "CO_UF_PROVA",
                "TX_RESPOSTAS_CN",
                "TX_RESPOSTAS_CH",
                "TX_RESPOSTAS_LC",
                "TX_RESPOSTAS_MT",
                "TX_GABARITO_CN",
                "TX_GABARITO_CH",
                "TX_GABARITO_LC",
                "TX_GABARITO_MT"
            ], 
            axis=1, 
            inplace=True
        )
        print("Salvando os dados do CSV para o banco de dados...")
        save_to_database(db_name, chunk, conn)