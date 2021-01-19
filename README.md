# Short links with [bitly](https://bit.ly/) in the console  
  
This is a console utility for shortening links using [bit.ly API](https://dev.bitly.com/). Using an existing bitly link, you can get count of clicks for all the time.  
  
## Getting Started  
  
You need to create a Bitly account [bitly](https://bit.ly/) and get a GENERIC ACCESS TOKEN.  
  
## How to run  
  
Download the project and create a .env file. Create a 'BITLY_TOKEN' variable in this file, which will store your bitly token.  
A sample `.env` file might look like this:
```
BITLY_TOKEN=<your token>
```

  
### Requirements  
  
```
pip install requests
  
pip install -U python-dotenv 
```
or
```
pip install -r requirements.txt
```
  
### Shorten your first link!  
  
```
python main.py
```
  
You need to enter a link. A successful response will return the shortened link in the link object.  
If you enter an existing bit ly link, the result will be the number of clicks for the entire time.  
  
## License  
This project is licensed under the MIT License - see the LICENSE file for details