import argparse

parser = argparse.ArgumentParser(description="Testing")
parser.add_argument('-a', dest='adding', default=False, action='store_true', help="This for testing")

args = parser.parse_args()
print(args.adding)
