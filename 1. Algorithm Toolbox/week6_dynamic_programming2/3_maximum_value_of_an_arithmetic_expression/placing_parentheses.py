# Uses python3

import sys

def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False

def get_maximum_value(dataset):

    numbers = list(map(int,expression[0::2]))
    ops = list(expression[1::2])


    min_matrix = [[0 for i in range(len(numbers))] for j in range(len(numbers))]
    max_matrix = [[0 for i in range(len(numbers))] for j in range(len(numbers))]

    for i in range(len(numbers)):
        max_matrix[i][i] = numbers[i]
        min_matrix[i][i] = numbers[i]

    for s in range(len(numbers)):
        for i in range(len(numbers) - s - 1):
            j=i+s+1
            mini,maxi = min_max(i,j,min_matrix,max_matrix,ops)
            min_matrix[i][j] = mini
            max_matrix[i][j] = maxi
    

    return max_matrix[0][len(numbers)-1]

def min_max(i,j, min_matrix, max_matrix,ops):
    mini = sys.maxsize
    maxi = -sys.maxsize

    for k in range(i,j):
        a = evalt(max_matrix[i][k], max_matrix[k+1][j], ops[k])
        b = evalt(max_matrix[i][k], min_matrix[k+1][j], ops[k])
        c = evalt(min_matrix[i][k], max_matrix[k+1][j], ops[k])
        d = evalt(min_matrix[i][k], min_matrix[k+1][j], ops[k])
        mini = min(mini, a, b, c, d)
        maxi = max(maxi, a, b, c, d)
    return mini,maxi

if __name__ == "__main__":
    #f = open("02","r")
    #lines = f.readlines()
    #expression = str(lines[0])
    expression = input()

    #print(get_maximum_value(expression))

    print(get_maximum_value(expression))
       