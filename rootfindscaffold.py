
import math

def root_find(n, d, start = None, stop = None):

    '''
    Takes an integer and finds the specified root of it using the binary search algorithm, generalized binomial expansion formula, and Newton's Method formula
    Args:
        n: integer for which we want to find a root (int)
        d: root value (int)
        start: value at which we want to start searching (int or float)---default value is one
        stop: index before which we want to stop searching (int or float)---default value is n
    Returns:
        the desired root of n (float)
    '''

    #default values
    if start == None: start = 1
    if stop == None: stop = n

    print('*******')
    print(f'start: {start}')
    print(f'stop: {stop}')

    #midpoint calc
    mid = math.floor((start + stop) / 2)
    print(f'mid: {mid}')
    print('*******')

    #calculation of mid to specified degree
    current_value = (mid ** d)
    next_value = ((mid + 1) ** d)

    #base case---if midpoint to specified degree is within plus or minus one of n, approximate the root, then use Newton's Method formula to increase accuracy and return it
    if ((n >= (current_value)) and (n <= (next_value))):
        print(f'found range! root is between {mid} and {(mid + 1)}')

        #finding closest integer
        nearest_int = mid if ((n < (mid + 0.5) ** d)) else (mid + 1)
        print(f'nearest int: {nearest_int}')

        #using generalized binomial expansion formula to approximate the root...
        diff = n - (nearest_int ** d)
        decimal = (diff/(d * (nearest_int ** (d - 1))))
        approx = (nearest_int + decimal)
        print(f'first approx: {approx}')

        #using Newton's Method Formula to increase accuracy...
        approx_two = (1/d)*(((d-1) * approx) + (n/(approx ** (d - 1))))
        print(f'second approx: {approx_two}')
        return (1/d)*(((d-1) * approx_two) + (n/(approx_two ** (d - 1))))

    #binary search
    if current_value > n:
        return root_find(n, d, start, mid)
    else:
        return root_find(n, d, mid, stop)


print(f'root is: {root_find(64, 5)}')