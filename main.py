import sys
import argparse
import communicate

main_parser = argparse.ArgumentParser(
	description = """
	This is a tester for interactive problem.
	
	You can communicate your code which is checker and code which you want to check.
	"""
)

main_parser.add_argument(
	"checker",
	metavar = "checker_file",
	type = str,
	nargs = 1,
	help = """
	File that you want to use to check your source code.
	"""
)

main_parser.add_argument(
	"source",
	metavar = "source_file",
	type = str,
	nargs = 1,
	help = """
	File that contains your source you want to check.
	"""
)

main_parser.add_argument(
	"-e",
	dest = "end_characters",
	metavar = "characters",
	type = str,
	nargs = '*',
	default = [],
	help = """
	List of characters which will end the communication.
	"""
)

main_parser.add_argument(
	"-f", "--first",
	dest = "source_first",
	action = "store_true",
	default = False,
	help = """
	Set source code will go first.
	"""
)

def run():
	arg = main_parser.parse_args()
	communication = communicate.Communication(arg.checker, arg.source)
	arg.end_characters.append('')
	communication.communicate(arg.end_characters, arg.source_first)

if __name__ == '__main__':
	try:
		run()
	except Exception as e:
		print(f"Exit code of program: {e}")
		sys.exit(1)