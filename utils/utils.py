import re

def confure_setup_sql_script(year: str):
    """_summary_

    Args:
        year (str): _description_
    """
    caminho_arquivo = 'scripts/setup_raw_data.sql'

    # A nova string para substituir a encontrada
    nova_string = f'raw_data_{year}'

    # Expressão regular para encontrar 'raw_data_' seguido de 4 dígitos
    padrao = r'raw_data_\d{4}'

    # Abrir o arquivo para leitura
    with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
        conteudo = arquivo.read()

    # Substituir todas as ocorrências que correspondem ao padrão
    conteudo_modificado = re.sub(padrao, nova_string, conteudo)

    # Abrir o arquivo novamente para escrita e salvar o conteúdo modificado
    with open(caminho_arquivo, 'w', encoding='utf-8') as arquivo:
        arquivo.write(conteudo_modificado)

    print("Substituição realizada com sucesso!")

def configure_global_variables(year: str) -> dict:
    """_summary_

    Args:
        year (str): _description_
    """
    #Renomear as variáveis para o ano vigente
    confure_setup_sql_script(year)

    return {
        "URL": f"https://download.inep.gov.br/microdados/microdados_enem_{year}.zip",
        "ZIP_FILE_NAME": f"microdados_enem_{year}.zip",
        "CSV_FILE_NAME": f"database/DADOS/MICRODADOS_ENEM_{year}.csv",
        "RAW_TABLE_NAME": f"raw_data_{year}",
        "EXTRACT_TO_PATH": "database",
        "DATABASE_PATH": "database/microdata_enem.db"
    }