import random

# definizione della procedura che simula una partita

def partita():
    
    messaggio = "" # inizializzazione della var messaggio
    nomeVincitore = "nessuno"
    mosse = ["sasso", "carta", "forbici"]
    numero = random.randint(0, 2)
    sceltaComputer = mosse[numero]
    sceltaGiocatore = input("Quale mossa scegli?")
    print("Il computer ha scelto:", sceltaComputer)
    print("Tu hai scelto:", sceltaGiocatore)
    
    # devo confrontare la mosse
    if sceltaGiocatore == sceltaComputer:
        messaggio = "Nessuno vince ..."

    # situazioni in cui vince il computer    
    elif sceltaComputer == "carta" and sceltaGiocatore == "sasso":
        messaggio = "Ho vinto io!!!!"
        nomeVincitore = "computer"
    elif sceltaComputer == "forbici" and sceltaGiocatore == "carta":
        messaggio = "Ho vinto io!!!!" 
        nomeVincitore = "computer" 
    elif sceltaComputer == "sasso" and sceltaGiocatore == "forbici":
        messaggio = "Ho vinto io!!!!"
        nomeVincitore = "computer"

    # situazioni in cui vince il giocatore    
    elif sceltaGiocatore == "carta" and sceltaComputer == "sasso":
        messaggio = "Hai vinto tu!!!!" 
        nomeVincitore = "giocatore"   
    elif sceltaGiocatore == "forbici" and sceltaComputer == "carta":
        messaggio = "Hai vinto tu!!!!" 
        nomeVincitore = "giocatore"   
    elif sceltaGiocatore == "sasso" and sceltaComputer == "forbici":
        messaggio = "Hai vinto tu!!!!"
        nomeVincitore = "giocatore"  

    # se il giocatore non ha scelto una delle mosse corrette?
    else:
        messaggio = "Non ho capito ..."

    print(messaggio)
    print("------------------------------------")

    #restituisco il nome del vincitore
    return nomeVincitore





# inizio programma vero e proprio

print("Sasso, carta, forbici: benvenuto!")

# lista con i punteggi di gioco
punteggio = [0,0]
# facciamo che:
# il primo elemento = punteggio del giocatore
# il secondo elemento = punteggio del computer


continua = True
while continua:

    # lancio una partita e salvo il vincitore nella variabile
    vincitore = partita()

    # incremento i punteggi guardando la variabile 'vincitore'
    if vincitore == "giocatore": # assegno un punto al giocatore
        punteggio[0] += 1
    if vincitore == "computer": # assegno un punto al computer
        punteggio[1] += 1

    if input("Vuoi fare un'altra partita (s/n) ?") != "s":
        continua = False

print("Numero vittorie giocatore:", punteggio[0])
print("Numero vittorie computer:", punteggio[1])
print("Grazie per aver giocato, torna presto!")






    
