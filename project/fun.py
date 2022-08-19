#!/usr/bin/env python3

# Car Troubleshooting Flowchart

def fun():
    # Instruction
    print('Please enter "Y" or "N" for all the following questions.\n')
    error_message = 'Don\'t try to break my code!\nAnswer with "Y" or "N" only!!\nTry Again!'
    chk = input('Does it move?\n--> ')
    if chk.lower() == 'n':
        m = input('Should it?\n--> ')
        if m.lower() == 'n':
            print('No Problem!')
        elif m.lower() == 'y':
            print('Try use WD-40!')
        else:
            print(error_message)

    elif chk.lower() == 'y':
        n = input('Should it?\n--> ')
        if n.lower() == 'y':
            print('No Problem!')
        elif n.lower() == 'n':
            print('Try use duct tape!')
        else:
            print(error_message)
    else:
        print(error_message)
