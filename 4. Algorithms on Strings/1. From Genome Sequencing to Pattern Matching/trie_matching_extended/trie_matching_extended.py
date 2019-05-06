# python3
import sys

NA = -1

class Node:
    def __init__(self,ID,parent):
        self.parent = parent
        self.child = None
        self.ID = ID
        self.isPattern = False


def build_trie(patterns):
    num_nodes=0
    tree = dict()
    for i in range(len(patterns)):
        j=0
        pattern = patterns[i]
        if tree=={}:
            for c in pattern:
                tree[num_nodes] = {c:Node(num_nodes+1,num_nodes)}
                tree[num_nodes][c].parent = j
                num_nodes+=1
                j+=1
                if j>=len(pattern):
                    tree[num_nodes-1][c].isPattern = True
        else:   
            parent_node=0
            cur_node=0
            j=0
            for c in pattern:
                
                if c in tree[cur_node] and parent_node==0:
                    cur_node = tree[cur_node][c].ID
                    j+=1
                    if j>=len(pattern):
                        tree[parent_node][c].isPattern = True
                else:                   
                     if parent_node in tree.keys():
                        tree[cur_node].setdefault(c,Node(num_nodes+1,parent_node))
                        j+=1
                        if j>= len(pattern):
                            tree[cur_node][c].isPattern = True
                     else:
                        tree[parent_node] = {c:Node(num_nodes+1,parent_node)}
                        j+=1
                        if j>= len(pattern):
                            tree[num_nodes][c].isPattern = True
                     num_nodes+=1
                     parent_node = num_nodes

        
        
    return tree


def PrefixTrieMatching(text,tree,p):
    match=""
    i=0
    node = 0
    while i<len(text):
        
        t = text[i]
        if t in tree[node]:
            if tree[node][t].isPattern == True:
                first_char = p+i-len(match)
                return first_char
            else:
                i+=1
                node=tree[node][t].ID
                match+=t
        else:
            return

        if node not in tree.keys():
            first_char = p + i - len(match)
            return first_char


    return

def TrieMatching(text,tree):
    results=[]
    p=0
    while text:
        first_char = PrefixTrieMatching(text,tree,p)
        if first_char!=None:
            results.append(first_char)
        text = text[1:]
        p+=1
    return results

def solve(text,n,patterns):


    tree = build_trie(patterns)
    results = TrieMatching(text,tree)

    return results

if __name__=='__main__':
    #patterns=[]
    #f = open("sample_tests/sample4","r")
    #lines = f.readlines()
    #text = lines[0].strip()
    #n = int(lines[1].strip())
    #for i in range(2,2+n):
    #    patterns.append(str(lines[i]).strip())

    text = sys.stdin.readline ().strip ()
    n = int (sys.stdin.readline ().strip ())
    patterns = []
    for i in range (n):
        patterns += [sys.stdin.readline ().strip ()]

    ans = solve(text, n, patterns)
    sys.stdout.write (' '.join(str(x) for x in ans))
    sys.stdout.write ('\n')