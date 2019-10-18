import sys

# Test number for primeness
def isPrime(num):
	for i in range(2,num):
		if (num % i) == 0:
			return False
	return True

def getMaxSpaces(primes):
	# return twice the length of the largest prime number to determine spacing
	numLen = len(str(primes[-1]))
	return numLen*2

def getCorrectSpaces(maxSpaces, num):
	# return the correct amount of blank spaces with the pipe character
	# This makes everything line up on the command line all nice and pretty
	spaces = "".ljust(maxSpaces-len(str(num))) + " | "
	return spaces

def createTable():
	try:
		if sys.argv[1]:
			#the sys arg is how many primes to grab
			N = int(sys.argv[1]) # if argument can be cast to an integer use it
			i = 2 # minimum starting number for a prime
			primes = []

			#Put all of the prime numbers into a list
			while N > 0:
				if isPrime(i):
					primes.append(i)
					if len(primes) == N:
						break
				i += 1	

			#create a table of the prime numbers that multiplies rows by cols
			maxSpaces = getMaxSpaces(primes) # add spaces to make it legible to everyone
			space = "" #start with 0 spaces 
			row = getCorrectSpaces(maxSpaces, '') #add initial space to the first row
			rowCount = 0
			for x in primes:
				row = row + str(x) + getCorrectSpaces(maxSpaces, x) 
			print row
			for x in primes:
				row = row + str(x) + getCorrectSpaces(maxSpaces, x)
				# create all of the rest of the rows
				rowX = str(x) + getCorrectSpaces(maxSpaces, x)
				for y in primes:
					rowCol = x * y
					rowX = rowX + str(rowCol) + getCorrectSpaces(maxSpaces,x * y)
				print rowX
			rowCount += 1
	except:
		print "Please provide an integer.  (ex. `python index.py 10`)"

def createTableTest():
	#Test if we are creating for prime numbers correctly
	#prime numbers to test 3, 5, 11, 17
	prime_nums = [3,5,17,20,25]
	#Result True, True, True, False, False
	print "Testing results should be True, True, True, False, False"
	for x in prime_nums:
		print isPrime(x)
	
try:
	if sys.argv[1] == "test":
		createTableTest()
	else:
		createTable()
except:
	print "Please provide an integer.  (ex. `python index.py 10`)"

