import traceback
import sys

class Board:
    def __init__(self, size = 3):
        self.__board = [[-1 for x in range(size)] for y in range(size)]
        self.__mark = ['0','x']
        self.size = size
        self.__valid = True
        self.__complete = False
        self.__winner = -1
        self.__curplayer = 1


    def __check__equal(self, arr):
        return all(x == arr[0] for x in arr)

    def PrintBoardState(self):
        print(self.__board)

    def CheckIfGameOver(self):
        for row in self.__board:
            if self.__check__equal(row) == True and row[0] != -1:
                self.__winner = row[0]
                self.__complete = True
                return self.__complete, self.__winner

        for i in range(0,self.size):
            col = [self.__board[j][i] for j,row in enumerate(self.__board)]
            if self.__check__equal(col) == True and col[0] != -1:
                self.__winner = col[0]
                self.__complete = True
                return self.__complete, self.__winner

        diag1 = [self.__board[i][i] for i in range(0,self.size)]
        if self.__check__equal(diag1) == True and diag1[0] != -1:
            self.__winner = diag1[0]
            self.__complete = True
            return self.__complete, self.__winner

        diag2 = [self.__board[i][self.size - i - 1] for i in range(0,self.size)]
        if self.__check__equal(diag2) == True and diag2[0] != -1:
            self.__winner = diag2[0]
            self.__complete = True
            return self.__complete, self.__winner

        return self.__complete, self.__winner

    def SetMark(self, mark, index):
        if(int(index) <1 or int(index) >9):
            print("Invalid index, enter index between [1,9]")
            return False

        x = int((index - 1)/3)
        y = (index - 1) % 3

        if self.__board[x][y] != -1:
            print("There is already a move made on this index. Please select a valid index")
            return False

        self.__board[x][y] = mark
        self.DisplayBoard()
        return True

    def DisplayBoard(self):
        for row in self.__board:
            for e in row:
                elem = '_'
                if e == 1:
                    elem = 'x'
                if e == 0:
                    elem = '0'
                print("\t\t",elem, end = '')
            print("\n\n")

    def CheckComplete(self):
        return self.__complete

    def CheckWinner(self):
        return self.__winner

class GamePlay:
    def __init__(self, user = 'x'):
        self.__users = [1,0]
        self.__human = [True,False] # Player 0 is human, player 1 is AI
        self.__curplayer   = 0 # This is position in the list
        self.__moves_available = [i for i in range(1,10)]
        print(self.__moves_available)
        if user == '0':
            self.__users = [0,1]
            self.__curplayer = 1
        self.__b = Board()

    def __simple__ai(self):
        import time
        time.sleep(1)
        return self.__moves_available[0]

    def __make__move(self, difficult = 0):
        move = 0
        if self.__human[self.__curplayer] == True:
            while True:
                print("Please make your move by entering the index")
                index = int(input())
                if self.__b.SetMark(self.__users[self.__curplayer],index) == True:
                    move = index
                    break
        else:
            print("### Its the computers turn ####")
            if difficult == 0:
                index = self.__simple__ai()
                self.__b.SetMark(self.__users[self.__curplayer],index)
                move = index

        self.__moves_available.remove(move)

    def StartGame(self):
        while self.__b.CheckComplete() == False and len(self.__moves_available) != 0:
            self.__make__move()
            comp,win = self.__b.CheckIfGameOver()
            print(comp,win)
            self.__curplayer = not self.__curplayer

        if self.__b.CheckWinner() == -1:
            print("Well Played the game finished in a draw")
        else:
            if self.__human[self.__b.CheckWinner()] == False:
                print("Sorry! :( Computer has won")
            else:
                print("Congratulations Human! You have won")

def main():
    try:
        print("Welcome to tic tac toe")
        #'''
        while True:
            print("Please Enter x or 0 as the player of choice. x plays first")
            ch = input()
            if ch =='x' or ch =='0':
                if(ch == 'x'):
                    g = GamePlay('x')
                else:
                    g = GamePlay('0')
                g.StartGame()
                break
            else:
                print("Incorrect Input")
        #'''    
        #b = Board()
        #b.PrintBoardState()
        #print(b.CheckIfGameOver())
    except:
        traceback.print_exc(file=sys.stdout)

if __name__ == '__main__':
    main()