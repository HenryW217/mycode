#!/usr/bin/env python3

# Engineering Flowchart
# Duct Tape and WD-40
import time

def main():
    print ( 'Please enter "Yes" or "No" for all the following questions.')
    time.sleep(1)

    chk = input('Does it move? ')
    if chk.lower() == 'no':
        n1 = input('Should it? ')
        if n1.lower() == 'no':
            print('No Problem!')
        elif n1.lower() == 'yes':
            print('Try use WD-40!')
        else:
            print('Don\'t try to break my code!\nAnswer with "Yes" or "No" only!!\nTry Again!')

    elif chk.lower() == 'yes':
        n2 = input('Should it? ')
        if n2.lower() == 'yes':
            print('No Problem!')
        elif n2.lower() == 'no':
            print('Try use duct tape!')
        else:
            print('Don\'t try to break my code!\nAnswer with "Yes" or "No" only!!\nTry Again!')
    else:
        print('Don\'t try to break my code!\nAnswer with "Yes" or "No" only!!\nTry Again!')

main()
