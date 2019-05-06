#uses python3
import sys
import itertools

class Tips:

    def __init__(self, k, reads):
        self.k = k
        self.threshold = self.k
        self.graph = {}
        self.paths = {}
        self.edges_removed = 0

        self.de_Bruijn(self.getKmers(reads))

    def getKmers(self, reads):
        getKmer = lambda read: [ read[j:j + self.k] for j in range(len(read) - self.k + 1) ]
        return [ kmer for read in reads for kmer in getKmer(read) ]

    def de_Bruijn(self, kmers):

        def add_edge(graph, left, right):
            graph.setdefault(left, [set(), 0])
            graph.setdefault(right, [set(), 0])

            if right not in graph[left][0]:
                graph[left][0].add(right)
                graph[right][1] += 1

        for kmer in kmers:
            left, right = kmer[:-1], kmer[1:]
            if left != right:
                add_edge(self.graph, left, right)

    def get_tips(self):
        for k, v in self.graph.items():
            find_and_remove = None

            if len(v[0]) == 1 and v[1] == 0:
                find_and_remove = self.getIncoming 
            elif len(v[0]) > 1:
                find_and_remove = self.getOutgoing 
            else : continue

            isTip = True
            while isTip:
                isTip = False
                for edge in v[0]:
                    if find_and_remove(edge, 0):
                        v[0].remove(edge)
                        self.edges_removed += 1
                        isTip = True
                        break

        return self.edges_removed

    def getOutgoing(self, current, depth):
        if self.outgoing_num(current) > 1 or self.incoming_num(current) > 1:
            return False
        
        if depth == self.threshold:
            return False

        if self.outgoing_num(current) == 0:
            return True

        if self.getOutgoing(next(iter(self.graph[current][0])), depth + 1):
            self.graph[current][0].pop()
            self.edges_removed += 1
            return True
        
        return False

    def getIncoming(self, current, depth):
        if depth == self.threshold:
            return False

        if self.outgoing_num(current) == 0 or self.incoming_num(current) > 1:
            return True
        
        if self.getIncoming(next(iter(self.graph[current][0])), depth + 1):
            self.graph[current][0].pop()
            self.edges_removed += 1
            return True
        
        return False

    def incoming_num(self, v):
        return self.graph[v][1]

    def outgoing_num(self, v):
        return len(self.graph[v][0])

if __name__ == "__main__":
    k = 15
    reads = sys.stdin.read().split()
    print(Tips(k, reads).get_tips())