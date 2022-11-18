from account import *

class Test:

    def setup_method(self):
        self.p1 = Account('cole')

    def tear_down(self):
        del self.p1

    def test_init(self):
        assert self.p1.get_name() == 'cole'

    def test_deposit(self):
        assert self.p1.deposit(10) == 10

    def test_withdraw(self):
        assert self.p1.withdraw(10) is True

