import unittest
from unittest.mock import patch
import app



print(app.WORDS)
VAL_CHAR = 'a'
INVAL_CHAR = 1
POS = [0, 2]
LINES = ['_', '_', '_', '_', '_']
CHAR = 'a'
NEW_LINES = ['a', '_', 'a', '_', '_']

class Test(unittest.TestCase):   
    def test_check_valid_input(self):
        self.assertEquals(app.check(VAL_CHAR), True)

    def test_check_invalid_input(self):
        self.assertEquals(app.check(INVAL_CHAR), False)
    
    @patch('app.get_input', return_value='a')
    def test_vvod_bukv(self, input):
        self.assertEquals(app.vvod_bukv(), 'a')

    def test_attempt_valid(self):
        res = app.attempt('t', app.WORDS[1])
        self.assertEquals(res, [0,3])

    def test_attempt_invalid(self):
        res = app.attempt('x', app.WORDS[1])
        self.assertEquals(res, False)
    
    @patch('app.fail', return_value=4)
    def test_game_over(self, input):
        self.assertEquals(app.game(app.WORDS[1]), 1)

    def test_fail(self):
        self.assertEquals(app.fail(3), 4)

    def test_success(self):
        self.assertEquals(app.succes(POS, LINES, CHAR), NEW_LINES)

import sys

if __name__ == '__main__':
    unittest.main()