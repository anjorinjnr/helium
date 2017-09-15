from bs4 import BeautifulSoup
import requests
import json


URL = 'http://www.nafdac.gov.ng/index.php/product-registration/registered-drugs?resetfilters=0'

def fetch_data(data, attempt=0):
  print '%s: %s' % (attempt, data)
  r = requests.post(URL, data=data)
  soup = BeautifulSoup(r.text, 'html.parser')
  body = soup.find('tbody', class_='fabrik_groupdata')
  rows = []
  if body:
    rows = body.find_all('tr', class_='fabrik_row')
  elif attempt < 6:
    rows = fetch_data(data, attempt+1)
  return rows

def main():
  print 'main'
  # data = {
  #   'limitstart10': 9800,
  #   'limit10': 500
  # }
  # rows = fetch_data(data)
  # drugs = []
  # while rows:
  #   print 'got %s rows' % len(rows)
  #   for row in rows:
  #     cols = row.find_all('td')
  #     drug_data = [cols[1].get_text(strip=True), cols[2].get_text(strip=True),
  #                  cols[3].get_text(strip=True), cols[4].get_text(strip=True)]
  #     drugs.append('|'.join(drug_data))
  #
  #   data['limitstart10'] += 500
  #   rows = fetch_data(data)
  #
  # with open('./drugs_9800.csv', 'w') as f:
  #   for drug in drugs:
  #     f.write(drug + '\n')

  # print 'wrote %s registered drugs from NAFDAC to drugs.csv' % len(drugs)


if __name__ == '__main__':
  main()