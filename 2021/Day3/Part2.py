import math
from time import sleep
import numpy as np

def make_data(file):
    f = open(file)
    data = f.read().splitlines()
    return np.array([list(i) for i in data])

def make_flag(data, run):
    #Check the midway point. Round up to capture the tie breaker contidion.
    div = math.ceil(len(data)/2)
    mask = data.astype('int').sum(axis=0)
    #print(mask)
    if mask[run] >= div:
        return 1
    else:
        return 0


def get_reading(data,switch):
    for col in range(len(data[0])+1):
        #print("Data length is {}".format(len(data)))
        if len(data)==1:
            return(int(''.join(data[0]),base=2))
            return data
        flag = make_flag(data,col)
        removals = []       
        #print("Data is:")
        #print(data)
        #sleep(1)
        #print("Flag is {}".format(flag))
        for num, row in enumerate(data):
            if switch == 'o':         
                if row[col] != str(flag):
                    #print("Removing row {}".format(row))
                    removals.append(num)
            if switch == 'c':
                if row[col] == str(flag):
                    #print("Removing row {}".format(row))
                    removals.append(num)
        data = np.delete(data, (removals), axis=0)

def calc(file):
    data = make_data(file)
    return get_reading(data,'o') * get_reading(data,'o') 

if __name__=='__main__':
    print(calc('input.txt'))