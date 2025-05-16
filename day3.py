#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 01:13:49 2024

@author: tancredi

--- Day 3: Mull It Over ---

"Our computers are having issues, so I have no idea if we have any Chief Historians in stock! You're welcome to check the warehouse, though," says the mildly flustered shopkeeper at the North Pole Toboggan Rental Shop. The Historians head out to take a look.

The shopkeeper turns to you. "Any chance you can see why our computers are having issues again?"

The computer appears to be trying to run a program, but its memory (your puzzle input) is corrupted. All of the instructions have been jumbled up!

It seems like the goal of the program is just to multiply some numbers. It does that with instructions like mul(X,Y), where X and Y are each 1-3 digit numbers. For instance, mul(44,46) multiplies 44 by 46 to get a result of 2024. Similarly, mul(123,4) would multiply 123 by 4.

However, because the program's memory has been corrupted, there are also many invalid characters that should be ignored, even if they look like part of a mul instruction. Sequences like mul(4*, mul(6,9!, ?(12,34), or mul ( 2 , 4 ) do nothing.

For example, consider the following section of corrupted memory:

xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))
                                          
Only the four highlighted sections are real mul instructions. Adding up the result of each instruction produces 161 (2*4 + 5*5 + 11*8 + 8*5).

Scan the corrupted memory for uncorrupted mul instructions. What do you get if you add up all of the results of the multiplications?

Part 1 Answer = 183669043

"""

# This is the Regular Expression module!
import re
import time

#¶ This function takes the searched macropattern in the given data and computes the requested task for this day
def counter(macropattern,micropattern, line):
    l = re.findall(macropattern,line) # Creates a list with with all instaces found: ["mul(x,y)","mul(z,a)",...]
    linecounter = 0
    for mul in l:
        k = re.findall(micropattern, mul)
        listnum = k[0].split(",") #  list = string.split(separator)
        listnum = [int(num) for num in listnum if num.isdigit()] # redefine LISTNUM as an actual list of numbers
        linecounter += listnum[0]*listnum[1]
    return linecounter
    
start = time.time()

# Data extraction and unpack using "with" (opens and closes a file automatically) - usefull since 
# here each row can have a diffent lenght, i.e. np.genfromtxt can give problems
datafile = "/Users/tancredi/Desktop/python/AdventOfCode2024/data_for_puzzles/puzzle3.txt"

macropattern = r"mul\(\d{1,3},\d{1,3}\)"
micropattern = r"\d{1,3},\d{1,3}"

tot = 0  

with open(datafile) as f:
    for line in f:
        tot += counter(macropattern, micropattern, line)
    
print(f"Total = {tot}")

mid = time.time()

print(f"Part 1 - computation time = {(mid-start)*1000:.3f}ms")

"""
--- Part Two ---
As you scan through the corrupted memory, you notice that some of the conditional statements are also still intact. If you handle some of the uncorrupted conditional statements in the program, you might be able to get an even more accurate result.

There are two new instructions you'll need to handle:

The do() instruction enables future mul instructions.
The don't() instruction disables future mul instructions.
Only the most recent do() or don't() instruction applies. At the beginning of the program, mul instructions are enabled.

For example:

xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))

This corrupted memory is similar to the example from before, but this time the mul(5,5) and mul(11,8) instructions are disabled because there is a don't() instruction before them. The other mul instructions function normally, including the one at the end that gets re-enabled by a do() instruction.

This time, the sum of the results is 48 (2*4 + 8*5).

Handle the new instructions; what do you get if you add up all of the results of just the enabled multiplications?
"""

# This is a good method I could try!

string = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))don't()"

dostring = r"do\(\)"
dontstring = r"don't\(\)"
remove = 0

# Create an empty string and filling it line by line while stripping empty/"\n" characters (they mess up)
megaline = ""
with open(datafile) as f:
    for line in f: 
        megaline+=line.strip()
        

# Create two dictionaries with the data index for the beginning of "do()" and the end of "don't()"
# and assign True for do() and False for don't()
dolist = re.finditer(dostring, megaline)
dontlist = re.finditer(dontstring, megaline)
dont_start = {s.start():False for s in dontlist}
do_end= {e.end():True for e in dolist}
# Merge the two dictionaries in one dictionary sorted by line character value
stop_go_dict = dict(sorted((dont_start | do_end).items()))

# Make an "iterator" from the sorted dictionary to use the next() built-in function
iter_dict = iter(stop_go_dict)
next(iter_dict,len(megaline))

# Compute the mul(x,y) from the don't() sections (or minilines)
for line_char_value in stop_go_dict:    
    if (stop_go_dict[line_char_value] is False):
        next_key = next(iter_dict,len(megaline))
        miniline = megaline[line_char_value:next_key]
        remove += counter(macropattern, micropattern, miniline)
    else:
        next_key = next(iter_dict,len(megaline))


# Finally subtract the don't() from the Part 1 computed total
print(f"Remove = {remove}")
print("New Total = ", tot-remove)


end = time.time()

print(f"Part 2 - computation time = {(mid-start)*1000:.3f}ms")

print(f"Total computation time = {(end-start)*1000:.3f}ms")
        

# for match in m:
#     print(match.span())
    