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


"""EX=
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
"""

import re
import time
start= time.time()

datafile = "/Users/tancredi/Desktop/python/AdventOfCode/2024/data_for_puzzles/puzzle4.txt"

# open file and reading each line replacing \n directly, then saving each line in a list and append to []
s=[]
with open(datafile) as f:
    for line in f:
        line = line.replace("\n","")
        s.append(line)

s_norm = "".join(s) #make it a string (s is a list)

# s_trans =  reversed(s) # transpose the list (ie 90 degrees)
s_trans = list(map(list,zip(*s))) # creates a list of lists which is transposed
s_trans ="".join("".join(row) for row in s_trans) # since s_trans was a list of lists, we create a list of the jojned lists and then join it

# defining the regex patterns
forw = "XMAS"
back= "SAMX"

# searching for the occurrances of the patterns in the normal and rotated string
norm_forw= re.findall(forw, s_norm)
norm_back=re.findall(back, s_norm)
trans_forw= re.findall(forw, s_trans)
trans_back=re.findall(back, s_trans)

# print(len(norm_forw) + len(norm_back) + len(trans_forw) + len(trans_back))

# brutal force approach to search diagonally - does not work
# r,l = 0,0 
# for i in range(0,len(s)-3):
#     for j in range(0,len(s)-3):
#         if s[i][j] == "X":
#             if (s[i+1][j+1] == "M" and s[i+2][j+2] =="A" and s[i+3][j+3] =="S") or \
#                (s[i-1][j-1] == "M" and s[i-2][j-2] =="A" and s[i-3][j-3] =="S"):
#                 r +=1
#             if (s[i+1][j-1] == "M" and s[i+2][j-2] =="A" and s[i+3][j-3] =="S") or \
#                  (s[i-1][j+1] == "M" and s[i-2][j+2] =="A" and s[i-3][j+3] =="S"):
#                 l +=1
                
# GPT 4o- mini - for coding approach
diag = 0
N = len(s)
for i in range(N):
    for j in range(N):
        if s[i][j] != "X":
            continue
        # southeast (\)
        if i + 3 < N and j + 3 < N \
           and s[i+1][j+1]=="M" and s[i+2][j+2]=="A" and s[i+3][j+3]=="S":
            diag += 1
        # southwest (/)
        if i + 3 < N and j - 3 >= 0 \
           and s[i+1][j-1]=="M" and s[i+2][j-2]=="A" and s[i+3][j-3]=="S":
            diag += 1
        # northwest (\ reversed)
        if i - 3 >= 0 and j - 3 >= 0 \
           and s[i-1][j-1]=="M" and s[i-2][j-2]=="A" and s[i-3][j-3]=="S":
            diag += 1
        # northeast (/ reversed)
        if i - 3 >= 0 and j + 3 < N \
           and s[i-1][j+1]=="M" and s[i-2][j+2]=="A" and s[i-3][j+3]=="S":
            diag += 1
            
            
print(diag + len(norm_forw) + len(norm_back) + len(trans_forw) + len(trans_back), "first part")
# Printing total result (my approach)
# print(r+l + len(norm_forw) + len(norm_back) + len(trans_forw) + len(trans_back))


# ---- GPT APPROACH ----

# #!/usr/bin/env python3

# import re

# def get_input(file_path):
#     with open(file_path) as f:
#         return [line.strip() for line in f]

# def transpose(grid):
#     return ["".join(row) for row in zip(*grid)]

# def get_main_diagonals(grid):
#     rows, cols = len(grid), len(grid[0])
#     diagonals = []
#     for d in range(-rows + 1, cols):
#         diag = []
#         for i in range(rows):
#             j = i + d
#             if 0 <= j < cols:
#                 diag.append(grid[i][j])
#         diagonals.append("".join(diag))
#     return diagonals

# def get_anti_diagonals(grid):
#     rows, cols = len(grid), len(grid[0])
#     diagonals = []
#     for d in range(rows + cols - 1):
#         diag = []
#         for i in range(rows):
#             j = d - i
#             if 0 <= j < cols:
#                 diag.append(grid[i][j])
#         diagonals.append("".join(diag))
#     return diagonals

# def count_occurrences(lines, patterns):
#     count = 0
#     for line in lines:
#         for pat in patterns:
#             count += len(re.findall(pat, line))
#     return count

# def main():
#     file_path = "/Users/tancredi/Desktop/python/AdventOfCode/2024/data_for_puzzles/puzzle4.txt"
#     grid = get_input(file_path)
    
#     patterns = ["XMAS", "SAMX"]

#     # Horizontal
#     horiz = grid
#     # Vertical
#     vert = transpose(grid)
#     # Diagonals
#     diags = get_main_diagonals(grid) + get_anti_diagonals(grid)

#     total = (
#         count_occurrences(horiz, patterns)
#         + count_occurrences(vert, patterns)
#         + count_occurrences(diags, patterns)
#     )

#     print(total)


"""--- Part Two ---
The Elf looks quizzically at you. Did you misunderstand the assignment?

Looking for the instructions, you flip over the word search to find that this isn't actually an XMAS puzzle;
it's an X-MAS puzzle in which you're supposed to find two MAS in the shape of an X.
One way to achieve that is like this:

M.S
.A.
M.S
Irrelevant characters have again been replaced with . in the above diagram. 
Within the X, each MAS can be written forwards or backwards.

Here's the same example from before, but this time all of the X-MASes have been kept instead:

.M.S......
..A..MSMS.
.M.S.MAA..
..A.ASMSM.
.M.S.M....
..........
S.S.S.S.S.
.A.A.A.A..
M.M.M.M.M.
..........
In this example, an X-MAS appears 9 times.

Flip the word search from the instructions back over to the word search side and try again. 
How many times does an X-MAS appear?"""

import re
import time
start= time.time()

class Puzzle:
    
    def __init__(self, filename):
        self.filename = filename



    def get_input(self):
        matrix=[]
        with open(self.filename) as f:
            for line in f:
                line = line.replace("\n","")
                l = []
                for char in line:
                    l.append(char) # s is a list of strings: [xmas, maxs, msas,...])
                matrix.append(l)
        return matrix
    
    def search(self):
        count = 0
        matrix = self.get_input()
        N = len(matrix)
        M = len(matrix[0])
        print(N,M)
        for i in range(1,N-1):
            for j in range(1,M-1):
                if matrix[i][j] == "A":
                    if matrix[i-1][j-1] == "M" and matrix[i+1][j+1] == "S" and \
                        (matrix[i-1][j+1] == "S" and matrix[i+1][j-1] == "M" or \
                        matrix[i-1][j+1] == "M" and matrix[i+1][j-1] == "S"):
                            count +=1
                    if matrix[i-1][j-1] == "S" and matrix[i+1][j+1] == "M" and \
                        (matrix[i-1][j+1] == "S" and matrix[i+1][j-1] == "M" or \
                        matrix[i-1][j+1] == "M" and matrix[i+1][j-1] == "S"):
                            count +=1
                   
        return count
        


datafile = "/Users/tancredi/Desktop/python/AdventOfCode/2024/data_for_puzzles/puzzle4.txt"
puzzle_day4 = Puzzle(datafile)
# print(puzzle_day4.get_input()) # prints the string I converted from the file
print(puzzle_day4.search())
data = "/Users/tancredi/Desktop/python/AdventOfCode/2024/matrix_input.txt"
test = Puzzle(data)
print(test.search())
