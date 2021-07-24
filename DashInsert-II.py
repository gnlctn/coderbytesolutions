def DashInsertII(num):
  numbers=str(num)
  numlist=[]
  for i in range(len(numbers)-1):
    if int(numbers[i]) ==0:
      numlist.append(numbers[i])
    elif int(numbers[i])%2==0 and int(numbers[i+1])%2==0:
      numlist.append(numbers[i])
      numlist.append('*')
    elif int(numbers[i])%2 !=0 and int(numbers[i+1])%2 != 0:
      numlist.append(numbers[i])
      numlist.append('-')
    else:
      numlist.append(numbers[i])
    
  numlist.append(numbers[-1])
  return ''.join(numlist)

# keep this function call here 
print(DashInsertII(input()))
