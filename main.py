from etl.extract import extract_raw_data
from etl.load import load_raw_data
from etl.transform import transform_raw_data

URL = "https://download.inep.gov.br/microdados/microdados_enem_2022.zip"
ZIP_FILE_NAME = "microdados_enem_2022.zip"
EXTRACT_TO_PATH = "database"
CSV_FILENAME = 'database/DADOS/MICRODADOS_ENEM_2022.csv'
RAW_TABLE_NAME = "raw_data_2022"
REFINED_TABLE_NAME = "refined_data_2022"
DATABASE_PATH = "database/microdata_enem.db"

if __name__ == "__main__":
    #Extraindo os dados da fonte original INEP
    extract_raw_data(URL, ZIP_FILE_NAME, EXTRACT_TO_PATH)

    #Carregando os dados originais para o banco de dados local
    load_raw_data(CSV_FILENAME, RAW_TABLE_NAME, DATABASE_PATH)

    #Otimizando a base de dados carregada
    transform_raw_data(REFINED_TABLE_NAME, DATABASE_PATH)