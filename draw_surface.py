import pygame as py
import game_logic as gl
def board_background():
    sur_given=py.Surface((400,400))
    sur_given.fill((135, 0, 28))
    for i in range(50,351,100):
        py.draw.line(sur_given,(0,0,0),(48,i),(353,i),6)
        py.draw.line(sur_given,(0,0,0),(i,50),(i,350),6)
    return sur_given
def winscreen(a):
    sur_given=py.Surface((400,400))
    sur_given.fill((128, 0, 128))
    font = py.font.SysFont ("Times New Roman", 32)
    font1 = py.font.SysFont ("Times New Roman", 40)
    font2 = py.font.SysFont ("Times New Roman", 43)
    if a=='X':
        text1 = font.render ("You are", True,(255, 255, 255))
        text2 = font2.render ("eXcellent!", True,(255, 215, 0))
        text3 = font.render ("X have won the game!", True, (64, 224, 208))
    else:
        text1 = font.render ("Out of this world!", True, (255, 255, 255))
        text2=font.render("O is awesOme!",True,(255, 215, 0))
        text3=font1.render("O have wOn the game!",True,(64, 224, 208))
    text11=text1.get_rect()
    text22=text2.get_rect()
    text33=text3.get_rect()
    text11.center=(200,150)
    text22.center=(200,200)
    text33.center=(200,250)
    sur_given.blit(text1,text11)
    sur_given.blit(text2,text22)
    sur_given.blit(text3,text33)
    return sur_given
#to create another surface as a bachround for tie match with the following prompt "X marks the spot, but O blocks the way"
def tiescreen():
    sur_given=py.Surface((400,400))
    sur_given.fill((128, 0, 128))
    font = py.font.SysFont ("Times New Roman", 32)
    font1 = py.font.SysFont ("Times New Roman", 43)
    text = font.render ("X marks the spot,", True,(255, 255, 255))
    text1 = font1.render ("but O blocks the way", True,(255, 215, 0))
    text2 = font.render ("It's a tie!", True, (64, 224, 208)) 
    text00=text.get_rect()
    text11=text1.get_rect()
    text22=text2.get_rect()
    text00.center=(200,150)
    text11.center=(200,200)
    text22.center=(200,250)
    sur_given.blit(text,text00)
    sur_given.blit(text1,text11)
    sur_given.blit(text2,text22)
    return sur_given
def back():
    sur_given=py.Surface((40,40))
    sur_given.fill((63, 72, 204))
    py.draw.polygon(sur_given,(102, 0, 102), [(18,8), (2,19), (18,31),(18,24),(33,24),(33,14),(18,14)])
    return sur_given
def relode():
    sur_given=py.Surface((40,40))
    sur_given.fill((63, 72, 204))
    # i want to draw a reload icon here, it must look like a circle with a arrow ot the end of it
    py.draw.circle(sur_given,(102, 0, 102),(20,20),15)
    py.draw.circle(sur_given,(63, 72, 204),(20,20),5)
    return sur_given
def menu():
    sur_given = py.Surface((400,400))
    sur_given.fill((135, 0, 28))
    title_font = py.font.SysFont("Times New Roman", 70)
    title_text = title_font.render("Tic Tac Toe", True, (255, 215, 0))
    title_text_rect = title_text.get_rect()
    title_text_rect.center = (200, 180)
    title_text1 = title_font.render("Tic Tac Toe", True, (0,0, 0))
    title_text_rect1 = title_text1.get_rect()
    title_text_rect1.center = (205, 185)
    sur_given.blit(title_text1, title_text_rect1)
    sur_given.blit(title_text, title_text_rect)
    return sur_given
def info():
    sur_given = py.Surface((400,400))
    sur_given.fill((135, 0, 28))
    back_i=back()
    relode_i=relode()
    info=[">By clicking the",
          " you will enter a",
          " game with two human players",
          ">By clicking the",
          " you will enter a",
          " game with a human",
          " player and a AI",
          ">By clicking the following button",
          " you will go to the previous screen",
          " but the score does not change",
          ">By clicking thefollowing button",
          " you will clear the board and score"
        ]
    for i in range(len(info)):
        font = py.font.SysFont("Times New Roman", 20)
        text = font.render(info[i], True, (255, 215, 0))
        sur_given.blit(text,(10, 50+30*i))
    sur_given.blit(back_i,(310,270))
    sur_given.blit(relode_i,(310,350))
    return sur_given
def rules():
    sur_given=py.Surface((400,400))
    sur_given.fill((135, 0, 28))
    title_font = py.font.SysFont("Times New Roman", 60)
    text = title_font.render("Rules", True, (255, 215, 0))
    text_rect = text.get_rect()
    text_rect.center = (200, 50)
    sur_given.blit(text, text_rect)
    info=[
        ">The game is played on a grid that's 3 squares",
        "  by 3 squares.",
        ">You are X, your friend or AI is O.",
        ">Players take turns putting their marks in",
        " empty squares.",
        ">The first player to get 3 of their marks in",
        "  a row is the winner.",
        ">When all 9 squares are full, without any",
        "  player getting 3 marks in a row,",
        "  the game ends in a tie."
        ]
    title_font = py.font.SysFont("Times New Roman", 20)
    for i in range(len(info)):
        text = title_font.render(info[i], True, (255, 215, 0))
        sur_given.blit(text, (10,80+30*i))
    return sur_given