import numpy as np 
import pandas as pd 

paths = []

def alignement(seq1, seq2, scoreGap, scoreMatch, scoreMismatch):
    (matrice, numRow, numCol, rowSeq, colSeq) = createMatrice(seq1, seq2)
    matrice = firstScore(matrice,numCol, numRow, scoreGap)
    matrice = calcScore(matrice, numRow, numCol, scoreGap, scoreMatch, scoreMismatch, rowSeq, colSeq)
    chemin = backtrack(numRow, numCol)
    (alignedSeq1, indicator, alignedSeq2) = visAlignement(chemin)
    score(matrice, numRow, numCol, alignedSeq1, indicator, alignedSeq2)


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
                match(row, col)
            else:
                mismatch = matrice.iat[(row - 1),(col - 1)] + scoreMismatch
                gapSeq1 = matrice.iat[(row),(col - 1)] + scoreGap
                gapSeq2 = matrice.iat[(row - 1),(col)] + scoreGap
                minVal = matrice.iat[row,col] = min(mismatch,gapSeq1,gapSeq2)
                notMatch(row, col, minVal, mismatch, gapSeq1, gapSeq2)

    return matrice

# ajout du chemin si match
def match(row, col):
    pathTrack((row,col), ((row - 1),(col - 1)), "match")

# ajout du chemin si pas de match
def notMatch(row, col, minVal, mismatch, gapSeq1, gapSeq2):
    if mismatch == minVal:
        pathTrack((row,col), ((row - 1),(col - 1)), "mismatch")
    if gapSeq1 == minVal:
        pathTrack((row,col), (row,(col - 1)), "gapSeq1")
    elif gapSeq2 == minVal:
        pathTrack((row,col), ((row - 1),col), "gapSeq2")

# log des chemins pris
def pathTrack(current, previous, type):
    dict = {
        "current": current,
        "previous": previous,
        "type": type}
    paths.append(dict)

# donne l'alignement
def visAlignement(chemin):
    chemin = chemin[::-1]
    alignedSeq1 = ""
    indicator = ""
    alignedSeq2 = ""
    for dict in chemin:
        match dict.get("type"):
            case "match":
                alignedSeq1 += seq1[(dict.get("current"))[0] - 1]
                alignedSeq2 += seq2[(dict.get("current"))[1] - 1]
                indicator += "|"
            case "mismatch":
                alignedSeq1 += seq1[(dict.get("current"))[0] - 1]
                alignedSeq2 += seq2[(dict.get("current"))[1] - 1]
                indicator += ":"
            case "gapSeq1":
                alignedSeq1 += "-"
                alignedSeq2 += seq2[(dict.get("current"))[1] - 1]
                indicator += " "
            case "gapSeq2":
                alignedSeq1 += seq1[(dict.get("current"))[0] - 1]
                alignedSeq2 += "-"
                indicator += " "               
    return (alignedSeq1, indicator, alignedSeq2)

def backtrack(numRow, numCol):
    chemin = []
    fin = ((numRow - 1), (numCol -1))

    target = fin
    search = True

    while search:
        found = False
        for dict in paths:
            if dict.get("current") == target:
                chemin.append(dict)
                target = dict.get("previous") # sets new target
                found = True
                break
        if not found:
            search = False # stops the loop if no more matches are found

    return chemin

# extrait le score final de la matrice
def score(matrice, numRow, numCol, alignedSeq1, indicator, alignedSeq2):
    print(matrice)
    print("Score de l'alignement: ", matrice.iat[(numRow - 1),(numCol - 1)])
    print(alignedSeq1)
    print(indicator)
    print(alignedSeq2)
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