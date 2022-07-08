#pip install pip install mysql-connector-python
import requests
import mysql.connector
from mysql.connector.constants import ClientFlag

config = {
    'user': 'DS4A',
    'password': 'PatataAlpina',
    'host': '34.95.201.38',
    'client_flags': [ClientFlag.SSL],
    'ssl_ca': 'ssl/server-ca.pem',
    'ssl_cert': 'ssl/client-cert.pem',
    'ssl_key': 'ssl/client-key.pem',
    'database': 'DS4A'
}

QUERY_CONSTANTS = {
    'CONNECTION': None,
    'SENATORS': [
        'ALVARO URIBE VELEZ VELEZ',
        'IVAN DUQUE MARQUEZ',
        'GUSTAVO BOLIVAR MORENO',
        'MARIA JOSE PIZARRO RODRIGUEZ',
        'ALEXANDER LOPEZ MAYA',
        'IDA YOLANDA AVELLA ESQUIVEL',
        'ROY LEONARDO BARRERAS MONTEALEGRE',
        'MARTHA ISABEL PERALTA EPIEYU',
        'IVAN CEPEDA CASTRO',
        'PIEDAD ESNEDA CORDOBA RUIZ',
        'PEDRO HERNANDO FLOREZ PORRAS',
        'ISABEL CRISTINA ZULETA LOPEZ',
        'ALEX XAVIER FLOREZ HERNANDEZ',
        'CLARA EUGENIA LOPEZ OBREGON',
        'ROBERT DAZA GUEVARA',
        'YULY ESMERALDA HERNANDEZ SILVA',
        'WILSON NEBER ARIAS CASTILLO',
        'GLORIA INES FLOREZ SCHNEIDER',
        'NADYA GEORGETTE BLEL SCAFF',
        'CARLOS ANDRES TRUJILLO GONZALEZ',
        'MARCOS DANIEL PINEDA GARCIA',
        'EFRAIN JOSE CEPEDA SARABIA',
        'LILIANA ESTHER BITAR CASTILLA',
        'OSCAR BARRETO QUIROGA',
        'DIELA LILIANA BENAVIDES SOLARTE',
        'OSCAR MAURICIO GIRALDO HERNANDEZ',
        'NICOLAS ALBEIRO ECHEVERRY ALVARAN',
        'JUAN SAMY MERHEG MARUN',
        'GERMAN ALCIDES BLANCO ALVAREZ',
        'JUAN CARLOS GARCIA GOMEZ',
        'JOSE ALFREDO MARIN LOZANO',
        'MIGUEL ANGEL BARRETO CASTILLO',
        'SOLEDAD TAMAYO TAMAYO',
        'ESPERANZA ANDRADE SERRANO',
        'LIDIO ARTURO GARCIA TURBAY',
        'JUAN PABLO GALLO MAYA',
        'KARINA ESPINOSA OLIVER',
        'ALEJANDRO CARLOS CHACON CAMARGO',
        'FABIO RAUL AMIN SALEME',
        'MIGUEL ANGEL PINTO HERNANDEZ',
        'CLAUDIA MARIA PEREZ GIRALDO',
        'ALEJANDRO ALBERTO VEGA PEREZ',
        'JUAN DIEGO ECHAVARRIA SANCHEZ',
        'JAIME ENRIQUE DURAN BARRERA',
        'JOHN JAIRO ROLDAN AVENDAÑO',
        'MAURICIO GOMEZ AMIN',
        'MARIO ALBERTO CASTAÑO PEREZ',
        'LAURA ESTER FORTICH SANCHEZ',
        'SARA JIMENA CASTELLANOS RODRIGUEZ',
        'JONATHAN FERNEY PULIDO HERNANDEZ',
        'HUMBERTO DE LA CALLE LOMBANA',
        'ARIEL FERNANDO AVILA MARTINEZ',
        'ANGELICA LISBETH LOZANO CORREA',
        'INTI RAUL ASPRILLA REYES',
        'JAIRO ALBERTO CASTELLANOS SERRANO',
        'ANA CAROLINA ESPITIA JEREZ',
        'GUIDO ECHEVERRI PIEDRAHITA',
        'ANDREA PADILLA VILLARRAGA',
        'EDWING FABIAN DIAZ PLATA',
        'GUSTAVO ADOLFO MORENO HURTADO',
        'SOR BERENICE BEDOYA PEREZ',
        'IVAN LEONIDAS NAME VASQUEZ',
        'LEON FREDY MUÑOZ LOPERA',
        'MIGUEL URIBE TURBAY',
        'MARIA FERNANDA CABAL MOLINA',
        'JOSUE ALIRIO BARRERA RODRIGUEZ',
        'ANDRES FELIPE GUERRA HOYOS',
        'ESTEBAN QUINTERO CARDONA',
        'PAOLA ANDREA HOLGUIN MORENO',
        'PALOMA SUSANA VALENCIA LASERNA',
        'ENRIQUE CABRALES BAQUERO',
        'CARLOS MANUEL MEISEL VERGARA',
        'CIRO ALEJANDRO RAMIREZ CORTES',
        'JOSE VICENTE CARREÑO CASTRO',
        'HONORIO MIGUEL HENRIQUEZ PINEDO',
        'YENNY ESPERANZA ROZO ZAMBRANO',
        'MARIA ANGELICA GUERRA LOPEZ',
        'DAVID ANDRES LUNA SANCHEZ',
        'ARTURO CHAR CHALJUB',
        'ANTONIO LUIS ZABARAIN GUEVARA',
        'CARLOS ABRAHAM JIMENEZ LOPEZ',
        'EDGAR JESUS DIAZ CONTRERAS',
        'CARLOS MARIO FARELO DAZA',
        'JORGE ENRIQUE BENEDETTI MARTELO',
        'ANA MARIA CASTAÑEDA GOMEZ',
        'CARLOS FERNANDO MOTOA SOLARTE',
        'JOSE LUIS PEREZ OYUELA',
        'DIDIER LOBO CHINCHILLA',
        'JUAN CARLOS GARCES ROJAS',
        'JOHN MOISES BESAILE FAYAD',
        'NORMA HURTADO SANCHEZ',
        'JOSE DAVID NAME CARDOZO',
        'JUAN FELIPE LEMOS URIBE',
        'JULIO ELIAS CHAGUI FLOREZ',
        'ALFREDO RAFAEL DELUQUE ZULETA',
        'BERNER LEON ZAMBRANO ERASO',
        'JOSE ALFREDO GNECCO ZULETA',
        'ANTONIO JOSE CORREA JIMENEZ',
        'BEATRIZ LORENA RIOS CUELLAR',
        'CARLOS EDUARDO GUEVARA VILLABON',
        'ANA PAOLA AGUDELO GARCIA',
        'MANUEL ANTONIO VIRGUEZ PIRAQUIVE',
        'AIDA MARINA QUILCUE VIVAS',
        'POLIVIO LEANDRO ROSALES CADENA',
        'GUSTAVO FRANCISCO PETRO URREGO',
        'RODOLFO HERNÁNDEZ SUÁREZ'
    ],
    'SELECT': {
        'TB_PERSON PENDING': 'SELECT * FROM TB_PERSON WHERE PERSON_STATUS = 0',
        'TB_PERSON PENDING COUNT': 'SELECT COUNT(1) FROM TB_PERSON WHERE PERSON_STATUS = 0',
        'TB_RAW_PROCCESS EXISTS': 'SELECT 1 FROM TB_RAW_PROCESS WHERE ID_PROCESO = %s',
        'TB_RAW_PROCCESS PENDING': 'SELECT * FROM TB_RAW_PROCESS WHERE ES_PRIVADO = 0 AND PROCESS_STATUS = 0',
        'TB_RAW_PROCESSS PENDING COUNT': 'SELECT COUNT(1) FROM TB_RAW_PROCESS WHERE PROCESS_STATUS = 0 AND ES_PRIVADO = 0',
        'TB_SUJETO EXISTS': 'SELECT COUNT(1) FROM TB_SUJETOS_PROCESALES WHERE ID_PROCESO = %s AND ID_REG_SUJETO = %s'
    },
    'INSERT': {
        'TB_PERSON': "INSERT INTO TB_PERSON (PERSON_NAME, PERSON_STATUS) VALUES (%s, %s)",
        'TB_RAW_PROCESS': "INSERT INTO TB_RAW_PROCESS (ID_PROCESO, ID_CONEXION, LLAVE_PROCESO, FECHA_PROCESO, " + \
            "FECHA_ULTIMA_ACTUACION, DESPACHO, DEPARTAMENTO, SUJETOS_PROCESALES, ES_PRIVADO, CANT_FILAS, PROCESS_STATUS) " + \
            "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
        'TB_SUJETO_PROCESAL': 'INSERT INTO TB_SUJETOS_PROCESALES (ID_PROCESO, ID_REG_SUJETO, TIPO_SUJETO, ES_EMPLAZADO, ' + \
            'IDENTIFICACION, NOMBRE_RAZON_SOCIAL, CANT) VALUES (%s, %s, %s, %s, %s, %s, %s)',
        'TB_PERSON_PROCESO': 'INSERT INTO TB_PERSON_PROCESO (PERSON_ID, ID_PROCESO, LLAVE_PROCESO) VALUES (%s, %s, %s)',
        'TB_PROCESS_DETAIL': 'INSERT INTO TB_DETAILS_PROCESS (ID_PROCESO,LLAVE_PROCESO,ID_CONEXION,ES_PRIVADO, ' + \
            'FECHA_PROCESO,DESPACHO,PONENTE,TIPO_PROCESO,CLASE_PROCESO,SUB_CLASE_PROCESO,RECURSO,UBICACION, ' \
            'CONTENIDO_RADICACION,FECHA_CONSULTA,ULTIMA_ACTUALIZACION) VALUES (%s,%s,%s,%s, ' + \
            '%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
        'TB_ACTUACION': 'INSERT INTO TB_ACTUACION (ID_PROCESO,ID_ACTUACION,LLAVE_PROCESO,CONS_ACTUACION,FECHA_ACTUACION, ' + \
            'ACTUACION,ANOTACION,FECHA_INICIAL,FECHA_FINAL,FECHA_REGISTRO,COD_REGLA,TIENE_DOCUMENTOS,CANT) ' + \
            'VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'
    },
    'UPDATE': {
        'TB_PERSON UPD_STATUS': "UPDATE TB_PERSON SET PERSON_STATUS = %s WHERE PERSON_ID = %s",
        'TB_RAW_PROCESS UPD_STATUS': "UPDATE TB_RAW_PROCESS SET PROCESS_STATUS = %s WHERE ID_PROCESO = %s "
    }
}

class DB_Manager():
    def __init__(self):
        None

    def exists_sujeto(self, iIdProceso, iIdRegSujeto):
        vCursor = QUERY_CONSTANTS['CONNECTION'].cursor()
        vCursor.execute(QUERY_CONSTANTS['SELECT']['TB_SUJETO EXISTS'], [iIdProceso, iIdRegSujeto])
        vResponse = vCursor.fetchone()
        return vResponse is not None
    
    def insert_sujeto_procesal(self,
        iIdProceso,
        iIdRegSujeto,
        iTipoSujero,
        iEsEmplazado,
        iIdentificacion,
        iNombreRazonSocial,
        iCant
    ):
        #if self.exists_sujeto(iIdProceso, iIdRegSujeto):
        #    return
        
        vCursor = QUERY_CONSTANTS['CONNECTION'].cursor()
        vCursor.execute(
            QUERY_CONSTANTS['INSERT']['TB_SUJETO_PROCESAL'],
            [   iIdProceso,
                iIdRegSujeto,
                iTipoSujero,
                iEsEmplazado,
                iIdentificacion,
                iNombreRazonSocial,
                iCant
            ]
        )
        QUERY_CONSTANTS['CONNECTION'].commit()

    def select_pending_process(self):
        vCursor = QUERY_CONSTANTS['CONNECTION'].cursor()
        vCursor.execute(QUERY_CONSTANTS['SELECT']['TB_RAW_PROCCESS PENDING'])
        vRows = vCursor.fetchall()
        return vRows
    
    def count_persons_pending(self):
        vCursor = QUERY_CONSTANTS['CONNECTION'].cursor()
        vCursor.execute(QUERY_CONSTANTS['SELECT']['TB_PERSON PENDING COUNT'])
        vCount = vCursor.fetchone()[0]
        return vCount

    def count_process_pending(self):
        vCursor = QUERY_CONSTANTS['CONNECTION'].cursor()
        vCursor.execute(QUERY_CONSTANTS['SELECT']['TB_RAW_PROCESSS PENDING COUNT'])
        vCount = vCursor.fetchone()[0]
        return vCount

    def exists_raw_process(self, iIdProceso):
        vCursor = QUERY_CONSTANTS['CONNECTION'].cursor()
        vCursor.execute(QUERY_CONSTANTS['SELECT']['TB_RAW_PROCCESS EXISTS'], [iIdProceso])
        vResponse = vCursor.fetchone()
        return vResponse is not None

    def select_persons_pending(self):
        vCursor = QUERY_CONSTANTS['CONNECTION'].cursor()
        vCursor.execute(QUERY_CONSTANTS['SELECT']['TB_PERSON PENDING'])
        vRows = vCursor.fetchall()
        return vRows

    def insert_person(self, iPersonName):
        vCursor = QUERY_CONSTANTS['CONNECTION'].cursor()
        vCursor.execute(
            QUERY_CONSTANTS['INSERT']['TB_PERSON'],
            [iPersonName, False]
        )
        QUERY_CONSTANTS['CONNECTION'].commit()

    def update_process_status(self, iIdProceso):
        vCursor = QUERY_CONSTANTS['CONNECTION'].cursor()
        vCursor.execute(
            QUERY_CONSTANTS['UPDATE']['TB_RAW_PROCESS UPD_STATUS'],
            [True, iIdProceso]
        )
        QUERY_CONSTANTS['CONNECTION'].commit()
    
    def update_person_status(self, iPersonId):
        vCursor = QUERY_CONSTANTS['CONNECTION'].cursor()
        vCursor.execute(
            QUERY_CONSTANTS['UPDATE']['TB_PERSON UPD_STATUS'],
            [True, iPersonId]
        )
        QUERY_CONSTANTS['CONNECTION'].commit()

    def insert_person_process(
        self,
        iIdPerson,
        iIdProceso,
        iLlaveProceso
    ):
        vCursor = QUERY_CONSTANTS['CONNECTION'].cursor()
        vCursor.execute(
            QUERY_CONSTANTS['INSERT']['TB_PERSON_PROCESO'],
            [iIdPerson, iIdProceso, iLlaveProceso]
        )
        QUERY_CONSTANTS['CONNECTION'].commit()

    def insert_detail_process(
        self,
        iIdProceso,
        iLlaveProceso,
        iIdConexion,
        iEsPrivado,
        iFechaProceso,
        iDespacho,
        iPonente,
        iTipoProceso,
        iClaseProceso,
        iSubClaseProceso,
        iRecurso,
        iUbicacion,
        iContenidoRadicacion,
        iFechaConsulta,
        iUltimaActualizacion
    ):
        vCursor = QUERY_CONSTANTS['CONNECTION'].cursor()
        vCursor.execute(
            QUERY_CONSTANTS['INSERT']['TB_PROCESS_DETAIL'],
            [   iIdProceso,
                iLlaveProceso,
                iIdConexion,
                iEsPrivado,
                iFechaProceso,
                iDespacho,
                iPonente,
                iTipoProceso,
                iClaseProceso,
                iSubClaseProceso,
                iRecurso,
                iUbicacion,
                iContenidoRadicacion,
                iFechaConsulta,
                iUltimaActualizacion
            ]
        )
        QUERY_CONSTANTS['CONNECTION'].commit()

    def insert_actuacion(
        self,
        iIdProceso,
        iIdActuacion,
        iLlaveProceso,
        iConsActuacion,
        iFechaActuacion,
        iActuacion,
        iAnotacion,
        iFechaInicial,
        iFechaFinal,
        iFechaRegistros,
        iCodRegla,
        iTieneDocumentos,
        iCant
    ):
        #print("\nQUERY: ", QUERY_CONSTANTS['INSERT']['TB_ACTUACION'])
        vCursor = QUERY_CONSTANTS['CONNECTION'].cursor()
        vCursor.execute(
            QUERY_CONSTANTS['INSERT']['TB_ACTUACION'],
            [   iIdProceso,
                iIdActuacion,
                iLlaveProceso,
                iConsActuacion,
                iFechaActuacion,
                iActuacion,
                iAnotacion,
                iFechaInicial,
                iFechaFinal,
                iFechaRegistros,
                iCodRegla,
                iTieneDocumentos,
                iCant
            ]
        )
        QUERY_CONSTANTS['CONNECTION'].commit()

    def insert_raw_process(
        self,
        iIdProceso,
        iIdConexion,
        iLlaveProceso,
        iFechaProceso,
        iFechaUltimaActuacion,
        iDespacho,
        iDepartamento,
        iSujetosProcesales,
        iEsPrivado,
        iCantFilas
    ):
        if self.exists_raw_process(iIdProceso):
            return
        
        vCursor = QUERY_CONSTANTS['CONNECTION'].cursor()
        vCursor.execute(
            QUERY_CONSTANTS['INSERT']['TB_RAW_PROCESS'],
            [   iIdProceso,
                iIdConexion,
                iLlaveProceso,
                iFechaProceso,
                iFechaUltimaActuacion,
                iDespacho,
                iDepartamento,
                iSujetosProcesales,
                iEsPrivado,
                iCantFilas,
                False
            ]
        )
        QUERY_CONSTANTS['CONNECTION'].commit()

# We establish our SQL connection.
QUERY_CONSTANTS['CONNECTION'] = mysql.connector.connect(**config)
vDB = DB_Manager()

def download_process(iPersonName):
    vSizeResponse = 20
    vPage = 0
    vProcesos = []
    while vSizeResponse == 20:
        #print('LOADING...')
        vUrl = "https://consultaprocesos.ramajudicial.gov.co:448/api/v2/Procesos/Consulta/NombreRazonSocial"
        vParams = {
            'nombre': iPersonName,
            'tipoPersona': 'nat',
            'SoloActivos': 'false',
            'codificacionDespacho': None,
            'pagina': vPage
        }
        vJsonData = requests.get(vUrl, params = vParams).json()
        #print(vJsonData)

        for vProceso in vJsonData["procesos"]:
            vProcesos.append(vProceso)

        vSizeResponse = len(vJsonData["procesos"])
        vPage = vPage + 1

        if vSizeResponse == 20 and vJsonData['paginacion']['cantidadPaginas'] == vJsonData['paginacion']['pagina'] + 1:
            vSizeResponse = 0
    return vProcesos

def load_json_data_procces():
    vCountPending = vDB.count_persons_pending()
    vPersons = vDB.select_persons_pending()

    print("PENDING PERSONS:", vCountPending)
    vIndex = 0
    for vPerson in vPersons:
        vText = "PROCESS: " + str(100*vIndex/vCountPending) + "% --> " + vPerson[1] + "                          "
        print("\r" + vText, end="")
        
        try:
            vProcesos = download_process(vPerson[1])
            for vProceso in vProcesos:
                vDB.insert_raw_process(
                    vProceso['idProceso'],
                    vProceso['idConexion'],
                    vProceso['llaveProceso'],
                    vProceso['fechaProceso'],
                    vProceso['fechaUltimaActuacion'],
                    vProceso['despacho'],
                    vProceso['departamento'],
                    vProceso['sujetosProcesales'],
                    vProceso['esPrivado'],
                    vProceso['cantFilas']
                )

                vDB.insert_person_process(
                    vPerson[0],
                    vProceso['idProceso'],
                    vProceso['llaveProceso']
                )
            vDB.update_person_status(vPerson[0])
        except Exception as e:
            print("ERROR PROCESSING: ", e)
        vIndex = vIndex + 1
        vText = "PROCESS: " + str(100*vIndex/vCountPending) + "% --> " + vPerson[1] + "                          "
        print("\r" + vText, end="")

def save_senators():
    for vP in QUERY_CONSTANTS['SENATORS']:
        vDB.insert_person(vP)

def load_sujetos_procesales(iProcesoId):
    vSizeResponse = 40
    vPage = 1
    vSujetos = []
    while vSizeResponse == 40:
        vUrl = "https://consultaprocesos.ramajudicial.gov.co:448/api/v2/Proceso/Sujetos/"+str(iProcesoId)+"?pagina="+str(vPage)
        vJsonData = requests.get(vUrl).json()

        if      'Message'    in vJsonData \
            and 'StatusCode' in vJsonData \
            and vJsonData['StatusCode'] == 500:
            break

        for vS in vJsonData['sujetos']:
            vSujetos.append(vS)
        
        vSizeResponse = len(vJsonData['sujetos'])
        vPage = vPage + 1
    return vSujetos

def load_actuaciones(iIdProceso):
    #https://consultaprocesos.ramajudicial.gov.co:448/api/v2/Proceso/Actuaciones/129555211?pagina=1
    vSizeResponse = 40
    vPage = 1
    vActuaciones = []
    while vSizeResponse == 40:
        vUrl = "https://consultaprocesos.ramajudicial.gov.co:448/api/v2/Proceso/Actuaciones/"+str(iIdProceso)+"?pagina="+str(vPage)
        vJsonData = requests.get(vUrl).json()

        if      'Message'    in vJsonData \
            and 'StatusCode' in vJsonData \
            and vJsonData['StatusCode'] == 500:
            break

        for vS in vJsonData['actuaciones']:
            vActuaciones.append(vS)
        
        vSizeResponse = len(vJsonData['actuaciones'])
        vPage = vPage + 1
    return vActuaciones

def process_actuaciones(iIdProceso):
    vActuaciones = load_actuaciones(iIdProceso)

    for vAct in vActuaciones:
        vDB.insert_actuacion (
            iIdProceso,
            vAct['idRegActuacion'],
            vAct['llaveProceso'],
            vAct['consActuacion'],
            vAct['fechaActuacion'],
            vAct['actuacion'],
            vAct['anotacion'],
            vAct['fechaInicial'],
            vAct['fechaFinal'],
            vAct['fechaRegistro'],
            vAct['codRegla'],
            vAct['conDocumentos'],
            vAct['cant']
        )

def process_sujetos_procesales(iIdProceso):
    vSujetosProcesales = load_sujetos_procesales(iIdProceso)

    for vSP in vSujetosProcesales:
        vDB.insert_sujeto_procesal (
            iIdProceso,
            vSP['idRegSujeto'],
            vSP['tipoSujeto'],
            vSP['esEmplazado'],
            vSP['identificacion'],
            vSP['nombreRazonSocial'],
            vSP['cant']
        )

def process_details(iIdProceso):
    vUrlDetails = "https://consultaprocesos.ramajudicial.gov.co:448/api/v2/Proceso/Detalle/" + str(iIdProceso)
    vJsonData = requests.get(vUrlDetails).json()
    
    vDB.insert_detail_process(
        iIdProceso,
        vJsonData['llaveProceso'],
        vJsonData['idConexion'],
        vJsonData['esPrivado'],
        vJsonData['fechaProceso'],
        vJsonData['despacho'],
        vJsonData['ponente'],
        vJsonData['tipoProceso'],
        vJsonData['claseProceso'],
        vJsonData['subclaseProceso'],
        vJsonData['recurso'],
        vJsonData['ubicacion'],
        vJsonData['contenidoRadicacion'],
        vJsonData['fechaConsulta'],
        vJsonData['ultimaActualizacion']
    )

def load_pending_process():
    vCountPending = vDB.count_process_pending()
    vProcesos = vDB.select_pending_process()
    vIndex = 0
    print("Procesos publicos pendientes: ", vCountPending)
    for vP in vProcesos:
        vText = "PROCESS: " + str(100*vIndex/vCountPending) + "% --> " + str(vP[0]) + "                          "
        print("\r" + vText, end = "")

        try:
            #process_details(vP[0])
            #process_sujetos_procesales(vP[0])
            process_actuaciones(vP[0])
            vDB.update_process_status(vP[0])
        except Exception as e:
            print("ERROR PROCESSING: ", e)

        vIndex = vIndex + 1
        vText = "PROCESS: " + str(100*vIndex/vCountPending) + "% --> " + str(vP[0]) + "                          "
        print("\r" + vText, end = "")

#save_senators()
load_json_data_procces()
load_pending_process()
