# Lecture 3
# Simple Algorithms

#----------------------------------------------


# Guess and Check  - Exhaustive enumeration  


# Find the cube root of a perfect cube
x = -8        # x = int(raw_input('Enter an integer: '))
ans = 0
while ans**3 < abs(x):
	ans += 1
if ans**3 != abs(x):
	print x, 'is not a perfect cube'
else:
	if x < 0:
		ans = -ans
	print 'Cube root of ', x, " is", ans
print 10*"---"

count = 0
phrase = "hello, world"
for iteration in range(5):
    while True:
        count += len(phrase)
        break
    print "Iteration " + str(iteration) + "; count is: " + str(count)



# APPROXIMATION METHODS

#Approximating the square root using exhaustive enumeration
print 10*'---'
x = 252
epsilon = 0.01			# how close i want to get
step = epsilon**2 		# how small or big the step will be
numGuesses = 0
ans = 0.0
while abs(ans**2 - x) >= epsilon and ans <=x:
	ans += step	
	numGuesses += 1
print 'numGuesses= ', numGuesses
if abs(ans**2 - x) >= epsilon:
	print 'Failed on square root of ', x
else:
	print ans, 'is close to square root of ', x



# Bisection search for square root

x = 25
epsilon = 0.01
numGuesses = 0
low = 0.0
high = x
ans = (high + low)/2.0
while abs(ans**2 - x) >= epsilon:
    print('low = ' + str(low) + ' high = ' + str(high) + ' ans = ' + str(ans))
    numGuesses += 1
    if ans**2 < x:
        low = ans
    else:
        high = ans
    ans = (high + low)/2.0
print('numGuesses = ' + str(numGuesses))
print(str(ans) + ' is close to square root of ' + str(x))