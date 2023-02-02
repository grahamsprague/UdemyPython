

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
  # print(2) 2 is a prime but the only even prime
  mycount += 1
  
  for i in myiterable:
    is_prime = True

    if i != 1: # skipping 1 becuase we know its not a prime
      for x in range(3,int((i)/2)+1):
        
        if i % x == 0 and i != x: #skip 1 and the current 
          is_prime = False
          break

      if is_prime:
        # print(i)
        mycount += 1
      
  print(f'prime count for {max(potential_primes)+ 1}: {str(mycount)}')

print_primes(potential_primes)  

  


  
  