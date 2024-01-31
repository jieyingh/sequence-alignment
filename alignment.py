import numpy as np 
import pandas as pd 

def alignement(seq1, seq2, scoreGap, scoreMatch, scoreMismatch):
    (matrice, numRow, numCol, rowSeq, colSeq) = createMatrice(seq1, seq2)
    matrice = firstScore(matrice,numCol, numRow, scoreGap)
    calcScore(matrice, numRow, numCol, scoreGap, scoreMatch, scoreMismatch, rowSeq, colSeq)

# cree le dataframe
def createMatrice(seq1, seq2):
    rowSeq = ["start"] + list(seq1)
    colSeq = ["start"] + list(seq2)

    numRow = len(rowSeq)
    numCol = len(colSeq)

    matrice = pd.DataFrame(0, index=rowSeq, columns=colSeq)
    
    return (matrice, numRow, numCol, rowSeq, colSeq)

# calcul de la premiere colonne et rangee
def firstScore(matrice, numCol, numRow, scoreGap):
    for col in range(1,numCol):
        matrice.iat[0,col] = matrice.iat[0,(col -1)] + scoreGap
    for row in range(1,numRow):
        matrice.iat[row,0] = matrice.iat[(row -1),0] + scoreGap
    
    return matrice   

# calcule le score de chaque case
def calcScore(matrice, numRow, numCol, scoreGap, scoreMatch, scoreMismatch, rowSeq, colSeq):
    for row in range(1, numRow):
        for col in range(1, numCol):
            # matches, takes top left and adds scoreMatch
            if colSeq[col] == rowSeq[row]:
                matrice.iat[row,col] = matrice.iat[(row - 1),(col - 1)] + scoreMatch
            else:
                pass
    print(matrice)


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
        scoreGap = int(input(" Entrez le scoreGap: "))
        scoreMatch = int(input(" Entrez le scoreMatch: "))
        scoreMismatch = int(input(" Entrez le scoreMismatch: "))
    elif defaut == "Y":
        scoreGap = 2
        scoreMatch = 0
        scoreMismatch = 1

alignement(seq1, seq2, scoreGap, scoreMatch, scoreMismatch)