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