from sys import maxsize
import statistics

def get_cost(x,y):
    steps = abs(x-y)
    cost = 1
    step_holder = []
    for i in range(1,steps+1):
        step_holder.append(i)
    return sum(step_holder)

def calc(file):
    f = [int(x) for x in open(file).read().split(',')]
    ceiling = max(f)
    floor = min(f)
    best = maxsize
    meet_up = 0
    for i in range(floor,ceiling+1):
        #print("Trying {}".format(i))
        cost = 0
        for j in f:
            cost += get_cost(j,i)
        #print("Cost of using {} is {}".format(i, cost))
        if cost < best:
            best = cost
            meet_up = i
    return best

if __name__=='__main__':
    print(calc('input.txt'))