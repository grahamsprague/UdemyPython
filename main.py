
from time import time

def performance(fn):
  def wrapper(*args, **kwards):
      t1 = time()
      result = fn(*args, **kwards)
      t2 = time()
      print(f'took {t2 - t1} seconds.')
      return result
  return wrapper

potential_primes = range(1,10000,2)

@performance
def print_primes(myiterable):
  
  mycount = 0
  # print(2)
  mycount += 1
  
  for i in myiterable:
    is_prime = True

    if i != 1:
      for x in range(1,round((i)/2)):
        
        if i % x == 0 and i != x and x != 1:
          is_prime = False

      if is_prime:
        # print(i)
        mycount += 1
      
  print(f'prime count for {max(potential_primes)+ 1}: {str(mycount)}')

print_primes(potential_primes)  

  


  