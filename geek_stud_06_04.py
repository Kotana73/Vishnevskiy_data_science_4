
from itertools import count, cycle

my_count = count(8)
my_cycle = cycle('ABCD')

for _ in range(7):
    print('(my_count, my_cycle) = ({}, {})'.format(next(my_count), next(my_cycle)))

