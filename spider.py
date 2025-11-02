import sys
from playwright.sync_api import sync_playwright


def main():
	args = sys.argv[1:]
	if len(args) == 0:
		print("Usage: python spider.py  [-rlp] URL")
		return
	
	# Start playwright
	with sync_playwright() as p:
		# Launch Chromium in headless mode
		browser = p.chromium.launch(headless=True)

		# Create a browser context
		context = browser.new_context()

		# Open a new page
		page = context.new_page()
	
		# handle basic usage i.g., no options only url 
		if len(args) == 1:
			# Navigate to the page and wait until all network activity is done
			page.goto(args[0], wait_until="networkidle")

			# Get and print the page title
			title = page.title()
			print("Page title: ", title)

			# Get and print the first 200 characters of the fully rendered HTML
			html = page.content()

			print("\nRendered HTML (first 200 chars):")
			print(html[:200])

		# Clean up
		context.close()
		browser.close()

if __name__ == "__main__":
	main()