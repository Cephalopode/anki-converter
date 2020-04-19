#!/usr/bin/env python
# -*- coding: utf-8 -*-
import csv
f = open('./fav.csv')

fn = csv.reader(f)

with open('ouput.csv', 'wb') as csvfile:
	w = csv.writer(csvfile, delimiter=',',
	                            quotechar='"', quoting=csv.QUOTE_MINIMAL)

	for row in fn:
		defn = row[2:4]
		ex = row[5:7]
		out = []
		if row[:2] == ['en','ru']:
			n = ""
		elif row[:2] == ['ru','en']:
			defn = defn[::-1]
			ex = ex[::-1]
		else:
			continue
		out = ["<h3>"+defn[0]+"</h3>", "<h3>"+defn[1]+"</h3>"]
		if len(row)> 6 and row[5] and row[6]:
			out[1] += "<p>" + ex[1]+"</p><p>"+ ex[0] + "</p>"

		print out
		w.writerow(out)
