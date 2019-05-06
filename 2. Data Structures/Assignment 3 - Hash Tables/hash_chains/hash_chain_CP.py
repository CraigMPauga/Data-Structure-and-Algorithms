# python 3

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

	def __init__(self, bucket_count):
		self.bucket_count = bucket_count
		self.elems = [[]]* bucket_count

	def _hash_func(self,s):
		ans = 0
		for c in reversed(s):
			ans = (ans * self._multiplier + ord(c)) % self._prime
		return ans % self.bucket_count

	def write_search_result(self, was_found):
		print('yes' if was_found else 'no')

	def write_chain(self, chain):
		print(' '.join(chain))

	def read_query(self):
		#query = input().split()
		return Query(input().split())

	def read_test_query(self,i):	
		f = open("tests/01", "r")
		lines = f.readlines()
		return Query(lines[i+2].split())
		


	def process_query(self, query):

		if query.type == "check":
			if not self.elems[query.ind]:
				print ('\n')
			else:
				print(' '.join(reversed(self.elems[query.ind])))
		else:

			hash_index = self._hash_func(query.s)
			ind = self.elems[hash_index]

			if query.type == 'find':
				if ind != []:
					for elem in self.elems[hash_index]:
						if elem == query.s:
							print("yes")
							
						elif elem!= query.s:
							print("no")

				else:
					print("no")
				#self.write_search_result(ind != [])
			elif query.type == 'add':
				if ind == []:
					self.elems[hash_index]=[query.s]
				else:
					for elem in self.elems[hash_index]:
						if elem != query.s:
							self.elems[hash_index].append(query.s)
					
			else:
				if ind != []:
					j=0
					for elem in reversed(self.elems[hash_index]):
						j+=1
						if elem == query.s:
							del self.elems[hash_index][-j]
					
					#self.elems[query.ind] = None
					

	def process_queries(self):
		n = int(input()) 
		assert 1<=n<=10**5 and (n/5) <= self.bucket_count <= n

		for i in range(n):
			self.process_query(self.read_query())

	def test_process_queries(self):
		n = int(lines[1])
		for i in range(n):
			self.process_query(self.read_test_query(i))

if __name__ == '__main__':
	#test = True
	test = False
	if test:
        test_str = "tests/01"
		test_line_index = 2
		f = open(test_str, "r")
		lines = f.readlines()
		bucket_count = int(lines[0])
		proc = QueryProcessor(bucket_count)
		proc.test_process_queries()
	else:
		bucket_count = int(input())
		proc = QueryProcessor(bucket_count)
		proc.process_queries()
