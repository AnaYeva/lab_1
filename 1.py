print("Enter three numbers: ")
arr = [float(i) for i in input().split()][:3]
print("Your numbers", arr)
maximum, minimum = arr[0], arr[0]
for i in range(1, 3):
    if arr[i] > maximum:
        maximum = arr[i]

    if arr[i] < minimum:
        minimum = arr[i]

print("Minimum", minimum)
print("Maximum", maximum)
