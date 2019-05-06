# python3
import sys

def ComputePrefixFunction(P):
    s= [None for x in range(len(P))]
    s[0]=0
    border=0

    for i in range(1,len(P)):
        while (border>0 and P[i]!=P[border]):
            border = s[border-1]
        if P[i] == P[border]:
            border = border + 1
        else:
            border = 0
        s[i]=border
    return s

def find_pattern(pattern, text):
    if len(pattern)>len(text):
        return ''
    S = pattern +"$" + text
    s = ComputePrefixFunction(S)
    result = []

    for i in range(len(pattern)+1,len(S)):
        if s[i]==len(pattern):
            result.append(i-(2*len(pattern)))
    return result

if __name__ == '__main__':
  #lines =open("sample_tests/sample3","r").readlines()
  #pattern = lines[0].strip()
  #text = lines[1].strip()
  pattern = sys.stdin.readline().strip()
  text = sys.stdin.readline().strip()
  result = find_pattern(pattern, text)
  print(" ".join(map(str, result)))

