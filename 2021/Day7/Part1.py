import statistics

def calc(file):
    f = open(file).read().splitlines()
    l = [int(x) for x in f[0].split(',')]
    meetup = (int(statistics.median(l)))
    cost = 0
    for i in l:
        cost += abs(i-meetup)
    return cost

if __name__=='__main__':
    print(calc('input.txt'))