# el-arbitrage
I noticed that sometimes a bot in [Eternal Lands](http://eternal-lands.com/) is selling an item for less than another bot is paying for that item, creating an opportunity for profit. This little project is an effort (just for fun) to systematically find the biggest opportunities.

`scrape_elwiki.py` is a script to pull all items-related pages from the [Eternal Lands Wiki](http://www.el-wiki.net/). This takes a little over an hour; the results are stored locally (~80MB).

`get_EMUs.py` processes the wiki scrapings down to a list of items and weights and stores them as `weights.pkl`. This file is provided here, so there should be no need to actually run `scrape_elwiki.py` or `get_EMUs.py`.

`opportunities.ipynb` gets all current bot and NPC prices from [here](http://greypal.el-fd.org/cgi-bin/querybot) and lists the best profit-making opportunities.
