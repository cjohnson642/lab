from account import *


class Test:
    def setup_method(self):
        self.a1 = Account("John Doe")

    def teardown_method(self):
        del self.a1

    def test_init(self):
        assert self.a1.get_name() == "John Doe"
        assert self.a1.get_balance() == 0

    def test_deposit(self):
        assert self.a1.deposit(-2) is False
        assert self.a1.get_balance() == 0
        assert self.a1.deposit(0) is False
        assert self.a1.get_balance() == 0
        assert self.a1.deposit(100) is True
        assert self.a1.get_balance() == 100

    def test_withdraw(self):
        assert self.a1.withdraw(-50) is False
        assert self.a1.get_balance() == 0
        assert self.a1.withdraw(0) is False
        assert self.a1.get_balance() == 0
        assert self.a1.withdraw(150) is False
        assert self.a1.get_balance() == 0
        assert self.a1.deposit(200) is True
        assert self.a1.get_balance() == 200
        assert self.a1.withdraw(50) is True
        assert self.a1.get_balance() == 150
