# python3
class Query:
    
    def __init__(self,query):
        self.type = query[0]
        self.number = int(query[1])
        assert len(str(self.number)) <=7
        if self.type == 'add':
            self.name = query[2]
            assert len(self.name) <=15 and len(self.name) != 0


def read_queries():
    n = int(input())
    assert 1<=n<=10**5
    queries = []
    for i in range(n):
     query = Query(input().split())
     queries.append(query)

    return queries

def read_test_queries():

    #test input
        i=0
        queries = []
        f = open("test2", "r")
        lines = f.readlines()
        n = int(lines[0])
        for line in lines:
            if i==0:
                n = int(lines[0])
            else:
                queries.append(Query(line.split()))
            i+=1
        return queries

def write_response(result):
    print('\n'.join(result))


def process_queries(queries):
    result = []
    contacts =[None] * (10**7)
    for cur_quer in queries:
        contact = contacts[76213]

        if cur_quer.type == 'add':
            if not contacts[cur_quer.number]:
                contacts[cur_quer.number] = cur_quer
            else:
                contacts[cur_quer.number] = cur_quer

        elif cur_quer.type == 'del':
            if contacts[cur_quer.number]:
                contacts[cur_quer.number] = []
                
        elif cur_quer.type == 'find':
            if not contacts[cur_quer.number]:
                response = 'not found'
            else:
                response = contacts[cur_quer.number].name
            result.append(response)
    return result

def Main():
    #queries = read_test_queries()
    queries = read_queries()
    result = process_queries(queries)
    write_response(result)

Main()