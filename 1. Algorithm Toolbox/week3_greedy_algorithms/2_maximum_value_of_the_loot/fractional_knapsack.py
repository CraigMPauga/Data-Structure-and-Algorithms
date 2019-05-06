# Uses python3
import sys


def get_optimal_value(capacity, weights, values):
    
    value = 0
    A=[[None]*3]*len(weights)
    
    for i in range(len(weights)):
        s = [values[i], weights[i], int(values[i]/weights[i])] 
        A[i] = [values[i], weights[i], values[i]/weights[i]]
    A.sort(key = lambda x: x[2])

    for j in range(len(weights),0,-1):
        j=j-1
        if capacity == 0:
            return value
        else:
            a = min(capacity,weights[j])
            value = value + a * A[j][2]
            capacity = capacity - a
            values.pop(j)
            weights.pop(j)
            A.pop(j)


        

    # write your code here

    return value

if __name__ == "__main__":


    #f = open("01","r")
    #lines = f.readlines()
    #n, capacity = list(map(int, lines[0].split()))
    #for i in range(1,n+1):
    #    value, weight = list(map(int, lines[i].split()))
    #    values.append(value)
    #    weights.append(weight)
    data = list(map(int, sys.stdin.read().split()))
    data.append(list(map(int, sys.stdin.read().split())))

    #n, capacity = data[0:2]
    #values=[None]*n
    #weights=[None]*n
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]

    #for i in range(n):
    #    cur_list = "data" + str(i)

    #    data2 = list(map(int, sys.stdin.read().split()))
    ##    v,w = data2[0:2]
    #    values[i] = v
    #    weights[i] = w

    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
