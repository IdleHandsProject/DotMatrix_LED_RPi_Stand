###################################################
# ldp python module (ldp.py)
# use: import ldp (in your script)
# A set of functions to make it easier to interface 
# with Embedded Adventures' 80x8 led matrix LDP-8008
# By Pete Goss 14/1/2014
###################################################
# connect Raspberry Pi GPIO to J1 on LDP-8008
###################################################
# GPIO pin       LDP-8008 pin
#      3  ------------>  2  A (Row address)
#      5  ------------>  4  B (Row address)
#      6  ------------>  5  GND
#      7  ------------>  6  C (Row address)
#      8  ------------>  7  EN (Enable Display)
#     10  ------------>  8  D (Row address)
#     11  ------------>  9 \R1 (Red Led)
#     12  ------------> 10 \G1 (Green Led)
#     13  ------------> 14  L (Latch)
#     15  ------------> 16  S (Shift)
###################################################

import RPi.GPIO as gpio
gpio.setwarnings(False)
gpio.setmode(gpio.BOARD)

###################################################
# give the gpio pins labels that match the LDP-8008
###################################################
R1=11   
G1=12   
EN=8  
A=3  
B=5  
C=7  
D=10  
L=13  
S=15  

####################################
# init function
# usage: ldp.init()
# function initialises the LDP-8008
# use once at beginning of script
####################################

def init():
	# set GPIO pins as outputs
	gpio.setup(R1,gpio.OUT)
	gpio.setup(G1,gpio.OUT)
	gpio.setup(EN,gpio.OUT)
	gpio.setup(A,gpio.OUT)
	gpio.setup(B,gpio.OUT)
	gpio.setup(C,gpio.OUT)
	gpio.setup(D,gpio.OUT)
	gpio.setup(L,gpio.OUT)
	gpio.setup(S,gpio.OUT)

	#initialise the output pins
	gpio.output(R1,1)
	gpio.output(G1,1)
	gpio.output(S,1)
	gpio.output(L,0)
	gpio.output(EN,0)
	clear()
####################################
# end init function
####################################


####################################
# clear function
# usage: ldp.clear()
# function sets the shift register 
# bits to blank and turns off display
####################################
def clear():
		gpio.output(R1,1)
		gpio.output(G1,1)
		for i in range(80):
			gpio.output(S,1)
			gpio.output(S,0)
			gpio.output(S,1)
		displayoff()
####################################
# end init function
####################################


####################################
# shift function
# usage: ldp.shift()
# function shifts the current led colour 
# into the first column of the register
####################################
def shift():
		gpio.output(S,1)
		gpio.output(S,0)
		gpio.output(S,1)
####################################
# end shift function
####################################

####################################
# colour function
# usage: ldp.colour(colour_value)
# sets the current led colour 
# 0=blank 1=red 2=green 3=orange
####################################
def colour(n):
	if n == 3: #orange	
		gpio.output(R1,0)
		gpio.output(G1,0)
	elif n == 2: #green
		gpio.output(R1,1)
		gpio.output(G1,0)
	elif n == 1: #red
		gpio.output(R1,0)
		gpio.output(G1,1)
	else: # off
		gpio.output(R1,1)
		gpio.output(G1,1)
####################################
# end colour function
####################################

####################################
# colourshift function
# usage: ldp.colourshift(colour_value)
# sets the current led colour 
# and also shifts it into the register
# 0=blank 1=red 2=green 3=orange
####################################
def colourshift(n):
	if n == 3: #orange	
		gpio.output(R1,0)
		gpio.output(G1,0)
	elif n == 2: #green
		gpio.output(R1,1)
		gpio.output(G1,0)
	elif n == 1: #red
		gpio.output(R1,0)
		gpio.output(G1,1)
	else: # off
		gpio.output(R1,1)
		gpio.output(G1,1)
	gpio.output(S,1)
	gpio.output(S,0)
	gpio.output(S,1)
####################################
# end colour function
####################################

####################################
# showrow function
# usage: ldp.showrow(row_value)
# displays the register on a row 
# row_value = 0-7
####################################
def showrow(n):
	if n == 7:
		gpio.output(A,1)
		gpio.output(B,1)
		gpio.output(C,1)
		gpio.output(D,0)
	elif n == 6:
		gpio.output(A,0)
		gpio.output(B,1)
		gpio.output(C,1)
		gpio.output(D,0)
	elif n == 5:
		gpio.output(A,1)
		gpio.output(B,0)
		gpio.output(C,1)
		gpio.output(D,0)
	elif n == 4:
		gpio.output(A,0)
		gpio.output(B,0)
		gpio.output(C,1)
		gpio.output(D,0)
	elif n == 3:
		gpio.output(A,1)
		gpio.output(B,1)
		gpio.output(C,0)
		gpio.output(D,0)
	elif n == 2:
		gpio.output(A,0)
		gpio.output(B,2)
		gpio.output(C,0)
		gpio.output(D,0)
	elif n == 1:
		gpio.output(A,1)
		gpio.output(B,0)
		gpio.output(C,0)
		gpio.output(D,0)
	else:
		gpio.output(A,0)
		gpio.output(B,0)
		gpio.output(C,0)
		gpio.output(D,0)
	# latch the data
	gpio.output(L,1)
	gpio.output(L,0)
	# display the row
	gpio.output(EN,1)
####################################
# end showrow function
####################################

####################################
# displayoff function
# usage: ldp.displayoff()
# turns off the display 
####################################
def displayoff():
	gpio.output(EN,0)
####################################
# end displayoff function
####################################

####################################
# displayon function
# usage: ldp.displayon()
# turns on the display 
####################################
def displayon():
	gpio.output(EN,1)
####################################
# end displayon function
####################################
