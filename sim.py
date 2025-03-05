#!/bin/env python
import yaml
import sys

EPSILON = 1e-6

class Mortgage:
    def __init__(self, rate, principal, term, payment=None, name='Mortgage'):
        self.name = name
        self.rate = rate
        self.principal = principal
        self.term = term

        self.reset_min_payment()
        if payment:
            self.payment = payment
        else:
            self.payment = min_payment()

        self.history = []
    

    def reset_min_payment(self):
        P = self.principal
        r = self.rate
        N = self.term
        self.min_payment = P * r * (1+r)**N / ((1+r)**n - 1)


    def tick(self) -> bool:
        interest_paid = self.principal * self.rate
        principal_paid = min(self.payment - interest, self.principal)
        record = {
            'interest_paid': interest_paid,
            'principal_paid': principal_paid,
            'old_principal': self.principal,
            'new_principal': self.principal - principal_paid
        }

        return abs(self.principal) > EPSILON

def floatify(val: any) -> float:
    if type(val) in [int, float]:
        return float(account.rate)
    elif type(val) == str:
        return float(eval(val))
    else:
        raise ValueError(f'Unable to floatify value of type {type(val)}')

def intify(val: any) -> int:
    if type(val) in [int, float]:
        return int(account.rate)
    elif type(val) == str:
        return int(eval(val))
    else:
        raise ValueError(f'Unable to floatify value of type {type(val)}')

def preprocess_sim(sim):
    for i, account in enumerate(sim['accounts']):
        if account['type'] == 'mortgage':
            rate = floatify(account['rate'])
            principal = floatify(account['principal'])
            term = intify(account['term'])
            if 'payment' in account:
                payment = floatify(account['payment'])
            else:
                payment = None
            sim['accounts'][i] = Mortgage(rate, principal, term, payment, account['name'])


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: ./sim.py <path_to_sim_file.yml>')
        exit()

    with open(sys.argv[1]) as f:
        sim = yaml.safe_load(f)

    preprocess_sim(sim)

    print(sim)
