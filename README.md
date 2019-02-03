# credential-harvester
A simple credential harvester written with python and hosted with flask server.

This is a credential havester use with caution
This was made for educational purposes only
I am not responsible for anything you do with this
Options:
	-p or --port
		defines port to run the server on
		default is 5000
	-u or --url
		defines url to redirect to
		defines html to scrape for harvester
	-i or --input
		defines file with modified html
		use only when an error occurs during scraping
		usually this is because of unstandard forms
	-r or --redirect
		defines redirect when using the input option
		only use with input option other wise you typed to much
	-o or --output
		defines how credential will be outputed
		you should specify a file or "stdout"
		default is "stdout"
	-h or --help
		prints this nifty help screen
