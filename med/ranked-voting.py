#! /usr/bin/env python3.3

import sys
from collections import OrderedDict

#inputs
[n, m] = (input('Type N and M: ')).split()
candidates = (input('Type ' + m + ' candidates: ')).split()
n, m = int(n), int(m)

#checking exactly m candidates are entered
if len(candidates) !=  m:
    sys.exit('Please enter exactly ' + m + ' candidates')

#initializing the vote total tracker
vote_tracker = OrderedDict()
for i in range(m):
    vote_tracker[candidates[i]] = 0

#ballot inputs
ballots = [[] for x in range(n)]
for i in range(n):
    ballots[i] = (input('Enter ballot: ')).split()

winner = ''
loser = ''
least_votes = n

#ENTIRE VOTE TOTALING ALGORITHM NEEDS TO BE CHANGED

#for i in range(m):

while winner == '':
    print("Round " + str(i) + ": ", end = '')
    for j in range(n):
        for i in range(m):
            if candidates[int(ballots[j][i])] in vote_tracker:
                vote_tracker[candidates[int(ballots[j][i])]] += 1
                break

    vote_tracker = OrderedDict(sorted(vote_tracker.items(),
                                     key = lambda t: t[1]))
    for c in vote_tracker.items():
        print(str(100 * c[1] / n) + '% ' + c[0], end = ', ')
        if c[1] > n / 2:
            winner = c[0]
            print(winner + ' is the winner')
            break
        if c[1] < least_votes:
            least_votes = c[1]
            loser = c[0]
    if winner != '':
        break
    del(vote_tracker[loser])
    for k in vote_tracker.items():
        vote_tracker[k] = 0




