import time
import random

dx = [1, -1]
dy = [1, -1]

def dfs(x, y, visited):
    visited[x][y] = True
    count += 1
    
    dx = x + 1
    if dx < H and not visited[dx][y] and H_wall[x][y] == "0":
        dfs(dx, y, visited)
    dx = x - 1
    if dx >= 0 and not visited[dx][y] and H_wall[x - 1][y] == "0":
        dfs(dx, y, visited)
    dy = y + 1
    if dy < W and not visited[x][dy] and V_wall[x][y] == "0":
        dfs(x, dy, visited)
    dy = y - 1
    if dy >= 0 and not visited[x][dy] and V_wall[x][y - 1] == "0":
        dfs(x, dy, visited)

def main(local):
    T, H, W , i0 = map(int, input().split())
    H_wall = ["1"*W] + [input().replace("\r", "") for _ in range(H-1)] + ["1"*W]
    V_wall = ["1" + input().replace("\r", "") + "1" for _ in range(H)]
    V_wall[i0] = "0"+V_wall[i0][1:]
    K = int(input())
    SD = [[k] + [int(i) for i in input().split()] for k in range(K)]
    SD.sort(key=lambda x: (x[1], x[2]))
    
    corner_set = set()
    for i in range(H):
        for j in range(W):
            if int(H_wall[i][j]) + int(V_wall[i][j]) + int(H_wall[i+1][j]) + int(V_wall[i][j+1]) == 3:
                corner_set.add((i, j))

    # start = time.time()
    # while time.time() - start < 1.5:
    #     i =  random.randint(0, H-1)
    #     j =  random.randint(0, W-1)
    #     for di, dj in [(0, 0), (0, 1), (1, 0), (1, 1)]:
            

    ans = []
    D_dict = {t:set() for t in range(1, T+1)}
    SD_i = 0
    for t in range(1, T+1):
        while SD_i < len(SD) and SD[SD_i][1] == t:
            if len(corner_set) > 0:
                corner = corner_set.pop()
                D_dict[SD[SD_i][2]].add(corner)
                ans.append([SD[SD_i][0]+1, corner[0], corner[1], t])
            SD_i += 1

        corner_set |= D_dict[t]
        D_dict[t] = []
    
    if local:
        with open("seed2_output.txt", mode="w") as f:
            print(len(ans), file=f)
            for a in ans:
                print(*a, file=f)
        print(len(ans))

    else:
        print(len(ans))
        for a in ans:
            print(*a)

if __name__ == '__main__':
    main(True)