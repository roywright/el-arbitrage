# Tools
import pandas as pd
import pickle
import re

# Load the entire contents of el-wiki
with open('pages.pkl', 'rb') as f:
    pages = pickle.load(f)

# Get every item's name and weight
#   o Name is essentially the last bit of the URL
#   o Weight is the smallest number mentioned with "EMU" after it
weights = [
    (
        p[0].replace(
            'http://www.el-wiki.net/',''
        ).replace('_',' ').replace('%26','&'), 
        min([
            int(n) 
            for n in re.findall('(\d+)\s*emu', str(p[1]).lower())
        ], default = None)
    ) 
    for p in pages
]
# Filter out anything without a weight
weights = [w for w in weights if w[1] is not None]

# Structure the weights as a dataframe
weights = pd.DataFrame(
    weights, 
    columns = ['Item', 'Weight']
).set_index('Item')

# No real item should have weight 0, so change it to 1
weights.loc[weights.Weight == 0, 'Weight'] = 1

# Store the weights to disk
weights.to_pickle('weights.pkl')