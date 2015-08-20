# Ett script som 'skrapar' http://[seriens namn].thecomicseries.com
# efter länkadresserna till bilderna och sparar ner dessa
# med korrekt namn ist för långt löpnummer.
# Scriptet är baserat på scraping scriptet i Programming the RPi boken
# 
# Written for Python 3
# 2015-08-15

import urllib.request


def scrape(scrape_material):
    
    i = scrape_material.find('"comicimagewrap"')
    
    i = scrape_material.find('=', i+1)
    i = scrape_material.find('"', i+1)
    # Find the first '<' after the two '>'
    j = scrape_material.find('"', i+1)
    imgurl = scrape_material[i+1:j]
    
    
    name = file_name_constructor(scrape_material)
    file_type = save_file(imgurl, name)
    
    if file_type == 'png' or file_type == 'jpg':
        print(name + '.' + file_type, " downloaded\n")
    else:
        print("These aren't the files you're looking for.\n")


# Det sker en ändring av filformat en bit in därav storleken på den här funktionen.
def save_file(from_url, to_name):
    
    if from_url[-3:] == 'png':
        urllib.request.urlretrieve(from_url, to_name + '.png')
        return 'png'
    elif from_url[-3:] == 'jpg':
        urllib.request.urlretrieve(from_url, to_name + '.jpg')
        return 'jpg'
    else:
        #return from_url[-4:]
        pass


def file_name_constructor(lots_of_html):
    i = lots_of_html.find('heading">Comic')
    i = lots_of_html.find(' ', i)
    j = lots_of_html.find('<', i)
    
    number = lots_of_html[i:i+4].strip('-')
    number = number.strip()
    k = 0
    
    # en-, två- eller tresiffrigt?
    if len(number) == 1:
        k = i + 5
        number = '00' + number
    elif len(number) == 2:
        k = i + 6
        number = '0' + number
    elif len(number) == 3:
        k = i + 7
    else:
        print('Something went wrong with the number extraction.')
        print('Check file_name_constructor().\n')
    
    # används namn eller numrering?
    if number == lots_of_html[ j-3 :j ]:
        name = number
    else:
        name = number + ' ' + lots_of_html[k:j]
    
    return name


# range sätts till det spann av sidor man vill ha bilder från
for n in range(1,4):
    u = 'http://nmg.thecomicseries.com/comics/{}'.format(n)
    print(u)
    f = urllib.request.urlopen(u)
    contents = str(f.read())
    f.close()
    scrape(contents)
