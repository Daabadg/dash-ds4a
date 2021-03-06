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

personaProcesosTipo = pd.read_sql_query("""
SELECT * FROM VW_PERSONA_PROCESO_TIPO_SUJETO
""",conn)


personaProcesosDepartamento = pd.read_sql_query("""
SELECT	* FROM 	VW_SENADORES_DEPARTAMENTO_CONTEO_DE_CASOS;
""",conn)

personProcesoDetails = pd.read_sql_query("""
SELECT	* FROM 	VW_PERSON_PROCESO_DETAILS;
""",conn)

partidoProcesoFecha = pd.read_sql_query("""
SELECT * FROM VW_PARTIDO_CASOS_BY_YEAR_MONTH;
""",conn)

