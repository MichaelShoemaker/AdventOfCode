def count_increases(file):
    f = open(file)
    data = f.readlines()
    count = 0
    previous_line = -9999999

    for line in data:
        current_line = line
        if int(current_line) > int(previous_line):
            count +=1
        previous_line = current_line
    return count

if __name__=='__main__':
    print(count_increases('input.txt'))