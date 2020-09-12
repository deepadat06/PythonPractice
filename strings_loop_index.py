"""
Task
Given a string,S , of length N that is indexed from 0 to N-1, print its even-indexed and odd-indexed characters as 2 space-separated strings on a single line (see the Sample below for more detail).
Note: 0 is considered to be an even index.
Constraints
1 <= T <=10
2 <= length of S<= 10000
"""


T = int(input())
S = []


if T >= 1 and T <= 10:
    for i in range(0,T):
        s = input()
        S.append(s)
    for item in S:
        even = ""
        odd = ""
        l=len(item)
        for j in range(0,l):
            if(j%2==0):
                even = even + item[j]
            else:
                odd = odd + item[j]
        print(even + " " + odd)
