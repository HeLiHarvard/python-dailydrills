#! /usr/bin/env python3.3

import sys

[n, m] = (input('Type N and M: ')).split()

candidates = (input('Type ' + m + ' candidates: ')).split()

n, m = int(n), int(m)

if len(candidates) !=  m:
    sys.exit('Please enter exactly ' + m + ' candidates')

ballots = [[] for x in range(n)]

for i in range(n):
    ballots[i] = (input('Enter ballot: ')).split()

vote_totals = []
winner = ''

for i in range(m):
    for j in range(n):
        vote_totals[ballots[j][i]] += 1
    for k in range(m):
        if vote_totals[k] > n / 2:
            winner = candidates[k]
            break
    if winner != '':
        break


print(winner)










