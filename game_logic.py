import pygame as py
size=3
class Board():
    def __init__(self) -> None:
        self.data=[['' for _ in range(size)] for _ in range(size)]
        self.index=0
    def __iter__(self):
        return self
    def __next__(self):
        if self.index>=len(self.data):
            self.index=0
            raise StopIteration
        result=self.data[self.index]
        self.index+=1
        return result
    def copy(self,other):
        for i in range(size):
            for j in range(size):
                other.data[i][j]=self.data[i][j]
    def win_check_m(self):
        if self.data[0][0]==self.data[1][1] and self.data[1][1]==self.data[2][2] and self.data[1][1]!='':
            return [True,self.data[0][0]]
        elif self.data[1][0]==self.data[1][1] and self.data[1][0]==self.data[1][2] and self.data[1][1]!='':
            return [True,self.data[1][0]]
        elif self.data[2][0]==self.data[2][1] and self.data[2][0]==self.data[2][2] and self.data[2][0]!='':
            return [True,self.data[2][0]]
        elif self.data[0][0]==self.data[1][0] and self.data[0][0]==self.data[2][0] and self.data[0][0]!='':
            return [True,self.data[0][0]]
        elif self.data[0][1]==self.data[1][1] and self.data[0][1]==self.data[2][1] and self.data[2][1]!='':
            return [True,self.data[1][1]]
        elif self.data[0][2]==self.data[1][2] and self.data[1][2]==self.data[2][2] and self.data[2][2]!='':
            return [True,self.data[1][2]]
        elif self.data[0][2]==self.data[1][1] and self.data[1][1]==self.data[2][0] and self.data[1][1]!='':
            return [True,self.data[1][1]]
        elif self.data[0][0]==self.data[0][1] and self.data[0][1]==self.data[0][2] and self.data[0][1]!='':
            return [True,self.data[0][1]]
        return [False,""]
    def full(self):
        for i in range(size):
            for j in range(size):
                if self.data[i][j]=='':
                    return False
        return True
class Button:
    def __init__(self,x,y,width,height,color,hover_color,text1,text2,text3,text_color,text_size,hover_text_color,hover_boder) -> None:
        self.x=x
        self.y=y
        self.width=width
        self.height=height
        self.color=color
        self.hover_color=hover_color
        self.text1=text1
        self.text2=text2
        self.text3=text3
        self.text_color=text_color
        self.text_size=text_size
        self.hover_text_color=hover_text_color
        self.hover_border=hover_boder
    def draw(self,screen):
        py.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height),border_radius=10)
        py.draw.rect(screen, self.hover_color, (self.x, self.y, self.width, self.height),border_radius=10,width=4)
        font_style=py.font.SysFont("Times New Roman", self.text_size)
        screen.blit(font_style.render(self.text1,True,self.text_color),(self.x+10,self.y+5))
        screen.blit(font_style.render(self.text2,True,self.text_color),(self.x+70,self.y+30))
        screen.blit(font_style.render(self.text3,True,self.text_color),(self.x+80,self.y+55))
    def is_hover(self):
        mouse=py.mouse.get_pos()
        if self.x<=mouse[0] and mouse[0]<=self.x+self.width and self.y<=mouse[1]and mouse[1]<=self.y+self.height:
            return True
        return False
    def hover_effect(self,screen):
        if self.is_hover():
            py.draw.rect(screen, self.hover_color, (self.x, self.y, self.width, self.height),border_radius=10)
            py.draw.rect(screen, self.hover_border, (self.x, self.y, self.width, self.height),border_radius=10,width=4)
            font_style=py.font.SysFont("Times New Roman", self.text_size)
            screen.blit(font_style.render(self.text1,True,self.hover_text_color),(self.x+80,self.y+5))
            screen.blit(font_style.render(self.text2,True,self.hover_text_color),(self.x+70,self.y+30))
            screen.blit(font_style.render(self.text3,True,self.hover_text_color),(self.x+10,self.y+55))
        else:
            self.draw(screen)
    def is_clicked(self):
        if self.is_hover():
            if py.mouse.get_pressed()[0]:
                return True
        return False
class AI:
    def __init__(self, board, human, ai):
        self.board = board
        self.min = human
        self.max = ai

    def evaluate(self, board, depth):
        if board.win_check_m()[0]:
            if board.win_check_m()[1] == self.max:
                return 10 - depth
            else:
                return -10 + depth
        return 0

    def minimax(self, board, depth, is_max):
        if board.win_check_m()[0] or board.full():
            return self.evaluate(board, depth)
        if is_max:
            best = -1000
            for i in range(size):
                for j in range(size):
                    if board.data[i][j] == '':
                        board.data[i][j] = self.max
                        best = max(best, self.minimax(board, depth + 1, False))
                        board.data[i][j] = ''
            return best
        else:
            best = 1000
            for i in range(size):
                for j in range(size):
                    if board.data[i][j] == '':
                        board.data[i][j] = self.min
                        best = min(best, self.minimax(board, depth + 1, True))
                        board.data[i][j] = ''
            return best

    def find_best_move(self):
        best_val = -1000
        best_move = [None, None]
        for i in range(size):
            for j in range(size):
                if self.board.data[i][j] == '':
                    self.board.data[i][j] = self.max
                    move_val = self.minimax(self.board, 0, False)
                    self.board.data[i][j] = ''
                    if move_val > best_val:
                        best_val = move_val
                        best_move = [i, j]
        return best_move
        