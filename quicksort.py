import random

def partition(a):
  pi, seq = a[0], a[1:]
  lo = [x for x in seq if x <= pi]
  hi = [x for x in seq if x > pi]
  return lo, pi, hi

def quicksort(a):
  if len(a) <= 1:
    return a
  lo, pi, hi = partition(a)
  return quicksort(lo) + [pi] + quicksort(hi)

# Sanity check
l = random.sample(range(100), 20)
print l
print quicksort(l)
