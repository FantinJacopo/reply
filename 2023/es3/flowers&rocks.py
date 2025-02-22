INPUT_FILE = 'input.txt'
OUTPUT_FILE = 'output.txt'
'''
with open(OUTPUT_FILE, 'W') as f:
    f.write("")

def solve(W, H, F, G, terrain):
    for i in range(H):
        for j in range(W):
            if terrain[i][j] == 0:
                place_flower((i, j), terrain, W + H)
    return

def place_flower(pos, terrain, min_distance, flowers = []):
    for d in range(min_distance, 1, -1):
        for i, j in [(pos[0] + d, pos[1]), (pos[0] - d, pos[1]), (pos[0], pos[1] + d), (pos[0], pos[1] - d)]:
            if 0 <= i < len(terrain) and 0 <= j < len(terrain[0]) and terrain[i][j] == 0:
                place_flower((i, j), terrain, d, flowers)
    return

with open(INPUT_FILE, 'r') as file:
    T = int(file.readline().strip())

    for case in range(T):
        W, H, F, G = map(int, file.readline().split())

        terrain = [[0 for _ in range(W)] for _ in range(H)]
        for _ in range(G):
            X, Y = map(int, file.readline().split())
            terrain[X][Y] = 1

        with open('', 'a') as f:
            f.write("Case #{}: {}\n".format(case + 1, solve(W, H, F, G, terrain)))
    
'''





# CODICE DEI PRIMI


W, H, F, G = 0, 0, 0, 0
coords = []
case_id = 0
connect = []

def bruteforce(used, pos, cnt):
    if cnt >= F:
        return True
    elif G - pos < F - cnt:
        return False
    elif (used >> pos) & 1:
        return bruteforce(used, pos + 1, cnt)
    else:
        return bruteforce(used | connect[pos], pos + 1, cnt + 1) or bruteforce(used, pos + 1, cnt)

def check(d):
    for i in range(G):
        connect[i] = 0

    for i in range(G):
        for j in range(G):
            if abs(coords[i][0] - coords[j][0]) + abs(coords[i][1] - coords[j][1]) <= d:
                connect[i] |= (1 << j)    # se dovesse dare errore è perchè in c++ va scritto 1LL per long long
    res = bruteforce(0, 0, 0)
    return res

def solve_primi():
    with open(INPUT_FILE, 'r') as file:
        W, H, F, G = map(int, file.readline().split())

        for i in range(G):
            coords[i] = map(int, file.readline().split())

        L = 0
        R = (W + H) / 2
        while L < R:
            mid = (L + R) / 2
            if check(mid + 1):
                L = mid + 1
            else:
                R = mid

        with open(OUTPUT_FILE, 'a') as f:
            f.write("Case #{}: {}\n".format(case_id + 1, L))


def main_primi():
    with open(INPUT_FILE, 'r') as file:
        T = int(file.readline().strip())

        for case_id in range(T):
            solve_primi()