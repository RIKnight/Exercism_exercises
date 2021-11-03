#! /usr/bin/env python
"""
    Name:
        exchange.py
    Purpose:
        exercism, python track, exchange: 
            Currency exchange calculator for "my friend Chandler"
    Note:
        This program has not passed all of the unit tests.  
        I suspect that whomever wrote the unit tests either incorrectly implmented
            the application of the "spread", or whomever wrote the README.md
            which describes this problem does not know how to calculate percentage.
        The readme suggests that 1.0/1.2*(1-90/100) = 1/1.32, but it is closer to 1/1.33.
    Written by:
        Z Knight, 2021.11.03
"""

def exchange_money(budget, exchange_rate):
    """

    :param budget: float - amount of money you are planning to exchange.
    :param exchange_rate: float - unit value of the foreign currency.
    :return: float - exchanged value of the foreign currency you can receive.
    """

    return budget / exchange_rate


def get_change(budget, exchanging_value):
    """

    :param budget: float - amount of money you own.
    :param exchanging_value: int - amount of your money you want to exchange now.
    :return: float - amount left of your starting currency after exchanging.
    """

    return budget - exchanging_value


def get_value_of_bills(denomination, number_of_bills):
    """

    :param denomination: int - the value of a bill.
    :param number_of_bills: int - amount of bills you received.
    :return: int - total value of bills you now have.
    """

    return denomination * number_of_bills


def get_number_of_bills(budget, denomination):
    """

    :param budget: float - the amount of money you are planning to exchange.
    :param denomination: int - the value of a single bill.
    :return: int - number of bills after exchanging all your money.
    """

    return budget // denomination


def exchangeable_value(budget, exchange_rate, spread, denomination):
    """

    :param budget: float - the amount of your money you are planning to exchange.
    :param exchange_rate: float - the unit value of the foreign currency.
    :param spread: int - percentage that is taken as an exchange fee.
    :param denomination: int - the value of a single bill.
    :return: int - maximum value you can get.
    """

    max_exchange = exchange_money(budget, exchange_rate) * (1-spread/100)
    num_bills = get_number_of_bills(max_exchange, denomination)
    return int(num_bills * denomination)


def non_exchangeable_value(budget, exchange_rate, spread, denomination):
    """

    :param budget: float - the amount of your money you are planning to exchange.
    :param exchange_rate: float - the unit value of the foreign currency.
    :param spread: int - percentage that is taken as an exchange fee.
    :param denomination: int - the value of a single bill.
    :return: int non-exchangeable value.
    """

    max_exchange = exchange_money(budget, exchange_rate) * (1-spread/100)
    return max_exchange - exchangeable_value(budget, exchange_rate, spread, denomination)
