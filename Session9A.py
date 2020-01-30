"""
    Search:
        1. Binary Search
        https://www.cs.usfca.edu/~galles/visualization/Search.html
"""

def binarySearch(numbers, element):

    low = 0
    high = len(numbers) - 1

    print(">> Initial LOW", low)
    print(">> Initial HIGH", high)

    while low <= high:

        mid = low + (high-low)//2
        print(">> MID", mid)

        if numbers[mid] == element:
            return True

        # Since our Data will be sorted, we can decide where to go !!
        # Left in case element to be searched is lesser than mid or right other way around !!

        if numbers[mid] < element:
            low = mid + 1
        else:
            high = mid - 1


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
element = 7


print(">> is {} in {} : {}".format(element, numbers, binarySearch(numbers, element)))

"""
    
    Time Complexity Analysis:
    
    1st Iteration
        Length of List : n
    2nd Iteration
        Length of List is Halved : n/2
    3rd Iteration
        Length of List is Further Halved : n/2(pow)(2) -> n/4
    .
    ..
    ...
    
    for kth Iteration
        Length of List is n/2(pow)(k)
        
    BUT, after k divisions length of List shall become 1 :)    
             
    i.e.
    n/2(pow)(k) = 1    
    Hence, 
    n = 2(pow)(k)
    
    Use Log Function with base 2:
    
    log(base2)(n) = log(base2) (2(pow)(k))
    
    log(base2)(n) = k log(base2)(2)
    
    => log(base x)(x) = 1
    
    => log(base2)(n) = k
    
    i.e. at kth iteration we get -> log(base2)(n) 
    

"""

