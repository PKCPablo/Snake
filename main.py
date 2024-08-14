##################################################
# Program realized by: 	Pablo Rodríguez Gómez    #
# Contact:				pablinelchulin@gmail.com #
# Status:				Completed                #
# Project Started:  	05/06/2020               #
# Project Finalized:	08/06/2020               #
##################################################
#
#	TO DO
#
#	- Nothing :)
#
#
#

import pygame
import os
import time
import math
import random

####################################################################################
# CLASSES #
###########



	#########
	# APPLE #
	#########

	# TYPES
	# 0 -> Normal Apple 	(1p)
	# 1 -> Golden Apple 	(3p)
	# 2 -> Enchanted Apple 	(5p)

class objective:
		def __init__(self, i, init_x, init_y, t):
			self.img 	= pygame.image.load(i)
			self.x 		= 0.0 + init_x
			self.y 		= 0.0 + init_y
			self.type	= t

		def add_point(self):
			if self.type == 0:
				return 1
			elif self.type == 1:
				return 3
			elif self.type == 2:
				return 5
			else:
				print("UNEXPECTED ERROR")
				return 0

		def sD(self):
			screen.blit(self.img, (self.x, self.y))


def appleCreation(head):
	while True:
		xA = 0.0 + random.randint(0,15) * 32
		yA = 0.0 + random.randint(0,15) * 32

		last = head
		aux = False

		while last != None:
			x = last.givX()
			y = last.givY()

			distance = math.sqrt(math.pow(xA - x, 2) + math.pow(yA - y, 2))

			if distance > 0 and distance < 32:
				aux = True

			last = last.next

		if aux == True:
			continue
			print("ERROR IN CONTINUE")

			#Randomization of type of apple

		string 	= ''
		tA 		= None
		prob 	= random.randint(1,100)

		if 		prob < 60:
			string 	= 'Sprites/apples/apple_32x32.png'
			tA 		= 0
		elif 	prob < 90:
			string = 'Sprites/apples/golden_apple_32x32.png'
			tA 		= 1
		else:
			string = 'Sprites/apples/enchanted_golden_apple_32x32.png'
			tA 		= 2
		

		apple = objective(string ,xA, yA, tA)

		return apple


###################


	#########
	# SNAKE #
	#########

class obj:
	def __init__(self, i, init_x, init_y, init_dir):
		self.img 	= pygame.image.load(i)
		self.imgSD	= self.img
		self.x		= 0.0 + init_x
		self.y 		= 0.0 + init_y

		self.next	= None
		self.direction = init_dir

	#  1
	# 234

	def sD(self):

		screen.blit(self.imgSD, (self.x, self.y))

		if self.next != None:
			self.next.sD()

	def givX(self):
		return self.x
	def givY(self):
		return self.y

	def move(self, dirt, boolean, cant):

		if boolean == True:
			if self.next != None:
				nextDir = self.direction

			self.direction = dirt

		else:
			if self.next != None:
				nextDir = self.next.direction

		#Init movement
		x_ch = 0
		y_ch = 0

		#  1
		# 2-4
		#  3

		self.imgSD = self.img

		if self.direction == 1:
			x_ch 		= 0
			y_ch 		= -0.2

		elif self.direction == 2:
			x_ch 		= -0.2
			y_ch		= 0

			self.imgSD = pygame.transform.rotate(self.img, 90)

		elif self.direction == 3:
			x_ch 		= 0
			y_ch 		= 0.2

			self.imgSD = pygame.transform.rotate(self.img, 180)

		elif self.direction == 4:
			x_ch 		= 0.2
			y_ch 		= 0

			self.imgSD = pygame.transform.rotate(self.img, 270)

		self.x += x_ch * cant
		self.y += y_ch * cant

		#Give next obj direction

		if self.next != None:
			self.next.move(nextDir, boolean, cant)

		return 0.2 * cant


	#Create new object body for Snake

def addBody(last):
	dirt 	= last.direction

	difX = 0
	difY = 0

	if dirt == 1:
		difX = 0 
		difY = 32

	elif dirt == 2:
		difX = 32 
		difY = 0

	elif dirt == 3:
		difX = 0 
		difY = -32

	elif dirt == 4:
		difX = -32 
		difY = 0


	x = last.givX() + difX
	y = last.givY() + difY

	last.next 	=	obj('Sprites/snake_body/snake_body_32x32.png', x, y, dirt)

	return last.next


####################################################################################
# DEFINITIONS #
###############

	####################
	# Random Functions #
	####################

		#Line jump

def sl(): 
	print("\n")

		#Score display

def display_score(score_value, x, y):
		score = font.render("Score: " + str(score_value), True, (255, 255, 255))
		screen.blit(score, (x, y))

	######################
	# Colision Functions #
	######################

		#Apple Colision

def appleEatColision(apple, head):
	xH = head.givX()
	yH = head.givY()

	xA = apple.x
	yA = apple.y

	distance = math.sqrt(math.pow(xH - xA, 2) + math.pow(yH - yA, 2))

	if distance < 24.0:
		return True

	return False

		#Border colision detection

def borderColisionDetec(head):
	x = head.givX()
	y = head.givY()

	dirt = head.direction

		# X AXIS

	if x < -6 and dirt == 2:
		#print("Colision detected at X Axis (LEFT)")
		return True
	elif x > 485 and dirt == 4:
		#print("Colision detected at X Axis (RIGHT)")
		return True

		# Y AXIS

	if y < -6 and dirt == 1:
		#print("Colision detected at Y Axis (UP)")
		return True
	elif y > 485 and dirt == 3:
		#print("Colision detected at Y Axis (DOWN)")
		return True

	return False

		#Body colision detection

def bodyColisionDetec(head): #Terminar apuntando cabeza (direccion)
	last = head.next
	colDirt = False

	while last != None:
		xH = head.givX()
		yH = head.givY()

		xB = last.givX()
		yB = last.givY()

		distance = math.sqrt(math.pow(xH - xB, 2) + math.pow(yH - yB, 2))

		if distance < 20.0:
			#print("Colision detected")
			return True

		last = last.next

	return False

	########################
	# Game over definition #
	########################

def gameOver(scr):
	print("Game Over")

	scr.fill((0, 0, 0))
	game_over_icon = pygame.image.load('Sprites/game_over/game_over.png')
	screen.blit(game_over_icon, (0, 0))
	pygame.display.update()

	time.sleep(7.5)

	os.system("cls")
	exit()

####################################################################################
# MAIN #
########

	#Display dimension definition (px)

width 	= 512 # w = 512		, h = 512 	-> 16x16 cells de 32x32 px
height 	= 512 # w = 1024	, h = 1024	-> 16x16 cells de 64x64 px


	#Pygame init

pygame.init()

if pygame.display.get_init() != True:
	print("ERROR AT DISPLAY MONTAGE")

else:

		# Display #

	screen = pygame.display.set_mode((width, height))  			#Display Creation

	pygame.display.set_caption("Snake") 						#Title
	icon = pygame.image.load('Sprites/snake_logo.png') 			#Icon load
	pygame.display.set_icon(icon)								#Icon display

	background = pygame.image.load('Sprites/background/background.png')	#Background load

	
	##################
	# SNAKE CREATION #
	##################

		#Explanation
		# This snake was created using a node tree structure.
		# This type of sctructure means that each element saves the elements before.
		#
		# Element 1 -> Element 2 -> Element 3 -> Element 4 -> None
		#
		# 'None' is the last element of the node tree, you can use it as an indicator of the end of the tree.
		#
		# 'first' and 'last' function is to save the position of the first and the last element on the tree.


	#Snake node tree Init

	first		= None #Any node created
	last		= None #Any node created

	s_head 		= obj('Sprites/snake_head/snake_head_32x32.png', 256, 224, 1) 	#Element 1
	first 		= s_head
	last 		= s_head

	last.next 	= obj('Sprites/snake_body/snake_body_32x32.png', 256, 256, 1) 	#Element 2
	last 		= last.next

	last.next 	=	obj('Sprites/snake_body/snake_body_32x32.png', 224, 256, 4) #Element 3
	last 		= last.next

	last.next 	=	obj('Sprites/snake_body/snake_body_32x32.png', 224, 224, 3) #Element 4
	last 		= last.next

	##########################
	# END OF SNAKE NODE TREE #
	##########################

		#Movement change 				[INIT]

	x_ch 		= 0
	y_ch 		= -0.1 	#Pointing to UP

		#Movement Follow for body 		[INIT]

	direction = 1

		#Movement Limitation to 32x32 	[INIT]

	mov_total 	= 0
	lock 	= False

		#PUNTUATION and smth of apples 	[INIT]

	score = 0
	font = pygame.font.Font('Fonts/INVASION2000.ttf', 32)

	textX = 10
	textY = 10

	apple_exist = False

		# Acceleration

	bodyN = 2
	appleEated = 1

	####################
	# LOOP OF THE GAME #
	####################

	running = True
	while running:
		for event in pygame.event.get(): #Analize of each event

				#EXIT display event

			if event.type == pygame.QUIT:
				gameOver(screen)

				#Movement Key event interpretation

			if event.type == pygame.KEYDOWN:

				if event.key ==	pygame.K_UP:
					direction 	= 1

				elif event.key == pygame.K_DOWN:
					direction	= 3

				elif event.key == pygame.K_LEFT:
					direction	= 2

				elif event.key == pygame.K_RIGHT:
					direction	= 4

			#Colision detection & GAME OVER throw

		borderColision 	= borderColisionDetec(first)
		bodyColision 	= bodyColisionDetec(first)

		if borderColision or bodyColision:
			gameOver(screen)

			#Movement + Limitation 32x32

		if mov_total < 32.0:
			mov_total 	+= first.move(direction, lock, bodyN)
			lock 		= False
		else:
			mov_total 	= 0.0
			lock 		= True

			


			#Background ~ RGB [TEMPORARY] -> Replace with image

		screen.fill((30, 0, 30))
		screen.blit(background, (0, 0))

			#Display of snake

		first.sD()

			#Creation of apple

		if apple_exist == False:
			apple 		= appleCreation(first)
			apple_exist = True	

		#Display of apple

		apple.sD()

		#Colision detection & Apple delete

		if appleEatColision(apple, first):
			apple_exist = False
			last = addBody(last)
			score += apple.add_point()

			#Acceleration ratio

			appleEated += 1

			if appleEated < 5:
				bodyN += 1
			elif appleEated == 10:
				bodyN = 10
			elif appleEated == 50: #NOT TESTED
				bodyN = 20
			elif appleEated == 80: #NOT TESTED
				bodyN = 40


		#Display fo score

		display_score(score, textX, textY)


		#Update action

		pygame.display.update()