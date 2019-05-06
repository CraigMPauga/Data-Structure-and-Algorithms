# python3

import sys, threading
sys.setrecursionlimit(10**6) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeOrders:

    def test_read(self):
      input_file = open('tests/02', "r")
      lines = input_file.readlines()
      self.n = int(lines[0])
      self.key = [0 for i in range(self.n)]
      self.left = [0 for i in range(self.n)]
      self.right = [0 for i in range(self.n)]
      self.index = [i for i in range(self.n)]
      self.result =[]
      for i in range(self.n):
        [a, b, c] = map(int, lines[i+1].split())
        self.key[i] = a
        self.left[i] = b
        self.right[i] = c
          
    def resetResult(self):
        self.result=[]

    def read(self):
      self.n = int(sys.stdin.readline())
      assert 1<=self.n<=10**5
      self.key = [0 for i in range(self.n)]
      self.left = [0 for i in range(self.n)]
      self.right = [0 for i in range(self.n)]
      self.index = [i for i in range(self.n)]
      self.result = []
      for i in range(self.n):
        [a, b, c] = map(int, sys.stdin.readline().split())
        assert 0 <= a <= 10**9
        assert -1 <= b
        assert c <= (self.n) - 1
        self.key[i] = a
        self.left[i] = b
        self.right[i] = c

    def inOrder(self,index,key,left,right):

        if self.left[index] == -1:
            pass
        else:
            self.inOrder(self.index[left],self.key[left],self.left[left],self.right[left])

        self.result.append(self.key[index])

        if self.right[index] == -1:
            pass
        else:
            self.inOrder(self.index[right],self.key[right],self.left[right],self.right[right])
        return self.result

    def preOrder(self,index,key,left,right):

        self.result.append(self.key[index])
        if self.left[index] == -1:
            pass
        else:
            self.preOrder(self.index[left],self.key[left],self.left[left],self.right[left])

        

        if self.right[index] == -1:
            pass
        else:
            self.preOrder(self.index[right],self.key[right],self.left[right],self.right[right])              
        return self.result

    def postOrder(self,index,key,left,right):

        if self.left[index] == -1:
            pass
        else:
            self.postOrder(self.index[left],self.key[left],self.left[left],self.right[left])

        

        if self.right[index] == -1:
            pass
        else:
            self.postOrder(self.index[right],self.key[right],self.left[right],self.right[right])
        self.result.append(self.key[index])
        return self.result


def main():
    tree = TreeOrders()
    tree.read()
    print(" ".join(str(x) for x in tree.inOrder(tree.index[0],tree.key[0],tree.left[0],tree.right[0])))
    tree.resetResult()
    print(" ".join(str(x) for x in tree.preOrder(tree.index[0],tree.key[0],tree.left[0],tree.right[0])))
    tree.resetResult()
    print(" ".join(str(x) for x in tree.postOrder(tree.index[0],tree.key[0],tree.left[0],tree.right[0])))

threading.Thread(target=main).start()

