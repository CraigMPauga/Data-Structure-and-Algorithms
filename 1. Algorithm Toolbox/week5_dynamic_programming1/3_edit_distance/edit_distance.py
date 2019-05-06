# Uses python3
def edit_distance(s, t):
    s_len = len(s)+1
    t_len = len(t)+1
    D = [[0]*t_len for i in range(s_len)]


    #Fill the distance for each first column and row. This should just be equal to i
    for i in range(0,s_len):
        D[i][0] = i

    for j in range(0,t_len):
        D[0][j] = j
        
    #Fill out the distance matrix for the subsequent strings
    for i in range(1,s_len):
        for j in range(1,t_len):

            insertion = D[i][j-1]+1
            deletion = D[i-1][j]+1
            match = D[i-1][j-1]
            mismatch = D[i-1][j-1]+1

            if s[i-1]!=t[j-1]:
                D[i][j] = min(insertion, deletion, mismatch)
            elif s[i-1]==t[j-1]:
                D[i][j] = min(insertion, deletion, match)
                   
    return D[s_len-1][t_len-1]

if __name__ == "__main__":
    #f = open("01","r")
    #lines = f.readlines()
    #str1 = str(lines[0].strip())    
    #str2 = str(lines[1].strip())
    #print(edit_distance(str1, str2))
    print(edit_distance(input(), input()))
    