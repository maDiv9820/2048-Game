from hashlib import new
import random
def start_game():
    mat = []
    for i in range(4):
        mat.append([0]*4)
    
    return mat

def add_new_2(mat):
    r = random.randint(0, 3)
    c = random.randint(0, 3)

    while mat[r][c] != 0:
        r = random.randint(0, 3)
        c = random.randint(0, 3)
    
    mat[r][c] = 2

def get_current_state(mat):
    for i in range(4):
        for j in range(4):
            if mat[i][j] == 2048:
                return 'WON'
        
    for i in range(4):
        for j in range(4):
            if mat[i][j] == 0:
                return 'GAME NOT OVER'
            if i + 1 < 4 and mat[i][j] == mat[i+1][j]:
                return 'GAME NOT OVER'
            if j + 1 < 4 and mat[i][j] == mat[i][j+1]:
                return 'GAME NOT OVER'

    return 'LOST'

def compress(mat):
    new_mat = []
    for i in range(4):
        new_mat.append([0] * 4)

    change = False   
    for i in range(4):
        pos = 0
        for j in range(4):
            if mat[i][j] != 0:
                new_mat[i][pos] = mat[i][j]
                if pos != j:
                    change = True
                pos += 1

    return new_mat, change

def merge(mat):
    change = False
    for i in range(4):
        for j in range(3):
            if mat[i][j] == mat[i][j+1] and mat[i][j] != 0:
                mat[i][j] *= 2
                mat[i][j+1] = 0
                change = True

    return change

def reverse(mat):
    new_mat = []
    for i in range(4):
        new_mat.append([])
        for j in range(4):
            new_mat[i].append(mat[i][3 - j])

    return new_mat

def transpose(mat):
    new_mat = []
    for i in range(4):
        new_mat.append([])
        for j in range(4):
            new_mat[i].append(mat[j][i])

    return new_mat

def move_up(mat):
    transpose_mat = transpose(mat)
    compress_mat, change1 = compress(transpose_mat)
    change2 = merge(compress_mat)
    changed = change1 or change2
    compress_mat, change1 = compress(compress_mat)
    transpose_mat = transpose(compress_mat)
    return transpose_mat, changed

def move_down(mat):
    transpose_mat = transpose(mat)
    reverse_mat = reverse(transpose_mat)
    compress_mat, change1 = compress(reverse_mat)
    change2 = merge(compress_mat)
    changed = change1 or change2
    compress_mat, change1 = compress(compress_mat)
    reverse_mat = reverse(compress_mat)
    transpose_mat = transpose(reverse_mat)
    return transpose_mat, changed

def move_right(mat):
    reverse_mat = reverse(mat)
    compress_mat, change1 = compress(reverse_mat)
    change2 = merge(compress_mat)
    changed = change1 or change2
    compress_mat, change1 = compress(compress_mat)
    reverse_mat = reverse(compress_mat)
    return reverse_mat, changed

def move_left(mat):
    compress_mat, change1 = compress(mat)
    change2 = merge(compress_mat)
    changed = change1 or change2
    compress_mat, change1 = compress(compress_mat)
    return compress_mat, changed