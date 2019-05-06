#python3

from math import floor

class HeapBuilder():

    def __init__(self):
        self._swaps = []
        self._data =[]

    def ReadInput(self):
        #manual input
        #n = 5
        #self._data = [5, 4, 3, 2, 1]
        #auto input
        n = int(input())
        self._data = [int(s) for s in input().split()]


    def PrintAnswer(self):
        print(len(self._swaps))
        for swap in self._swaps:
            print(swap[0],swap[1])

    def BuildHeap(self):
        size = len(self._data)
        n = size
        swaps = 0
        iter = floor(n/2)
        while (iter+1):
            self.SiftDown(iter)
            iter-=1
        #for k in range(2,0, -1):
        #    self.SiftDown(k)

            
    def SiftDown(self, i):
        maxIndex = i
        size = len(self._data)

        l = self.LeftChild(i)
        if l <= size-1 and self._data[l] < self._data[maxIndex]:
            maxIndex = l

        r = self.RightChild(i)
        if r <= size-1 and self._data[r] < self._data[maxIndex]:
            maxIndex = r

        if i != maxIndex:

            val_maxIndex = self._data[maxIndex]
            val_i = self._data[i]
            self._data[i] = val_maxIndex
            self._data[maxIndex] = val_i
            self._swaps.append([i,maxIndex])
            self.SiftDown(maxIndex)

    def Parent(self, i):
        return floor(i/2)

    def LeftChild(self, i):
        return 2*i + 1

    def RightChild(self, i):
        return 2*i + 2

    def Solve(self):
        self.ReadInput()
        self.BuildHeap()
        self.PrintAnswer()


def main():
    heapBuilder = HeapBuilder()
    heapBuilder.Solve()

main()