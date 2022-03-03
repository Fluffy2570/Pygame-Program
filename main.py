#imports pygame
import pygame
#import constants from
from pygame import *

#Camera
Width = 500
Height = 500

enemyx = 200
enemyy = 125

enemyright = True
enemyleft = False

#Player
player_location = [0,0]

pygame.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode((Width, Height))

moveUp = False
moveLeft = False
moveDown = False
moveRight = False

player = image.load("images.png")
player = transform.scale(player, (20,20))

enemy = image.load("mario.png")
enemy = transform.scale(enemy, (30,30))

player_rect = Rect(player_location[0],player_location[1],player.get_width(),player.get_height())

enemy_rect = Rect(enemyx,enemyy,player.get_width(),player.get_height()-10)
dirt = image.load("dirt.png")
grass = image.load("grass.png")

testbox = pygame.Rect(250,150,50,50)
gamemap = [
  ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
  ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
  ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
  ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],  
  ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
  ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
  ['0','0','0','0','0','0','1','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
  ['0','0','0','0','0','0','','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
  ['0','0','0','0','1','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0','0'],
  ['1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1','1']]

def collision_test(rect, tiles):
    hit_list = []
    for tile in tiles:
        if rect.colliderect(tile):
            hit_list.append(tile)
    return hit_list

def move(rect, movement, tiles):
    collision_types = {'top': False, 'bottom': False, 'right': False, 'left': False}
    rect.x += movement[0]
    hit_list = collision_test(rect, tiles)
    for tile in hit_list:
        if movement[0] > 0:
            rect.right = tile.left
            collision_types['right'] = True
        elif movement[0] < 0:
            rect.left = tile.right
            collision_types['left'] = True
    rect.y += movement[1]
    hit_list = collision_test(rect, tiles)
    for tile in hit_list:
        if movement[1] > 0:
            rect.bottom = tile.top
            collision_types['bottom'] = True
        elif movement[1] < 0:
            rect.top = tile.bottom
            collision_types['top'] = True
    return rect, collision_types

player_y_momentum = 0
air_timer = 0

while True:
  screen.fill(((0, 155, 255)))


    

  tile_rects = []
  y = 0
  for row in gamemap:
    x = 0
    for tile in row:
      if tile == '1':
        screen.blit(grass,(x*16, y * 16))
      if tile == '2':
        screen.blit(dirt,(x*16, y * 16))
      if tile != '0':
        tile_rects.append(pygame.Rect(x*16,y*16,16,16))
      x += 1
    y += 1

  if(enemyright == True):
    enemyx += 2
    if(enemyx > 250):
      enemyright = False
      enemyleft = True
  if(enemyleft == True):
    enemyx -= 2
    if(enemyx < 200):
      enemyright = True
      enemyleft = False

  screen.blit(player, (player_rect.x, player_rect.y))
 


 
  player_movement = [0, 0]
  if moveRight:
      player_movement[0] += 2
  if moveLeft:
      player_movement[0] -= 2
  player_movement[1] += player_y_momentum
  player_y_momentum += 0.2
  if player_y_momentum > 3:
      player_y_momentum = 3

  player_rect, collisions = move(player_rect, player_movement, tile_rects)

  if collisions['bottom']:
      player_y_momentum = 0
      air_timer = 0
  else:
      air_timer += 1

  for event in pygame.event.get():

    if(event.type == QUIT):
      pass
    if(event.type == KEYDOWN):
      if(event.key == K_LEFT):
        moveLeft = True
      if(event.key == K_RIGHT):
        moveRight = True
      if(event.key == K_DOWN):
        moveDown = True
      if(event.key == K_UP):
        player_y_momentum -= 5
    if(event.type == KEYUP):
      if(event.key == K_LEFT):
        moveLeft = False
      if(event.key == K_RIGHT):
        moveRight = False
      if(event.key == K_UP):
        moveDown = False
      if(event.key == K_UP):
        moveUp = False

  pygame.display.update()
  clock.tick(45)
