#!/usr/bin/python
import urllib2
import json
import sys
import time
import fontv
import ldp


upvotes = 0
upvotelast = 0
displaywidth=80
totalwidth=0
# the matrix is a representation of the led's that are lit on the 80x8 display
#
matrix=[[0 for i in xrange(80)] for i in xrange(8)]
#
# function to shift left all the vaules of the matrix array
# this allows us to put new data in the first column
#
def shiftmatrix():
	for row in range(8):
		for col in range(79,0,-1):
			matrix[row][col]=matrix[row][col-1]
# end def

# function to read the matrix array and output the values to the display device
# 
def showmatrix():
	ldp.displayoff()
	for row in reversed(range(8)):
		for col in reversed(range(80)):
			ldp.colourshift(matrix[row][col])
		ldp.showrow(row)
# end def
def showmatrix2():
	for row in range(8):
		for col in range(80):
			ldp.colourshift(matrix[row][col])
		ldp.showrow(row)
#
# Main
#
# initialise the display
#
ldp.init()
#
# assign the command line args for the text and colour
#
#textinput=str(sys.argv[1])
#colour=int(sys.argv[2])
textinput = "NULL"
colour=1


def displayUpdate(upvote):
	colour=1
	num = 0
	while num<3:
		try:
			#show = 0
			textinput = upvote
			textinput+='  ::  '
			if num == 2:
			    textinput = upvote + "                "
			
			# save the ascii values of the input characters into the inputarray 
			# the font module uses the ascii value to index the font array
			inputarray=[]
			for char in textinput:
				inputarray.append(ord(char))

			# dotarray is  8 X n
			# n is determined by the number of characters multiplyed by 8 
			# n will be len(dotarray[0]) after filling dotarray from characters
			# in the inputarray
			#
			dotarray=[[] for i in xrange(8)]
			#
			# fill the dot array with the colour digits
			# this is the dot pattern that we want to show
			#
			for row in range(8):
				for ascii in inputarray:
					# get the width of the character from the first element of the font variable
					width=fontv.array[ascii][0]
					binary='{0:{fill}{align}{width}{base}}'.format(fontv.array[ascii][row+1],base='b',fill='0',align='>',width=width)
					for digit in range(width):
						if binary[digit] == '0':
							dotarray[row].append(0)
						else:
							dotarray[row].append(colour)
			#
			# Continually output to the display until Ctrl-C
			#
			
			
				# loop around each column in the dotarray
				
				
			for col in range(len(dotarray[0])):
				for row in range(8):
					# copy the current dotarray column values to the first column in the matrix
					matrix[row][0]=(dotarray[row][col])
				# now that we have updated the matrix lets show it
				showmatrix()
				# shift the matrix left ready for the next column
				shiftmatrix()
			ldp.displayoff()
			num += 1
		except KeyboardInterrupt:
			ldp.clear()
			print "Finished"
			sys.exit()


def displayUpdateStatic(upvote):
	colour=2
	textinput = upvote
	inputarray=[]
	for char in textinput:
		inputarray.append(ord(char))

	# dotarray is  8 X n
	# n is determined by the number of characters multiplyed by 8 
	# n will be len(dotarray[0]) after filling dotarray from characters
	# in the inputarray
	#
	dotarray=[[] for i in xrange(8)]
	#
	# fill the dot array with the colour digits
	# this is the dot pattern that we want to show
	#
	for row in range(8):
		for ascii in inputarray:
			# get the width of the character from the first element of the font variable
			width=fontv.array[ascii][0]
			binary='{0:{fill}{align}{width}{base}}'.format(fontv.array[ascii][row+1],base='b',fill='0',align='>',width=width)
			for digit in range(width):
				if binary[digit] == '0':
					dotarray[row].append(0)
				else:
					dotarray[row].append(colour)


	totalwidth=len(dotarray[0])
	if totalwidth > displaywidth:
		print 'Message is Larger than the Display'
		sys.exit()

	offset=int((displaywidth - totalwidth) / 2)

	# Fill the matrix initially with offset spaces to centre align the message
	#
	for col in range(offset):
		for row in range(8):
			matrix[row][col]=0
	# now fill the rest of the matrix with the dotarray
	for col in range(totalwidth):
		for row in range(8):
			# copy the current dotarray column values to the first column in the matrix
			matrix[row][offset+col]=(dotarray[row][col])


	#
	# Continually output to the display until Ctrl-C
	#

			# now that we have updated the matrix lets show it
	value = 0
	while value < 500:
		value = value + 1
		try:
			showmatrix2()
			
		except KeyboardInterrupt:
			ldp.clear()
			print "Finished"
			sys.exit()
			#time.sleep(0.0001)



# append extra characters to text input to allow for wrap-around

while True:
	newnum = "UpVotes = " + str(upvotes)
	displayUpdateStatic(newnum)
	ldp.clear()
	try:
		url = sys.argv[1] + ".json"
		response = urllib2.urlopen(url)
		data = json.load(response)
		upvotes = data[0]['data']['children'][0]['data']['score']
		print upvotes
		if (upvotes > upvotelast):
			newline = ("Upvote!")
			displayUpdate(newline)
			print "New Upvote! " + str(upvotes)
			upvotelast = upvotes
		
	except KeyboardInterrupt:
		ldp.clear()
		print "Finished"
		sys.exit()