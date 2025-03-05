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


def preprocess_sim(sim):
    for i, account in enumerate(sim['accounts']):
        if account['type'] == 'mortgage':
            if type(account['rate']) in [int, float]:
                rate = float(account.rate)
            elif type(account[])
            sim['accounts'][i] = Mortgage(**account)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage: ./sim.py <path_to_sim_file.yml>')
        exit()

    with open(sys.argv[1]) as f:
        sim = yaml.safe_load(f)

    preprocess_sim(sim)

    print(sim)
