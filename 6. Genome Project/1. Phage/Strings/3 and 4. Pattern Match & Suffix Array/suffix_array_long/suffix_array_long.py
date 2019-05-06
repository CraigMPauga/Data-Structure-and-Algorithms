# python3
import sys

def SortCharacter(S):

    order = [0 for x in range(len(S))]
    count = [0 for x in range(256)]

    for i in range(len(S)):
        count[ord(S[i])] = count[ord(S[i])]+1
    for j in range(len(count)):
        count[j] = count[j] + count[j-1]
    for i in range(len(S)-1,-1,-1):
        c=S[i]
        count[ord(c)] = count[ord(c)]-1
        order[count[ord(c)]] = i
    return order

def ComputeCharClasses(S,order):
    eclass = [-1 for x in range(len(S))]
    eclass[order[0]]=0
    
    for i in range(0,len(S)):
        if S[order[i]]!=S[order[i-1]]:
            eclass[order[i]]=eclass[order[i-1]]+1
        else:
            eclass[order[i]]=eclass[order[i-1]]
    return eclass

def SortDoubled(S,L,order,eclass):
    newOrder = [0 for x in range(len(S))]
    count = [0 for x in range(len(S))]

    for i in range(len(S)):
        count[eclass[i]] = count[eclass[i]]+1
    for j in range(1,len(S)):
        count[j] = count[j] + count[j-1]
    for i in range(len(S)-1,-1,-1):
        start = (order[i] - L + len(S))%len(S)
        cl = eclass[start]
        count[cl] = count[cl] - 1
        newOrder[count[cl]] = start
    return newOrder

def UpdateClasses(order,eclass,L):
    n = len(order)
    newClass = [0 for x in range(n)]
    newClass[order[0]]=0

    for i in range(1,n):
        cur = order[i] 
        prev = order[i-1]
        mid = ((cur+L)%n)
        midPrev = ((prev+L)%n)
        
        if eclass[cur]!=eclass[prev] or eclass[mid]!=eclass[midPrev]:
            newClass[cur] = newClass[prev]+1
        else:
            newClass[cur] = newClass[prev]
    return newClass




def build_suffix_array(S):
 
    order = SortCharacter(S)
    eclass = ComputeCharClasses(S,order)
    L=1
    while L<len(S):
        order = SortDoubled(S,L,order,eclass)
        eclass = UpdateClasses(order,eclass,L)
        L=2*L
    result = order

    return result


if __name__ == '__main__':
  #text =open("sample_tests/sample2","r").readlines()[0].strip()
  text = sys.stdin.readline().strip()
  print(" ".join(map(str, build_suffix_array(text))))
