import sys


def main():
	args = sys.argv[1:]
	if len(args) == 0:
		print("Usage: python spider.py  [-rlp] URL")

if __name__ == "__main__":
	main()