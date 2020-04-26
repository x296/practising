from random import randrange

def mergeSort(array):
	if len(array) > 1:
		mid = len(array) // 2
		leftArray = array[:mid]
		rightArray = array[mid:]

		mergeSort(leftArray)
		mergeSort(rightArray)

		array.clear()

		while len(leftArray) > 0 and len(rightArray) > 0:
			if leftArray[0] <= rightArray[0]:
				array.append(leftArray[0])
				leftArray.pop(0)
			else:
				array.append(rightArray[0])
				rightArray.pop(0)

		for i in leftArray:
			array.append(i)

		for i in rightArray:
			array.append(i)

def binarySearch(array, left, right, searchingValue):
	if right >= left:
		mid = left + right - 1 // 2

		if searchingValue == array[mid]:
			return mid

		elif searchingValue > array[mid]:
			return binarySearch(array, mid + 1, right, searchingValue)

		else:
			return binarySearch(array, left, mid - 1, searchingValue)

	else:
		return "The value does not occur in this array."


defaultList = []

print("Welcome to the Binary Search Algorithm!")

for _ in range(10):
	defaultList.append(randrange(100))

print("This is default array:", *defaultList)

mergeSort(defaultList)
print("This is sorted default array:", *defaultList)

userValue = int(input("Type a value you want to find: "))

result = binarySearch(defaultList, 0, len(defaultList) - 1, userValue)

if str(type(result))[8:11] == "int":
	print("\nThe value you are looking for ({}) was found in array at {} index.".format(userValue, result))

else:
	print("\n" + result)
