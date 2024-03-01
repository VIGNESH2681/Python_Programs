arr = [23,45,21,36,78,29]
max = arr[0]
min = arr[0]
n=len(arr)

#Find maximum element in an array
for i in range(1,n):
    if arr[i] > max:
        max = arr[i]

print("Maximum element is:",max)

#Find Minimum element in an array
for i in range(1,n):
    if arr[i] < min:
        min = arr[i]

print("Minimum element is:", min)
