#!/usr/bin/env python3

# AUTHOR=EMARD
# LICENSE=GPL

import pygame
import struct
import socket

pygame.init()
(width, height) = (512, 128)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption(u'Press PAUSE to quit')
pygame.display.flip()
pygame.event.set_grab(True)
pygame.mouse.set_visible(False)
font = pygame.font.SysFont('DSEG14 Classic', height)

event2ps2 = {
      pygame.K_1            : 0x16,
      pygame.K_2            : 0x1E,
      pygame.K_3            : 0x26,
      pygame.K_4            : 0x25,
      pygame.K_5            : 0x2E,
      pygame.K_6            : 0x36,
      pygame.K_7            : 0x3D,
      pygame.K_8            : 0x3E,
      pygame.K_9            : 0x46,
      pygame.K_0            : 0x45,
      pygame.K_MINUS        : 0x4E,
      pygame.K_EQUALS       : 0x55,
      pygame.K_BACKSPACE    : 0x66,
      pygame.K_TAB          : 0x0D,
      pygame.K_q            : 0x15,
      pygame.K_w            : 0x1D,
      pygame.K_e            : 0x24,
      pygame.K_r            : 0x2D,
      pygame.K_t            : 0x2C,
      pygame.K_y            : 0x35,
      pygame.K_u            : 0x3C,
      pygame.K_i            : 0x43,
      pygame.K_o            : 0x44,
      pygame.K_p            : 0x4D,
      pygame.K_LEFTBRACKET  : 0x54,
      pygame.K_RIGHTBRACKET : 0x5B,
      pygame.K_CAPSLOCK     : 0x58,
      pygame.K_a            : 0x1C,
      pygame.K_s            : 0x1B,
      pygame.K_d            : 0x23,
      pygame.K_f            : 0x2B,
      pygame.K_g            : 0x34,
      pygame.K_h            : 0x33,
      pygame.K_j            : 0x3B,
      pygame.K_k            : 0x42,
      pygame.K_l            : 0x4B,
      pygame.K_SEMICOLON    : 0x4C,
      pygame.K_QUOTE        : 0x52,
      pygame.K_RETURN       : 0x5A,
      pygame.K_LSHIFT       : 0x12,
      pygame.K_z            : 0x1A,
      pygame.K_x            : 0x22,
      pygame.K_c            : 0x21,
      pygame.K_v            : 0x2A,
      pygame.K_b            : 0x32,
      pygame.K_n            : 0x31,
      pygame.K_m            : 0x3A,
      pygame.K_COMMA        : 0x41,
      pygame.K_PERIOD       : 0x49,
      pygame.K_SLASH        : 0x4A,
      pygame.K_RSHIFT       : 0x59,
      pygame.K_LCTRL        : 0x14,
      pygame.K_LALT         : 0x11,
      pygame.K_SPACE        : 0x29,
      pygame.K_RALT         :(0x11 | 0x80),
      pygame.K_RCTRL        :(0x14 | 0x80),
      pygame.K_INSERT       :(0x70 | 0x80),
      pygame.K_DELETE       :(0x71 | 0x80),
      pygame.K_HOME         :(0x6C | 0x80),
      pygame.K_END          :(0x69 | 0x80),
      pygame.K_PAGEUP       :(0x7D | 0x80),
      pygame.K_PAGEDOWN     :(0x7A | 0x80),
      pygame.K_UP           :(0x75 | 0x80),
      pygame.K_DOWN         :(0x72 | 0x80),
      pygame.K_LEFT         :(0x6B | 0x80),
      pygame.K_RIGHT        :(0x74 | 0x80),
      pygame.K_NUMLOCK      :(0x77 | 0x80),
      pygame.K_KP7          : 0x6C,
      pygame.K_KP4          : 0x6B,
      pygame.K_KP1          : 0x69,
      pygame.K_KP_DIVIDE    :(0x4A | 0x80),
      pygame.K_KP8          : 0x75,
      pygame.K_KP5          : 0x73,
      pygame.K_KP2          : 0x72,
      pygame.K_KP0          : 0x70,
      pygame.K_KP_MULTIPLY  : 0x7C,
      pygame.K_KP9          : 0x7D,
      pygame.K_KP6          : 0x74,
      pygame.K_KP3          : 0x7A,
      pygame.K_KP_PLUS      : 0x79,
      pygame.K_KP_ENTER     :(0x5A | 0x80),
      pygame.K_ESCAPE       : 0x76,
      pygame.K_F1           : 0x05,
      pygame.K_F2           : 0x06,
      pygame.K_F3           : 0x04,
      pygame.K_F4           : 0x0C,
      pygame.K_F5           : 0x03,
      pygame.K_F6           : 0x0B,
      pygame.K_F7           : 0x83,
      pygame.K_F8           : 0x0A,
      pygame.K_F9           : 0x01,
      pygame.K_F10          : 0x09,
      pygame.K_F11          : 0x78,
      pygame.K_F12          : 0x07,
      pygame.K_SCROLLOCK    : 0x7E,
      pygame.K_BACKSLASH    : 0x5D,
}


def show_display():
    text = str("%05d" % counter)
    screen.fill((0,0,0))
    screen.blit(font.render(text, True, (255, 255, 255)), (0, 0))
    pygame.display.flip()

try:
  f = open("counter.txt", "r")
  counter = int(f.readline())
  f.close()
except:
  counter = 0

f = open("counter.txt", "w")
show_display()
while(True):
  event = pygame.event.wait()
  if event.type == pygame.KEYDOWN:
    if event.key == pygame.K_PAUSE:
      f.close()
      break
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
    f.seek(0)
    f.write("%05d\n" % counter)
    continue

