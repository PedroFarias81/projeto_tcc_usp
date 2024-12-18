CREATE TABLE IF NOT EXISTS raw_data_2023 (
    NU_INSCRICAO VARCHAR(12),           -- Numero da Inscrição do Enem
    TP_FAIXA_ETARIA VARCHAR(2),         -- Faixa etária 
    TP_SEXO VARCHAR(1),                 -- Sexo
    TP_ESTADO_CIVIL VARCHAR(1),         -- Estado Civil
    TP_COR_RACA VARCHAR(1),             -- Cor/Raça
    TP_NACIONALIDADE VARCHAR(1),        -- Nacionalidade
    TP_ST_CONCLUSAO VARCHAR(1),         -- Situação de conclusão do Ensino Médio
    TP_ANO_CONCLUIU VARCHAR(2),         -- Ano de Conclusão do Ensino Médio
    TP_ESCOLA VARCHAR(1),               -- Tipo de escola do Ensino Médio
    TP_ENSINO VARCHAR(1),               -- Tipo de instituição que concluiu ou concluirá o Ensino Médio
    IN_TREINEIRO VARCHAR(1),            -- Indica se o inscrito fez a prova com intuito de apenas treinar seus conhecimentos
    NO_MUNICIPIO_ESC VARCHAR(150),      -- Nome do município da escola
    SG_UF_ESC VARCHAR(2),               -- Sigla da Unidade da Federação da escola
    TP_DEPENDENCIA_ADM_ESC VARCHAR(1),  -- Dependência administrativa (Escola)
    TP_LOCALIZACAO_ESC VARCHAR(1),      -- Localização (Escola)
    TP_SIT_FUNC_ESC VARCHAR(1),         -- Situação de funcionamento (Escola)
    NO_MUNICIPIO_PROVA VARCHAR(150),    -- Nome do município da aplicação da prova
    SG_UF_PROVA VARCHAR(2),             -- Sigla da Unidade da Federação da aplicação da prova
    CO_MUNICIPIO_ESC VARCHAR(7),        -- Código do Município da Escola
    CO_UF_ESC VARCHAR(2),               -- Código da Sigla da Escola
    CO_MUNICIPIO_PROVA VARCHAR(7),      -- Código do Municipio do Local de Prova 
    CO_UF_PROVA VARCHAR(2),             -- Código da Sigla do Local de Prova
    NU_NOTA_CN DECIMAL(4, 2),           -- Nota da prova de Ciências da Natureza
    NU_NOTA_CH DECIMAL(4, 2),           -- Nota da prova de Ciências Humanas
    NU_NOTA_LC DECIMAL(4, 2),           -- Nota da prova de Linguagens e Códigos
    NU_NOTA_MT DECIMAL(4, 2),           -- Nota da prova de Matemática
    TP_LINGUA VARCHAR(1),               -- Língua Estrangeira
    TP_STATUS_REDACAO VARCHAR(1),       -- Situação da redação do participante
    NU_NOTA_COMP1 NUMERIC,              -- Nota da competência 1 - Demonstrar domínio da modalidade escrita formal da Língua Portuguesa.
    NU_NOTA_COMP2 NUMERIC,              -- Nota da competência 2 - Compreender a proposta de redação e aplicar conceitos das várias áreas de conhecimento para desenvolver o tema, dentro dos limites estruturais do texto dissertativo-argumentativo em prosa.
    NU_NOTA_COMP3 NUMERIC,              -- Nota da competência 3 - Selecionar, relacionar, organizar e interpretar informações, fatos, opiniões e argumentos em defesa de um ponto de vista.
    NU_NOTA_COMP4 NUMERIC,              -- Nota da competência 4 - Demonstrar conhecimento dos mecanismos linguísticos necessários para a construção da argumentação.
    NU_NOTA_COMP5 NUMERIC,              -- Nota da competência 5 - Elaborar proposta de intervenção para o problema abordado, respeitando os direitos humanos.
    NU_NOTA_REDACAO NUMERIC,            -- Nota da prova de redação
    Q001 VARCHAR (1),                   -- Até que série seu pai, ou o homem responsável por você, estudou?
    Q002 VARCHAR (1),                   -- Até que série sua mãe, ou a mulher responsável por você, estudou?
    Q003 VARCHAR (1),                   -- Grupo que contempla a ocupação mais próxima da ocupação do seu pai ou do homem responsável por você.
    Q004 VARCHAR (1),                   -- Grupo que contempla a ocupação mais próxima da ocupação do sua mãe ou da mulher responsável por você.
    Q005 VARCHAR (2),                   -- Incluindo você, quantas pessoas moram atualmente em sua residência?
    Q006 VARCHAR (1),                   -- Qual é a renda mensal de sua família? (Some a sua renda com a dos seus familiares.)
    Q007 VARCHAR (1),                   -- Em sua residência trabalha empregado(a) doméstico(a)?
    Q008 VARCHAR (1),                   -- Na sua residência tem banheiro?
    Q009 VARCHAR (1),                   -- Na sua residência tem quartos para dormir?
    Q010 VARCHAR (1),                   -- Na sua residência tem carro?
    Q011 VARCHAR (1),                   -- Na sua residência tem motocicleta?
    Q012 VARCHAR (1),                   -- Na sua residência tem geladeira?
    Q013 VARCHAR (1),                   -- Na sua residência tem freezer (independente ou segunda porta da geladeira)?
    Q014 VARCHAR (1),                   -- Na sua residência tem máquina de lavar roupa? (o tanquinho NÃO deve ser considerado)
    Q015 VARCHAR (1),                   -- Na sua residência tem máquina de secar roupa (independente ou em conjunto com a máquina de lavar roupa)?
    Q016 VARCHAR (1),                   -- Na sua residência tem forno micro-ondas?
    Q017 VARCHAR (1),                   -- Na sua residência tem máquina de lavar louça?
    Q018 VARCHAR (1),                   -- Na sua residência tem aspirador de pó?
    Q019 VARCHAR (1),                   -- Na sua residência tem televisão em cores?
    Q020 VARCHAR (1),                   -- Na sua residência tem aparelho de DVD?
    Q021 VARCHAR (1),                   -- Na sua residência tem TV por assinatura?
    Q022 VARCHAR (1),                   -- Na sua residência tem telefone celular?
    Q023 VARCHAR (1),                   -- Na sua residência tem telefone fixo?
    Q024 VARCHAR (1),                   -- Na sua residência tem computador?
    Q025 VARCHAR (1)                    -- Na sua residência tem acesso à Internet?
)