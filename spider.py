import sys
from playwright.sync_api import sync_playwright


def parse_args():
	"""Parse CLI arguments manually (simple approach)"""
	args = sys.argv[1:]

	if len(args) == 0:
		print("Usage: python spider.py [-r | -l | -p] URL")
		sys.exit(1)
	
	flags = [a for a in args if a.startswith("-")]
	urls = [a for a in args if not a.startswith("-")]

	if len(urls) != 1:
		print("Error: you must provide exactly one URL.")
		sys.exit(1)
	
	return flags, urls[0]

def run_scraper(url, flags):
	"""Everything Playwright-related happens inside this function."""
	with sync_playwright() as p:
		# Launch Chromium in headless mode
		browser = p.chromium.launch(headless=True)
		# Create a browser context
		context = browser.new_context()
		# Open a new page
		page = context.new_page()

		# Navigate to the page and wait until all network activity is done
		page.goto(url, wait_until="networkidle")

		# ---- BASIC ACTIONS ----
		print("Title: ", page.title())

		html = page.content()
		print("\nRendered HTML (first 200 chars):")
		print(html[:200])

		# PLACEHOLDERS: handle flags here
		if "-r" in flags:
			print("\n[-r] Raw HTML length: ", len(html))
		
		if "-l" in flags:
			print("\n[-l] Curl URL: ", page.url)
		
		if "-p" in flags:
			print("\n[-p] Printing page text:")
			print(page.inner_text("body"))
		
		context.close()
		browser.close()

def main():
	flags, url = parse_args()
	run_scraper(url, flags)
	
	

if __name__ == "__main__":
	main()