
import random

def printBoard(board):
  print('   |   |')
  print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
  print('   |   |')
  print('-----------')
  print('   |   |')
  print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
  print('   |   |')
  print('-----------')
  print('   |   |')
  print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
  print('   |   |')


def get_winner(currentBoard,currentInput):
  if(
    (currentBoard[1] == currentBoard[2] == currentBoard[3] == currentInput) or #row 1
    (currentBoard[4] == currentBoard[5] == currentBoard[6] == currentInput) or #row 2
    (currentBoard[7] == currentBoard[8] == currentBoard[9] == currentInput) or #row 3
    (currentBoard[1] == currentBoard[4] == currentBoard[7] == currentInput) or #col 1
    (currentBoard[2] == currentBoard[5] == currentBoard[8] == currentInput) or #col 2
    (currentBoard[3] == currentBoard[6] == currentBoard[9] == currentInput) or #col 3
    (currentBoard[1] == currentBoard[5] == currentBoard[9] == currentInput) or #diag 1
    (currentBoard[3] == currentBoard[5] == currentBoard[7] == currentInput)  #diag 2
    ):
    return True
  else:
    return False


def get_player_turn():  
  if(random.randint(1,2) == 1):
    return "computer"
  else:
    return "player"

def get_player_sign():
  print("Do you want to be X or O ? ")
  playerSign = input().upper()
  while not(playerSign == 'X' or playerSign =='O'):
    print("Wrong Input, Do you want to be X or O ? ")
    playerSign = input().upper()
  
  if(playerSign == 'X'):
    computerSign = 'O'
  else:
    computerSign = 'X'

  return [playerSign,computerSign]

def get_player_play(playerSign, board):
  print("Your turn, please provide one number between 1-9 :")
  playerInput = input()
  while not(playerInput.isdigit()) or int(playerInput) not in range(1, 10):
    print("Wrong input, please provide one number between 1-9 :")
    playerInput = input()
  signed = False

  while not(signed):
    if (board[int(playerInput)] != ' '):
      print("Please choose another box")
      playerInput = input().upper()
    else:
      board[int(playerInput)] = playerSign
      signed = True
  return [playerInput,board]

def get_possible_player_win(board,computerSign):
  if(computerSign == 'X'):
    testSign = 'O'
  else:
    testSign = 'X'
  dupPlayerBoard = board.copy()
  foundWinMove = False
  
  for b in range(1,10):
    if(dupPlayerBoard[b] == ' '):
      dupPlayerBoard[b] = testSign
      isWinner = get_winner(dupPlayerBoard,testSign)
      if(isWinner):
        foundWinMove = True
        return b
      else:
        dupPlayerBoard[b] = [' ']

  if(not foundWinMove) :
    return "No possible win"

def get_computer_best_move(board,computerSign):
  dupBoard = board.copy()
  foundWinMove = False
  
  for a in range(1,10):
    if(dupBoard[a] == ' '):
      dupBoard[a] = computerSign
      isWinner = get_winner(dupBoard,computerSign)
      if(isWinner):
        foundWinMove = True
        return a
      else:
        dupBoard[a] = [' ']

  if(not foundWinMove):
    willPlayerWin = get_possible_player_win(board,computerSign)
    if(not (willPlayerWin == "No possible win")):
      return willPlayerWin
    else:
      foundRandom = False
      while(not foundRandom):
        randomInput = random.randint(1,9)
        if (board[randomInput] == ' '):
          foundRandom = True
          return randomInput


def get_computer_play(computerSign, board):
  print("Its my turn :")
  signed = False
  
  while signed == False:
    computerInput = get_computer_best_move(board,computerSign)
    if (board[computerInput] == ' '):
      board[computerInput] = computerSign
      signed = True
  
  return [computerInput,board]


def grid_available(board):
  for x in range(1, len(board)):
    if(board[x] == ' '):
      return True

  return False


def challengeAgain():
  print('Do you want to try again? input Y/N only')
  try_again = input().upper()
  while (not (try_again == 'Y' or try_again == 'N')):
    print('Please input Y or N only')
    try_again = input().upper()

  if(try_again == 'Y'):
    tic_tac_toe()
  else:
    print('Bye Bye!')

def tic_tac_toe():
  defaultBoard = [' '] * 10
  print(defaultBoard)
  printBoard(defaultBoard)

  playerSign,computerSign = get_player_sign()  
  playerTurn = get_player_turn()
  currentPlayer = playerTurn
  gameEnd = False

  playerWin = False
  computerWin = False

  while not(gameEnd):
    if(not(grid_available(defaultBoard))):
      gameEnd = True
    else:
      if(currentPlayer == 'player'):
        playerInput,defaultBoard = get_player_play(playerSign, defaultBoard)
        printBoard(defaultBoard)
        hasWinner = get_winner(defaultBoard,playerSign)
        currentPlayer = 'computer'
        if(hasWinner):
          gameEnd = True
          playerWin = True
      else:
        computerInput,defaultBoard = get_computer_play(computerSign, defaultBoard)
        printBoard(defaultBoard)
        hasWinner = get_winner(defaultBoard,computerSign)
        currentPlayer = 'player'
        if(hasWinner):
          gameEnd = True
          computerWin = True

  if(gameEnd):
    if(playerWin):
      print('Congratulation, you have won the game')
    elif(computerWin):
      print('Sorry, you did not win the game')
    else:
      print('This game DRAW!')
    challengeAgain()
   
print("Tic Tac Toe Test")
print("======================================")
tic_tac_toe()