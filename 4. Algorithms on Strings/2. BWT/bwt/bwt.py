# python3
import sys

def BWT(text):
    M=[[0 for x in range(len(text))] for y in range(len(text))]
    for i in range(len(text)):
        s1=text[i:]
        s2=text[:i]
        s = list(s1+s2)
        M[i] = s
    
    M.sort(key=lambda x: (x[0:len(text)]))
    s=""
    for i in range(len(text)):
        c=M[i][-1]
        s=s+c
    return s

if __name__ == '__main__':
    text=open("sample_tests/sample3","r").readlines()[0].strip()
    #text = sys.stdin.readline().strip()
    print(BWT(text))