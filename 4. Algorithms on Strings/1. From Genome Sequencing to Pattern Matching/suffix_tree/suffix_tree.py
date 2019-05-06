# python3
import sys

class suffTree(object):
    
    class Node(object):
        def __init__(self,lab):
            self.out = {}


def build_trie(text):
    tree = dict()
    num_nodes=0
    for i in range(len(text)):
        
        if tree=={}:
            for c in text:
                tree[num_nodes] = {c:num_nodes+1}
                num_nodes+=1             
        else:   
            parent_node=0
            cur_node=0
            for c in text:
                
                if c in tree[cur_node] and parent_node==0:
                    cur_node = tree[cur_node][c]
                else:                   
                    if parent_node in tree.keys():
                        tree[cur_node].setdefault(c,num_nodes+1)
                    else:
                        tree[parent_node] = {c:num_nodes+1}
                    num_nodes+=1
                    parent_node = num_nodes
        text = text[1:]
             
    return tree

def build_suffix_tree(text):
    """
    Build a suffix tree of the string text and return a list
    with all of the labels of its edges (the corresponding 
    substrings of the text) in any order.
    """
    result=[]
    tree={}
    
    # write your code here
    #tree = build_trie(text)
    for i in range(len(text)):
        temp_text=""
        currentNode = 0
        for j in range(i,len(text)):
            currentSymbol = text[j]

            if tree[currentNode][currentSymbol] in tree.keys():
                currentNode = tree[currentNode][currentSymbol]
            else:
                suffix_tree.setdefault(currentNode,{})

            #temp_text=temp_text+currentSymbol

            #if currentSymbol!="$" and len(tree[child_node])>1:                
            #    suffix_tree.setdefault(currentSymbol,temp_text)
            #    temp_text=""
            #elif (temp_text) in suffix_tree.keys():
            #    temp_text=""
            #else:
            #    temp_text = temp_text
            #if currentSymbol=="$":
            #    suffix_tree.setdefault(i,temp_text)

    for v in suffix_tree.values():
        result.append(v)
    # Implement this function yourself
    return result


if __name__ == '__main__':
    
    f = open("sample_tests/sample3","r")
    lines = f.readlines()
    text = str(lines[0].strip())

    #text = sys.stdin.readline().strip()
    result = build_suffix_tree(text)
    print("\n".join(result))