# http://www.checkio.org/mission/task/info/atm/python-3/

# Withdraw without any incident
# 120 - 10 - 0.5 - 1% = 109.4
# 109.4 - 20 - 0.5 - 1% = 88.7
# 88.7 - 30 - 0.5 - 1% = 57.9

from decimal import Decimal

STD_COMMISSION = Decimal("0.5")

def is_amount_valid(x):
    return x % 5 == 0

def get_remaining_balance(withdrawal, balance):
    for amount in withdrawal:
        amount += amount * Decimal('0.01') + STD_COMMISSION
        if amount <= balance:
            balance -= amount
    return balance


def checkio(data):
    balance, withdrawal = data
    return get_remaining_balance(filter(is_amount_valid, withdrawal), balance)

if __name__ == '__main__':
    assert Decimal(checkio([Decimal('120'), [Decimal('10') , Decimal('20'), Decimal('30')] ])) ==\
           Decimal('57.9') ,'First'

    # With one Insufficient Funds, and then withdraw 10 $
    assert Decimal(checkio([Decimal('120'), [Decimal('200') , Decimal('10')] ])) ==\
           Decimal('109.4'), 'Second'

    #with one incorrect amount
    assert Decimal(checkio([Decimal('120'),[Decimal('3'),Decimal('10')] ])) ==\
           Decimal('109.4'), 'Third'

    assert checkio([Decimal('120'), [Decimal('200') , Decimal('119')] ]) == Decimal('120') , 'Fourth'

    print 'All Ok'