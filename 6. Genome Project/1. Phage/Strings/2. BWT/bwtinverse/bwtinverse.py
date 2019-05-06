# python3
import sys
import time
def InverseBWT(bwt):
    first = {}
    first_count = {}
    last = {}
    last_count = {}
    lex=set()

    #Build Last Column
    for x in range(len(bwt)):
        c=bwt[x]
        if c not in last:
            lex.add(c)
            last[c] = {x:[1,x]}
            last_count[c] = 1
        else:
            lex.add(c)
            count = last_count[c]+1
            last_count[c] = count
            last[c].setdefault(x,[count,x])

    #Build sorted btw
    sbwt= [0 for x in range(len(bwt))]
    lex = sorted(lex)
    i=0
    j=0
    reps=0
    while i < len(bwt):
        if i==0:
            sbwt[0] = lex[j]
            reps=last_count[lex[i]]
            j+=1
            i=i+reps
        else:
            char = lex[j]
            reps = last_count[lex[j]]
            char_arr = [char] * reps
            sbwt[i:(i+reps)]  = char_arr
            i=i+reps
            j+=1

        

    #Build First Column   
    for x in range(len(bwt)):
        if sbwt[x] not in first:
            count=1
            first[sbwt[x]] = {1:[1,x]}
            first_count[sbwt[x]] = 1 
        else:
            count = first_count[sbwt[x]]+1
            first_count[sbwt[x]] = count            
            first[sbwt[x]].setdefault(count,[count,x])

    #Navigate between first and last columns
    ans=''
    while len(ans)<len(bwt):
        if ans == '':
            symbol = '$'
            count = 1
            ans+=symbol
        char_ind = first[symbol][count][1]
        symbol = bwt[char_ind]
        ans+=symbol
        count = last[symbol][char_ind][0]
    ans = ans[::-1]
    return ans



if __name__ == '__main__':
    #bwt=open("sample_tests/sample3","r").readlines()[0].strip()
    bwt = sys.stdin.readline().strip()
    ans = InverseBWT(bwt)
    print(ans)
    #print(InverseBWT(bwt))