#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 02:41:57 2024

@author: tancredi

Advent of Code 2024!

--- Day 2: Red-Nosed Reports ---

Fortunately, the first location The Historians want to search isn't a long walk from the Chief Historian's office.

While the Red-Nosed Reindeer nuclear fusion/fission plant appears to contain no sign of the Chief Historian, the engineers there run up to you as soon as they see you. Apparently, they still talk about the time Rudolph was saved through molecular synthesis from a single electron.

They're quick to add that - since you're already here - they'd really appreciate your help analyzing some unusual data from the Red-Nosed reactor. You turn to check if The Historians are waiting for you, but they seem to have already divided into groups that are currently searching every corner of the facility. You offer to help with the unusual data.

The unusual data (your puzzle input) consists of many reports, one report per line. Each report is a list of numbers called levels that are separated by spaces. For example:

7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9
This example data contains six reports each containing five levels.

The engineers are trying to figure out which reports are safe. The Red-Nosed reactor safety systems can only tolerate levels that are either gradually increasing or gradually decreasing. So, a report only counts as safe if both of the following are true:

The levels are either all increasing or all decreasing.
Any two adjacent levels differ by at least one and at most three.
In the example above, the reports can be found safe or unsafe by checking those rules:

7 6 4 2 1: Safe because the levels are all decreasing by 1 or 2.
1 2 7 8 9: Unsafe because 2 7 is an increase of 5.
9 7 6 2 1: Unsafe because 6 2 is a decrease of 4.
1 3 2 4 5: Unsafe because 1 3 is increasing but 3 2 is decreasing.
8 6 4 4 1: Unsafe because 4 4 is neither an increase or a decrease.
1 3 6 7 9: Safe because the levels are all increasing by 1, 2, or 3.
So, in this example, 2 reports are safe.

Analyze the unusual data from the engineers. How many reports are safe?

Part 1 : Answer = 442

Computational time = 3.6ms

"""

import time

def check_ascending(array):
    for i in range(len(array)-1):
        if array[i] >= array[i+1]:
            return False
    return True# if descending then give Falsreturn False
        

def check_descending(array):
    for i in range(len(array)-1):
        if array[i] <= array[i+1]: # if ascending then give False
            return False
    return True

def check_distance(array):
    for i in range(len(array)-1):
        dist = abs(array[i]-array[i+1])
        if dist > 3 or dist < 1: # Distance is either 0 or 4,5,...
            return False
    return True

def is_safe(array):
    return ((check_ascending(array) or check_descending(array) is True) and check_distance(array) is True)

# --- Check if above functions are working as expected ---

    # ex = [1,2,3,4] # safe
    # ex1 = [4,3,2,1] # safe
    # ex2 = [0,2,3,3,4] # not STRICTLY ascending
    # ex3 = [4,3,3,2,1] # not STRICTLY descending
    # ex4 = [1,4,5,6,10] # there's a distance which is 4 (6,10)
    
    # print(check_ascending(ex2))
    # print(check_descending(ex2))
    # print(check_ascending(ex2)) 
    # print(check_descending(ex3))
    # print(check_distance(ex4) and check_ascending(ex4))
    
    # print(is_safe(ex))
    # print(is_safe(ex1))
    # print(is_safe(ex3))
    # print(is_safe(ex4))

# ---

start = time.time()


# Data extraction and unpack using "with" (opens and closes a file automatically) - usefull since 
# here each row can have a diffent lenght, i.e. np.genfromtxt can give problems
datafile = "/Users/tancredi/Desktop/python/AdventOfCode2024/data_for_puzzles/puzzle2.txt"


safecount=0

# Data extraction 
with open(datafile) as f:
    for line in f:
        dataline = [int(num) for num in line.split() if num.isdigit()] # Thanks ChatGPT
        # Analysis
        if is_safe(dataline) is True:
            safecount+=1

print(safecount)
        
mid = time.time()

print(f"Part 1 - computation time = {(mid-start)*1000:.3f}ms")

"""
--- Part Two ---
The engineers are surprised by the low number of safe reports until they realize they forgot to tell you about the Problem Dampener.

The Problem Dampener is a reactor-mounted module that lets the reactor safety systems tolerate a single bad level in what would otherwise be a safe report. It's like the bad level never happened!

Now, the same rules apply as before, except if removing a single level from an unsafe report would make it safe, the report instead counts as safe.

More of the above example's reports are now safe:

7 6 4 2 1: Safe without removing any level.
1 2 7 8 9: Unsafe regardless of which level is removed.
9 7 6 2 1: Unsafe regardless of which level is removed.
1 3 2 4 5: Safe by removing the second level, 3.
8 6 4 4 1: Safe by removing the third level, 4.
1 3 6 7 9: Safe without removing any level.
Thanks to the Problem Dampener, 4 reports are actually safe!

Update your analysis by handling situations where the Problem Dampener can remove a single level from unsafe reports. How many reports are now safe?

Part 2 Answer = 493

"""

def make_safe(array):
    if is_safe(array):
        return True
    else: 
        for i in range(len(array)):
            tmp = array[:i] + array[i+1:]
            if is_safe(tmp):
                return True
        return False    

makecount= 0

with open(datafile) as f:
    for line in f:
        dataline = [int(num) for num in line.split() if num.isdigit()] # Thanks ChatGPT
        # Analysis
        if is_safe(dataline) is True:
            safecount+=1
        if make_safe(dataline) is True:
            makecount+=1

print(makecount)

end = time.time()

print(f"Part 2 - computation time = {(mid-start)*1000:.3f}ms")

print(f"Total computation time = {(end-start)*1000:.3f}ms")