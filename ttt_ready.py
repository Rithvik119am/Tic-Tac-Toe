import pygame as py
import game_logic as gg
import draw_surface as ds
from sys import exit
def ai():
    
    global game_board
    rithvik=gg.AI(game_board,"X","O")
    if game_board.full():
        return
    ai_move=rithvik.find_best_move()
    game_board.data[ai_move[0]][ai_move[1]]="O"
def now_move():
    global move
    move+=1
    if move%2==0:
        return "X"
    return "O"
def now_move_ai():
    global move
    move=0
    move+=2
    if move%2==0:
        return "X"
def display(board):
    x_pos=65
    y_pos=45
    for i in board:
        for j in i:
            screen.blit(font_style.render(str(j),True,"Black"),(x_pos,y_pos))
            x_pos+=100
        x_pos=65
        y_pos+=100
def win_check():
    global x_win_count,o_win_count,ss,move,game_state_key
    checker=game_board.win_check_m()
    if checker[0] and checker[1]=='X':
        move=1
        screen.blit(x_wins_background,(0,0))
        if game_state_key==game_play_key_human_Vs_human:
            game_state_key=x_win_key
        elif game_state_key==game_play_key_human_Vs_ai:
            game_state_key=x_win_ai_key
        if ss==0:
            x_win_count+=100
            ss=1
    if checker[0] and checker[1]=='O':
        screen.blit(o_wins_background,(0,0))
        if game_state_key==game_play_key_human_Vs_human:
            game_state_key=o_win_key
        elif game_state_key==game_play_key_human_Vs_ai:
            game_state_key=o_win_ai_key
        if ss==0:
            o_win_count+=100
            ss=1
def tie_check():
    global move,game_state_key
    checker=True
    for i in game_board:
        for j in i:
            if j =='':
                checker=False
    if checker:
        if game_state_key==game_play_key_human_Vs_human:
            game_state_key=tie_key
        elif game_state_key==game_play_key_human_Vs_ai:
            game_state_key=tie_ai_key
        move=1
        screen.blit(tie_background,(0,0))
def clear_board():
    global game_board,ss
    ss=0
    for i in range(0,3):
        for j in range(0,3):
            game_board.data[i][j]=''
def menu_flow():
    global game_state_key
    screen.blit(menu_background,(0,0))
    hum_vs_hum_button.hover_effect(screen)
    hum_vs_ai_button.hover_effect(screen)
    info.draw(screen)
    rules.draw(screen)
    if hum_vs_hum_button.is_clicked():
        game_state_key=game_play_key_human_Vs_human
    if hum_vs_ai_button.is_clicked():
        game_state_key=game_play_key_human_Vs_ai
    if info.is_clicked():
        game_state_key=info_key
    if rules.is_clicked():
        game_state_key=rules_key
py.init()
ss=0
clock=py.time.Clock()
screen=py.display.set_mode((400,400))
py.display.set_caption("Tic Tac Toe")
font_style=py.font.SysFont ("Times New Roman",100)
font_style1=py.font.Font(None,50)
background=ds.board_background()
x_wins_background=ds.winscreen("X")
o_wins_background=ds.winscreen("o")
tie_background=ds.tiescreen()
back_button=ds.back()
relode=ds.relode()
menu_background=ds.menu()
rules_background=ds.rules()
info_background=ds.info()
box1=py.Rect(55,55,95,95)
box2=py.Rect(155,55,95,95)
box3=py.Rect(255,55,95,95)
box4=py.Rect(55,155,95,95)
box5=py.Rect(155,155,95,95)
box6=py.Rect(255,155,95,95)
box7=py.Rect(55,255,95,95)
box8=py.Rect(155,255,95,95)
box9=py.Rect(255,255,95,95)
box10=py.Rect(0,0,40,40)
box11=py.Rect(0,40,80,40)
game_board=gg.Board()
hum_vs_hum_button=gg.Button(180,30,190,90,(135, 0, 28),(255, 117, 26),"Human", "Vs"," Human",(255,117,26),30,(135, 0, 28),(0,0,0))
hum_vs_ai_button=gg.Button(16,266,180,100,(135, 0, 28),(255, 117, 26),"Human", "Vs","   AI",(255,117,26),30,(135, 0, 28),(0,0,0))
info=gg.Button(300,290,75,50,(135, 0, 28),(255, 117, 26),"Info",None,None,(255,117,26),30,(135, 0, 28),(0,0,0))
rules=gg.Button(295,350,90,50,(135, 0, 28),(255, 117, 26),"Rules",None,None,(255,117,26),30,(135, 0, 28),(0,0,0))
x_win_count=0
o_win_count=0
move=1
game_state_key=0
menu_key=0
game_play_key_human_Vs_human=1
game_play_key_human_Vs_ai=2
rules_key=3
x_win_key=4
o_win_key=5
tie_key=8
x_win_ai_key=6
o_win_ai_key=7
tie_ai_key=9
info_key=10
while True:
    for events in py.event.get():
        mouse_pos=py.mouse.get_pos()
        mouse_click=py.mouse.get_pressed()
        if events.type==py.QUIT:
            py.quit()
            exit()
        if game_state_key==menu_key:
            pass
        elif game_state_key==rules_key or game_state_key==info_key:
            if box10.collidepoint(mouse_pos) and mouse_click[0]:
                    game_state_key=menu_key
        elif game_state_key==game_play_key_human_Vs_human:   
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
                elif box10.collidepoint(mouse_pos) and mouse_click[0]:
                    move=1
                    game_state_key=menu_key
                    clear_board()
                elif box11.collidepoint(mouse_pos) and mouse_click[0]:
                    clear_board()
                    x_win_count=0
                    o_win_count=0
        elif (game_state_key==x_win_key or game_state_key==o_win_key or game_state_key==tie_key) and box10.collidepoint(mouse_pos) and mouse_click[0]:
            clear_board()
            game_state_key=game_play_key_human_Vs_human
        elif (game_state_key==x_win_ai_key or game_state_key==o_win_ai_key or game_state_key==tie_ai_key) and box10.collidepoint(mouse_pos) and mouse_click[0]:
            clear_board()
            game_state_key=game_play_key_human_Vs_ai
        elif game_state_key==game_play_key_human_Vs_ai:   
            if events.type==py.MOUSEBUTTONDOWN:
                if box1.collidepoint(mouse_pos) and mouse_click[0] and game_board.data[0][0]=='':
                    game_board.data[0][0]=now_move_ai()
                    ai()
                elif box2.collidepoint(mouse_pos) and mouse_click[0] and game_board.data[0][1]=='':
                    game_board.data[0][1]=now_move_ai()
                    ai()
                elif box3.collidepoint(mouse_pos) and mouse_click[0] and game_board.data[0][2]=='':
                    game_board.data[0][2]=now_move_ai()
                    ai()
                elif box4.collidepoint(mouse_pos) and mouse_click[0] and game_board.data[1][0]=='':
                    game_board.data[1][0]=now_move_ai()
                    ai()
                elif box5.collidepoint(mouse_pos) and mouse_click[0] and game_board.data[1][1]=='':
                    game_board.data[1][1]=now_move_ai()
                    ai()
                elif box6.collidepoint(mouse_pos) and mouse_click[0] and game_board.data[1][2]=='':
                    game_board.data[1][2]=now_move_ai()
                    ai()
                elif box7.collidepoint(mouse_pos) and mouse_click[0] and game_board.data[2][0]=='':
                    game_board.data[2][0]=now_move_ai()
                    ai()
                elif box8.collidepoint(mouse_pos) and mouse_click[0] and game_board.data[2][1]=='':
                    game_board.data[2][1]=now_move_ai()
                    ai()
                elif box9.collidepoint(mouse_pos) and mouse_click[0] and game_board.data[2][2]=='':
                    game_board.data[2][2]=now_move_ai()
                    ai()
                elif box10.collidepoint(mouse_pos) and mouse_click[0]:
                    move=1
                    game_state_key=menu_key
                    clear_board()
                elif box11.collidepoint(mouse_pos) and mouse_click[0]:
                    clear_board()
                    x_win_count=0
                    o_win_count=0            
    if game_state_key==menu_key:
        menu_flow()
    elif game_state_key==game_play_key_human_Vs_human:
        screen.blit(background,(0,0))
        display(game_board)
        screen.blit(font_style1.render(f"X : {x_win_count}",True,"Black"),(70,7))
        screen.blit(font_style1.render(f"O : {o_win_count}",True,"Black"),(250,7))
        win_check()
        tie_check()
        screen.blit(relode,(0,40))
        screen.blit(back_button,(0,0))
        for i in range(0,81,40):
            py.draw.line(screen,"Black",(2,i),(40,i),3)
        for i in range(0,41,40):
            py.draw.line(screen,"Black",(i,2),(i,40),3)
        py.draw.line(screen,"Black",(0,40),(0,80),3)
        py.draw.line(screen,"Black",(40,40),(40,80),3)
    elif game_state_key==game_play_key_human_Vs_ai:
        screen.blit(background,(0,0))
        display(game_board)
        screen.blit(font_style1.render(f"X : {x_win_count}",True,"Black"),(70,7))
        screen.blit(font_style1.render(f"O : {o_win_count}",True,"Black"),(250,7))
        win_check()
        tie_check()
        screen.blit(relode,(0,40))
        screen.blit(back_button,(0,0))
        for i in range(0,81,40):
            py.draw.line(screen,"Black",(2,i),(40,i),3)
        for i in range(0,41,40):
            py.draw.line(screen,"Black",(i,2),(i,40),3)
        py.draw.line(screen,"Black",(0,40),(0,80),3)
        py.draw.line(screen,"Black",(40,40),(40,80),3)
    elif game_state_key==info_key:
        screen.blit(info_background,(0,0))
        screen.blit(back_button,(0,0))
        hum_vs_hum=gg.Button(180,20,190,90,(135, 0, 28),(255, 117, 26),"Human", "Vs"," Human",(255,117,26),30,(135, 0, 28),(0,0,0))
        hum_vs_ai=gg.Button(180,140,190,90,(135, 0, 28),(255, 117, 26),"Human", "Vs","   AI",(255,117,26),30,(135, 0, 28),(0,0,0))
        hum_vs_hum.hover_effect(screen)
        hum_vs_ai.hover_effect(screen)
    elif game_state_key==rules_key:
        screen.blit(rules_background,(0,0))
        screen.blit(back_button,(0,0))
    clock.tick(60) 
    py.display.update()         