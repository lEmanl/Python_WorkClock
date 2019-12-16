import argparse

def args_parser():
    #   Description of CL Tool
    parser = argparse.ArgumentParser(
        description = "Log work hours and format that information"
    )

    groupInit = parser.add_mutually_exclusive_group()
    groupCheckOut = parser.add_mutually_exclusive_group()
    groupCheckIn = parser.add_mutually_exclusive_group()
    groupStatus = parser.add_mutually_exclusive_group()
    groupCheckout = parser.add_mutually_exclusive_group()

    #   Option to initialize employee
    groupInit.add_argument(
        "--init",
        help = "Provide username of the employee"
    )

    #   Optional argument, used to clock in and out
    groupCheckOut.add_argument(
        "-i", "--clockin", type = str,
        help = "Provide username to clock out"
    )
    groupCheckout.add_argument(
        "-d", "--description", type = str,
        default = "None", help = "Provide description for work done",
    )
    groupCheckIn.add_argument(
        "-o", "--clockout", type = str,
        help = "Provide username to clock out"
    )

    #   Option to check status of work session
    groupStatus.add_argument(
        "-s", "--status",
        help = "Provide username to check status of"
    )

    #   Option to checkout work information
    parser.add_argument(
        "-r", "--report",
        help = "Provide username to report"
    )
    parser.add_argument(
        "-f", "--format",
        default = "List", help = "Provide format for report"
    )
    
    return parser