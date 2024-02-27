import paramiko
import pandas as pd

#=== Adicionar credenciais
ssh_host = '15.235.110.107'
ssh_port = 2205
ssh_user = ''
ssh_password = ''

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

try:
    ssh_client.connect(ssh_host, port=ssh_port, username=ssh_user, password=ssh_password)
    sftp_client = ssh_client.open_sftp()
    print('conectado')
except:
    print('Falha na conexão, credenciais possivelmente incorretas')
    exit()
    
remote_path = '/opt/dados/registro_atendimento_2020_2021_2022.csv'

# É impotante destacar que o arquivo em questão possui mais de 50mb de extensão.
# Sendo assim, a sua leitura remota através da biblioteca pandas pode levar muito tempo
# A depender do uso dos dados, pode valer a pena a utilização de outro método de leitura

with sftp_client.open(remote_path) as file:
    df = pd.read_csv(file)
    print('DataFrame pronto')