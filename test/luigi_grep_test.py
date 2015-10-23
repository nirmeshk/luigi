from hypothesis import given, assume
from hypothesis.strategies import text

from helpers import unittest

import json
from luigi.tools import luigi_grep

class MyUrlOpen(object):
    def read(self):
        jobs = [{deps:['HTTMock', 'hypothesis'], status: 'UNKNOWN', name: 'findMe'},
            {},
            {}]
       
        return {'status_code': 200,
            'content': json.dumps(jobs)}

def f(url) : return MyUrlOpen()
luigi_grep.urlopen = f

class TestLuigiGrep(unittest.TestCase):

    def setUp(self):
        self.grep = luigi_grep.LuigiGrep('localhost', 3005)


    #@given(text())
    def test_prefix_search(self):
        self.grep.prefix_search('Starts')
        pass

    #@given(text())
    def test_status_search(self):
        self.grep.status_search('UNKNOWN')
        pass