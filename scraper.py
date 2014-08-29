#!/usr/bin/python

#this script sets up the DB, reads the CSV of existing followers, writes values to the database, and closes everything down

import sqlite3
import csv

#open our CSV file of followers
ifile  = open('followers.csv', "rb")
reader = csv.reader(ifile)

#Open the database
conn = sqlite3.connect('data.db')
print "Opened database successfully";
conn.execute("DROP TABLE IF EXISTS DATA")
#
conn.execute('''CREATE TABLE data
       (TWITTERAC   TEXT    NOT NULL,
       DATE           TEXT    NOT NULL,
       FCOUNT         INT     NOT NULL
      );''')
print "Table created successfully";


rownum = 0
for row in reader:
    # Save header row.
    if rownum == 0:
        header = row
    else:
        colnum = 0
        for col in row:
        	if colnum == 0:
                #left-hand column is the date
        		twdate = row[colnum]
        		
        	else:
                    
                #establish the twitter ac name
                    twitter_ac = header[colnum]
                    #align the number of followers with the account name - and set as an integer
        	    tw_followers = int(row[colnum])
        	    #if there are some followers write out the date, ac, and follwers by passing to the tw_output function
        	    if tw_followers > 0:

                        query="""INSERT INTO DATA (TWITTERAC, DATE, FCOUNT) VALUES (?, ?, ?) """
                        write_data = [twitter_ac, twdate, tw_followers]

                        conn.execute(query, write_data)

                        #conn.execute("INSERT INTO DATA (TWITTERAC,DATE, FCOUNT) \
                        #VALUES (twitter_ac, twdate, tw_followers )");
                    
                        conn.commit()
                        print "here"

        	colnum += 1
            
    rownum += 1
#close the file and the database
ifile.close()
conn.close()
print "Ended"
