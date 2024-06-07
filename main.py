from datetime import date, datetime, timedelta
import tools
import json
import db
from pandas import DataFrame as df
import pandas as pd
from fpdf import FPDF
import numpy as np


#class PDF(FPDF):
    #def header(self):
    #    self.set_font("helvetica", "B", 16)
    #    self.cell(40)
     #   self.cell(40,10, "Simple PDF", border=1, align="C")
     #   self.ln(20)

   # def footer(self):
   #     self.set_y(-15)
    #    self.set_font("helvetica", "I", 16)
   #     self.cell(0,10, f"Page {self.page_no()}/{{nb}}", align="C")

#pdf = PDF()



def main():
    dataInicio = f"""{date.today().strftime("%Y-%m-%d")}T{date.today().strftime("%H:%M:%S")}"""
    ##--
    dfTarefasRotina =  db.get_TarefasDaRotina()



    ##ESTA DANDO ERRO PQ TEM TAREFA GATILHO QUE NÃO POSSUI TAREFA DO WF(nao gerou), PRECISA VER COMO TIRAR ESSAS



    
    diferenca_em_segundos_lista = []
    
    def TempoDaGatilhoParaPrimeiraWF():
        numero_tarefa_rotina_list =[]
        numero_tarefa_wf_list =[]
        data_fim_list =[]
        data_fim_wf_list =[]
        data_geracao_list =[]
        diferenca_segundos_list  =[]
        numero_id_estrutura_list = []
        modificado_tarefa_rotina_list =[]
        modificado_tarefa_wf_list =[]
        inicio_real_rotina_list = []
        inicio_real_wf_list = []
        criado_rotina_list = []
        criado_wf_list = []
        dispositivo_Rotina_list = []
        dispositivo_wf_list = []
        contagem = 0
        qtd = 0


        #pdf.add_page()
        for index,row in dfTarefasRotina.iterrows():
            contagem = contagem + 1
            #numero_tarefa_rotina = "Numero da Tarefa da Rotina: {}".format(row['numero'])
            numero_tarefa_rotina = row['numero']
            #print(numero_tarefa_rotina)
            dfTarefasWorkflow = db.get_TarefasDoWorkflow(row['numero'])
            
            if (dfTarefasWorkflow.empty):
                qtd = qtd+1
                qtd_tarefas_sem_wf = "Quantidade de tarefas sem Workflow: {}".format(qtd) 
                #print(qtd_tarefas_sem_wf) 
                #pdf.cell(0,10,qtd_tarefas_sem_wf )
                continue
            else:
                    for tarefas in dfTarefasWorkflow['numero']: 
                        #numero_tarefa_wf = "Numero da Tarefa do Workflow: {}".format(dfTarefasWorkflow['numero'].iloc[0])
                        inicio_real_rotina = row['inicioreal']
                        numero_id_estrutura = row['ObjetoOrigemId']
                        numero_tarefa_wf = tarefas
                        modificado_tarefa_rotina = row['modificado']
                        modificado_tarefa_wf = dfTarefasWorkflow['modificado'].iloc[0]
                        dfHorariofimDaExecucaoGatilho = db.get_HorariofimDaExecucao(row['id'])
                        criado_rotina = dfHorariofimDaExecucaoGatilho['criado'].iloc[0]
                        dispositivo_rotina = dfHorariofimDaExecucaoGatilho['dispositivo'].iloc[0]
                        try:
                            criado_wf = dfTarefasWorkflow['criado'].iloc[0]
                        except IndexError:
                            criado_wf = np.nan
                        try:
                            inicio_real_wf = dfTarefasWorkflow['inicioreal'].iloc[0]
                        except IndexError:
                            inicio_real_wf = np.nan
                        try:
                            dfHorariofimDaExecucaoWF = db.get_HorariofimDaExecucao(dfTarefasWorkflow['id'].iloc[0])
                        except IndexError:
                            dfHorariofimDaExecucaoWF = np.nan
                        try:
                            dispositivo_wf = dfHorariofimDaExecucaoWF['dispositivo'].iloc[0]
                        except IndexError:
                            dispositivo_wf = np.nan
                        try:
                            dfHorarioGeracaoProxTarefa = db.get_HorarioGeracaoProxTarefa(dfTarefasWorkflow['id'].iloc[0])
                        except IndexError:
                            dfHorarioGeracaoProxTarefa = np.nan
                        dfHorariofimDaExecucaoGatilho
                        dataGatilho = dfHorariofimDaExecucaoGatilho['data'].iloc[0]
                        try:
                            data_fim_wf = dfHorariofimDaExecucaoWF['data'].iloc[0]
                        except IndexError:
                            data_fim_wf = np.nan
                        dataCriacao = dfHorarioGeracaoProxTarefa['disponibilizacao'].iloc[0]
                        inicio_real_rotina_list.append(inicio_real_rotina)
                        inicio_real_wf_list.append(inicio_real_wf)
                        numero_id_estrutura_list.append(numero_id_estrutura)
                        numero_tarefa_rotina_list.append(numero_tarefa_rotina)
                        numero_tarefa_wf_list.append(numero_tarefa_wf)
                        data_fim_list.append(dataGatilho)
                        data_fim_wf_list.append(data_fim_wf)
                        data_geracao_list.append(dataCriacao)
                        modificado_tarefa_rotina_list.append(modificado_tarefa_rotina)
                        modificado_tarefa_wf_list.append(modificado_tarefa_wf)
                        criado_rotina_list.append(criado_rotina)
                        criado_wf_list.append(criado_wf)
                        dispositivo_Rotina_list.append(dispositivo_rotina)
                        dispositivo_wf_list.append(dispositivo_wf)

                        diferenca_tempo = dataCriacao - dataGatilho
                        minutes = diferenca_tempo.seconds // 60
                        seconds = diferenca_tempo.seconds % 60

                        diferenca_segundos_list.append('{:02}:{:02}'.format(minutes, seconds))
                        print("passou")
                #diferenca_segundos_list.append([(dataCriacao - dataGatilho).total_seconds()])
                #data_inicio = "Data do Inicio da tarefa: {}".format(dataGatilho)
                #data_geracao = "Data da disponibilizacao da tarefa: {}".format(dataCriacao)
                #diferenca_segundos = "Tempo para Disponibilizar: {}".format([(dataCriacao - dataGatilho).total_seconds()])
                #diferenca_em_segundos_lista.append([(dataCriacao - dataGatilho).total_seconds()])

                #pdf.set_font("helvetica", "B", 10)
                #pdf.cell(0,10,numero_tarefa_rotina , ln=1)
                #pdf.cell(0,10,numero_tarefa_wf , ln=1)
                #pdf.cell(0,10,data_inicio,ln=1)
                #pdf.cell(0,10,data_geracao,ln=1 )
                #pdf.cell(0,10,diferenca_segundos,ln=1  )
                #pdf.set_font("helvetica", "B", 16)
                #pdf.cell(0,10,"--------------------- --------------------- ", ln=1 )
        df_result = pd.DataFrame({
            'ID da rotina': numero_id_estrutura_list,
            'Numero Tarefa Rotina': numero_tarefa_rotina_list,
            'Inicio Real Tarefa Rotina': inicio_real_rotina_list,
            'Data Termino Execucao (85) Tarefa Rotina': data_fim_list,
            'Data Criado Execução (85) Tarefa Rotina': criado_rotina_list,
            'Modificado Tarefa Rotina': modificado_tarefa_rotina_list,
            'Numero Tarefa WF': numero_tarefa_wf_list,
            'Data Inicio Real WF': inicio_real_wf_list,
            'Data Termino Execucao (85) Tarefa WF': data_fim_wf_list,
            'Data Criado Tarefa Workflow': criado_wf_list,
            'Data Disponibilização Tarefa WF': data_geracao_list,
            'Modificado Tarefa WF': modificado_tarefa_wf_list,
            'Dispositivo Rotina': dispositivo_Rotina_list,
            'Dispositivo WF': dispositivo_wf_list
            #'Tempo para Disponibilizar': diferenca_segundos_list,
        })
        print(df_result)
        
                    #pdf.output("sample.pdf")
                
        return df_result.to_excel('output.xlsx', index=False)        
    

                
        
        

    TempoDaGatilhoParaPrimeiraWF()
    
    
    

    ##pega o horario do inicio da do workflow, caso tenha mais de uma tarefa no workflow
    ##(fazer if na dftarefas workflow para ver se tem mais de uma)
    ##dfHorarioinicioDaExecucaoWF = db.get_HorarioinicioDaExecucao(dfTarefasWorkflow['id'].iloc[0])

if __name__ == "__main__":
    main()