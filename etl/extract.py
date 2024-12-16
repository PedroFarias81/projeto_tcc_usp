import requests
import os
import time
import shutil
import zipfile

max_retries = 5

def download_zip(url: str, file_name: str) -> None:
    """
    Função responsável por realizar o download de um arquivo zip usando a 
    biblioteca requests e salvar o zip com um nome especificado

    Args:
        url (str): URL do arquivo a ser baixado
        file_name (str): Nome do arquivo a ser reescrito
    """
    for attempt in range(max_retries):
        try:
            print("Iniciado o download do arquivo, espere um pouco...")
            response = requests.get(url)
            
            with open(file_name, 'wb') as output_file:
                binary_data = response.content.decode('latin1')
                binary_data = binary_data.encode('latin1')
                output_file.write(binary_data)

            print("Download concluído!")
            break
            
        except requests.exceptions.ConnectionError as e:
            print(f"Tentativa {attempt + 1} falhou: {e}")
            time.sleep(2)

        except requests.exceptions.HTTPError as e:
            print(f"Erro HTTP {e}")
    
def extract_zip(file_name: str, extract_to='.') -> None:
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
    important_files = ["DADOS", "DICION╡RIO"]
    folders = [folder for folder in os.listdir(extract_to) if not folder.endswith(".db")]

    for folder in folders:
        if folder not in important_files:
            shutil.rmtree(extract_to+'/'+folder)
            print(f"Removido a pasta {folder}")

def extract_raw_data(url: str, file_name: str, extract_to: str) -> None:
    """_summary_

    Args:
        url (str): _description_
        file_name (str): _description_
        extract_to (str): _description_
    """
    download_zip(url, file_name)
    extract_zip(file_name, extract_to)
    remove_unecessary_files(extract_to)