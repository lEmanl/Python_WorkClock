import argparse
import sys

from ArgsUtil import arg_parser

parser = args_parser()
args = parser.parse_args()

print(args)