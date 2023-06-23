from crawler import Crawler, Userinfo

import argparse

if __name__ == "__main__":
	
	parser = argparse.ArgumentParser()

	parser.add_argument("username")
	parser.add_argument("-e", "--exact",
		help="Return accounts whose usernames exactly match (on the stdout)",
		action="store_true",
	)
	parser.add_argument("-w", "--write_html",
		help="Write the HTML file on the output/",
		action="store_true",
	)

	args = parser.parse_args()

	crawler = Crawler()
	userinfos = crawler.crawl(args.username, args.write_html,
		validator=(lambda x: x == args.username) if args.exact else None
	)

	for userinfo in userinfos:
		print(userinfo)