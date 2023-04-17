# Prime Calculator Challenge
from time import time


def performance(func):

  def wrap_func(*args, **kwargs):
    t1 = time()
    result = func(*args, **kwargs)
    t2 = time()
    print(f'It took {t2 - t1} s')
    return result

  return wrap_func


max_value = 400000


@performance
def calc_primes():

  primes = [2]

  test_list = [num for num in range(2, max_value) if num % 2 != 0]

  for test_value in test_list:
    for i in range(2, int(test_value / 2) + 1):
      if (test_value % i) == 0:
        break
    else:
      primes.append(test_value)

  return {'total': len(primes), 'primes': primes}


results = calc_primes()

# total should be 9,592 (from 100,000)

print(f"{results['total']} prime numbers found between 2 and {max_value}")
#print(results['primes'])