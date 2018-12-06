# Tools
import pandas as pd
import pickle
import re

# Load the entire contents of el-wiki
with open('pages.pkl', 'rb') as f:
    pages = pickle.load(f)

# Get every item's wiki page title, weight, and stackability
weights = [
    (
        # Wiki page title is essentially the last bit of the URL
        p[0].replace('http://www.el-wiki.net/','')
            .replace('_',' ').replace('%26','&'), 
      
        # Weight is the smallest number mentioned with "EMU" after it
        min([int(n) 
            for n in re.findall('(\d+)\s*emu', str(p[1]).lower())], 
            default = 1), 

        # Stackability is usually either "yes" or "no"
        ','.join(re.findall('stackable:\s*([a-z]+)', str(p[1]).lower()))
    ) 
    for p in pages
]

# Structure the item information as a dataframe
weights = pd.DataFrame(weights, columns = ['WikiPage', 'Weight', 'Stackable'])

# No real item should have weight 0, so change it to 1
weights.loc[weights.Weight == 0, 'Weight'] = 1

# Store the weights to disk
weights.to_pickle('weights.pkl')
