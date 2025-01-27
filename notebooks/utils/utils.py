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

def load_data_by_year(year: str) -> str:
    """_summary_

    Args:
        year (str): _description_

    Returns:
        str: _description_
    """
    #Criando a conexão com o banco de dados criado
    conn = create_connection("../database/microdata_enem.db")

    #Selecionando apenas os dados de estudantes maranhenses e com nota não nula na redação
    query = f"SELECT * FROM raw_data_{year}"
    df = pd.read_sql(query, conn)

    return df

def clean_raw_data(df: pd.DataFrame) -> pd.DataFrame:
    """_summary_

    Args:
        df (pd.DataFrame): _description_

    Returns:
        pd.DataFrame: _description_
    """

    #Descartando as variáveis não importantes para o problema:
    variaveis_nao_importantes = [
        "NU_INSCRICAO",
        "NO_MUNICIPIO_ESC",
        "NO_MUNICIPIO_PROVA",
        "SG_UF_ESC",
        "SG_UF_PROVA",
        "NU_NOTA_COMP1",
        "NU_NOTA_COMP2",
        "NU_NOTA_COMP3",
        "NU_NOTA_COMP4",
        "NU_NOTA_COMP5",
    ]

    #Selecionando as variáveis numéricas para tratamento diferente das colunas restantes
    variaveis_numericas = [
        "NU_NOTA_CN",
        "NU_NOTA_CH",
        "NU_NOTA_LC",
        "NU_NOTA_MT",
        "NU_NOTA_REDACAO"
    ]

    #Utilizando apendas as variáveis categóricas relacionados a dados da escola ou dados demográficos
    variaveis_categoricas = [coluna for coluna in df.columns if (coluna not in variaveis_nao_importantes) and (coluna not in variaveis_numericas)]

    #Transformando as colunas para o seu tipo original
    for coluna in variaveis_categoricas:
        df[coluna] = df[coluna].astype('category')

    for coluna in variaveis_numericas:
        df[coluna] = df[coluna].astype(float)
    
    #Pegando apenas as colunas necessárias para a criação do modelo
    df = df[variaveis_categoricas + variaveis_numericas].reset_index(drop=True)
    
    #Removendo todos os registros que contem ao menos um valor nulo
    df = df.dropna()

    # Removendo todas as redações zeradas (Ainda em observação...)
    df = df.loc[df.NU_NOTA_MT > 0, :]

    return df.reset_index(drop=True)
