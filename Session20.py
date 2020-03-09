"""
numbers: 91, 76, 22, 11, 21, 34, 66
index  : 0 .. 					 n-1
heap   :
					91
			76				22

		11		21		34		66

		aindex 	:  	0 -> 91
		left	: 	1 -> 76
		right	:	2 -> 22

		index   : 	1 -> 76
		left	: 	3 -> 11
		right	:	4 -> 21

		element : i
		left    : 2*i + 1
		right   : 2*i + 2

MaxHeap -> Root is greater than children
MinHeap -> Root is smaller than children

					91
			76				66

		11		21		34		22

numbers: 91, 76, 66, 11, 21, 34, 22

heapSort
numbers: 22, 76, 66, 11, 21, 34, 91
numbers: 22, 76, 66, 11, 21, 34
			22
		76		 66
	11     21  34

			76
		22		  66
	11		21  34

numbers: 22, 76, 66, 11, 21, 34, 91
numbers: 34, 22, 66, 11, 21, 76, 91


"""
# Max Heap or Min Heap
def heapify(numbers, n, i):

    maxNumIdx = i
    leftIdx = 2*i + 1
    rightIdx = 2*i + 2

    print("[HEAPIFY] numbers:{} | n:{} | i:{} | maxNumIdx: {} | leftIdx:{} | rightIdx:{}"
          .format(numbers, n, i, maxNumIdx, leftIdx, rightIdx))

    if leftIdx < n and numbers[i] < numbers[leftIdx]:
        print("[maxNumIdx:{} >> Left Index:{}]".format(maxNumIdx, leftIdx))
        maxNumIdx = leftIdx

    if rightIdx < n and numbers[maxNumIdx] < numbers[rightIdx]:
        print("[maxNumIdx:{} >> Right Index:{}]".format(maxNumIdx, rightIdx))
        maxNumIdx = rightIdx

    # Swap The Elements to Build the Max Heap
    if maxNumIdx != i:
        print("[maxNumIdx:{} != i:{}]".format(maxNumIdx, i))
        numbers[i], numbers[maxNumIdx] = numbers[maxNumIdx], numbers[i]
        # Recursion
        print("[Recursion]: heapify numbers:{} | n:{} | maxNumIdx:{}"
              .format(numbers, n, maxNumIdx))
        heapify(numbers, n, maxNumIdx)

def heapSort(numbers):

    print("[HEAP SORT]:", numbers)

    n = len(numbers)

    # Building Max Heap for numbers:
    for i in range(n, 0, -1):
        heapify(numbers, n, i)


numbers = [91, 76, 22, 11, 21, 34, 66]

print("Original Numbers:", numbers)
heapSort(numbers)
print("Sorted Numbers:", numbers)
