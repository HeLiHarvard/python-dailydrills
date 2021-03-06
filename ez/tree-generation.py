#! /usr/bin/env python3.3

import sys

tree_info = (input('Tree info: ')).split()

tree_base = int(tree_info[0])

if not (tree_base % 2) or (tree_base < 3 or tree_base > 21) :
    sys.exit("Please enter an odd number between 3 and 21")

trunk_char = tree_info[1]
leaf_char = tree_info[2]

i = 1 #variable to count for how many tree layers to draw in while loop

while i <= tree_base:
    spaces = int((tree_base - i) / 2)
    print((' ' * spaces) + (leaf_char * i))
    i += 2

spaces = int((tree_base - 3) / 2)

print ((' ' * spaces) + (trunk_char * 3))
