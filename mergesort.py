import random

def merge(a, b):
  result = []
  while a and b:
    if a[-1] >= b[-1]:
      result.append(a.pop())
    else:
      result.append(b.pop())
  result.reverse()
  result = (a or b) + result
  print result
  return result

# 4 8 6 2 9 
def mergesort(a):
  if len(a) <= 1:
    return a
  mid = len(a)//2
  lhs, rhs = a[:mid], a[mid:]
  lo = mergesort(lhs)
  hi = mergesort(rhs)
  return merge(lo, hi)

lo, hi = range(10), range(10, 20)
print merge(lo, hi)
# Sanity check
l = random.sample(range(100), 20)
# l= [4, 8, 6, 2, 9, 7]
# print l
# print mergesort(l)

