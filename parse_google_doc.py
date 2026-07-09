
# https://docs.google.com/document/d/e/2PACX-1vQiVT_Jj04V35C-YRzvoqyEYYzdXHcRyMUZCVQRYCu6gQJX7hbNhJ5eFCMuoX47cAsDW2ZBYppUQITr/pub
# r = requests.get("https://docs.google.com/document/d/e/2PACX-1vTMOmshQe8YvaRXi6gEPKKlsC6UpFJSMAk4mQjLm_u1gmHdVVTaeh7nBNFBRlui0sTZ-snGwZM4DBCT/pub")

import requests
import re

r = requests.get("https://docs.google.com/document/d/e/2PACX-1vQiVT_Jj04V35C-YRzvoqyEYYzdXHcRyMUZCVQRYCu6gQJX7hbNhJ5eFCMuoX47cAsDW2ZBYppUQITr/pub")

r_split = r.text.splitlines()
keyword = "assessment exercise"
blah = ""
for line in r_split:
    if keyword in line:
        blah = line

blah2_tr = blah.split('<tr ')
split_by_tr = []

for line in blah2_tr:
    if not line.isascii():
        split_by_tr.append(line)

coords = []
pattern = r'>([^<>]+)<'
for row in split_by_tr:
    matches = re.findall(pattern, row)
    if len(matches) == 3:
        coords.append(matches)
		
y_max = max([int(x[2]) for x in coords])
x_max = max([int(x[0]) for x in coords])

real_coords = dict()
for coord in coords:
    real_coords[(int(coord[0]), int(coord[2]))] = coord[1]

for y in range(y_max, -1, -1):
    line = ""
    for x in range(0, x_max+1):
        temp_coords = (x, y)
        line += real_coords.get(temp_coords, " ")
    print(line)
