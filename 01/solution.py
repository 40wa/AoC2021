
def p1():
    with open('./problem.txt', 'r') as f:
        lines = f.readlines()
        prev = int(lines[0])
        tot = 0
        for idx in range(1, len(lines)):
            curr = int(lines[idx])

            if curr > prev:
                tot += 1

            prev = curr

        print(tot)


def p2():
    with open('./problem.txt', 'r') as f:
        lines = f.readlines()
        #lines = ['199', '200', '208', '210', '200', '207', '240', '269', '260', '263']

        tot = 0

        for idx in range(3, len(lines)):
            print(lines[idx], lines[idx-3])
            if int(lines[idx]) > int(lines[idx-3]):
                tot += 1


        print(tot)


if __name__=='__main__':
    p2()
