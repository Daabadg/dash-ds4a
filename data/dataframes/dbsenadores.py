import pandas as pd


infoSenadores = pd.read_csv(r'assets\csv\SENADORES_PARTIDOS.csv',encoding='utf8')
infoSenadores = infoSenadores.rename(columns={'Fecha Nac. (DD-MM-AAAA)':'Fecha Nacimiento','Información ':'Descripcion'})
#infoSenadores = infoSenadores.dropna()
infoSenadores['Fecha Nacimiento'] = pd.to_datetime(infoSenadores['Fecha Nacimiento'],format='%d/%m/%Y',errors='coerce');
infoSenadores['Edad'] = 2022 - infoSenadores['Fecha Nacimiento'].dt.year