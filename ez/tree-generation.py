#! /usr/bin/env python3.3

import sys

tree_info = (input('Tree info: ')).split()

tree_base = int(tree_info[0])

if !(tree_base % 2):
    sys.exit("Please enter an odd number")

trunk_char = tree_info[1]
leaf_char = tree_info[2]

i = 1 #variable to count for how many tree layers to draw in while loop

while i <= tree_base:
    spaces = (tree_base - i) // 2
    print((' ' * spaces) + (leaf_char * i) + (' ' * spaces))
    i += 2

spaces = (tree_base - 3) / 2

print ((' ' * spaces) + (trunk_char * 3) + (' ' * spaces))
