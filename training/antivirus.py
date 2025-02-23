def solve(l1, l2, l3, l4, files, M):
    v = 0
    i1 = i2 = i3 = i4 = 0
    controlla_prossimo_carattere = False
    while True:
        while i1 < l1:
            while i2 < l2:
                while i3 < l3:
                    while i4 < l4:
                        if(files[i1] == files[i2] == files[i3] == files[i4]):
                            v += 1
                            i1 += 1
                            i2 += 1
                            i3 += 1
                            if v == M:
                                controlla_prossimo_carattere = True
                        else:
                            if controlla_prossimo_carattere:
                                return f"{i1-M} {i2-M} {i3-M} {i4-M}"
                            v = 0
                        i4 += 1
                    i3 += 1
                i2 += 1
            i1 += 1

def read_input_file(file_path):
    with open(file_path, 'r') as file:
        T = int(file.readline().strip())

        for case in range(T):
            l1, l2, l3, l4 = map(int, file.readline().strip().split())
            M = int(file.readline().strip())
            files = []
            for i in range(4):
                files[i] = map(int, file.readline().strip().split())
            with open(output, 'a') as o:
                o.write("Case #" + str(case + 1) + ": " + str(solve(l1, l2, l3, l4, files, M)) + "\n")

file_path = "input.txt"
output = "output.txt"
with open(output, 'w') as o:
    o.write("")
    read_input_file(file_path)