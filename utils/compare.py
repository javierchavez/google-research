import itertools
import math
import json
import collections
import logging
from sortedcontainers import SortedList, SortedSet, SortedDict

__author__ = 'Javier Chavez'
__email__ = 'javierc@cs.unm.edu'

class Hamming(object):

    def __init__(self, iterable=None, tnp=None, key=''):
        """Inits Hamming class
        Args:
            tnp: total permissions in already sorted order
            it is best to have this class generate it for you.
        """
        # _all holds all permissions in string
        self._all = tnp or set()

        # key assciociated to hamming
        self._set_key(key)
        
        if key is not None and iterable is not None:
            self.bin_transform(iterable)

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
        """Number of iterations that will take place for
        a given number of combinations and cardinality
        
        Args:
            n: cardinality of set
            r: number of combinations

        return:
           number of iterations
        """
        f = math.factorial
        return f(n) / f(r) / f(n-r)

    def _set_key(self, key):
        if key is None and self.key is None:
            # iterable will be treated as iterable[i]
            # e.g. ["elem", "elem", "elem"]
            raise Exception("Not yet implemented.")
            # logging.info('Assuming matrix')
        elif key is not None:
            # iterable will be treated as iterable[i]['key']
            # e.g. [{'key':[]}, {'key':[]}, {'key':[]}]
            self.key = key
        elif key is None and self.key is not None:
            # if the key is already set and we are passing
            # none then ignore it.
            pass
        else:
            logging.warning("key is in unknown state")
            
    
    def _overlay(self, values_array):
        """overlay is the same as a boolean meatrix data structure
        every value is checked and outputted in 1d list
        which a[i] represents presents of x 
        """
        return [1 if x in values_array else 0 for x in self._all ]

    def get_permission_list(self):
        return [p for p in self._all]
    
    def map_names(self, arr):
        """Maps HammingSet to its named key"""
        if self._all is None:
            raise Exception("bin_transform needs to run first")
        return SortedDict(zip(self._all, arr))


    def accumulate(self, iterable, key=None):
        """Accumulate permissions and, transform 
           
        Args:
            key: needs to be a key of iterable[i] which
            also needs to be iterable to be able to generate
            a set of unique elements for all iterable[i][key].
            For example: 
                iterable[0]['key'] = ["val", "other"] 
        """        
        self._set_key(key)
        
        for obj in iterable:
            self._all = self._all | set(obj[self.key])

        # Set (defined order)
        self._all = SortedSet(self._all)
        
    
    def bin_transform(self, iterable, key=None, out_file=None):
        """Take a collection of objects. Changes iterable in place.
        
        Args:
            key: needs to be a key of iterable[i] which
            also needs to be iterable to be able to generate
            a set of unique elements for all iterable[i][key].
            For example: 
                iterable[0]['key'] = ["val", "other"] 
        """
        self._set_key(key)
        if not self._all :
            # Get total permissions
            _all = set()
            for obj in iterable:
                _all = set(obj[self.key]) | _all
                
            # Create a Set (defined order)
            self._all = SortedSet(_all)

        return self._bin_t(iterable)

    
    def _bin_t(self, iterable):
        # NOTE: this is manipulating the arguments VALUE.
        # not needed but realize a deep copy may be needed
        # inorder to preserve iterable
        for obj in iterable:
            # bool transform
            obj[self.key] = self._overlay(obj[self.key])

        # Not needed since the iterable is being changed!!!
        return iterable

        
    def sums(self, iterable, key=None):
        """Sum of all m's (m by n matrix). vertical sum 
        
        Returns:
            A 1 by n matrix such that each column is the sum 
            of all previous rows in that column. For example
            sum([[1, 2], [2, 3]])
            = [3, 5]
        """
        self._set_key(key)
        
        totals = []
        for obj in iterable:
            totals.append(obj[self.key])
        return self._sum_cols(totals)

    def hamming_dist(self, iterable, threshhold, key=None):
        """Get the hamming distance of objects
        
        Args:
            threshhold: is the number of objects to use
            when averaging the hamming distance.
        """
        self._set_key(key)
        
        if threshhold > len(iterable):
            raise IndexError("Threshhold is too large")

        # take threshhold from array 
        _sm = iterable[:threshhold]

        # get arrays        
        _xx = [x[self.key] for x in _sm]

        # generate combinations
        _c = itertools.combinations(_xx, 2)
        # get number of combinations
        # iterations = self._nCr(threshhold, 2)
        
        dist = 0.0
        # more efficient to just add 1
        list_len = 0
        
        for a in _c:
            dist += self._hamming_distance(a[0], a[1])
            list_len += 1
        return dist/list_len
  

            
            
            
    
