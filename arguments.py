import argparse

parser = argparse.ArgumentParser(description = "This program prints the name of my dogs"

)
parser.add_argument('-c','--color',metavar = 'color',required = True,choices = ("read",'yellow'),helps = ' the color to searchfor' )
args = parser.parse_args()
print(args.color)
