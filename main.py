import pandas as pd
from datetime import datetime
import pandas as pd
import pyodbc 

server = 'localhost' # Substitua pelo nome do servidor SQL Server
database = 'AdventureWorksDW2019'  # Substitua pelo nome do banco de dados
conexaoDB = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                      f'SERVER={server};'
                      f'DATABASE={database};'
                      'Trusted_Connection=yes;')

cursor = conexaoDB.cursor()   # criando cursor de comando 

import pandas as pd
from datetime import datetime

# Minha query
query = "SELECT * FROM DimProduct"

# lê direto para um DataFrame
df = pd.read_sql(query, conexaoDB)

# gera a data no formato YYYYMMDD
data_atual = datetime.now().strftime("%Y%m%d")

# caminho com data no nome
caminho = fr"C:\Users\Bruno\Desktop\projetos_engenharia\teste_automacao_python\resultado_query_{data_atual}.csv"

# salva em CSV
df.to_csv(caminho, index=False, encoding="utf-8-sig")

print(f"CSV gerado com sucesso em: {caminho}")
