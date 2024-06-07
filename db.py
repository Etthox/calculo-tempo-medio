import pandas as pd
import queries
import pyodbc

# ---- PARAMS AND LOG ----
#Database credentials
DB_ADDRESS = '...'
DB_DATABASE = '...'
DB_USERNAME = '...'
DB_PASSWORD = '...'

#Conx string create based on given info
CONX_STRING = ('Driver={SQL Server};'
        'Server=' + DB_ADDRESS +
        ';Database=' + DB_DATABASE +
        ';UID=' + DB_USERNAME +
        ';PWD=' + DB_PASSWORD + ';')


# ---- OBJETO DE CONEXAO ----
#define a conexão para o banco
conn = pyodbc.connect(CONX_STRING)
cursor = conn.cursor()


def get_TarefasDaRotina():
    try:
        return pd.read_sql(queries.get_TarefasDaRotina, conn)      
    except Exception as e:
        raise e

def get_TarefasDoWorkflow(NumeroTarefa):
    try:
        return pd.read_sql(queries.get_TarefasDoWorkflow.format(NumeroTarefa = NumeroTarefa), conn)      
    except Exception as e:
        raise e

def get_HorariofimDaExecucao(idTarefa):
    try:
        return pd.read_sql(queries.get_HorariofimDaExecucao.format(idTarefa = idTarefa), conn)      
    except Exception as e:
        raise e
    
    
def get_HorariofimDaExecucao_wf(idTarefa):
    try:
        return pd.read_sql(queries.get_HorariofimDaExecucao_wf.format(idTarefa = idTarefa), conn)      
    except Exception as e:
        raise e


def get_HorarioGeracaoProxTarefa(idTarefa):
    try:
        return pd.read_sql(queries.get_HorarioGeracaoProxTarefa.format(idTarefa = idTarefa), conn)      
    except Exception as e:
        raise e
