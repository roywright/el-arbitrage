# Tools
import requests
from bs4 import BeautifulSoup
import pickle
from time import sleep

# Get the list of results ready
pages = []

# Gets the contents of an el-wiki page and all its linked pages recursively
def get_page(url):
    
    # If we've already seen this page, skip it!
    if url in [p[0] for p in pages]: 
        return None
    
    # Wait a sec, then get the page's contents
    sleep(1)
    result = requests.get(url)
    c = result.content
    
    # Store the URL and contents
    pages.append((url, c))
    
    # Once in a while, report progress and store results to disk
    if len(pages) % 10 == 0: 
        print(len(pages), 'pages scraped...')
        with open('pages.pkl', 'wb') as f:
            pickle.dump(pages, f)    
    
    # Look at every link in the page
    soup = BeautifulSoup(c, 'html.parser')
    for link in soup.find_all('a'):
        h = link.get('href')
        if h is None:
            continue
        if h[0] == '/':
            h = 'http://www.el-wiki.net' + h
        
        # Only process el-wiki pages, with a few exclusions
        if (
            'el-wiki.net' in h 
            and 'php' not in h and '#' not in h
            and 'png' not in h and 'jpg' not in h and 'gif' not in h
            and 'User:' not in h and 'File:' not in h
            and 'Template:' not in h and 'Special:' not in h
        ):
            try: get_page(h)
            except: pass

# Run the function, starting from the top wiki page            
get_page('http://www.el-wiki.net/Main_Page')

# Store the final results to disk
with open('pages.pkl', 'wb') as f:
    pickle.dump(pages, f)    