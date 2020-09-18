import curses
import os
import playsound
import time

from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN
from random import randint

class SnakeGame:
	def __init__(self):
		playsound.playsound('/Users/ssaxena/Desktop/snake_game/background.mp3',False)
		curses.initscr()
		curses.start_color()
		curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLUE)
		self.window = curses.newwin(20, 50, 0, 0)
		self.window.keypad(1)
		self.window.bkgd(' ', curses.color_pair(1))
		self.key = KEY_RIGHT

		self.score = 0
		
		self.snake = [[4,10], [4,9], [4,8]] 
		
		self.food = [10,20]
		self.render_sceen()

	def render_sceen(self):
		self.window.addstr(0, 0, '|########## Score : ' + str(self.score) + ' SNAKE GAME ###############|')
		self.window.addch(self.food[0], self.food[1], '*')
		for i in range(1,20):
			self.window.addstr(i-1, 0, '|') 
			self.window.addstr(i-1, 49, '|')

		for i in range(1,48):
			self.window.addstr(19,i, '-')

		self.window.addstr(19, 0, '|')
		self.window.addstr(19, 48, '-')
		

	def start(self):
		while self.key!=27:
			self.window.addstr(0, 0, '|########## Score : ' + str(self.score) + ' SNAKE GAME ###############|')
			self.window.timeout(150 - (len(self.snake)/100)%120)
			prevKey = self.key                                                
			event = self.window.getch()

			self.key = self.key if event == -1 else event 
			# print(self.snake)

			if self.key == ord(' '):                                            
			    self.key = -1                                                   
			    while self.key != ord(' '):
			        self.key = self.window.getch()
			    self.key = prevKey
			    continue

			if self.key not in [KEY_LEFT, KEY_RIGHT, KEY_UP, KEY_DOWN, 27]:     
			    self.key = prevKey


			self.snake.insert(0, [self.snake[0][0] + (self.key == KEY_DOWN and 1) + (self.key == KEY_UP and -1), self.snake[0][1] + (self.key == KEY_LEFT and -1) + (self.key == KEY_RIGHT and 1)])

			if self.snake[0][0] == 0 or self.snake[0][0] == 19 or self.snake[0][1] == 0 or self.snake[0][1] == 49:
				os.system(" say ohh fuck")
				time.sleep(1)
				break

			if self.snake[0] in self.snake[1:]:
				os.system(" say ohh fuck")
				break


			if self.snake[0] == self.food:                                         
			    self.food = []
			    self.score += 1
			    while self.food == []:
			        self.food = [randint(1, 18), randint(1, 48)]                 
			        if self.food in self.snake: self.food = []
			    self.window.addch(self.food[0], self.food[1], '*')
			    playsound.playsound('/Users/ssaxena/Desktop/snake_game/eating.mp3',False)
			else:    
			    last = self.snake.pop()                                        
			    self.window.addch(last[0], last[1], ' ')
			self.window.addch(self.snake[0][0], self.snake[0][1], '#')

		curses.endwin()



snake_game = SnakeGame()
snake_game.start()

