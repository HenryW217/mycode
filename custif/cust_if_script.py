#!/usr/bin/env python3

# Engineering Flowchart
# Duct Tape and WD-40
import time

def main():
    print ( 'Please enter "Yes" or "No" for all the following questions.\n--Don\'t worry about the case.--')
    time.sleep(1)

    chk = input('Does it move? ')
    if chk.lower() == 'no':
        m = input('Should it? ')
        if m.lower() == 'no':
            print('No Problem!')
        elif m.lower() == 'yes':
            print('Try use WD-40!')
        else:
            print('Don\'t try to break my code!\nAnswer with "Yes" or "No" only!!\nTry Again!')

    elif chk.lower() == 'yes':
        n = input('Should it? ')
        if n.lower() == 'yes':
            print('No Problem!')
        elif n.lower() == 'no':
            print('Try use duct tape!')
        else:
            print('Don\'t try to break my code!\nAnswer with "Yes" or "No" only!!\nTry Again!')
    else:
        print('Don\'t try to break my code!\nAnswer with "Yes" or "No" only!!\nTry Again!')

main()
