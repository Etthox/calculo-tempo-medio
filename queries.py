get_TarefasDaRotina = """
select id, numero, modificado,ObjetoOrigemId,inicioreal from vista.dbo.tarefa where objetoorigemid IN
(
'493c9792-f6fa-4616-81a1-ba85c252327b',
'5b97cae1-f65c-4be4-83d1-c09d5d9da51f'
) and inicioreal >= '2024-01-01 00:00:00.000'
and terminoreal <= '2024-03-31 23:59:59.000' and status = '85'  order by objetoorigemid
"""

get_TarefasDoWorkflow = """
DECLARE @numero AS BIGINT = {NumeroTarefa}

DECLARE @idTarefa AS UNIQUEIDENTIFIER = (SELECT Id FROM vista.dbo.tarefa WHERE Numero = @numero)
 
SELECT id, numero, modificado,inicioreal,criado
FROM vista.dbo.tarefa
WHERE ObjetoOrigemId IN (
    SELECT Id
    FROM vista.dbo.Sequenciamento
    WHERE InstanciaId IN (
        SELECT Id
        FROM vista.dbo.Instancia
        WHERE ThreadId = @idTarefa
    )

)order by numero
"""


get_HorariofimDaExecucao = """
select data,dispositivo,criado from vista.dbo.Execucao where TarefaId = '{idTarefa}'  and status = '85' 
"""

get_HorariofimDaExecucao_wf = """
select data,dispositivo from vista.dbo.Execucao where TarefaId = '{idTarefa}'  and status = '85' 
"""

get_HorarioGeracaoProxTarefa = """
select disponibilizacao from vista.dbo.tarefa with (nolock) where id = '{idTarefa}'
"""


