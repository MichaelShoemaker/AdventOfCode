def count_increases(file):
    f = open(file)
    data = f.readlines()
    num_data = []
    for n in data:
        num_data.append(int(n))
    mark1 = 0
    mark2 = 1
    count = 0

    while mark2 <= len(num_data)-2:
        if sum(num_data[mark2:mark2+3]) > sum(num_data[mark1:mark1+3]):
            count += 1
        mark1 +=1
        mark2 +=1
        
    return count

if __name__=='__main__':
    print(count_increases('input.txt'))