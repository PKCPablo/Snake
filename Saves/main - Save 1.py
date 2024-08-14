##################################################
# Program realized by: 	Pablo Rodríguez Gómez    #
# Contact:				pablinelchulin@gmail.com #
# Status:				In Progress              #
# Project Started:  	05/06/2020               #
# Project Finalized:	DD/MM/2020               #
##################################################
#
#	TO DO
#
#	- Colision detection
#	- Apple generation
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

		def add_point():
			if self.type == 0:
				return 1
			elif self.type == 1:
				return 3
			elif self.type == 2:
				return 5
			else:
				print("UNEXPECTED ERROR")

		def sD(self):
			screen.blit(self.img, (self.x, self.y))


def appleCreation():
	#Creation of apples
	xA = 0.0 + random.randint(0,15) * 32
	yA = 0.0 + random.randint(0,15) * 32

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
		self.x		= 0.0 + init_x
		self.y 		= 0.0 + init_y

		self.next	= None
		self.direction = init_dir

	#  1
	# 234

	def sD(self):
		screen.blit(self.img, (self.x, self.y))
		if self.next != None:
			self.next.sD()

	def givX(self):
		return self.x
	def givY(self):
		return self.y

	def move(self, dirt, boolean):

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

		if self.direction == 1:
			x_ch 		= 0
			y_ch 		= -0.1

		elif self.direction == 2:
			x_ch 		= -0.1
			y_ch		= 0

		elif self.direction == 3:
			x_ch 		= 0
			y_ch 		= 0.1

		elif self.direction == 4:
			x_ch 		= 0.1
			y_ch 		= 0

		self.x += x_ch
		self.y += y_ch

		#Give next obj direction

		if self.next != None:
			self.next.move(nextDir, boolean)

		return 0.1


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

	print(dirt)

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

	######################
	# Colision Functions #
	######################

		#Border colision detection

def borderColisionDetec(head): #Terminar apuntando cabeza (direccion)
	x = head.givX()
	y = head.givY()

	dirt = head.direction

	if x < 0.1 or x > 479.9:
		print("Colision detected at X Axis")
	if y < 0.1 or y > 479.9:
		print("Colision detected at Y Axis")

		#Body colision detection

def bodyColisionDetec(head): #Terminar apuntando cabeza (direccion)
	last = head.next
	colDirt = False

	while last != None:
		xB = last.givX()
		yB = last.givY()

		distance = math.sqrt(math.pow(head.givX() - xB, 2) + math.pow(head.givY() - yB, 2))

		if distance < 32.0:
			dirt = head.direction

			if colDirt == True:
				print("Colision detected")
				return True

		last = last.next

	return False

	########################
	# Game over definition #
	########################

def gameOver(scr):
	print("Game Over")
	scr.fill((0, 0, 0))
	#game_over_icon = 'Sprites/game_over/game_over_img.png'
	#screen.blit(game_over_icon, (width/2, height/2))
	time.sleep(4)
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

	screen = pygame.display.set_mode((width, height))  	#Display Creation

	pygame.display.set_caption("Snake") 				#Title
	icon = pygame.image.load('Sprites/snake_logo.png') 	#Icon load
	pygame.display.set_icon(icon)						#Icon display

	
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
	aux 	= True
	lock 	= False

		#PUNTUATION and smth of apples 	[INIT]

	points = 0
	apple_exist = False

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

			if (event.type == pygame.KEYDOWN):

				if event.key ==	pygame.K_UP:
					aux 		= True
					direction 	= 1

				elif event.key == pygame.K_DOWN:
					aux 		= True
					direction	= 3

				elif event.key == pygame.K_LEFT:
					aux 		= True
					direction	= 2

				elif event.key == pygame.K_RIGHT:
					aux 		= True
					direction	= 4

				elif event.key == pygame.K_q: #TEMPORARY KEY ASIGNATION
					last = addBody(last)


			#Colision detection & GAME OVER throw

		borderColision 	= borderColisionDetec(first)
		bodyColision 	= bodyColisionDetec(first)

		if borderColision or bodyColision:
			gameOver(screen)

			#Movement + Limitation 32x32

		if mov_total < 32.1 and aux == True:
			mov_total 	+= first.move(direction, lock)
			lock 		= False
		else:
			mov_total 	= 0.0
			lock 		= True

			aux 		= False


			#Background ~ RGB [TEMPORARY] -> Replace with image

		screen.fill((30, 0, 30))

			#Display of snake

		first.sD()

			#Creation of apple

		if apple_exist == False:
			apple 		= appleCreation()
			apple_exist = True

		#Display of apple

		apple.sD()

		#Colision detection & Apple delete
		


		pygame.display.update()