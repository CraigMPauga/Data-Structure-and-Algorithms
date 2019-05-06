#Uses python3
import sys

# Return the trie built from patterns
# in the form of a dictionary of dictionaries,
# e.g. {0:{'A':1,'T':2},1:{'C':3}}
# where the key of the external dictionary is
# the node ID (integer), and the internal dictionary
# contains all the trie edges outgoing from the corresponding
# node, and the keys are the letters on those edges, and the
# values are the node IDs to which these edges lead.

def tree_rec(tree,k,c,nodes):
    if c in tree[k]:
        tree_rec(tree,tree[k][c],c)
        
    else:
        tree[k] = {c:nodes+1}

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


if __name__ == '__main__':
    #patterns =[]
    #f = open("sample_tests/sample3","r")
    #lines = f.readlines()
    #n = int(lines[0])
    #for i in range(1,n+1):
    #    patterns.append(str(lines[i]).strip())
    patterns = sys.stdin.read().split()[1:]
    tree = build_trie(patterns)
    for node in tree:
        for c in tree[node]:
            print("{}->{}:{}".format(node, tree[node][c], c))
