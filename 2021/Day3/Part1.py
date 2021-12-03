import numpy as np

def make_data(file):
    f = open(file)
    data = f.read().splitlines()
    return np.array([list(i) for i in data]).astype(np.int)

def list_to_bin(strlist):
    return ''.join([str(i) for i in strlist])

def calc_mask(data, flag):
        if flag == 'gamma':
            return [1 if i > len(data)/2 else 0 for i in data.sum(axis=0)]
        elif flag == 'epsilon':
            return [1 if i < len(data)/2 else 0 for i in data.sum(axis=0)]

def calc_power(data):
    return int(list_to_bin(calc_mask(data,'gamma')), base=2) * int(list_to_bin(calc_mask(data,'epsilon')), base=2)


if __name__=='__main__':
    print(calc_power(make_data('input.txt')))