import pandas as pd
import numpy as np
import random
import sys
from random import sample
#this function is not working and is showing recursion depth error, please explain why it is happening:
struct_arr = np.zeros((9,9))
numbers_list = [1,2,3,4,5,6,7,8,9]
def get_random_number(A,i,j):
    block_number_row = (i//3)*3 
    block_number_col = (j//3)*3 
    k = random.choice(numbers_list)
    #print(block_number_row)
    if(k in struct_arr[block_number_row:block_number_row + 3, [block_number_col ,block_number_col + 1,block_number_col + 2]] or k in struct_arr[i] or k in struct_arr[:,j]):
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
        
print(struct_arr)



def q1():
    square = range(3) 
    rows  = [ g*3 + c1 for g in sample(square,3) for c1 in sample(square,3) ] 
    cols  = [ g*3 + c2 for g in sample(square,3) for c2 in sample(square,3) ]
    nums  = sample(range(1,10), 9)

    # produce board using randomized baseline pattern
    board = [ [nums[(3*(r%3)+r//3+c)%9] for c in cols] for r in rows ]

    for line in board: print(line)
    sudoku = np.array(board)
    #checking the 3rd statement:
    def check_if_sudoku(sudoku):
        for i in range(9):
            for j in range(9):
                block_start_i = (i//3) * 3
                block_start_j = (j//3) * 3
                element_here = sudoku[i][j]
                temp_arr = np.ndarray.copy(sudoku)
                temp_arr[i][j] = 100
                if(sudoku[i][j] in temp_arr[block_start_i: block_start_i + 3, [block_start_j,block_start_j + 1, block_start_j + 2]] or sudoku[i][j] in temp_arr[i] or sudoku[i][j] in temp_arr[:,j]):
                    #print(sudoku[i][j])
                    #print(temp_arr[block_start_i: block_start_i + 3][block_start_j: block_start_j + 3])
                    return False
                #else:
                    #print(board[i][j])         written just for checking
        return True
    _3_3_3_3_array = np.ones((3,3,3,3))

    for i in range(3):
        for j in range(3):
            row_num = (i//3)* 3
            col_num = (j//3)*3
            _3_3_3_3_array[i][j] = sudoku[row_num: row_num + 3,[col_num, col_num + 1, col_num + 2]]

    #print(_3_3_3_3_array)
    testcase1 = np.array([[8,6,1,7,9,4,3,5,2],[3,5,2,1,6,8,7,4,9],[4,9,7,2,5,3,1,8,6],[2,1,8,9,7,5,6,3,4],[6,7,5,3,4,1,9,2,8],[9,3,4,6,8,2,5,1,7],[5,2,6,8,1,9,4,7,3],[7,4,3,5,2,6,8,9,1],[1,8,9,4,3,7,2,6,5]])
    testcase2 = np.array([[8,6,1,7,9,4,3,5,2],[3,5,2,1,6,8,7,4,9],[4,9,7,2,5,3,1,8,6],[2,1,8,9,7,5,6,3,4],[6,7,5,3,4,1,9,2,8],[9,3,4,6,8,2,5,1,7],[5,2,6,8,1,9,4,7,3],[7,4,3,5,2,6,8,9,1],[1,8,9,4,3,7,2,6,1]])

    print(check_if_sudoku(testcase2))

def q2():
    '''n = int(input("n"))
    p = int(input("p"))
    q = int(input("q"))'''


    #tried using broadcasting
    #struct_arr = np.zeros((n,n))
    

    '''struct_arr = [np.random.randint(1,10,n) for i in struct_arr]
    for i in range(n):
        for j in range(n):
            struct_arr[i][j] = np.random.randint(1,10,10)[0]
    n_n_array = np.array(struct_arr)
    print(n_n_array)
    #arr_p_q = [n_n_array[i:i + p][:,j:j + q] for i in range(0,n,p) for j in range(0,n,q)]'''
    n=12
    p=3
    q=6

    struct_arr = np.array([[5,136,171,124,58,4,131,69,28,196,176,51],[20,125,163,154,158,153,139,16,21,64,120,144],[197,134,49,95,23,168,68,45,40,142,156,32],[108,134,5,70,127,153,56,34,189,114,134,109  
],[195,132,31,185,147,43,147,61,92,168,39,62],[42,71,65,130,166,170,119,159,30,186,119,30],[126,198,184,67,84,75,147,4,1,69,190,33],[122,109,138,74,113,7,30,143,148,51,105,58  
],[34,102,45,182,0,178,166,51,195,135,75,189],[88,168,92,14,4,81,53,53,113,171,58,107],[109,17,146,24,178,59,77,179,75,105,118,86],[178,185,79,113,40,4,9,143,143,111,39,9]])
    n_n_array = np.array(struct_arr)
    arr_p_q = []
    for i in range(0,n,p):
        for j in range(0,n,q):
            arr_p_q.append(n_n_array[i:i + p][:,j:j + q])

    print(arr_p_q) #contiguous arrays

    average_list = [np.average(i) for i in arr_p_q]
    print(average_list)
    arr_sub = []
    k = 0
    for i in range(0,n,p):
        for j in range(0,n,q):
            arr_sub.append(n_n_array[i:i + p][:,j:j + q] - average_list[k])
            k += 1

    print(arr_sub)
    w = 0
    final_struct = np.zeros((n,n))
    for i in range(0,n,p):
        for j in range(0,n,q):
            final_struct[i:i + p][:,j:j + q] = arr_sub[w]
            w += 1
    print(final_struct)

def q3():
    n = int(input("number of equations:"))
    m = int(input("number of variables"))
    matrix = np.random.randn(n,m) #mean zero variance 1
    print("G is:")
    complex_matrix_skel = (np.random.randn(n,m))*1j
    G = matrix + complex_matrix_skel
    print(G)
    print("z is ")
    column_matrix = np.random.randn(n,1)
    complex_matrix_skel2 = column_matrix + (np.random.randn(n,1))*1j
    print(complex_matrix_skel2)

'''if __name__ == "__main__":
    q3()'''