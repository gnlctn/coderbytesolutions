def FizzBuzz(num):
  listt=[]
  for i in range (1,num+1):
    if i%3 == 0 and i%5 !=0 :
      listt.append('Fizz')
    elif i%5 ==0 and i%3 != 0 :
      listt.append('Buzz')
    elif i%5 ==0 and i%3 == 0 :
      listt.append('FizzBuzz') 
    else:
      listt.append(str(i))
  a= " ".join(listt)


  # code goes here
  return a

# keep this function call here 
print(FizzBuzz(input()))
