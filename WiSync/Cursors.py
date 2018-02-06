import pygame

__textselect_strings = (               # sized 24x24
  "XXXXXXXXXXXXXXXX        ",
  "X..............X        ",
  "XXXXXXX..XXXXXXX        ",
  "      X..X              ",
  "      X..X              ",
  "      X..X              ",
  "      X..X              ",
  "      X..X              ",
  "      X..X              ",
  "      X..X              ",
  "      X..X              ",
  "      X..X              ",
  "      X..X              ",
  "      X..X              ",
  "XXXXXXX..XXXXXXX        ",
  "X..............X        ",
  "XXXXXXXXXXXXXXXX        ",
  "                        ",
  "                        ",
  "                        ",
  "                        ",
  "                        ",
  "                        ",
  "                        ")

__HCURS_text_select, __HMASK_text_select = pygame.cursors.compile(__textselect_strings, 'X', '.', 'o')
text_select = ((24, 24), (5, 1), __HCURS_text_select, __HMASK_text_select)

__block_strings = (               # sized 24x24
  "XXXXXXXXXXXXXXXXXXXXXXXX",
  "X......................X",
  "X......................X",
  "X......................X",
  "X......................X",
  "X......................X",
  "X......................X",
  "X......................X",
  "X......................X",
  "X......................X",
  "X......................X",
  "X......................X",
  "X......................X",
  "X......................X",
  "X......................X",
  "X......................X",
  "X......................X",
  "X......................X",
  "X......................X",
  "X......................X",
  "X......................X",
  "X......................X",
  "X......................X",
  "XXXXXXXXXXXXXXXXXXXXXXXX")

__HCURS_block, __HMASK_block = pygame.cursors.compile(__block_strings, 'X', '.', 'o')
block = ((24, 24), (5, 1), __HCURS_block, __HMASK_block)
