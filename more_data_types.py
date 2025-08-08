#ARRAY
arr = []
arr.append(123)
arr.append(234)
arr.append(4.6)
arr.append("Hi")

print(arr)
print(arr[0])

#DICTIONARY: Key and Value
#The value of key and value can be anything int, float, str etc.
marks = {}
print(type(marks))

marks["Maths"] = 94
marks["Science"] = 92
marks["English"] = 88.5
marks["Hindi"] = "Fail"
marks[123] = 100
print(marks)

list_to_sum = {}
arr = [1,2,3]
list_to_sum[arr] = 6
print(list_to_sum)