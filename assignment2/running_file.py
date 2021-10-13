import numpy as np
from random import sample
import random

#generating a random 9X9 sudoku

'''struct_arr = np.zeros((9,9))
numbers_list = [1,2,3,4,5,6,7,8,9]
def get_random_number(A,i,j):
    block_number_row = (i//3)*3 
    block_number_col = (j//3)*3 
    k = random.choice(numbers_list)
    #print(block_number_row)
    if(k not in struct_arr[block_number_row:block_number_row + 3][block_number_col:block_number_col + 3] and k not in struct_arr[i] and k not in struct_arr[:,j]):
        return get_random_number(A, i , j)
    else:
        print(block_number_col)
        return k
for i in range(0,9):
    print(struct_arr)
    for j in range(0,9):
        if i == 1:
            print("yes")
        struct_arr[i][j] = get_random_number(struct_arr, i, j)
        
print(struct_arr)'''

base  = 3
side  = base*base

# pattern for a baseline valid solution
def pattern(r,c): 
    return (base*(r%base)+r//base+c)%side

# randomize rows, columns and numbers (of valid base pattern)

#def shuffle(s): return sample(s,len(s)) 
def get_random_list(sequence):
    np.random.shuffle(sequence)
    return sequence
rBase = range(base)
square_len = np.arange(0,3) 
#rows  = [ g*base + r for g in shuffle(rBase) for r in shuffle(rBase) ] 
#cols  = [ g*base + c for g in shuffle(rBase) for c in shuffle(rBase) ]
print(get_random_list(square_len))
row_index_corrected = [ row_num*3 + c1 for row_num in get_random_list(square_len) for c1 in get_random_list(square_len) ] 
col_index_corrected = [ col_num*3 + c2 for col_num in get_random_list(square_len) for c2 in get_random_list(square_len) ] 
num_list = np.arange(1,10)
#nums  = shuffle(num_list)
nums = get_random_list(num_list)
# produce board using randomized baseline pattern
board = [ [nums[pattern(r,c)] for c in col_index_corrected] for r in row_index_corrected ]

for line in board: print(line)