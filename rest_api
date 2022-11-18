# %% Bibliotecas
import json, requests
import pandas as pd
import numpy as np

#Busca por value column
def return_column_value(df,column_value,value):
    df_column = df.iloc[:,column_value]
    index = np.where(df_column == value)
    value = index[0]
    result = df.iloc[value]
    return result

#return_column_value(df, 2, 'Luffy')['id']

# %% validaLogin
def validaLogin(username, password, email = ''):
    
    global index
    
    var = []
    response = requests.get("REST API")
    json_data = json.loads(response.text)
    df = pd.DataFrame(json_data)  
    id_df = df['id']
    id_username = return_column_value(df, 2, username)['id']
    id_email = return_column_value(df, 4, email)['id']
    id_password = return_column_value(df, 3, password)['id']    
    id_df = list(id_df)
    
    # %% Verifica se o Username, Usuário ou o Password está errado
    print(10*'*', 'Primeiro Campo', 10*'*','\n')
    try:
        id_username = int(id_username)
    except TypeError:
        try:
            id_email = int(id_email)
        except TypeError:
            print('username e email invalidos!\n')
    try:
        id_password = int(id_password)
    except TypeError:
        print('password invalidos!\n')
        
    def verificador():    
    # %% Verificador do Primeiro Campo
        if isinstance(id_email, int):
            print("email aprovado\n")
            var.append(id_email)
        else:
            print("email nao aprovado\n")
        
        if isinstance(id_username, int):
            print("username aprovado\n")
            var.append(id_username)
        else:
            print("username nao aprovado\n")   
    # %% Verificador do Segundo Campo            
        print(10*'*', 'Segundo Campo', 10*'*','\n')
        if id_password in id_df:
            print('password aprovado\n')
        else:
            print("password nao aprovado\n")     
        try:
            if isinstance(var[0], int):
                index = var[0]
        except IndexError:
            print('Usuario nao cadastrado!')
            print('Retornar ao login!\n')
            
        print(10*'*','Verificacao concluida!', 10*'*','\n')    
        return 
    return verificador()
        
# %% validaLogin
validaLogin('Luffy', '123456', 'uffy@gmal.com')
