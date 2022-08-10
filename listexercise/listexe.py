#!/usr/bin/env python3

foodList1 = [ 'Chow Mein', 'Fried Rice' ]
foodList2 = [ 'Orange Chicken', 'String Bean Chicken Breast' ]
foodList3 = [ 'Kung Pao Chicken', 'Mushroom Chicken' ]

listOfFavFood = [foodList1, foodList2, foodList3]

print(listOfFavFood)

print(f'My favorite foods are {listOfFavFood[0][1]}, {listOfFavFood[1][0]} and {listOfFavFood[2][1]}\n\n\n\n\n')


superman = {
            'outfitColor': ['blue', 'red'], 
            'canFly': True, 
            'hasCar': False, 
            'numOfFans': 2000000
            }

batman = {
          'outfitColor': ['black', 'grey'],
          'canFly': False,
          'hasCar': True,
          'numOfFans': 3000000
          }

spiderman = {
             'outfitColor': ['blue', 'red'],
             'canFly': True, # after 2021 I believe
             'hasCar': False,
             'numOfFans': 1000000
             }
print( 'The Keys are:' + str(superman.keys()) +  str(batman.keys()) + str(spiderman.keys() ))

print( 'The Vaules are:' +  str(superman.values()) + str(batman.values()) + str(spiderman.values()) )
