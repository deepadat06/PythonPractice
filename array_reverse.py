"""
Task
Given an array,A , of N integers, print A's elements in reverse order as a single line of space-separated numbers.
"""

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    arr_rev = []

    if(n >=1 and n <= 1000):
        arr = list(map(int, input().rstrip().split()))
        len_arr = len(arr)
        for i in range(len_arr-1,-1,-1):
            arr_rev.append(str(arr[i]))
        print(" ".join(arr_rev))
