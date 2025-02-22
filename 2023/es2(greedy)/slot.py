OUTPUT_FILE = 'output.txt'
INPUT_FILE = 'input.txt'

def solve(N, Bf, Bi, machines):
    for i in range(N):
        machines[i] = (machines[i][0], machines[i][1] - machines[i][0])

    machines.sort(key=lambda x: x[1], reverse=True)
    p = 0
    while Bi < Bf:
        curr = 0
        while machines[curr][0] > Bi:
            curr += 1
        Bi += machines[curr][1]
        p += 1

    return p


with open(OUTPUT_FILE, 'W') as f:
    f.write("")

with open(INPUT_FILE, 'r') as file:
    T = int(file.readline().strip())
    for case in range(T):
        N, Bf, Bi = map(int, file.readline().split())
        machines = []
        for _ in range(N):
            Ci, Ri = map(int, file.readline().split())
            machines.append((Ci, Ri))

    with open('', 'a') as f:
        f.write("Case #{}: {}\n".format(case + 1, solve(N, Bf, Bi, machines)))