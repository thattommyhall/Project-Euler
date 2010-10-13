from __future__ import division
import sys,os,math
#from path import path
from time import time
import psyco
from decorator import decorator

@decorator
def timed(func, *args, **kw):
    """times a function with and without using psyco"""
    start = time()
    func(*args,**kw)
    end = time()
    withoutpsyco = end-start
    print "Took",withoutpsyco,"without psyco"

    start = time()
    accfunc = psyco.proxy(func)
    accfunc(*args,**kw)
    end = time()
    withpsyco = end-start
    print "Took",withpsyco,"with psyco"
    print "A",withoutpsyco/withpsyco,"x speedup"

class memoized(object):
   """Decorator that caches a function's return value each time it is called.
   If called later with the same arguments, the cached value is returned, and
   not re-evaluated.
   """
   def __init__(self, func):
      self.func = func
      self.cache = {}
   def __call__(self, *args):
      try:
         return self.cache[args]
      except KeyError:
         self.cache[args] = value = self.func(*args)
         return value
      except TypeError:
         # uncachable -- for instance, passing a list as an argument.
         # Better to not cache than to blow up entirely.
         return self.func(*args)
   def __repr__(self):
      """Return the function's docstring."""
      return self.func.__doc__

def perms(somelist):
    if len(somelist) == 1:
        yield somelist
    else:
        for i in range(len(somelist)):
            this = somelist[i]
            rest = somelist[:i] + somelist[i+1:]
            for p in perms(rest):
                yield this + p


