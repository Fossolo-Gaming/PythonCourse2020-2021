import random

# ------------------------------------------------------------
# sezione liste e parametri dello script
# ------------------------------------------------------------

v_soggetti = [
    "Pierino",
    "Mario Rossi",
    "Il sole",
    "Un micio",
    "Un cagnolino",
    "Un calciatore famoso",
    "Una presidentessa neoeletta",
    "Il presidente del mondo"
    ]

v_verbi = [
    "mangia",
    "apre",
    "chiude",
    "si toglie",
    "beve",
    "indossa",
    "compone"
    ]

v_oggetti = [
    "una mela",
    "un'automobile",
    "un libro",
    "due cappelli",
    "un vestito",
    "un brano"
    ]

numMinFrasi = 50

# ------------------------------------------------------------
# sezione procedure
# ------------------------------------------------------------

def scriviFrase():
    
    # genero una frase casuale
    numSoggetto = random.randint(0, len(v_soggetti)-1) # len > length = lunghezza
    numVerbo    = random.randint(0, len(v_verbi)-1)
    numOggetto  = random.randint(0, len(v_oggetti)-1)
    frase = v_soggetti[numSoggetto] + " " + v_verbi[numVerbo] + " " + v_oggetti[numOggetto] + "."
    mioFile.write(frase)

def scriviCapitolo():

    # determino il numero massino di frasi da generare
    numMaxFrasi = random.randint(50, 150)

    # chiedo e stampo il titolo del capitolo
    titoloCapitolo = input("Titolo del capitolo? ")
    mioFile.write(titoloCapitolo + "\n")

    # genero un numero casuale di frasi casuali
    for i in range(numMinFrasi, numMaxFrasi):
        scriviFrase()

    # vado a capo al termine del capitolo (aggiungo un fine linea)
    mioFile.write("\n") 

# ------------------------------------------------------------
# programma vero e proprio ...
# ------------------------------------------------------------

# variabili per il titolo e l'autore del libro
titoloLibro = input("Titolo del libro? ")
autoreLibro = input("Autore del libro? ")

# var con il nome del file
nomeFile = titoloLibro + ".txt"

# apretura o creazione del file
mioFile = open(nomeFile, 'a')

mioFile.write(titoloLibro + "\n")
mioFile.write("Un romanzo di " + autoreLibro + "\n\n\n")


scriviCapitolo()
scriviCapitolo()
scriviCapitolo()
scriviCapitolo()

# chiusura del file
mioFile.close()
