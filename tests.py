import json
import unittest
import collections
from utils import compare


__author__ = 'Javier Chavez'
__email__ = 'javierc@cs.unm.edu'



class CompareTestCase(unittest.TestCase):
    """Tests for `compare.py`."""

    def setUp(self):
        self.hamming = compare.Hamming(key="permissions")
        fp = open('datasets/2k13_all_by_term.json', 'r')
        self.searches = json.load(fp)
        fp.close()


    def test_accum(self):

        for term in self.searches:
            self.hamming.accumulate(self.searches[term])
 
    
    def test_uniques(self):
        for term in self.searches:
            self.hamming.accumulate(self.searches[term])
        
        ll = self.hamming.get_list()
        self.assertEqual(95, len(ll))
        
    # test array are all same len
    def test_transform_values(self):
        arr = []
        for term in self.searches:
            arr.append([x['permissions'] for x in self.hamming.bin_transform(self.searches[term])])
 
        for t in arr:
            for a in t:
                for i in a:
                    self.assertLessEqual(i, 1, msg=None)

    def test_transform_lens(self):
        arr = []
        

        for term in self.searches:
            self.hamming.accumulate(self.searches[term])
 
        for term in self.searches:
            arr.append([x['permissions'] for x in self.hamming.bin_transform(self.searches[term])])

        for t in arr:
            for a in t:
                self.assertEqual(95, len(a))
                

    # x list is in sorted order
    def test_list_sorted(self):
        from sortedcontainers import SortedDict, SortedList
        
        for term in self.searches:
            self.hamming.accumulate(self.searches[term])
        
        ll = self.hamming.get_list()
        s_ll =  list(SortedList(ll))
        for i, item in enumerate(ll):
            self.assertEqual(ll[i], s_ll[i])
        

    def test_bools(self):
        for term in self.searches:
            self.hamming.accumulate(self.searches[term])

        terms= []
        o_terms = []
        for term in self.searches:
            terms.append(self.hamming.bin_transform(self.searches[term]))
            o_terms.append(self.searches[term])

        trans_apps = sum(terms, [])
        orig_apps = sum(o_terms, [])
        p_list = self.hamming.get_list()
        for y, app in enumerate(orig_apps):
            for x, perm in enumerate(app['permissions']):
                ind = p_list.index(perm)
                self.assertIs(trans_apps[y]['permissions'][ind], 1)

    # def test_sums:
    #     _all = []
    #     for obj in iterable:
    #         _all.append(obj[self.key])
    #     trans_apps = sum(_all, [])
    #     from collections import Counter
    #     c= Counter(trans_apps)
    #     return dict(c)


if __name__ == '__main__':
    unittest.main()
