n,m = 5,5

import time
def HCF(a, b):
    if(b == 0): return a
    else: return HCF(b, a%b)

nodes = []
for y in range(n):
    for x in range(m):
        nodes.append([x,y])

tree = {}
edges = []
start = time.time()
for n1 in nodes:
    connections = []
    for n2 in nodes:
        dist = [n2[0]-n1[0], n2[1]-n1[1]]
        if dist==[0,0]: continue
        hcf = HCF(abs(dist[0]), abs(dist[1]))
        if hcf==1:
            connections.append(f"{n2[0]}:{n2[1]}")
            edge = sorted([n1,n2])
            if edge not in edges: edges.append(edge)
    tree[f"{n1[0]}:{n1[1]}"] = connections

for node in nodes:
    print(len(tree[f"{node[0]}:{node[1]}"]), end="\n\n" if node[0]==m-1 else " , ")
print(len(edges))
print(time.time()-start)