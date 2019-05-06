#python3

import sys

from math import floor


class Thread():
   
    def __init__(self, index, finish_time):
        self.index = index
        self.finish_time = finish_time

    def get_finish_time(self):
        return self.finish_time

    def get_index(self):
        return index
        


class PriorityQueue():
    
    def __init__(self, num_threads):
        self.queue = []

    def put(self, thread):
        self.queue.append(thread)
        size = len(self.queue)
        self.SiftUp(size-1)

    def pop(self,):
        size = len(self.queue) -1
        self.queue[0] = self.queue[size]
        del self.queue[-1]
       
        self.SiftDown(0)
     
    def SiftDown(self,i):
        maxIndex = i
        size = len(self.queue)
        l = self.LeftChild(i)
        if l <= size-1 and self.queue[l].finish_time <= self.queue[maxIndex].finish_time:
            if (self.queue[l].finish_time == self.queue[maxIndex].finish_time) and (self.queue[l].index < self.queue[maxIndex].index):
                maxIndex = l
            if self.queue[l].finish_time != self.queue[maxIndex].finish_time:
                maxIndex = l

        r = self.RightChild(i)
        if r <= size-1 and self.queue[r].finish_time <= self.queue[maxIndex].finish_time:
            if (self.queue[r].finish_time == self.queue[maxIndex].finish_time) and (self.queue[r].index < self.queue[maxIndex].index):
                maxIndex = r
            if self.queue[r].finish_time != self.queue[maxIndex].finish_time:
                maxIndex = r

        if i != maxIndex:

            val_maxIndex = self.queue[maxIndex]
            val_i = self.queue[i]
            self.queue[i] = val_maxIndex
            self.queue[maxIndex] = val_i
            self.SiftDown(maxIndex)

    def LeftChild(self, i):
        return 2*i + 1

    def RightChild(self, i):
        return 2*i + 2
   
    def SiftUp(self,i):
        curIndex = i
        parent = floor((curIndex-1)/2)
        parent_finishTime = self.queue[parent].finish_time
        currentNode_finishTime = self.queue[curIndex].finish_time
        currentNode_index = self.queue[curIndex].index
        parentNode_index = self.queue[parent].index

        while (parent_finishTime >= currentNode_finishTime) and (curIndex > 0):
            if (parent_finishTime == currentNode_finishTime):
                if(currentNode_index < parentNode_index):
                    val_current= self.queue[curIndex]
                    val_parent = self.queue[parent]
                    self.queue[parent] = val_current
                    self.queue[curIndex] = val_parent
            else:
                val_current= self.queue[curIndex]
                val_parent = self.queue[parent]
                self.queue[parent] = val_current
                self.queue[curIndex] = val_parent

            curIndex=parent
            parent = floor((curIndex-1)/2)
            parent_finishTime = self.queue[parent].finish_time
            currentNode_finishTime = self.queue[curIndex].finish_time

            #self.SiftUp(parent)
        
    def Parent(self, i):
        return floor(i/2)


class JobQueue():

    def ReadInput(self):
        #terminal input
        self.num_threads, self.num_jobs = map(int, input().split())
        self.jobs = list(map(int, input().split()))
        assert 1<=self.num_threads<=10**5
        assert 1<=self.num_jobs<=10**5
        #test input
        #self.num_threads, self.num_jobs = 4, 20
        #self.jobs = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
        #self.num_threads, self.num_jobs = 2, 5
        #self.jobs = [1, 2, 3, 4, 5]

        #file input
        #f = open("tests/08", "r")
        #lines = f.readlines()
        #self.num_threads = int(lines[0].split()[0])
        #assert 1<=self.num_threads<=10**5
       
       # self.num_jobs = int(lines[0].split()[1])
        #assert 1<=self.num_jobs<=10**5

        #self.jobs = list(map(int, lines[1].split()))
        

    def CheckAnswer(self):
        
        myAnswer = open("answer", "r")
        testAnswer = open("tests/08.a","r")
        i=0
        for line1 in testAnswer:
            for line2 in myAnswer:
                if line1 == line2:
                    i+=1
                    print("Line" + " " + str(i) + " " + "is a match")
                    break
                else:
                    print("Failure at line " + str(i))
                    sys.exit("Failure at line " + str(i))

        print("Congrats!")
                    
                    

        
    def AssignJobs(self):
        
        q = PriorityQueue(self.num_threads)
        i=0
        cur_time = 0
        answer = open("answer","w")
        while (self.jobs):
            
            if (self.num_threads > len(q.queue)): 
                finish_time =  self.jobs[0]
                assert 0<= finish_time <= 10**9

                thread = Thread(i, finish_time)
                answer.write(str(i) + " " + str(cur_time) + '\n')       
                print(i, cur_time)
                self.jobs.pop(0)
                q.put(thread)
                i+=1
            else:
                while (self.jobs):
                    index = q.queue[0].index  
                    cur_time = q.queue[0].finish_time
                    answer.write(str(index) + " " + str(cur_time) + '\n')
                    print(index, cur_time)
                    q.pop()
                    q.put(Thread(index, cur_time + self.jobs[0]))
                    self.jobs.pop(0)
                   # pop_index = 0
                    #if len(q.queue) > 3:
                    #    left_child_time = q.queue[1].finish_time
                    #    right_child_time = q.queue[2].finish_time
                    #    cur_index = q.queue[0].index
                    #    left_child_index = q.queue[1].index
                    #    right_child_index = q.queue[2].index

                    #while ((q.queue[0].finish_time == q.queue[1].finish_time) or (q.queue[0].finish_time == q.queue[2].finish_time)):
                    #    if q.queue[0].finish_time == q.queue[1].finish_time:
                    #        min_index = min(q.queue[0].index,q.queue[1].index)
                    #        if q.queue[0].index < q.queue[1].index:
                     #           pop_index = 0
                     #       else:
                     #           pop_index = 1
                     #   elif q.queue[0].finish_time == q.queue[2].finish_time:
                     #       min_index = min(q.queue[0].index,q.queue[2].index)
                     #       if q.queue[0].index < q.queue[2].index:
                     #           pop_index = 0
                     #       else:
                     #           pop_index = 2
#
#                        finish_time = cur_time + self.jobs[0]
#                        answer.write(str(min_index) + " " + str(cur_time) + '\n')
#                        print(min_index, cur_time)
#                        q.pop(pop_index)
#                        q.put(Thread(min_index, finish_time))
#                        self.jobs.pop(0)#


                    #if(self.jobs):
                    #    index = q.queue[0].index
                    #    answer.write(str(index) + " " + str(cur_time) + '\n')
                    #    print(index, cur_time)
                    #    q.pop()
                    #    q.put(Thread(index, cur_time + self.jobs[0]))
                    #    self.jobs.pop(0)
                         


                      #if  (len(q.queue) >= 3) and cur_time == left_child_time:   
                      #    min_index = min(cur_index,left_child_index)
                      #    max_index = max(cur_index,left_child_index)
                      #    answer.write(str(min_index) + " " + str(cur_time) + '\n')
                      #    print(min_index, cur_time)
                      ##    q.pop()
                       #   q.put(Thread(min_index, cur_time + self.jobs[0]))
                       #   self.jobs.pop(0)
                        #  answer.write(str(max_index) + " " + str(cur_time) + '\n')
                        #  print(max_index, cur_time)
                        #  q.pop()
                        #  q.put(Thread(max_index, cur_time + self.jobs[0]))
                        #  self.jobs.pop(0)

                      #elif (len(q.queue) >= 3) and cur_time == right_child_time:
                      #    min_index = min(cur_index,right_child_index)
                      #    max_index = max(cur_index,right_child_index)
                      #    answer.write(str(min_index) + " " + str(cur_time) + '\n')
                      #    print(min_index, cur_time)
                      ##    q.pop()
                        #  q.put(Thread(min_index, cur_time + self.jobs[0]))
                        #  self.jobs.pop(0)
                        #  answer.write(str(max_index) + " " + str(cur_time) + '\n')
                        #  print(max_index, cur_time)
                       #   q.pop()
                       #   q.put(Thread(max_index, cur_time + self.jobs[0]))
                       #   self.jobs.pop(0)
                      #else:
                      #    index = q.queue[0].index
                      #    answer.write(str(index) + " " + str(cur_time) + '\n')
                      #    print(index, cur_time)
                      #    q.pop()
                      #    q.put(Thread(index, cur_time + self.jobs[0]))
                      #    self.jobs.pop(0)
        
    def ProcessJobs(self):
        pass

    def Solve(self):
        self.ReadInput()
        self.AssignJobs()
        #self.CheckAnswer()


def Main():
    jobQueue = JobQueue()
    jobQueue.Solve()

Main()


