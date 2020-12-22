import requests
import json
import sqlite3

conn = sqlite3.connect('announcements.db')
c = conn.cursor()

company_tickers = ['EML']

for company in company_tickers:
    c.execute(
        f"CREATE TABLE IF NOT EXISTS {company} (document_key text, date text)")

    r = requests.get(
        'https://asx.api.markitdigital.com/asx-research/1.0/markets/announcements?entityXids[]=204124784&page=0&itemsPerPage=1').json()
    for announcement in r['data']['items']:
        c.execute(f"INSERT INTO {company} VALUES (?, ?)",
                  (announcement["documentKey"], announcement["date"]))

conn.commit()
conn.close()
