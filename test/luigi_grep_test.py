from hypothesis import given, assume
from hypothesis.strategies import text

from helpers import unittest

import json
from luigi.tools import luigi_grep


class MyUrlOpen(object):
    def __init__(self, jobs):
        self.jobs = jobs

    def read(self):
        return json.dumps({'status_code': 200, 'response': json.dumps(self.jobs)})


class TestLuigiGrep(unittest.TestCase):

    def setUp(self):
        self.grep = luigi_grep.LuigiGrep('localhost', 3005)

    @given(text())
    def test_prefix_search(self, name_prefix):
        assume(len(name_prefix) > 1)
        job = {"deps": ["HTTMock", "hypothesis"], "status": "UNKNOWN", "name": name_prefix}
        jobs = {name_prefix: job}

        def f(url):
            return MyUrlOpen(jobs)
        luigi_grep.urlopen = f

        results = self.grep.prefix_search(name_prefix)
        for x in results:
            assert x[name_prefix] == job
