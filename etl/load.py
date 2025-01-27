import pandas as pd
import sqlite3
import shutil

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
    Função responsável por montar o schema da base de dados que será usada com
    base em um script sql. 

    Args:
        conn (sqlite3.Connection): Conexão com o sqlite3
        sql_script (str): Arquivo contendo o script sql que configura o setup do banco de dados
    """
    cursor = conn.cursor()
    cursor.executescript(sql_script)

def save_to_database(db_name: str, chunk: pd.DataFrame, conn: sqlite3.Connection) -> None:
    """
    Alguma docstring
    """
    chunk.to_sql(db_name, conn, if_exists='append', index=False)

def load_raw_data(filename: str, table_name: str, database_path: str) -> None:
     #Criando a conexão com o banco de dados
    conn = create_connection(database_path)

    #Configurando a conexão e criando o banco de dados do zero
    setup_sql_script = read_sql_script("scripts/setup_raw_data.sql")
    setup_database(conn, setup_sql_script)

    #Definindo o tamanho de cada pedaço que vai ser lido do dataframe
    chunksize = 10 ** 5
    print("Salvando os dados do CSV para o banco de dados...")

    for chunk in pd.read_csv(filename, chunksize=chunksize, sep=";", encoding="latin1", dtype=str):
        #Removendo colunas desnecessárias para qualquer análise futura
        chunk.drop(
            [
                "NU_ANO",               # Ano da realização da Prova
                "CO_PROVA_CN",          # Código do tipo de prova de Ciências da Natureza
                "CO_PROVA_CH",          # Código do tipo de prova de Ciências Humanas
                "CO_PROVA_LC",          # Código do tipo de prova de Linguagens e Códigos
                "CO_PROVA_MT",          # Código do tipo de prova de Matemática
                "CO_MUNICIPIO_ESC",     # Código do Município da Escola
                "CO_UF_ESC",            # Código da Sigla da Escola
                "CO_MUNICIPIO_PROVA",   # Código do Municipio do Local de Prova 
                "CO_UF_PROVA",          # Código da Sigla do Local de Prova
                "TP_PRESENCA_CN",       # Presença na prova objetiva de Ciências da Natureza
                "TP_PRESENCA_CH",       # Presença na prova objetiva de Ciências Humanas
                "TP_PRESENCA_LC",       # Presença na prova objetiva de Linguagens e Códigos
                "TP_PRESENCA_MT",       # Presença na prova objetiva de Matemática
                "TX_RESPOSTAS_CN",      # Vetor com as respostas do aluno em Ciências da Natureza
                "TX_RESPOSTAS_CH",      # Vetor com as respostas do aluno em Ciências Humanas
                "TX_RESPOSTAS_LC",      # Vetor com as respostas do aluno em Linguagens e seus Códigos
                "TX_RESPOSTAS_MT",      # Vetor com as respostas do aluno em Matemática
                "TX_GABARITO_CN",       # Gabarito das questões de Ciências da Natureza
                "TX_GABARITO_CH",       # Gabarito das questões de Ciências da Natureza
                "TX_GABARITO_LC",       # Gabarito das questões de Ciências da Natureza
                "TX_GABARITO_MT"        # Gabarito das questões de Ciências da Natureza
            ], 
            axis=1, 
            inplace=True
        )

        #Permanecer apenas com dados do MA e com dados que tenham a nota de matemática válidas
        chunk = chunk[
            ((chunk["SG_UF_PROVA"] == "MA") | (chunk["SG_UF_ESC"] == "MA")) & (chunk["NU_NOTA_MT"].notna())
        ]

        #Salvar o arquivo no banco de dados
        save_to_database(table_name, chunk, conn)

    print("Dados armazenados dentro do banco de dados!")
    
    #Excluindo a base CSV após o carregamento dos dados no banco de dados
    shutil.rmtree("database/DADOS")
    print("Dados originais CSV removidos.")