from domande import Domanda
from giocatori import Giocatore
from random import *
from operator import *
def main(): 
    domande_lista=[]
    giocatori_lista=[]
    file="Lab01/domande.txt"
    domande_lista=crealistadomande(file, domande_lista)
    livello_massimo=trovalivellomassimo(domande_lista)
    domande_per_livello=dividiperlivello(domande_lista, livello_massimo)

    for i in range(0,livello_massimo+1):
        risposta=stampadomanda(domande_per_livello[i])
        if risposta==False:
            punteggio=i
            break
        print("Risposta corretta! \n")
        punteggio=i+1

    print(f"Hai totalizzato {punteggio} punti!")
    nickname=input("Inserisci il tuo nickname: ")

    giocatore=Giocatore(nickname, punteggio)
    giocatori_lista.append(giocatore)
    aggiungipunteggio("Lab01/punti.txt", giocatore)


def crealistadomande(file,domande_lista):
    try:
        infile=open(file,'r', encoding='utf-8')
        domanda_lista=[]
        count=0
        for line in infile:
            if count<=5:
                domanda_lista.append(line)
                count+=1
            else:
                count=0
                questa_domanda=Domanda(domanda_lista[0],int(domanda_lista[1]),domanda_lista[2],domanda_lista[3],
                                            domanda_lista[4], domanda_lista[5])
                domande_lista.append(questa_domanda)
                domanda_lista=[]  

        infile.close()   
    except FileNotFoundError:
        print("Errore: file non trovato")
    return domande_lista

def trovalivellomassimo(domande_lista):
    livello_massimo=0
    for i in range(0, len(domande_lista)):
        if domande_lista[i].punteggio>livello_massimo:
            livello_massimo=domande_lista[i].punteggio
    return livello_massimo

def dividiperlivello(domande, max):
    divise=[]
    for i in range(0, max+1):
        livello=[]
        for j in range(0, len(domande)):
            if domande[j].punteggio==i:
                livello.append(domande[j])
        divise.append(livello)
    return divise

def stampadomanda(domande):
    domanda=domande[randint(0,len(domande)-1)]
    risposte=[domanda.giusta, domanda.sbagliata1, domanda.sbagliata2, domanda.sbagliata3]
    nuove_risposte=sample(risposte, 4)
    for i in range(0,4):
        if nuove_risposte[i]==domanda.giusta:
            rispostacorretta=i+1

    print(f"Livello {domanda.punteggio} ) {domanda.domanda} \n1. {nuove_risposte[0]} \n2. {nuove_risposte[1]} \n3. {nuove_risposte[2]} \n4. {nuove_risposte[3]}")
    rispostadata= int(input("Inserisci la risposta: "))
    if rispostadata==rispostacorretta:
        return True
    else:
        print(f"Risposta sbagliata! La risposta corretta era: {rispostacorretta}\n")
        return False
        

def aggiungipunteggio(file, giocatore):
    classifica=[]
    try:
        infile=open(file,'r', encoding='utf-8')
        for line in infile:
            riga=line.split(" ")
            classifica.append([riga[0],riga[1]])
        infile.close()   
    except FileNotFoundError:
        print("Errore: file non trovato")
    
    for i in range(0, len(classifica)):
        if int(classifica[i][1])<=giocatore.punteggio:
            classifica.insert(i, [giocatore.name, giocatore.punteggio])
            break


    try:
        infile=open(file,'w', encoding='utf-8')
        for i in range(0, len(classifica)):
            infile.write(f"{classifica[i][0]} {classifica[i][1]} \n")

        infile.close()
    except FileNotFoundError:
        print("Errore: file non trovato")



main()