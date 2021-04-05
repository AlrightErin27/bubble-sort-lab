ex1 = [5, 8, 1, 10, 7]
ex2 = [2, 6, 8, 13, 18, 19]
ex3 = [0, -23, 10]

def bubble_sort(arr):
  # get length of array
  len_arr = len(arr)
  #Go through the list as many times as there are integers
  for i in range(len_arr):
    # The last pair of adjacent integers to be (n-2, n-1)
    for j in range(len_arr - 1):
      if arr[j] > arr[j+1]:
        # Swap
        arr[j], arr[j+1] = arr[j+1], arr[j]


bubble_sort(ex3)
print(ex3)
# nums = [5, 3, 8, 6]
# bubble_sort(nums)
# print(f"nums should be [3, 5, 6, 8] and is, in fact: {nums}")
