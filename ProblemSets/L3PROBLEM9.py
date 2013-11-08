print 'Please think of a number between 0 and 100!'
low = 0
high = 100
ans = (high + low)/2
while True:
    print 'Is your secret number',ans
    x = str(raw_input('Enter "h" to indicate the guess is too high. Enter "l" to indicate the guess is too low. Enter "c" to indicate I guessed correctly: '))
    if x =='l' or x == 'h' or x == 'c':
        if x == 'l':
            low = ans
        if x == 'h':
            high = ans
        if x == 'c':
            print 'Game over. Your secret number was: ',ans
            break
        ans = (high + low)/2
    else:
        print 'Sorry, I did not understand your input.'

    
    
