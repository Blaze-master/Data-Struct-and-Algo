import pygame as pg
import time

n,m = 2,2

grid = []
for y in range(n):
    row = []
    for x in range(m):
        node = {f"{x}:{y}" : [],
                "pos" : [x,y]}
        row.append(node)
    grid.append(row)

for y0,row in enumerate(grid):
    for x0,node in enumerate(row):
        pos1 = node["pos"]
        vec = []
        for y1,r2 in enumerate(grid):
            for x1,n2 in enumerate(r2):
                pos2 = n2["pos"]
                if pos1 == pos2: continue
                x = x1 - x0
                y = y1 - y0
                ratio = None if y==0 else abs(x/y)
                pol_x = 0 if x<0 else 1
                pol_y = 0 if y<0 else 1
                i = (pol_x, pol_y, ratio)
                if not (i in vec):
                    node[f"{x0}:{y0}"].append(f"{x1}:{y1}")
                    vec.append(i)
                else:
                    p = vec.index(i)
                    p_pos_s = list(node.values())[0][p]
                    dist1 = abs(x)+abs(y)
                    p_pos = [int(q) for q in p_pos_s.split(":")]
                    dist2 = abs(p_pos[0]-x0) + abs(p_pos[1]-y0)
                    if dist1 < dist2:
                        vec.append(vec.pop(p))
                        node[f"{x0}:{y0}"].remove(p_pos_s)
                        node[f"{x0}:{y0}"].append(f"{x1}:{y1}")

        grid[y0][x0] = node

edges = []
for y0,row in enumerate(grid):
    for x0,node1 in enumerate(row):
        for node2 in node1[f"{x0}:{y0}"]:
            edge = sorted([f"{x0}:{y0}", node2])
            if edge not in edges: edges.append(edge)


# for e in edges:
#     print(e)


# sum = 0
for row in grid:
    for node in row:
        pos = node["pos"]
        # print(node[f"{pos[0]}:{pos[1]}"])
        print(node)
        # sum += len(node[f"{pos[0]}:{pos[1]}"])
# print(sum)
# print(edges)
print(len(edges))

pg.init()
running = True
xmax, ymax = 1000, 700
screen = pg.display.set_mode((xmax, ymax))

test_node = f"{1}:{0}" + "a"
screen.fill((255, 255, 255))

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    
    # screen.fill((255, 255, 255))

    if len(edges)>0:
        edge = edges.pop(0)
        # print(edge)
    else:
        continue

    # for edge in edges:
    p1 = [int(c)+1 for c in edge[0].split(":")]
    p2 = [int(c)+1 for c in edge[1].split(":")]
    start = [xmax*p1[0]/(m+1), ymax*p1[1]/(n+1)]
    end = [xmax*p2[0]/(m+1), ymax*p2[1]/(n+1)]
    color = (255, 0, 0) if edge[0] == test_node else (0,0,0)
    pg.draw.line(screen, color, start, end)

    pg.display.update()

    # passed = False
    # while not passed:
    #     for event in pg.event.get():
    #         if event.type == pg.KEYDOWN:
    #             passed = True
    #         if event.type == pg.QUIT:
    #             running = False
    #             passed = True
    
    # time.sleep(20/len(edges))
