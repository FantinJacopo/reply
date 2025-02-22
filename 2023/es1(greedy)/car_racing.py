import math
def read_input_file(file_path):
    test_cases = []

    with open(file_path, 'r') as file:
        T = int(file.readline().strip())

        for case in range(T):
            R, C = map(int, file.readline().strip().split())
            cars = []
            for _ in range(C):
                Cid, Cs, Ct, Cc, Cd = map(int, file.readline().strip().split())
                cars.append((Cid, Cs, Ct, Cc, Cd))
            test_cases.append((R, cars))
            with open(output, 'a') as o:
                o.write("Case #" + str(case +1) + ": " + str(solve(R, cars)) + "\n")
    return test_cases


def solve(R, cars):
    best = (0, -1)

    for car in cars:
        distance = 0
        id, speed, turbo, cooldown, duration = car
        time = 0
        boostActive = True
        while distance < R:
            d = turbo * duration if boostActive else speed * cooldown

            if d > R - distance:
                d = R - distance
                if(boostActive):
                    time += math.ceil(d / turbo)
                else:
                    time += math.ceil(d / speed)
                break
            else:
                distance += d
                time += duration if boostActive else cooldown
            boostActive = not boostActive
        if best[1] == -1 or time < best[1]:
            best = (id, time)

    return best[0]

# Example usage
file_path = "input.txt"
output = "output.txt"
with open(output, 'w') as o:
    o.write("")
    read_input_file(file_path)