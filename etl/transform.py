import pandas as pd
import zipfile
import shutil
import os

def extract_zip_content(file_name: str, extract_to='.') -> None:
    """
    Função responsável por extrair o arquivo .zip do arquivo e extrair 
    para o caminho atual da pasta ou um caminho especificado

    Args:
        file_name (str): Nome do arquivo .zip a ser extraído
        extract_to (str, optional): Caminho do arquivo a ser saldo o arquivo unzip. Defaults to '.'.
    """
    print(f"Extraindo arquivos para o caminho: {extract_to}")

    with zipfile.ZipFile(file_name, 'r') as zip_ref:
        zip_ref.extractall(extract_to)

    print(f"Arquivos extraídos!")

    os.remove(file_name)
    print("Arquivo zip removido após a extração")

def remove_unecessary_files(extract_to: str) -> None:
    """
    """
    important_files = ["DADOS", "DICIONÁRIO"]
    folders = [folder for folder in os.listdir(extract_to) if not folder.endswith(".db")]

    for folder in folders:
        if folder not in important_files:
            shutil.rmtree(extract_to+'/'+folder)
            print(f"Removido a pasta {folder}")

def transform_raw_data(file_name: str, extract_to: str):
    """
    _summary_
    """
    extract_zip_content(file_name, extract_to)
    remove_unecessary_files(extract_to)