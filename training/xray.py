def solve(N, R):
    S, D = 0
    mosse = 0
    while True:
        m = 1001
        while(D < N and m > 0):
            if R[D] == 0:
                if D == S:
                    S+=1
                else:
                    break
            elif R[D] < m:
                m = R[D]
            D += 1
        if S == D:
            break
        mosse += 1
        while S < D:
              R[S] -= m
    return mosse

def solveEasy(N, R):
    solution = R[0]
    for k in range(1, N):
        if R[k] > R[k-1]:
            solution += R[k] - R[k-1]


def read_input_file(file_path):
    with open(file_path, 'r') as file:
        T = int(file.readline().strip())

        for case in range(T):
            N = int(file.readline().strip())
            R = []
            for _ in range(N):
                R = list(map(int, file.readline().strip().split()))
            with open(output, 'a') as o:
                o.write("Case #" + str(case + 1) + ": " + str(solve(N, R)) + "\n")
                

file_path = "input.txt"
output = "output.txt"
with open(output, 'w') as o:
    o.write("")
    read_input_file(file_path)