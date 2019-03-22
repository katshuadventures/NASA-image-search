# nasa-image-search
``` html
<h1>A Flask web app that uses the NASA Image Gallery API to display images based on the user's search.</h1>

<h3>Frontend = 3 html pages, each styled with CSS:</h3>
<ul>
  <li><strong>index.html</strong> : the opening screen when you visit the site, includes a search bar and recommends popular searches</li>
  <li><strong>searchPage.html</strong> : the resulting page from the search that displays the top 9 images (with their title, date created, and descriptions), text about your current search, a search bar to restart your search, an option to refine searches based on date/center/location, and a hovering dropdown with more popular searches options</li>
  <li><strong>suggestions.html</strong> : the "error" page that the site is directed to whenever the search doesn't return at least 9 images, includes a search bar and recommends popular searches for the user to start a new search</li> 
</ul>

<h3>Backend = Flask via the python file __init__.py : </h3>
<ul>
  <li>form() renders the first page (index.html) whenever the user first visits the site</li>
  <li>All the other @app.route functions create the appropriate dictionary PARAMS based on the users' input into the html form or based on the specific popular search, then getdata(PARAMS) is called to get the results of the request</li>
  <li>The global variable last_keyword keeps track of the last inputted search so that it can be accessed when the search is refined</li>
  <li>Whenever a new keyword search is made, last_keyword is updated</li>
  <li>refine() accesses the last_keyword for the search and adds parameters from the html form in order to create PARAMS</li>
</ul>

<h6>My Helper Functions:</h6>
<ul>
  <li><strong>getdata(PARAMS)</strong> : makes the Python requests to the NASA API based on the inputted PARAMS, the resulting JSON from the request is iterated through with a for loop that stores the title, description, image link, and date created of the first 9 entries into 4 python lists (titles, descs, images, dates) with the index corresponding to each entry</li>
  <li><strong>curr_search(PARAMS)</strong> : returns the text message about what the user is currently search, this message is displayed above the search results for easy access</li>
</ul>

<h6>Two possible results:</h6>
<ul>
  <li>At least 9 images for the search -> the results of the search are rendered on the searchPage.html template to display to the user</li>
  <li>Less than 9 images for the search -> the for loop portion of getdata() is wrapped in a try - except clause so when there's an index error (less than 9 images), suggestions.html would be rendered to notify the user of the error</li>
</ul>
```
