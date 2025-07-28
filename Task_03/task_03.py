

def get_numbers():
    input = [12,18,7,10,16,14,11,8,12,15]
    return input

def find_min(numbers):
    return min(numbers)

def find_max(numbers):
    return max(numbers)

def find_mean(numbers):
    return sum(numbers)/len(numbers)

def find_mode(numbers):
    dct = {}
    for v in numbers:
        if v not in dct:
            dct[v]=1
        else:
            dct[v]+=1
    dct = dict(sorted(dct.items(), key=lambda k:k[1]))


    mode=[]
    key, val = next(iter(reversed(dct.items())))
    mode.append(key)
    for key,val in reversed(dct.items()):
        if key==mode[0]:
            mode.append(key)
        else:
            break
    mode.pop(0)
    return mode

def find_median(numbers, iqr=None):
    new_num = sorted(numbers)
    idx = len(new_num)//2

    median = new_num[idx]

    if iqr==None:
        return median
    else:
        return median,idx
    

def find_range(numbers):
    return find_max(numbers)-find_min(numbers)

def find_variance(numbers):
    mean = find_mean(numbers)
    sum_ = [(x-mean)**2 for x in numbers]
    return sum(sum_)/(len(numbers)-1)

def find_STD(numbers):
    import numpy as np
    return np.sqrt(find_variance(numbers))

def find_Quartiles(numbers):
    new_nums = sorted(numbers)
    q2,q2_idx = find_median(new_nums, True)
    q1_idx, q3_idx = q2_idx//2, (q2_idx+len(new_nums))//2
    
    q1 = new_nums[q1_idx]
    q3 = new_nums[q3_idx]


    return q1, q2, q3

def find_IQR(numbers):
    q1,_,q3 = find_Quartiles(numbers)
    return q3-q1

if __name__=='__main__':
    input = get_numbers()
    print(f'Numbers is {get_numbers}')
    print(f'Min: {find_min(input)}')
    print(f'Max: {find_max(input)}')
    print(f'Mean: {find_mean(input)}')
    print(f'Mode: {find_mode(input)}')
    print(f'Median: {find_median(input)}')
    print(f'Range: {find_range(input)}')
    print(f'Variance: {find_variance(input)}')
    print(f'Standard Deviation: {find_STD(input)}')
    print(f'Quartiles: {find_Quartiles(input)}')
    print(f'Interquartile Range(IQR): {find_IQR(input)}')