import statistics

def get_cost(x,y):
    steps = abs(x-y)
    cost = 0
    for i in range(1,steps+1):
        cost += i
    return cost

def calc(file):
    f = [int(x) for x in open(file).read().split(',')]

    # meetup = (int(statistics.mean(l)))
    # cost = 0
    # for i in l:
    #     cost += abs(i-meetup)
    return f

if __name__=='__main__':
    print(get_cost(-1,3))