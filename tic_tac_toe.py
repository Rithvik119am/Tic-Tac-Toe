import pygame as py
import random
import time
import game_logic as gg
random.seed(time.time())
from sys import exit
def now_move():
    global move
    move+=1
    if move%2==0:
        return "X"
    return "O"
def display(board):
    x_pos=80
    y_pos=50
    for i in board:
        for j in i:
            screen.blit(font_style1.render(str(j),True,"Black"),(x_pos,y_pos))
            x_pos+=100
        x_pos=80
        y_pos+=100
def win_check():
    checker=game_board.win_check_m()
    if checker[0] and checker[1]=='X':
        screen.blit(x_wins_background,(0,0))
    if checker[0] and checker[1]=='O':
        screen.blit(o_wins_background,(0,0))
def tie_check():
    checker=True
    for i in game_board:
        for j in i:
            if j =='':
                checker=False
    if checker:
        screen.blit(tie_background,(0,0))
py.init()
clock=py.time.Clock()
screen=py.display.set_mode((400,400))
py.display.set_caption("Tic Tac Toe")
font_style1=py.font.Font('assets/DS-DIGI.TTF',100)
background=py.image.load("assets/background.png").convert()
x_wins_background=py.image.load('assets/X_win.png').convert()
o_wins_background=py.image.load('assets/o_win.png').convert()
tie_background=py.image.load("assets/tie.png")
box1=py.Rect(55,55,95,95)
box2=py.Rect(155,55,95,95)
box3=py.Rect(255,55,95,95)
box4=py.Rect(55,155,95,95)
box5=py.Rect(155,155,95,95)
box6=py.Rect(255,155,95,95)
box7=py.Rect(55,255,95,95)
box8=py.Rect(155,255,95,95)
box9=py.Rect(255,255,95,95)
game_board=gg.Board()
move=1
while True:
    for events in py.event.get():
        mouse_pos=py.mouse.get_pos()
        mouse_click=py.mouse.get_pressed()
        if events.type==py.QUIT:
            py.quit()
            exit()
        if events.type==py.MOUSEBUTTONDOWN:
            if box1.collidepoint(mouse_pos) and mouse_click[0] and game_board.data[0][0]=='':
                game_board.data[0][0]=now_move()
            elif box2.collidepoint(mouse_pos) and mouse_click[0] and game_board.data[0][1]=='':
                game_board.data[0][1]=now_move()
            elif box3.collidepoint(mouse_pos) and mouse_click[0] and game_board.data[0][2]=='':
                game_board.data[0][2]=now_move()
            elif box4.collidepoint(mouse_pos) and mouse_click[0] and game_board.data[1][0]=='':
                game_board.data[1][0]=now_move()
            elif box5.collidepoint(mouse_pos) and mouse_click[0] and game_board.data[1][1]=='':
                game_board.data[1][1]=now_move()
            elif box6.collidepoint(mouse_pos) and mouse_click[0] and game_board.data[1][2]=='':
                game_board.data[1][2]=now_move()
            elif box7.collidepoint(mouse_pos) and mouse_click[0] and game_board.data[2][0]=='':
                game_board.data[2][0]=now_move()
            elif box8.collidepoint(mouse_pos) and mouse_click[0] and game_board.data[2][1]=='':
                game_board.data[2][1]=now_move()
            elif box9.collidepoint(mouse_pos) and mouse_click[0] and game_board.data[2][2]=='':
                game_board.data[2][2]=now_move()
    screen.blit(background,(0,0))
    display(game_board)
    clock.tick(60)
    win_check()
    tie_check()
    py.display.update()
    
            