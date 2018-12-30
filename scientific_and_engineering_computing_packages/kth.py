def get_kth(data, k):
  quick_sort(data, 0, len(data)-1, k)
  return data[k-1]
 
def  quick_sort(A, start, end, k):
  if (start == end): return
  
  i, j = start, end
  
  while (i < j):
    if (A[i] > A[j]):
      A[i], A[j] = A[j], A[i]
      j -= 1
    else:
      i += 1
      
  if (i == end): return
  
  quick_sort(A, start if k<i else i+1, i if k<i else end, k)

print(get_kth([0,1,2,3,4,5], 3))
print(get_kth([1,0,8,9,5,7], 3))
