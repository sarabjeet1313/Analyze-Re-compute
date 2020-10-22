import sys
import argparse

##################################### HELP utility #########################################

parser=argparse.ArgumentParser(
    description='''Welcome to compute utility. ''',
    epilog="""Sarabjeet Singh - Analyze Re""")
parser.add_argument('numericals', metavar='Threshold', type=float, nargs='+',
        			help='threshold value for the computation')
parser.add_argument('numericals', metavar='Limit', type=float, nargs='+',
        			help='limit value for the computation')
args=parser.parse_args()

#############################################################################################

# fetching cmdline arguments (Threshold & Limit)
threshold = float(sys.argv[1])
limit = float((sys.argv[2]))

# initalizing sum to 0 
summation = 0.0

################### cmdline utility to process every input ##################################

for num in sys.stdin:

	if num == "\n" or num == "":  ## exit condition
		break
	else:
		num = float(num)

	if num < threshold:
		print("0.0")
	else:
		out = num - threshold
		tempSum = summation + out
		
		if tempSum > limit:
			out = limit - summation
		
		summation += out
		print(out)

# n+1 output (total sum)
print(summation)

##########################################################################################
