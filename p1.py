import random
# Display function for tic-tac-toe layout
def display():
  print("- "*7)
  print('|',space_lst[0],'|',space_lst[1],'|',space_lst[2],'|')
  print("- "*7)
  print('|',space_lst[3],'|',space_lst[4],'|',space_lst[5],'|')
  print("- "*7)
  print('|',space_lst[6],'|',space_lst[7],'|',space_lst[8],'|')
  print("- "*7)


# Create tic-tac-toe board
space_mtx = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]
space_lst = [a for lst in space_mtx for a in lst]
display()

# While space_lst are open:
while ' ' in space_lst:

 # Computer randomly fills in O
  print("Computer's move...")
  while True:
    i = random.randint(0,2)
    j = random.randint(0,2)
  
    if (space_mtx[i][j] == ' '):
      # Display board
      space_mtx[i][j] = 'O'
      space_lst = [a for lst in space_mtx for a in lst]
      display()
      break
    else:
      pass
  
  #Check for win
  if ((space_lst[0] == space_lst[1] == space_lst[2] != ' ')or (space_lst[3] == space_lst[4] == space_lst[5] != ' ') or (space_lst[6] == space_lst[7] == space_lst[8] != ' ') or (space_lst[0] == space_lst[3] == space_lst[6] != ' ') or (space_lst[1] == space_lst[4] == space_lst[7] != ' ') or (space_lst[2] == space_lst[5] == space_lst[8] != ' ') or (space_lst[0] == space_lst[4] == space_lst[8] != ' ') or (space_lst[2] == space_lst[4] == space_lst[6] != ' ')):
    print('Too bad. Computer won')
    break
  if not(' ' in space_lst):
    print("It's a tie")
    break

 # Ask player to fill in X
  while True:
    try:
      i,j = map(int,input('Enter row,col for X:').split(','))
    except ValueError or IndexError:
        print('You typed something incorrectly. Try again')
    else:
        if (space_mtx[i-1][j-1] == ' '):
          # Display board
          space_mtx[i-1][j-1] = 'X'
          space_lst = [a for lst in space_mtx for a in lst]
          display()
          break
        else:
          print('Space is already filled. Try again')
          pass
 # Display board


  # Check for win
  if ((space_lst[0] == space_lst[1] == space_lst[2] != ' ')or (space_lst[3] == space_lst[4] == space_lst[5] != ' ') or (space_lst[6] == space_lst[7] == space_lst[8] != ' ') or (space_lst[0] == space_lst[3] == space_lst[6] != ' ') or (space_lst[1] == space_lst[4] == space_lst[7] != ' ') or (space_lst[2] == space_lst[5] == space_lst[8] != ' ') or (space_lst[0] == space_lst[4] == space_lst[8] != ' ') or (space_lst[2] == space_lst[4] == space_lst[6] != ' ')):
    print('Congratulations. You won')
    break
  if not(' ' in space_lst):
    print("It's a tie")
    break