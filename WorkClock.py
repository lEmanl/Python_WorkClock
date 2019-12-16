import argparse
import os

from ArgsUtil import args_parser
from ClockIn import db_user_clockin
from ClockOut import db_user_clockout
from Status import db_user_status
from Report import db_user_report
from UserInit import db_user_init
from Init import db_init

parser = args_parser()
args = parser.parse_args()

if(args.clockin):
    print(db_user_clockin(args.clockin, args.description))

elif(args.clockout):
    print(db_user_clockout(args.clockout, args.description))

elif(args.status):
    print(db_user_status(args.status))

elif(args.report):
    print(db_user_report(args.report, args.format))

elif(args.init):
    if(args.init == "MASTER"):
        print(db_init())

    else:
        print(db_user_init(args.init))

else:
    print("NoOp")