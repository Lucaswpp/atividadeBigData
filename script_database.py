from mysql import connector
from datamateria import *
from random import choice,uniform,randint



db_conexao = connector.connect(host="localhost",database="alunosdata",user="root",password="123456")
obj_db = db_conexao.cursor()

def MakeDataMateria():
    for nome,descricao in materias.items():
        obj_db.execute(f"insert into materia values (default,'{nome}','{descricao}')")
    
    db_conexao.commit()

def makeDataInfo():
    intervalo_id_materia = list(range(1,14))
    
    for _ in range(1,len(nomes_alunos)+1):
        materia_preferida = choice(intervalo_id_materia)
        materia_dificuldade = choice(intervalo_id_materia)

        if materia_preferida == materia_dificuldade:
            if materia_dificuldade == len(intervalo_id_materia):
                materia_dificuldade -= 1
            
            elif  materia_dificuldade == 1:
                materia_dificuldade += 1
            
            else:
                materia_dificuldade -= [1,-1][randint(0,1)]

        obj_db.execute(f"insert into info values (default, '{uniform(1,6):.1f}','{materia_preferida}','{materia_dificuldade}')")
    
    db_conexao.commit()

def MakeDataNotaandAlunos():
    intervalo_id_materia = list(range(1,14))
    for a_id in range(1,len(nomes_alunos)+1):
        for m_id in intervalo_id_materia:
            obj_db.execute(f"insert into alunos_notas values (default,{a_id},{m_id},'{uniform(1,10):.1f}')")
    
    db_conexao.commit()

def makeDataAluno():

    contador = 1
    for nome,sexo,escolaridade in nomes_alunos:
        obj_db.execute(f"insert into alunos values (default, '{nome}', '{sexo}','{escolaridade}',{contador})")

        contador += 1
    
    db_conexao.commit()

def makeDataDatabase():
    MakeDataMateria()
    makeDataInfo()
    makeDataAluno()
    MakeDataNotaandAlunos()


if __name__ == "__main__":
    makeDataDatabase()