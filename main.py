import json
import sqlite3
from configparser import ConfigParser
from datetime import datetime

import requests
from discord import Colour, Embed, RequestsWebhookAdapter, Webhook


def get_xid(company_ticker: str) -> str:
    """Returns the XID of a company according to its ticker."""
    r = requests.get(
        f"https://asx.api.markitdigital.com/asx-research/1.0/search/predictive?searchText={company_ticker}").json()
    return r['data']['items'][0]['xidEntity']


def send_webhook(config, company, announcement):
    webhook = Webhook.partial(
        int(config['Discord Settings']['id']), config['Discord Settings']['token'], adapter=RequestsWebhookAdapter())
    if announcement['isPriceSensitive'] is True:
        embed_colour = Colour.red()
    else:
        embed_colour = Colour.green()
    announcement_date = datetime.strptime(
        announcement['date'], "%Y-%m-%dT%H:%M:%S.%fZ")
    embed = Embed(
        title=f"{company} - {announcement['headline']}", colour=embed_colour, timestamp=announcement_date)
    embed.add_field(name='Company Name',
                    value=announcement['companyInfo'][0]['displayName'], inline=False)
    try:
        embed.add_field(name='Announcement Type',
                        value=announcement['announcementTypes'][0])
    except:
        print(
            f"[ERROR] Couldn't find announcement type for {company}'s announcement on {announcement_date}")
        pass
    embed.add_field(name='Announcement Time',
                    value=announcement_date.strftime("%H:%M:%S:%f UTC"))
    embed.add_field(name='Price Sensitive',
                    value=str(announcement['isPriceSensitive']))
    embed.add_field(name='Document URL',
                    value=f"https://cdn-api.markitdigital.com/apiman-gateway/ASX/asx-research/1.0/file/{announcement['documentKey']}?access_token=83ff96335c2d45a094df02a206a39ff4", inline=False)
    webhook.send(
        embed=embed, username=company, avatar_url="https://www2.asx.com.au/content/dam/asx/asx-logos/asx-brandmark.png")


def main():
    config = ConfigParser()
    config.read('config.ini')

    company_tickers = json.loads(config['Watchlist']['watchlist'])

    conn = sqlite3.connect('announcements.db')
    c = conn.cursor()

    for company in company_tickers:
        company_table_name = f"C_{company}"
        c.execute(
            f"CREATE TABLE IF NOT EXISTS {company_table_name} (document_key text, date text)")
        c.execute(
            f"SELECT Count() FROM {company_table_name}")
        table_rows = c.fetchone()[0]
        announcements = requests.get(
            f"https://asx.api.markitdigital.com/asx-research/1.0/markets/announcements?entityXids[]={get_xid(company)}&page=0&itemsPerPage=9999").json()
        for announcement in announcements['data']['items']:
            document_key = announcement["documentKey"]
            date = announcement["date"]
            c.execute(
                f"SELECT 1 FROM {company_table_name} WHERE document_key=?", (document_key,))
            if c.fetchone() is None:
                print(f"New announcement {document_key}, {date}")
                c.execute(
                    f"INSERT INTO {company_table_name} VALUES (?, ?)", (document_key, date))
                if table_rows != 0:
                    send_webhook(config, company, announcement)
                conn.commit()

    conn.close()


main()
