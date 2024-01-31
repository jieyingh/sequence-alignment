import numpy as np 
import pandas as pd 

def alignement(seq1, seq2, scoreGap, scoreMatch, scoreMismatch):
    (matrice, numRow, numCol) = createMatrice(seq1, seq2)
    calcScore(matrice, numRow, numCol, int(scoreGap), int(scoreMatch), int(scoreMismatch))

# cree le dataframe
def createMatrice(seq1, seq2):
    rowSeq = ["start"] + list(seq1)
    colSeq = ["start"] + list(seq2)

    numRow = len(rowSeq)
    numCol = len(colSeq)

    matrice = pd.DataFrame(0, index=rowSeq, columns=colSeq)
    
    return (matrice, numRow, numCol)

# calcule le score de chaque case
def calcScore(matrice, numRow, numCol, scoreGap, scoreMatch, scoreMismatch):
    # calcul de la premiere colonne et rangee
    for col in range(1,numCol):
        matrice.iat[0,col] = matrice.iat[0,(col -1)] + scoreGap
    for row in range(1,numRow):
        matrice.iat[row,0] = matrice.iat[(row -1),0] + scoreGap

    # calcul des autres scores
    for row in range(1, numRow):
        for col in range(1, numCol):
            matrice.iat[row,col] = col

    print(matrice, numRow, numCol, scoreGap, scoreMatch, scoreMismatch)

# extrait le score final de la matrice
def score(matrice):
    pass

# donne l'alignement
def visAlignement(matrice):
    # will return a list: top strand, bottom strand
    pass


# ================= display ==========================
seq1 = input(" Entrez la premiere sequence: ")
seq2 = input(" Entrez la deuxieme sequence: ")
defaut = None
while defaut != "Y" and defaut != "N":
    defaut = input(" Utiliser les scores par defaut: scoreGap = 2, scoreMatch = 0, scoreMismatch = 1? Y/N ")
    if defaut == "N":
        scoreGap = input(" Entrez le scoreGap: ")
        scoreMatch = input(" Entrez le scoreMatch: ")
        scoreMismatch = input(" Entrez le scoreMismatch: ")
    elif defaut == "Y":
        scoreGap = 2
        scoreMatch = 0
        scoreMismatch = 1

alignement(seq1, seq2, scoreGap, scoreMatch, scoreMismatch)