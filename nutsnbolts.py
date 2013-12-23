#! /usr/bin/env python3.3

number_of_items = int(input('Number of items: '))

item_list = {}
change_list = {}

for i in range(number_of_items):
    item_and_price = (input('Item: ')).split()
    item, price = item_and_price[0], int(item_and_price[1])
    item_list[item] = price

for i in range(number_of_items):
    item_and_price = (input('Item: ')).split()
    item, price = item_and_price[0], int(item_and_price[1])
    if item in item_list:
        if price != item_list[item]:
            change_list[item] = price - item_list[item]

for i in change_list:
    print(i, change_list[i])

