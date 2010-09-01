#!/usr/bin/python

import random

# inicializa listas
lista=[]
final=[]

# abre base de palavras
arquivo=open("palavras.txt","r")
resultado=open("bingo.html","w")

# percorre arquivo de palavras
while True:
        palavra=arquivo.readline()
# se chegar ao final do arquivo, interrompe
        if len(palavra)==0:
                break
# enquanto ler palavra valida, adiciona aa lista de palavras
        finalp=len(palavra)-1
        lista.append(palavra[:finalp])

# para escolher as 24 palavras da tabela
for contador in range (1,25):
        # gera um numero randomico menor que o numero de palavras na lista
        indice=int(len(lista)*random.random())
        escolhida=lista[indice]
        # Adiciona a palavra escolhida aa lista da cartela
        final.append(escolhida)
        # Remove a palavra da lista inicial, para evitar duplicata na cartela
        lista.remove(escolhida)


#resultado.write('Content-type: text/html')
#resultado.write('')
resultado.write('<HTML><HEAD><TITLE>WEB BINGO DO DCE!</TITLE></HEAD><BODY>')
resultado.write('<H1>Bingo do DCE</H1>')
resultado.write('<H2>Gerador de cartelas</H2>')
resultado.write('<P> Seu nome: ___________________________</P>')
resultado.write('<P> Seu RA: _____________________________</P>')

especial ='<IMG SRC="161590.jpg">'

resultado.write('<P>Cartela gerada:</P>')
resultado.write('<TABLE BORDER="1">')
resultado.write('<TR><TD> %s </TD><TD> %s </TD><TD> %s </TD><TD> %s </TD><TD> %s </TD></TR>' %(final[0],final[1],final[2],final[3],final[4]))
resultado.write('<TR><TD> %s </TD><TD> %s </TD><TD> %s </TD><TD> %s </TD><TD> %s </TD></TR>' %(final[5],final[6],final[7],final[8],final[9]))
resultado.write('<TR><TD> %s </TD><TD> %s </TD><TD> %s </TD><TD> %s </TD><TD> %s </TD></TR>' %(final[10],final[11],especial,final[12],final[13]))
resultado.write('<TR><TD> %s </TD><TD> %s </TD><TD> %s </TD><TD> %s </TD><TD> %s </TD></TR>' %(final[14],final[15],final[16],final[17],final[18]))
resultado.write('<TR><TD> %s </TD><TD> %s </TD><TD> %s </TD><TD> %s </TD><TD> %s </TD></TR>' %(final[19],final[20],final[21],final[22],final[23]))
resultado.write('</TABLE>')
resultado.write('</BODY></HTML>')

arquivo.close()
resultado.close()
