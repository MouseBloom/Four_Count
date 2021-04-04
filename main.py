def check_g(): # function checks horizontal victory
     for i in range(len(ground)):
          for j in range((len(ground[i]))-3):
               if ground[i][j] == ground[i][j+1] and ground[i][j] == ground[i][j+2] and ground[i][j] == ground[i][j+3] and ground[i][j] != 0:
                    return 'victory! '
     return ''

def check_v(): #function checks vertical victory
     for i in range(len(ground)-3):
          for j in range((len(ground[i]))):
               if ground[i][j] == ground[i+1][j] and ground[i][j] == ground[i+2][j] and ground[i][j] == ground[i+3][j] and ground[i][j] != 0:
                    return 'victory! '
     return ''

def check_d(): # function checks diagonal victory
     for i in range(len(ground) - 3):
          for j in range((len(ground[i])-3)):
               if ground[i][j] == ground[i+1][j+1] and ground[i][j] == ground[i+2][j+2] and ground[i][j] == ground[i+3][j+3] and ground[i][j] != 0:
                    return 'victory! '
     return ''


ground  = [[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]
for m in ground:
     for k in m:
          print(k, end=' ')
     print()
print('1 - means first player`s points \n2 - means second player`s points ')
for i in range(43): # main part of all this with turn choices and other stuff
     pl1 = int(input('Player1: Write index of column '))
     pl1 -= 1
     c = 0
     while c < 6:
          if ground[c][pl1] == 0:
               ground[c][pl1] = 1
               break
          if c == 5 and ground[c][pl1] != 0:
               print('You can`t make this choice')
               pl1 = int(input('Player1: Write index of column '))
               pl1 -= 1
               c = -1
          c += 1
     ground1 = ground.copy()
     ground1.reverse()
     for m in ground1:
          for k in m:
               print(k, end= ' ')
          print()
     print(check_g(),end='')
     if check_g() == 'victory! ':
          print('Player 1 wins, 4 horizontally!!!')
          exit()
     print(check_v(),end='')
     if check_v() == 'victory! ':
          print('Player 1 wins, 4 vertically!!!')
          exit()
     print(check_d())
     if check_d() == 'victory! ':
          print('Player 1  wins, 4 diagonally!!!')
          exit()


     pl2 = int(input('Player2: Write index of column '))
     pl2 -= 1
     c = 0
     while c < 6:
          if ground[c][pl2] == 0:
               ground[c][pl2] = 2
               break
          if c == 5 and ground[c][pl2] != 0:
               print('You can`t make this choice')
               pl2 = int(input('Player2: Write index of column '))
               pl2 -= 1
               c = -1
          c += 1
     ground1 = ground.copy()
     ground1.reverse()
     for m in ground1:
          for k in m:
               print(k, end=' ')
          print()
     print(check_g(),end='')
     if check_g() == 'victory! ':
           print('Player 2 wins, 4 horizontally!!')
           exit()
     print(check_v(),end='')
     if check_v() == 'victory! ':
          print('Player 2 wins, 4 vertically!!!')
          exit()
     print(check_d())
     if check_d() == 'victory! ':
          print('Player 2 wins, 4 diagonally!!!')
          exit()
print('It seems we have a draw')








