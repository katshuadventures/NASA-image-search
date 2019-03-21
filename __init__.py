from flask import Flask, render_template
from flask import request, redirect
import requests

app = Flask(__name__)

# Keeps track of the last keyword search for the searches to be refined upon
last_keyword = None

@app.route('/', methods=['GET', 'POST'])
def form():
	"""
	Displays the first html page upon going to the site
	"""
	return render_template('index.html')
	
@app.route('/search', methods=['GET', 'POST'])
def search():
	"""
	Returns the resulting images from searching the keywords entered into the form.
	Uses helper function getdata().
	"""

	global last_keyword
	keywords = request.form['search']
	last_keyword = keywords
	PARAMS = {'keywords': keywords} 
	return getdata(PARAMS)

@app.route('/Hubble+Space+Telescope', methods=['GET', 'POST'])
def HST():
	"""
	Returns the resulting images from searching Hubble Space Telescope.
	Uses helper function getdata().
	"""

	global last_keyword
	last_keyword ='Hubble Space Telescope'
	PARAMS = {'keywords': last_keyword}
	return getdata(PARAMS)

@app.route('/Apollo+11', methods=['GET', 'POST'])
def A11():
	"""
	Returns the resulting images from searching Apollo 11.
	Uses helper function getdata().
	"""
	global last_keyword
	last_keyword = 'Apollo 11'
	PARAMS = {'keywords': last_keyword}
	return getdata(PARAMS)

@app.route('/New+Horizons', methods=['GET', 'POST'])
def NH():
	"""
	Returns the resulting images from searching New Horizons.
	Uses helper function getdata().
	"""
	global last_keyword
	last_keyword = 'New Horizons'
	PARAMS = {'keywords': last_keyword}
	return getdata(PARAMS)

@app.route('/Galileo', methods=['GET', 'POST'])
def G():
	"""
	Returns the resulting images from searching Galileo.
	Uses helper function getdata().
	"""
	global last_keyword
	last_keyword = 'Galileo'
	PARAMS = {'keywords': last_keyword}
	return getdata(PARAMS)

@app.route('/Voyager+1', methods=['GET', 'POST'])
def V1():
	"""
	Returns the resulting images from searching Voyager 1.
	Uses helper function getdata().
	"""
	global last_keyword
	last_keyword = 'Voyager 1'
	PARAMS = {'keywords': last_keyword}
	return getdata(PARAMS)

@app.route('/Earth', methods=['GET', 'POST'])
def PP():
	"""
	Returns the resulting images from searching Earth.
	Uses helper function getdata().
	"""
	global last_keyword
	last_keyword = 'Earth'
	PARAMS = {'keywords': last_keyword}
	return getdata(PARAMS)

@app.route('/Katherine+Johnson', methods=['GET', 'POST'])
def KJ():
	"""
	Returns the resulting images from searching Katherine Johnson.
	Uses helper function getdata().
	"""
	global last_keyword
	last_keyword = 'Katherine Johnson'
	PARAMS = {'keywords': last_keyword}
	return getdata(PARAMS)

@app.route('/refine', methods=['GET', 'POST'])
def refine():
	"""
	Returns the image results based on the added refinements.
	Uses helper function getdata().
	"""
	start = request.form['start']
	end = request.form['end']
	loc = request.form.getlist('loc')
	center = request.form.getlist('center')
	PARAMS = {'keywords': last_keyword}
	if start != 'Start Year':
		PARAMS['year_start'] = start
	if end != 'Present':
		PARAMS['year_end'] = end
	if loc:
		PARAMS['location'] = loc[0]
	if center:
		PARAMS['center'] = center[0]
	return getdata(PARAMS)

def getdata(PARAMS):
	"""
	With the given PARAMS, makes the request to NASA's API.
	Receives a json string from the request.
	Indexs the json string to render the appropriate values on the search page
	If there's less than 9 images from the search, then the page is redirected to notify the error
	"""
	# NASA api-endpoint 
	URL = "https://images-api.nasa.gov/search"
  
	# Sends the get request and saving the response as response object 
	r = requests.get(url = URL, params = PARAMS) 
  
	# Extracts the data in json format 
	data = r.json() 

	# Records the title, description, image link, and date created of the first 9 (gallery size) images
	titles, descs, images, dates = [], [], [], []
	gallery_size = 9
	try:
		for i in range(gallery_size):
			titles.append(data['collection']['items'][i]['data'][0]['title'])
			descs.append(data['collection']['items'][i]['data'][0]['description'])
			images.append(data['collection']['items'][i]['links'][0]['href'])
			dates.append(data['collection']['items'][i]['data'][0]['date_created'])

	# Renders the next page with the appropriate images and text based on the search
		return render_template('searchPage.html', title1 = titles[0], desc1 = descs[0], image1 = images[0], date1 = dates[0],
			title2 = titles[1], desc2 = descs[1], image2 = images[1], date2 = dates[1],
			title3 = titles[2], desc3 = descs[2], image3 = images[2], date3 = dates[2],
			title4 = titles[3], desc4 = descs[3], image4 = images[3], date4 = dates[3],
			title5 = titles[4], desc5 = descs[4], image5 = images[4], date5 = dates[4],
			title6 = titles[5], desc6 = descs[5], image6 = images[5], date6 = dates[5],
			title7 = titles[6], desc7 = descs[6], image7 = images[6], date7 = dates[6],
			title8 = titles[7], desc8 = descs[7], image8 = images[7], date8 = dates[7],
			title9 = titles[8], desc9 = descs[8], image9 = images[8], date9 = dates[8],
			message = curr_search(PARAMS))
	
	# Renders the error page if there's less than 9 (gallery size) images available
	except IndexError:
		return render_template('suggestions.html')

def curr_search(PARAMS):
	""" 
	Returns the string of what we are currently searching.
	Includes the keyword, start year, end year, location, and center if the information is inputted.
	"""
	message = ''
	for key in PARAMS:
		if key == 'keywords':
			message += PARAMS[key]
		elif key == 'year_start':
			message += ' from year ' + PARAMS[key]
		elif key == 'year_end':
			message += ' up to year ' + PARAMS[key]
		elif key == 'location':
			message += ' on the ' + PARAMS[key]
		elif key == 'center':
			message += ' from ' + PARAMS[key]
	message += '.'
	return message

if __name__ == "__main__":
	app.run(debug = True)


 