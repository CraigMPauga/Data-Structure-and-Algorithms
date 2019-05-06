# Uses python3
import sys

def opt(k, rs):
	k_mers = set()
	for r in rs:
		for x in range(0, len(r)-k+1):
			k_mers.add(r[x:x+k])
	p = set()
	s = set()
	for kmer in k_mers:
		p.add(kmer[:-1])
		s.add(kmer[1:])
	return p == s

rs = []
for i in range(1618):
	r = sys.stdin.readline().strip()
	rs.append(r)

for k in range(len(rs[2]), 1, -1):
	if opt(k, rs):
		print(k)
		break