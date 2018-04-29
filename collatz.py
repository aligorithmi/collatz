def collatz_seq(n):
 global step
 step+=1
 if n==1 or n==2:
  return str(1)
 elif n%2:
  return str(3*n+1)+','+collatz_seq(3*n+1)
 else:
  return str(n//2)+','+collatz_seq(n/2)

n=raw_input('Enter number: ')
step=0
print collatz_seq(int(n))
print 'Number of step: ',step