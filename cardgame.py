import pygame, random
import sys
import time
import tkinter as tk
from random import *
from Cards import Card
pygame.init()


Game_over_message = ""
message = ""

#Screen Settings
land = pygame.image.load("стол.jpg")
land = pygame.transform.scale(land, (800, 600))
SCREENWIDTH = 800
SCREENHEIGHT = 600
size = (SCREENWIDTH, SCREENHEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Card Game")
screen.blit(land, (0,0))

def print_text(message, x, y, font_color = None, font_type = 'freesansbold.ttf', font_size=30):
    font_type = pygame.font.Font(font_type, font_size)
    if font_color is None:
        font_color = (0,0,0)
    else:
        font_color = font_color
    text = font_type.render(message, True, font_color)

    screen.blit(text, (x,y))




class Button():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.active_color = (23,204,58)
        self.inactive_color = (13,162,58)

    def draw(self, x, y, text, action = None, font_size = 30, font_color = (6,13,20)):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if x<mouse[0]<x+ self.width and y<mouse[1]<y + self.height:
                pygame.draw.rect(screen,self.active_color,  (x,y,self.width,self.height))

                if click[0] == 1:

                    if action is not None:
                        action()
        else:
            pygame.draw.rect(screen, self.inactive_color, (x,y,self.width,self.height) )

        print_text(message=text, x=x+10, y=y+10, font_size=font_size)


def game_menu():
    background = pygame.transform.scale(pygame.image.load("Samurai Menu.jpg"), (800,600))
    start_button = Button (300, 70)
    show = True
    while show:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    show = False
                    print("Enter")
                    main_game()
                if event.key == pygame.K_LEFT:
                    show = False
                    print ("Briefing")
                    briefing()

        screen.blit(background, (0,0))
        print_text("Samurai Card Game", 20, 10, font_size=40)
        print_text("Press ENTER to Start", 20, 70)
        print_text("Press Left Arrow for Briefing", 20, 100)
        print_text("Samurai Card Game", 18, 10, font_size=40, font_color = (255,255,255))
        print_text("Press ENTER to Start", 18, 70, font_size=30, font_color = (255,255,255))
        print_text("Press Left Arrow for Briefing", 18, 100, font_size = 30, font_color = (255,255,255))

        pygame.display.update()
        pygame.time.Clock().tick(60)



def briefing():
    show = False
    while not show:
        screen.blit(pygame.transform.scale(pygame.image.load("черный бэкграунд.jpg"), (800, 600)), (0, 0))
        print_text("How to play the Game", 30, 30, font_size=50)
        print_text("Your cards are Fallen Samurai which are located at the top left corner.", 10, 60,
                   font_color=(255, 255, 255), font_size=20)
        print_text("You always go first. In fact, you and your enemy throw cards at the same time.", 10, 90,
                   font_color=(255, 255, 255), font_size=20)
        print_text("Click a card to play it! Put a mouse cursor on it to see it's power.", 10, 120, font_color=(255,255,255), font_size = 20 )
        print_text("The Card with greater value thrown wins.", 10, 180, font_color=(255, 255, 255), font_size=20)
        print_text("The mysterious black rectangle at the bottom right corner will show the power.", 10, 150, font_color=(255, 255, 255), font_size=20)

        print_text("Press ENTER to Start the Game", 10, 400, font_color=(0, 255, 0), font_size=50)
        pygame.display.update()
        pygame.time.Clock().tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    show = False

                    main_game()
                    print("Enter")



#all_sprites_list = pygame.sprite.Group()
def Game_over():


    screen.blit(pygame.transform.scale(pygame.image.load("Last Samurai.jpg"), (800,600)), (0,0))

    print("Game Over")

    pygame.display.flip()
    pygame.time.Clock().tick(60)


def main_game():
    # Screen Settings
  land = pygame.image.load("стол.jpg")
  land = pygame.transform.scale(land, (800, 600))
  SCREENWIDTH = 800
  SCREENHEIGHT = 600
  size = (SCREENWIDTH, SCREENHEIGHT)
  screen = pygame.display.set_mode(size)
  pygame.display.set_caption("Card Game")
  screen.blit(land, (0, 0))

  mouse_width = 10
  mouse_height = 10
  mouse_x = 0
  mouse_y = 0

    # CARDS
  Card_one = Card("Samurai Demon.jpg", 20, 30, 10)
  Card_one.rect.x = 20
  Card_one.rect.y = 50

  Card_dva = Card("Samurai Demon 2.jpg", 20, 30, 8)
  Card_dva.rect.x = 150
  Card_dva.rect.y = 50

  Card_tri = Card("Samurai Demon 3.jpg", 20, 30, 7)
  Card_tri.rect.x = 280
  Card_tri.rect.y = 50

  Card_four = Card("Ruehin.gif", 20, 30, 5)
  Card_four.rect.x = 410
  Card_four.rect.y = 50

  Enemycard_one = Card("охотник.png", 20, 30, 10)
  Enemycard_one.rect.x = 20
  Enemycard_one.rect.y = 450

  Enemycard_dva = Card("охотник 2.jpg", 20, 30, 8)
  Enemycard_dva.rect.x = 150
  Enemycard_dva.rect.y = 450

  Enemycard_tri = Card("охотник 3.jpg", 20, 30, 6)
  Enemycard_tri.rect.x = 280
  Enemycard_tri.rect.y = 450

  Enemycard_four = Card("охотник 4.png", 20, 30, 5)
  Enemycard_four.rect.x = 410
  Enemycard_four.rect.y = 450

  all_sprites_list = pygame.sprite.Group()
  all_sprites_list.add(Card_one, Card_dva, Card_tri, Card_four, Enemycard_one, Enemycard_dva, Enemycard_tri, Enemycard_four )
  Card_list = [Card_one, Card_dva, Card_tri, Card_four]
  Enemycard_list = [Enemycard_one, Enemycard_dva, Enemycard_tri, Enemycard_four]


  j=3
  Players_turn = True
  game = True
  clock = pygame.time.Clock()
  player_score = 0
  enemy_score = 0
  duel_cards = []
  while game:

    for event in pygame.event.get():
     if event.type == pygame.QUIT:
            game = False
     if Players_turn == True:

      all_sprites_list.remove(duel_cards)
      duel_cards = []
      mouse_x, mouse_y= pygame.mouse.get_pos()
      for i in Card_list:
          if i.rect.x - mouse_width < mouse_x < i.rect.x + 80 and i.rect.y - mouse_height < mouse_y < i.rect.y + 130:
              pygame.draw.rect(screen, (0,0,0), (600, 450, 80,130))
              card_force ="{card_sila}".format(card_sila = i.force)

              print_text(card_force, 610, 480, font_color = (255,255,255))


      if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1:
          mouse_x, mouse_y = pygame.mouse.get_pos()

          for i in Card_list:
             if i.rect.x - mouse_width < mouse_x < i.rect.x + 80 and i.rect.y - mouse_height < mouse_y < i.rect.y + 130:

                      i.rect.x = 400
                      i.rect.y = 300
                      duel_cards.append(i)
                      screen.blit(land, (0, 0))

                      Card_list.remove(i)

                      Players_turn = False

      if Players_turn == False:


        enemycard_index = randint(0, j)

        Enemycard_list[enemycard_index].rect.x = 200
        Enemycard_list[enemycard_index].rect.y = 300

        duel_cards.append(Enemycard_list[enemycard_index])

        if duel_cards[0].force > duel_cards[1].force:
            who_wins = 1
            player_score =player_score + 1
            print(duel_cards[0].force, duel_cards[1].force, 'Player wins duel')
        if duel_cards[0].force == duel_cards[1].force:
            player_score =player_score+ 1
            enemy_score =enemy_score+ 1
            who_wins = 2
            print(duel_cards[0].force, duel_cards[1].force,"TIE!")
        if duel_cards[0].force < duel_cards[1].force:
            enemy_score =enemy_score+ 1
            who_wins = 3
            print(duel_cards[0].force, duel_cards[1].force,"Computer wins")

        screen.blit(land, (0,0))

        print_text("Player's Score: " + str(player_score), 530, 10)
        print_text("Enemy's Score: " + str(enemy_score), 530, 40)
        if who_wins == 1:
            print_text("Player Wins a Duel!", 180, 230, font_size = 50 )

        if who_wins == 2:
            print_text("TIE!", 280, 230, font_size = 50 )

        if who_wins == 3:
            print_text("Enemy Wins a Duel!", 180, 230, font_size = 50 )




        Enemycard_list.remove(Enemycard_list[enemycard_index])

        j = j-1
        if Enemycard_list == []:
            if player_score > enemy_score:
                Game_over_message = "Spirits of Fallen Samurai Win (Player wins)"
                all_sprites_list.remove(duel_cards)
                Game_over()
                print_text(Game_over_message, 100, 30, font_color=(255, 0, 0), font_size=30)
            if player_score < enemy_score:
                Game_over_message = "Enemy Has Destroyed You"
                all_sprites_list.remove(duel_cards)
                Game_over()
                print_text(Game_over_message, 200, 30, font_color=(255, 0, 0), font_size=30)
            if player_score== enemy_score:
                Game_over_message = "Nobody was left alive. There is No Winner."
                all_sprites_list.remove(duel_cards)
                Game_over()
                print_text(Game_over_message, 100, 30, font_color=(255, 0, 0), font_size=30)





        Players_turn = True


    all_sprites_list.update()

    all_sprites_list.draw(screen)

    pygame.display.flip()
    clock.tick(60)

game_menu()

pygame.quit()



