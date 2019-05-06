# python3


#General query class for each query object
class Query:
    def __init__(self,query):
        self.type = query[0]
        if self.type == 'check':
            self.ind = int(query[1])
        else:
            self.s = query[1]

class QueryProcessor:
    _multiplier = 263
    _prime = 1000000007

    def __init__(self,bucket_count,isTest):
        self.bucket_count = bucket_count
        self.elems = [[]] * bucket_count
        self.isTest = bool
    
    def read_query(self):
        return Query(input().split())

    def test_read_query(self,lines,i):
        return Query(lines[i+2].split())

    def hash_function(self,string):
        hash = 0
        for char in reversed(string):
            hash = (hash * self._multiplier + ord(char)) % self._prime
        return hash % self.bucket_count

    def processQuery(self,query):
     
        if query.type == "check":
            if not self.elems[query.ind]:
                print()                
            else:
                print(' '.join(self.elems[query.ind]))
        else:

            hash_index = self.hash_function(query.s)
            index = self.elems[hash_index]

            if query.type == 'find':
                if index != []:
                    for elem in index:
                        if elem == query.s:
                            response = 'yes'
                            break
                        elif elem != query.s:
                            response = 'no'
                else:
                    response = 'no'
                print(response)
            elif query.type == 'add':
                if index == []:
                    #not sure why this works. Could be potential memory issue
                    self.elems[hash_index] = [query.s]
                else:
                    for elem in index:
                        if elem == query.s:
                           exists = True
                           break
                        else:
                           exists = False
                    if not exists:
                        self.elems[hash_index].insert(0,query.s)
            else:
                if index != []:
                    for elem in index:
                        if elem == query.s:
                            index.remove(elem)
                            break


    def process_queries(self):
            n = int(input())
            assert 1<=n<=10**5 and (n/5) <= self.bucket_count <=n

            for i in range(n):
                self.processQuery(self.read_query())

    def test_process_queries(self,lines):
            
            n = int(lines[1])
            for i in range(n):
                self.processQuery(self.test_read_query(lines,i))


class TestCase:

    def __init__(self,i):
        self.i = i
    
    def RunTestCase(self):
        isTest = True
        self.testCaseInput = str("tests/0" + str(self.i))
        self.testCaseAnswer = str("tests/testOut/answer" + str(self.i))
        a = open(self.testCaseAnswer, "w")
        f = open(self.testCaseInput, "r")
        lines = f.readlines()
        bucket_count = int(lines[0])
        proc = QueryProcessor(bucket_count,isTest)
        proc.test_process_queries(lines)



if __name__ == '__main__':
        #isTest = True
        isTest = False
        if isTest:
            #for i in range(4):
            testCase = TestCase(4+1)
            testCase.RunTestCase()
        else:
            bucket_count = int(input())
            proc = QueryProcessor(bucket_count,isTest)
            proc.process_queries()