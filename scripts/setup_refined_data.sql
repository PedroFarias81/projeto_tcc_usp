SELECT
	TP_FAIXA_ETARIA,
	TP_SEXO,
	TP_ESTADO_CIVIL,
	TP_COR_RACA,
	TP_NACIONALIDADE,
	TP_ST_CONCLUSAO,
	TP_ANO_CONCLUIU,
	TP_ESCOLA,
    TP_ENSINO,
    IN_TREINEIRO,
	TP_DEPENDENCIA_ADM_ESC,
	TP_LOCALIZACAO_ESC,
	TP_SIT_FUNC_ESC,
	NU_NOTA_CN,
    NU_NOTA_CH,
    NU_NOTA_LC,
    NU_NOTA_MT,
    TP_LINGUA,
    TP_STATUS_REDACAO,
    NU_NOTA_REDACAO,
    Q001,
    Q002,
    Q003,
    Q004,
    Q005,
    Q006,
    Q007,
    Q008,
    Q009,
    Q010,
    Q011,
    Q012,
    Q013,
    Q014,
    Q015,
    Q016,
    Q017,
    Q018,
    Q019,
    Q020,
    Q021,
    Q022,
    Q023,
    Q024,
    Q025
FROM
	raw_data_2022
WHERE
	NU_NOTA_REDACAO NOTNULL
	AND SG_UF_PROVA = "MA"