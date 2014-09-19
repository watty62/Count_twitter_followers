This is a scraper that runs on [Morph](https://morph.io). To get started [see the documentation](https://morph.io/documentation).

The purpose of this scraper is to scrape the number of followers we have for a number of our corporate accounts and store these in a database table. 

The scraper.py file is in two parts.

Section A is a set-up routine which creates the database table, assigns columns, then writes in data in the new format from some lists which I generated from the followers.csv file. I chose to do this as I was unable to import and use the CSV library that I had used on my home laptop.

If you want to experiment with this, uncomment Section A, and comment out (using ''') section B.

Section B is the scraper itself.

It first checks the date - and only runs if it is the 1st of the month. 

Then it processes a list of twitter account names, constructing full URLs and scraping the number of followers for each from the twitter page. The actual figure only appears as a tooltip mouse-over - and I had [some help](http://stackoverflow.com/questions/25447571/grabbing-a-specific-value-from-a-webpage-using-lxml?noredirect=1#comment39705950_25447571)  working out how to get it out of the code! 

Once it has the number of followers per account it writes these off to the database.

As I write this (30/08/14 - or 20140830 as the script would call it!) the code hasn't executed for real - although it has all been tested in chunks.

I'll watch nervously on 1st Sept to see if it works as planned!

If you have any questions you can contact me on Twitter: [@watty62](http://twitter.com/watty62)
