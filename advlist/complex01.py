#!/usr/bin/env python3

def main():
    list1 = ['cisco_nxos', 'arista_eos', 'cisco_ios']
    print(f'list1 is {list1}')
    print(f'ls1-1 is {list1[1]}')

    list2 = ['juniper']
    list1.extend(list2)
    print(f'l1-e-l2 is {list1}')
    
    list3 = ['10.1.0.1', '10.2.0.1', '10.3.0.1']
    list1.append(list3)
    print(f'l1-a-l3 is {list1}')
    print(f'IP addresses are {list1[4]}')
    print(f'IP[0] is {list1[4][0]}')



main()

