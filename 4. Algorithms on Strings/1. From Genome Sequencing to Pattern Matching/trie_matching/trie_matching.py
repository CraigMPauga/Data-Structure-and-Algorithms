# python3
import sys

NA = -1

class Node:
	def __init__ (self):
		self.next = [NA] * 4

def build_trie(patterns):
    num_nodes=0
    tree = dict()
    # write your code here
    for i in range(len(patterns)):
        pattern = patterns[i]
        if tree=={}:
            for c in pattern:
                tree[num_nodes] = {c:num_nodes+1}
                num_nodes+=1             
        else:   
            parent_node=0
            cur_node=0
            for c in pattern:
                
                if c in tree[cur_node] and parent_node==0:
                    cur_node = tree[cur_node][c]
                else:                   
                    if parent_node in tree.keys():
                        tree[cur_node].setdefault(c,num_nodes+1)
                    else:
                        tree[parent_node] = {c:num_nodes+1}
                    num_nodes+=1
                    parent_node = num_nodes
             
    return tree

def solve (text, n, patterns):
	result = []
    tree = build_trie(patterns)

	return result


if __name__ == '__main__':
    patterns =[]
    f = open("sample_tests/sample1","r")
    lines = f.readlines()
    text = lines[0].strip()
    n = int(lines[1].strip())
    for i in range(2,2+n):
        patterns.append(str(lines[i]).strip())

    #text = sys.stdin.readline ().strip ()
    #n = int (sys.stdin.readline ().strip ())
    #patterns = []
    #for i in range (n):
    #    patterns += [sys.stdin.readline ().strip ()]

    ans = solve (text, n, patterns)

    sys.stdout.write (' '.join (map (str, ans)) + '\n')
