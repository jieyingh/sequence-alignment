import numpy as np 
import pandas as pd 

def alignement(seq1, seq2, scoreGap, scoreMatch, scoreMismatch):
    print(seq1, seq2, scoreGap, scoreMatch, scoreMismatch)
    createMatrice(seq1, seq2)

# cree le dataframe
def createMatrice(seq1, seq2):
    # transforme seq1 et seq2 en liste de characteres
    rowSeq = ["start"] + list(seq1)
    colSeq = ["start"] + list(seq2)

    numRow = len(rowSeq)
    numCol = len(colSeq)

    matrice = pd.DataFrame(0, index=rowSeq, columns=colSeq)
    print(matrice)
    print(numRow, numCol)

# calcule le score de chaque case
def calcScore(matrice):
    pass

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
scoreGap = input(" Entrez le scoreGap: ")
scoreMatch = input(" Entrez le scoreMatch: ")
scoreMismatch = input(" Entrez le scoreMismatch: ")

alignement(seq1, seq2, scoreGap, scoreMatch, scoreMismatch)