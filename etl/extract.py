import requests
import time

max_retries = 5

def extract_raw_data(url: str, file_name: str) -> None:
    """
    Função responsável por realizar o download de um arquivo zip usando a 
    biblioteca requests e salvar o zip com um nome especificado.

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