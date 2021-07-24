def SimpleMode(arr):
  output=0
  counts=1
  newarr=set(arr)
  for i in arr:
    count=arr.count(i)
    if count>counts:
      counts=count
      output=i
  if counts ==1:
    return -1
  else:
    return output

# keep this function call here 
print(SimpleMode(input()))
