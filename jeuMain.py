import random

board = ["-", "-", "-",
        "-", "-", "-",
        "-", "-", "-"]
currentPlayer = "x"
winner = None 
gameRunning = True
# var boolean

                  # printing le tableu

def printBoard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("----------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("----------")
    print(board[6] + " | " + board[7] + " | " + board[8])
#printBoard(board)



                 # demander mettre chifre
def playerInput(board):
    inp = int(input("Choisi un nombre de 1 á 9: "))
 #Convertit en entier integer
    if inp >= 1 and inp <= 9 and board[inp-1] == "-":
       board[inp-1] = currentPlayer
    else:
        print("Choisi un autre nombre!")   







        # check les gangants or nul
                 
         # Global - variable accessible et modifiable depuis n'importe quelle partie du code. 


      #check l'horisontal du plateu
      # != "-" vérifie que les cases ne sont pas vides + si elles sont egale
      # si - True alors y a un gagnant.
      # verifi un seul element !="-" parceque si tous les éléments de la ligne sont égaux ca suffi
      
def checkHorizontal(board):
    global winner
    if board[0] == board[1] == board[2] and board[1] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
         winner = board[3]
         return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        return True
                    



# gagnant les colones
def checkVertical(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True

    elif board[1] == board[4] == board[7] and board[1] != "-":
         winner = board[1]
         return True

    elif board[2] == board[5] == board[8] and board[2] != "-":
         winner = board[2]
         return True

# gagnant diagonale
def checkDiag(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "-":
         winner = board[2]
         return True





#  si c'est un MATCH NUL
# gameRunning -  variable globale.
# permet de modifier sa valeur depuis l'intérieur de la fonction.

def checkTie(board):
    global gameRunning

    #BOUCLE
    # verifie si toute les case sont remplie:
    if "-" not in board:
        #printBoard - une fonction (regarder plus haut)
        printBoard(board)
        print("C'est un match nul!")
        gameRunning = False

# gameRunning = False : Met fin au jeu en changeant 
#             l'état de la variable globale gameRunning.








# checkWin appelle 3 autres fonctions (responsable verifier une condition
 # de victoire differente)
def checkWin():
    if checkDiag(board) or checkHorizontal(board) or checkVertical(board):
# L'instruction IF utilise l'opérateur logique OR pour 
# combiner les résultats des trois fonctions. 
# Si l'une d'elles -> True, cela signifie - gagnant.

        print(f"Le gangant est: {winner} ")
#pour inclure une variable dans une chaîne: f-string (formatted string)





                 # switch player
def switchPlayer():
    global currentPlayer
    if currentPlayer == "x":
        currentPlayer = "O"
    else:
        currentPlayer = "x"


                # bot

def bot(board):
    while currentPlayer == "O":

        #génère un nombre aléatoire entre 0 et 8 inclus. 
        # Ce nombre représente une position sur le board
        position = random.randint(0, 8)
        if board[position] == "-":
            #si la position est vide, le bot place son O
            board[position] = "O"

            # appelle switchPlayer() (defini plus haut) 
            # pour passer le tour au joueur suivant.
            switchPlayer()
            
    



                 # check for win or tie again

while gameRunning:

    printBoard(board)
    playerInput(board)
    checkWin()
    checkTie(board)
    switchPlayer()
    bot(board)
    checkWin()
    checkTie(board)

#se répète jusqu'à ce que gameRunning devienne faux, 
# ce qui se produira quand checkWin() ou checkTie() détectera la fin du jeu.