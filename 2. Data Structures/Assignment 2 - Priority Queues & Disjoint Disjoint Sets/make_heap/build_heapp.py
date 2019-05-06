# python3

class HeapBuilder:
  def __init__(self):
    self._swaps = []
    self._data = []

  def ReadData(self):
    #n = int(input())
    #self._data = [int(s) for s in input().split()]
    #assert n == len(self._data)
    n=5
    self._data = [5, 4 ,3,2,1]


  def WriteResponse(self):
    print(len(self._swaps))
    for swap in self._swaps:
      print(swap[0], swap[1])

  def GenerateSwaps(self):
    pass
    # TODO: replace by a more efficient implementation
    #for i in range(len(self._data)):
    #  for j in range(i + 1, len(self._data)):
    #    if self._data[i] > self._data[j]:
    #      self._swaps.append((i, j))
    #      self._data[i], self._data[j] = self._data[j], self._data[i]
    
          

  def Solve(self):
    self.ReadData()
    self.GenerateSwaps()
    self.WriteResponse()

if __name__ == '__main__':
    heap_builder = HeapBuilder()
    heap_builder.Solve()
