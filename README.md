# Maoyan_price

Scraping movie price from [m.maoyan.com](http://m.maoyan.com). See _Main.ipynb_.


Since the website use __Ajax__ to dynamically load the webpage, used [selenium](http://www.seleniumhq.org) and [phantomjs](http://phantomjs.org) to run the javascript inside the html.

[Maoyan](http://m.maoyan.com) also hide the price information using self-defined font (woff file embedded in the html) to mapping characters, such as __ to the number _5_. I used the __convert__ method from  [ImageMagick](http://www.imagemagick.org) to generate a _30dp x 20dp_ .jpg image file( in the *mapping_num* folder) and recognized the number within using a 3 layer neural networks. The training data source and the training of the neural networks can refer to the _Training Neural Network.ipynb_ inside the _training_ folder.
### Sample data
_data.sqlite_: sample data scrape from [http://m.maoyan.com/shows/881?_v_=yes](http://m.maoyan.com/shows/881?_v_=yes) (881 stands for the cinema id in [maoyan](http://m.maoyan.com))

### Required

  - [Selenium](http://www.seleniumhq.org)
  - [Phantomjs](http://phantomjs.org)
  - [ImageMagick](http://www.imagemagick.org)
  - [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup)
  - numpy
  - scipy
