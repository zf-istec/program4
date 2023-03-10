#!/usr/bin/env python3
# -*- coding: utf-8 -*-


######################
# de Morgan example
######################

sword_charge = 0.95
shield_energy = 110

#if not (sword_charge >= 0.90 and shield_energy >= 100):
#    print("\nYour attack has no effect, the dragon fries you to a crisp!")
#else:
#    print("\nThe dragon crumples in a heap. You rescue the gorgeous princess!")

######################
# 1st simplification
######################

#if sword_charge < 0.90 or shield_energy < 100:
#    print("\nYour attack has no effect, the dragon fries you to a crisp!")
#else:
#    print("\nThe dragon crumples in a heap. You rescue the gorgeous princess!")

######################
# 2nd simplification
######################

#if sword_charge >= 0.90 and shield_energy >= 100:
#    print("\nThe dragon crumples in a heap. You rescue the gorgeous princess!")
#else:
#    print("\nYour attack has no effect, the dragon fries you to a crisp!")

######################
# 3rd simplification
######################

sword_check = sword_charge >= 0.90
shield_check = shield_energy >= 100

if sword_check and shield_check:
    print("\nThe dragon crumples in a heap. You rescue the gorgeous princess!")
else:
    print("\nYour attack has no effect, the dragon fries you to a crisp!")

# is it easiest to read?
