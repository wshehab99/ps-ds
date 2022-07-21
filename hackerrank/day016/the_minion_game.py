def minion_game(string):
    player1=0
    player2=0
    for i in range(len(string)):
        if string[i] in 'AEIOU':
            player1+= len(string)-i 
        else :
            player2+=len(string)-i

    if player1 > player2:
        print("Kevin", player1)
    elif player1 < player2:
        print("Stuart",player2)
    else:
        print("Draw")

s=input()
minion_game(s)