
start=int(input("Enter starting limit"))
end=int(input("Enter ending limit"))
for num in range(start,end+1)
  sum=0
  copy=num
  while copy!=0
    digit=copy%10;
    sum+=digit**3
    copy//=10
   if num==copy:
      print(num)
