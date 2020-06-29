import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-fn", help="First Name")
parser.add_argument("-ln", help="Last Name")
args = parser.parse_args()
if args.fn:
    first_name = args.fn
else:
    first_name = input('Input first name: ')
if args.ln:
    last_name = args.ln
else:
    last_name = input('Input last name: ')

print("Hello World,")
print("I am {} {}".format(first_name, last_name))
