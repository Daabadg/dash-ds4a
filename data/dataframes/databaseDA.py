import requests
import mysql.connector
import pandas as pd
from mysql.connector.constants import ClientFlag
from mysql.connector import Error

config = {
    'user': 'DS4A',
    'password': 'PatataAlpina',
    'host': '34.95.201.38',
    'client_flags': [ClientFlag.SSL],
    
    'database': 'DS4A'
}
conn = mysql.connector.connect(**config)

listaPartidos = pd.read_sql_query("""
SELECT * FROM DATA_SENADORES_PARTIDO_EXPORT 
""",conn)

conteoProcesos = pd.read_sql_query("""
SELECT * FROM VW_PERSON_CONTEO_DE_PROCESOS
""",conn)

depPartidos = pd.read_sql_query("""
SELECT * FROM VW_PARTIDO_DEPARTAMENTO_CONTEO_DE_CASOS
""",conn)
depPartidos = depPartidos.rename(columns={"CODIGO_DEPARTAMENTO":"COD_DPTO"})
depPartidos['COUNT'] = depPartidos['CANTIDAD_PROCESOS_PUBLICOS']+depPartidos['CANTIDAD_PROCESOS_PRIVADOS']

