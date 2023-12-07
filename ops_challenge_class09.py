#!/usr/bin/env python3

# Script Name:                  Python Conditionals
# Author:                       David Renteria
# Date of latest revision:      12/07/2023
# Purpose:                      Statements using logical conditionals

# Declaration of variables
straw_weight = 105
jr_fly = 108
fly_weight = 112
jr_bantam = 115
bantam_weight = 118
jr_feather = 122
feather_weight = 126
jr_light = 130
light_weight = 135
jr_welter = 140
welter_weight = 147
jr_middle = 154
middle_weight = 160
super_mid = 168
lt_heavy = 175
cruiser = 200
heavy = 205

# Declaration of functions


# Main
if straw_weight == jr_fly: 
    print("Strong wind will carry you away!")
elif (jr_bantam != bantam_weight):
    print("They make that shirt for men?")
else:
    print("Get your weight up!")

if (feather_weight < jr_feather):
    print("Light as a feather....")
elif (light_weight <= jr_light or jr_welter > welter_weight) and (jr_middle >= middle_weight or super == lt_heavy):
    print("Float like a butterfly")
else:
    print("His momma named him Cassius, so I'm gon call him Cassius!")

if heavy > light_weight:
    if middle_weight <= fly_weight:
        pass
    else:
        print("I'd rather watch men in tights hug on the floor.") # don't let Marco see this code lol
# End