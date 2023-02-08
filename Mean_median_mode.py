# Enter your code here. Read input from STDIN. Print output to STDOUT
N = int(input())
arr = list(map(int, input().rstrip().split()))
ordered_arr = sorted(arr)
import numpy as np

def find_mean():
  mean = sum(arr)/N
  return mean

def find_median():
  if N % 2 == 0:
      first_index = int((N/2) - 1)
      second_index = int(((N/2) + 1) -1)
      numerator = (ordered_arr[first_index]) + (ordered_arr[second_index])
      median = numerator/2
  else:
      index = (N+1)/2
      median = ordered_arr[index-1]
  return median

def find_mode(ordered_arr):
    vals, counts = np.unique(ordered_arr, return_counts=True) #if mode has multiple occurrences, it will pick the least number because array is ordered
    index = np.argmax(counts)
    return vals[index]
  
mean = find_mean()
median = find_median()
mode = find_mode(ordered_arr)

print(mean)
print(median)
print(mode)
