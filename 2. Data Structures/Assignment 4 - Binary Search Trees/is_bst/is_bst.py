# python3

import sys, threading
import math

INT_MAX = 4294967296
INT_MIN = -4294967296

sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**25)  # new thread will get stack of such size

class TreeOrders:

    def test_read(self):
      input_file = open('tests/04', "r")
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
      assert 0<=self.n<=10**5
      self.key = [0 for i in range(self.n)]
      self.left = [0 for i in range(self.n)]
      self.right = [0 for i in range(self.n)]
      self.index = [i for i in range(self.n)]
      self.result = []
      for i in range(self.n):
        [a, b, c] = map(int, sys.stdin.readline().split())
        assert -2**31 <= a <= (2**31) - 1
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

    def isBST(self,index,key,left,right,mini,maxi,isBST):
        return self.isBSTUtil(index,key,left,right,mini,maxi,isBST)


    def isBSTUtil(self,index,key,left,right,mini,maxi,isBST):

         #False if this node violates min/max constraint
        if key<mini or key> maxi:
            return False

        #Check if node is leaf
        if self.left[index] == -1 and self.right[index] == -1:
            return True
           
        if self.left[index] == -1:
            left_check = True
        elif key ==self.key[left]:
            left_check = False
        else:
            left_check = self.isBSTUtil(self.index[left],
                                    self.key[left],
                                    self.left[left],
                                    self.right[left],
                                    mini,
                                    self.key[index],
                                    isBST) 
        if self.right[index] == -1:
            right_check = True
        else:
            right_check = self.isBSTUtil(self.index[right],
                                    self.key[right],
                                    self.left[right],
                                    self.right[right],
                                    self.key[index],
                                    maxi,
                                    isBST)
        if left_check and right_check:
            return True
        else:
            return False
    

def main():
    tree = TreeOrders()
    tree.test_read()
    if tree.index ==[]:
        print("CORRECT")
    elif len(tree.index) == 1:
        print("CORRECT")
    elif tree.isBST(tree.index[0],tree.key[0],tree.left[0],tree.right[0],INT_MIN,INT_MAX,True):
        print("CORRECT")
    else:
        print("INCORRECT")

threading.Thread(target=main).start()

