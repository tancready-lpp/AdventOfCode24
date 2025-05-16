#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 22:17:45 2024

@author: tancredi


--- Day 4: Ceres Search ---
"Looks like the Chief's not here. Next!" One of The Historians pulls out a device and pushes the only button on it. After a brief flash, you recognize the interior of the Ceres monitoring station!

As the search for the Chief continues, a small Elf who lives on the station tugs on your shirt; she'd like to know if you could help her with her word search (your puzzle input). She only has to find one word: XMAS.

This word search allows words to be horizontal, vertical, diagonal, written backwards, or even overlapping other words. It's a little unusual, though, as you don't merely need to find one instance of XMAS - you need to find all of them. Here are a few ways XMAS might appear, where irrelevant characters have been replaced with .:


..X...
.SAMX.
.A..A.
XMAS.S
.X....

The actual word search will be full of letters instead. For example:

MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX

In this word search, XMAS occurs a total of 18 times; here's the same word search again, but where letters not involved in any XMAS have been replaced with .:

....XXMAS.
.SAMXMS...
...S..A...
..A.A.MS.X
XMASAMX.MM
X.....XA.A
S.S.S.S.SS
.A.A.A.A.A
..M.M.M.MM
.X.X.XMASX

Take a look at the little Elf's word search. How many times does XMAS appear?

"""

import re
import time

ex ="""....XXMAS. 
.SAMXMS... 
...S..A... 
..A.A.MS.X 
XMASAMX.MM 
X.....XA.A 
S.S.S.S.SS 
.A.A.A.A.A 
..M.M.M.MM 
.X.X.XMASX 
"""

start= time.time()

datafile = "/Users/tancredi/Desktop/python/AdventOfCode2024/data_for_puzzles/puzzle4.txt"

# open file and reading each line replacing \n directly, then saving each line in a list and append to []
s=[]
with open(datafile) as f:
    for line in f:
        line = line.replace("\n","")
        s.append(line)

s_norm = "".join(s) #make it a string

s_trans =  reversed(s) # transpose the list (ie 90 degrees)
s_trans ="".join(s_trans) #make it a string

# defining the regex patterns
forw = "XMAS"
back= "SAMX"

# # trying to rotate by 45 degrees by making diagonals straight
# diag = 0
# anti = 0
# for i in range(-len(s), len(s)):
#     tmp = []
#     for j in range(-i,i):
#         tmp.append(s[i][j])
#     pmt = reversed(tmp)
#     tmp = "".join(tmp)
#     pmt = "".join(pmt)
#     tmp_f = re.findall(forw, tmp)
#     tmp_b = re.findall(back, tmp)
#     pmt_f = re.findall(forw, pmt)
#     pmt_b = re.findall(back, pmt)
#     diag += (len(tmp_f) + len(tmp_b))
#     anti += (len(pmt_f) + len(pmt_b))
# print(diag, anti)
# print(tmp)

# print(type(s_trans))
# print(type(s_norm))

# searching for the occurrances of the patterns in the normal and rotated string
norm_forw= re.findall(forw, s_norm)
norm_back=re.findall(back, s_norm)
trans_forw= re.findall(forw, s_trans)
trans_back=re.findall(back, s_trans)


# diag_forw = re.findall(forw, tmp)
# diag_back=re.findall(back, tmp)
# print(len(diag_forw))
# print(len(diag_back))

print(len(norm_forw) + len(norm_back) + len(trans_forw) + len(trans_back))

# brutal force approach to search diagonally
r,l = 0,0 
for i in range(2,len(s)-2):
    for j in range(2,len(s)-2):
        if s[i][j] == "M":
            if (s[i-1][j-1] == "X" and s[i+1][j+1] =="A" and s[i+2][j+2] =="S") or (s[i+1][j+1] == "X" and s[i-1][j-1] =="A" and s[i-2][j-2] =="S"):
                r +=1
            elif (s[i+1][j-1] == "X" and s[i-1][j+1] =="A" and s[i-2][j+2] =="S") or (s[i-1][j+1] == "X" and s[i+1][j-1] =="A" and s[i+2][j-2] =="S"):
                l +=1
                
# Printing total result
print(r+l + len(norm_forw) + len(norm_back) + len(trans_forw) + len(trans_back))
