#!/usr/bin/env python3

i = 0

while i < 3:
    answer = input('Finish the movie title, "Monty Python\'s The Life of ...')
    
    i = i + 1

    if answer.lower() == 'brian':
        print('Correct!')
        break

    elif answer.lower() == 'shrubbery':
        print('You gave the super secret answer!')
        break
    
    elif i == 3:
        print('Sorry, the answer was Brian.')
        break

    else:
        print('Sorry, try again!')







