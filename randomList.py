import sys
from random import randint

def ascending(minimum, maximum, file_name):
    print("generating ascending list")
    f = open(file_name, "a")
    for i in range(minimum, maximum + 1):
        f.write(str(i) + '\n')

def decending(minimum, maximum, file_name):
    print("generating decending list")
    f = open(file_name, "a")
    for i in reversed(range(minimum, maximum + 1)):
        f.write(str(i) + '\n')

    f.close()

def rand_order(minimum, maximum, file_name, randomize):
    print("generating random list")
    nums = [0] * (maximum)
    for i in range(0, maximum):
        nums[i] = i + 1

    print(nums)
    for i in range(randomize):
        x = randint(0, maximum - 1)
        y = randint(0, maximum - 1)
        tmp = nums[x]
        nums[x] = nums[y]
        nums[y] = tmp
    
    f = open(file_name, "a")
    for i in nums:
        f.write(str(i) + '\n')

    f.close()

def printFile(file_name):
    f = open(file_name, "r")
    print(f.read())
    f.close()

def main():
    user_in = input("file name to write to: ");
    in_min = int(input("min value: "));
    in_max = int(input("max value: "));
    in_rand = input("randomize values(y/n): ");
    if(in_rand == 'y'):
        randomize = int(input("number of scrambles: "))
        rand_order(in_min, in_max, user_in, randomize)    
    else:
        ascend = input("ascending or decending order(a/d)")
        if(ascend == 'a'):
            ascending(in_min, in_max, user_in)
        else:
            decending(in_min, in_max, user_in)
        
    printFile(user_in)
    return 0

if __name__ == '__main__':
    sys.exit(main())

