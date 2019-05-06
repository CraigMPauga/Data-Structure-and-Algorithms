# python3
import sys

class suffTree(object):
    
    class Node(object):
        def __init__(self,lab):
            self.lab = lab
            self.out = {}

    def __init__(self,s):
        self.root = self.Node(None)
        self.root.out[s[0]] = self.Node(s)

        for i in range(1,len(s)):
            cur = self.root
            j=i
            while j<len(s):
                if s[j] in cur.out:
                    child = cur.out[s[j]]
                    lab = child.lab

                    k=j+1
                    while k-j < len(lab) and s[k] == lab[k-j]:
                        k+=1
                    if k-j == len(lab):
                        cur = child
                        j=k
                    else:
                        cExist, cNew = lab[k-j], s[k]
                        mid = self.Node(lab[:k-j])
                        mid.out[cNew] = self.Node(s[k:])
                        mid.out[cExist] = child
                        child.lab = lab[k-j:]
                        cur.out[s[j]]=mid
                else:
                    cur.out[s[j]] = self.Node(s[j:])

def retrieveLabels(node,result):
    child = node.out
    label = ""
    if child!={}:
        for k,v in child.items():
            label = label + v.lab
            retrieveLabels(v,result)
            result.append(label)
            label = ""
    else:
        return result

if __name__ == '__main__':
    result =[]
    f = open("sample_tests/sample2","r")
    lines = f.readlines()
    #text = str(lines[0].strip())
    text = "GAA$"
    #text = sys.stdin.readline().strip()
    suffix_Tree = suffTree(text) 
    root = suffix_Tree.root
    retrieveLabels(root,result)

    print("\n".join(result))