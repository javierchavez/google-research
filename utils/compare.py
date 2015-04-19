import itertools
import math
import json
import collections
from sortedcontainers import SortedList, SortedSet, SortedDict


class Hamming(object):

    def __init__(self, iterable=None, tnp=None, key=''):
        """Inits Hamming class
        Args:
            tnp: total permissions in already sorted order
            it is best to have this class generate it for you.
        """
        self._hs = None
        # _all holds all permissions in string
        self._all = tnp
        # all x will be motified by bin_transform 
        self._o_array = iterable
        # key assciociated to hamming
        self.key = key
        
        if key is not None and iterable is not None:
            self.bin_transform(iterable, key)

    @staticmethod
    def _sum_cols(m):
        """Sum of all the columns in a matrix"""
        return [sum(col) for col in zip(*m)]

    @staticmethod
    def _hamming_distance(s1, s2):
        # carinality of sets must be equal
        assert len(s1) == len(s2)
        return sum(ch1 != ch2 for ch1, ch2 in zip(s1, s2))

    @staticmethod
    def _nCr(n,r):
        f = math.factorial
        return f(n) / f(r) / f(n-r)
    
    def _overlay(self, values_array):
        """overlay is the same as a boolean meatrix data structure
        every value is checked and outputted in 1d list
        which a[i] represents presents of x 
        """
        return [1 if x in values_array else 0 for x in self._all ]

    
    def map_names(self, arr):
        """Maps HammingSet to its named key"""
        if self._all is None:
            raise Exception("bin_transform needs to run first")
        return SortedDict(zip(self._all, arr))

    
    def bin_transform(self, iterable, key='', out_file=None):
        """Take a collection of objects """
        self.key = self.key or key
        # Get total permissions
        _all = set()
        for obj in iterable:
            _all = set(obj[self.key]) | _all
    
        # Create a Set (defined order)
        self._all = SortedSet(_all)
        
        # NOTE: this is manipulating the arguments VALUE
        for obj in iterable:
            # bool transform
            obj[key] = self._overlay(obj[self.key])

        self._o_array = iterable
        # Not needed since the iterable is being changed!!!
        return iterable

    def sums(self):
        totals = []
        for obj in self._o_array:
            totals.append(obj[self.key])
        return self._sum_cols(totals)

    def hamming_dist(self, threshhold):
        """Get the hamming distance of objects
        
        Args:
            threshhold: is the number of objects to use
            when averaging the hamming distance.
        """
        _sm = self._o_array[:threshhold]
        dist = 0.0
        iteration = 0
        
            
        for i, app in enumerate(_sm):
            for ii, appii in enumerate(_sm[i:]):
                # since we are checking every object in different
                # orders we dont want to check the same two objs
                # twice we can check to see if they are the same
                # in addition to removing elements 
                if app['name'] != appii['name']:
                    dist += self._hamming_distance(app[self.key],
                                            appii[self.key])
                    iteration += 1                     

        return dist/iteration
            
            
            
    
