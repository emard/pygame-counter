#!/usr/bin/env python3

# AUTHOR=EMARD
# LICENSE=GPL

import pygame
import struct
import socket

pygame.init()
width = 1024
height = width // 4
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption(u'Press PAUSE to quit')
pygame.display.flip()
pygame.event.set_grab(True)
pygame.mouse.set_visible(False)
font = pygame.font.SysFont('DSEG14 Classic', height)

def show_display():
    text = str("%05d" % counter)
    screen.fill((0,0,0))
    screen.blit(font.render(text, True, (255, 255, 255)), (0, 0))
    pygame.display.flip()

try:
  f = open("counter.txt", "r")
  counter = int(f.readline())
  f.close()
  del f
except:
  counter = 0

show_display()
while(True):
  event = pygame.event.wait()
  if event.type == pygame.KEYDOWN:
    if event.key == pygame.K_SPACE:
      counter += 1
    if event.key == pygame.K_1:
      counter += 10000
    if event.key == pygame.K_2:
      counter = (counter // 10000) * 10000 + ((counter + 1000) % 10000)
    if event.key == pygame.K_3:
      counter = (counter // 1000) * 1000 + ((counter + 100) % 1000)
    if event.key == pygame.K_4:
      counter = (counter // 100) * 100 + ((counter + 10) % 100)
    if event.key == pygame.K_5:
      counter = (counter // 10) * 10 + ((counter + 1) % 10)
    counter %= 100000
    show_display()
    f = open("counter.txt", "w")
    f.seek(0)
    f.write("%05d\n" % counter)
    f.close()
    del f
    if event.key == pygame.K_PAUSE:
      break
    continue
