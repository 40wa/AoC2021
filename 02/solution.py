

def p1():
    with open('problem.txt', 'r') as f:
        pos = [0, 0]

        for l in f.readlines():
            ipt = l.strip().split()
            opcode = len(ipt[0])
            val = int(ipt[1])
            if opcode == 2:
                #up
                pos[1] -= val
            elif opcode == 4:
                #down
                pos[1] += val
            elif opcode == 7:
                pos[0] += val

        print(pos)
        print(pos[0] * pos[1])


def p2():
    with open('problem.txt', 'r') as f:
        pos = [0,0]
        aim = 0

        for l in f.readlines():
            ipt = l.strip().split()
            opcode = len(ipt[0])
            val = int(ipt[1])
            if opcode == 2:
                #up
                aim -= val
            elif opcode == 4:
                #down
                aim += val
            elif opcode == 7:
                pos[0] += val
                pos[1] += aim * val

        print(pos)
        print(pos[0] * pos[1])

if __name__=='__main__':
    p2()
