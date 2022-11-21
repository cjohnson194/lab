from account import *
import pytest

class Test:

    def setup_method(self):
        self.p1 = Account('cole')

    def tear_down(self):
        del self.p1

    def test_init(self):
        assert self.p1.get_name() == 'cole'
        assert self.p1.get_balance() == 0

    def test_deposit(self):
        assert self.p1.get_balance() == pytest.approx(0, abs=0.001)

        assert self.p1.deposit(20.5) is True
        assert self.p1.get_balance() == pytest.approx(20.5, abs=0.001)

        assert self.p1.deposit(-20.5) is False
        assert self.p1.get_balance() == pytest.approx(20.5, abs=0.001)

        assert self.p1.deposit(0) is False
        assert self.p1.get_balance() == pytest.approx(20.5, abs=0.001)

    def test_withdraw(self):
        assert self.p1.get_balance() == pytest.approx(0, abs=0.001)

        assert self.p1.deposit(20.5) is True
        assert self.p1.get_balance() == pytest.approx(20.5, abs=0.001)

        assert self.p1.withdraw(10.5) is True
        assert self.p1.get_balance() == pytest.approx(10, abs=0.001)

        assert self.p1.withdraw(-10) is False
        assert self.p1.get_balance() == pytest.approx(10, abs=0.001)

        assert self.p1.withdraw(0) is False
        assert self.p1.get_balance() == pytest.approx(10, abs=0.001)





