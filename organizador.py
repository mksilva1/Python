"""
Projeto 1 - organizador
Requisito: Este programa verifica os arquivos contidos em uma pasta, cria
sub-pastas chamadas de documentos e planilhas. Após move os arquivos conforme
o seu tipo para as sub-pastas
Autor: Marcelo Kipper da Silva
Versão: 0.9.0 
Data 30/08/2022.
"""

# Importa a biblioteca de funções do sistema operacional
import os

# Importa a biblioteca High-level file operations
import shutil

# Obtem a lista dos arquivos e sub-pastas da pasta atual.
arquivos = os.listdir('.')

# Conta o número de arquivos na pasta
quantidade = len(arquivos)

# Mostra os arquivos encontrados
existe_doc = False
existe_plan = False
print("A pasta contém os seguintes arquivos:")
i=0 # zera contador
while i < quantidade:
    print (arquivos[i])
    if arquivos[i] == 'documentos': # verifica se já esxiste a pasta
        existe_doc = True
    if arquivos[i] == 'planilhas': # verifica se já esxiste a pasta
        existe_plan = True
    i+=1
print('')

# Cria as sub-pastas documentos e planilhas, caso não existam
if existe_doc == False:
    os.mkdir('documentos')
if existe_plan == False:
    os.mkdir('planilhas')

# Analisa os arquivos e move para as respecitvas pastas
i=0 # zera contador
while i < quantidade:
    arq = arquivos [i] # obtem o nome de cada arquivo na pasta
    ext = arq[-4:] # obtem os ultimos 4 caracteres do nome
    
    if ext == '.xls': # se for xls move para a pasta planilhas
        shutil.move(arq,'planilhas') 
        print(f"O arquivo {arq} foi movido para a pasta planilhas.")
        
    if ext == '.doc' or ext == 'docx': # se for doc ou docx move para a pasta documentos
        shutil.move(arq,'documentos')
        print(f"O arquivo {arq} foi movido para a pasta documentos.")
    i+=1




