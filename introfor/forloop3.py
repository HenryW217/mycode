#!/usr/bin/env python3

farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]

for x in farms:
    farmname = x.get('name', 'Unkown Farm')
    agrlist = x.get('agriculture', 'Unsure agriculture')
    for y in agrlist:
        print(farmname + ' has: ' + y)
