""" Telugu Words Extractor """

import json
import requests
import time

from bs4 import BeautifulSoup

URL = "http://dsalsrv02.uchicago.edu/cgi-bin/romadict.pl?table=brown\
       &page=%s&display=simple"

START_PAGE, END_PAGE, OUTPUT_FILE = 1, 1410, 'words.json'


def get_words(html):
    """ Takes html and returns a list of telugu words"""
    words = []
    soup = BeautifulSoup(html)
    for paragraph in soup.find_all('p'):
        words.append(paragraph.find('span').get_text())
    return list(set(words))


def extract_words(url, start_page, end_page):
    """ Extracts words from the given range of URLs using 'get_words' """
    all_words = []
    for page in range(start_page, end_page):
        if (page % 50) == 0:
            time.sleep(4)
        try:
            all_words.extend(get_words(requests.get(url % page).content))
            print "successfully extracted words from page - %d" % page
        except requests.exceptions.ConnectionError:
            print "please connect to internet"
            break
        except:
            print "skipping page - %d" % page
    return sorted(list(set(all_words)))


def save_as_json_dump(data, output_file):
    """ Writes the given data into the specified output file"""
    with open(output_file, 'w') as outfile:
        json.dump(data, outfile)


save_as_json_dump(extract_words(URL, START_PAGE, END_PAGE),
                  OUTPUT_FILE)
