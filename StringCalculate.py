def StringCalculate(strParam):
  strParam.split()
  a=[]
  
  for i in strParam:
    if i.isalnum():
      a.append(i)
    elif i == '(' or i==')':
      a.append(i)
    elif i=='+' or i=='-' or i=='*' or i=='/' :
      a.append(i)
  b=''.join(a)

  return eval(b)
      

  

  # code goes here
  

# keep this function call here 
print(StringCalculate(input()))
