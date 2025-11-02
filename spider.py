import sys
import requests
from playwright.sync_api import sync_playwright


def main():
	args = sys.argv[1:]
	if len(args) == 0:
		print("Usage: python spider.py  [-rlp] URL")
		return
	
	# handle basic usage i.g., no options only url 
	if len(args) == 1:
		res = requests.get(args[0])
		if res.status_code != 200:
			print("BLOCKED: ", res.status_code)
		else:
			print(res.text)

if __name__ == "__main__":
	main()