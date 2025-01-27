from etl.extract import extract_raw_data
from etl.load import load_raw_data
from etl.transform import transform_raw_data
from utils.utils import configure_global_variables

if __name__ == "__main__":
    #Renomear os dados para o ano
    YEAR = "2022"
    global_variables = configure_global_variables(YEAR)

    #Extraindo os dados da fonte original INEP
    print("-----Extração dos Dados-----")
    extract_raw_data(global_variables["URL"], global_variables["ZIP_FILE_NAME"])

    #Otimizando a base de dados carregada
    print("-----Transformação dos Dados-----")
    transform_raw_data(global_variables["ZIP_FILE_NAME"], global_variables["EXTRACT_TO_PATH"])

    #Carregando os dados originais para o banco de dados local
    print("-----Carregamento dos Dados-----")
    load_raw_data(global_variables["CSV_FILE_NAME"], global_variables["RAW_TABLE_NAME"], global_variables["DATABASE_PATH"])
