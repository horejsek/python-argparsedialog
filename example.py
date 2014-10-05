# -*- coding: utf-8 -*-

#from argparse import ArgumentParser
from argparsedialog import ArgumentParser


parser = ArgumentParser(
    prog='Example program',
    description='Example of argument parser converted to graphical wizzard using dialog.',
    epilog='Epilog of argument parser.',
)

parser.add_argument('--value', dest='value', help='Help of argument --value.')
parser.add_argument('--value-default', dest='value_default', default='default value')

choices = ['chocie one', 'choice two', 'choice three']
parser.add_argument('--value-choice', dest='value_choice', choices=choices)
parser.add_argument('--value-choices', dest='value_choices', choices=choices, action='append')

parser.add_argument('--value-append', dest='value_append', action='append')
parser.add_argument('--value-append-const', dest='value_append_const', action='append_const', const='foo')

parser.add_argument('--list-one', dest='list_one', nargs='?')
parser.add_argument('--list-two', dest='list_two', nargs=2)
parser.add_argument('--list-unlimited', dest='list_unlimited', nargs='*')

parser.add_argument('--flag-const', dest='flag_const', action='store_const', const='foo')
parser.add_argument('--flag-default', dest='flag_default', action='store_const', const='foo', default='bar')
parser.add_argument('--flag-true', dest='flag_true', action='store_true')
parser.add_argument('--flag-false', dest='flag_false', action='store_false')

parser.add_argument('-v', dest='v', action='count')

parser.add_argument('positional_value')


args = parser.parse_args()
print(args)
