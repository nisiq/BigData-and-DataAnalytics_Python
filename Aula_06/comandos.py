import seaborn as sns
    #Biblioteca utilizada para plotar gráficos com um visual mais interessante
    #pip install seaborn


df = pd.read_csv('nome.csv', sep=',')
    #Cria um objeto chamado df.
    #Ele irá armazenar o dataset lido, deve-se passar o diretório
    #do arquivo e o caractere separador, para arquivo csv - sep = ‘,’

df.head(5) 
    #Exibe as primeiras 5 linhas do dataframe

df.shape
    #Retorna o tamanho do dataset


df.columns = ['usuarioid', 'fileid', 'notas', 'momento']
    #Renomeia as colunas do dataframe

df['notas']
    #Retorna uma série do dataframe, no caso a coluna das notas

df['notas']
    #Exibe uma coluna do dataframe

df[‘notas’].unique()
   #Unificando a coluna do dataframe em um array (estrutura que permite guardar outras variáveis)

df[‘notas’].value_counts()
   #Retorna a quantidade de vezes que um elemento aparece no dataframe

df.notas
    #Acessando uma coluna do dataframe

df.notas.plot()
    #Plotando um gráfico com as notas dos filmes

df.notas.plot(kind='hist')
    #Alterar o tipo de gráfico

"""
Variáveis qualitativas - são variáveis que podem ser
utilizadas para caracterizar algo ou classificar. 
Exemplo: Cor dos olhos, fumante, não fumante

Nominais ou Ordinais - Nominais não existe ordenação
Ordinais - Existe uma ordem que respeita a categoria

Variáveis quantitativas - representa um valor numérico em
si. Exemplo: Nº de cigarros, pressão arterial.
"""





