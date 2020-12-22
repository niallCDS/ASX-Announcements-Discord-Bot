import requests
import json
import sqlite3
from discord import Webhook, RequestsWebhookAdapter, Embed, Colour

conn = sqlite3.connect('announcements.db')
c = conn.cursor()

company_tickers = ['EML']

for company in company_tickers:
    c.execute(
        f"CREATE TABLE IF NOT EXISTS {company} (document_key text, date text)")

    r = requests.get(
        'https://asx.api.markitdigital.com/asx-research/1.0/markets/announcements?entityXids[]=204124784&page=0&itemsPerPage=50').json()
    for announcement in r['data']['items']:
        document_key = announcement["documentKey"]
        date = announcement["date"]
        c.execute(
            f"SELECT 1 FROM {company} WHERE document_key=?", (document_key,))
        if c.fetchone() is None:
            print(f"New announcement {document_key}, {date}")
            c.execute(
                f"INSERT INTO {company} VALUES (?, ?)", (document_key, date))
            webhook = Webhook.partial(
                790900535250649088, 'w4_92oUaUEdWINNjZEC6-BXUOubFa7xjaGEy_z9UbNk1-oH1scDJ5EBK912qrb-dAIW-', adapter=RequestsWebhookAdapter())
            if announcement['isPriceSensitive'] is True:
                embed_colour = Colour.red()
            else:
                embed_colour = Colour.orange()
            embed = Embed(
                title=f"{announcement['companyInfo'][0]['symbol']} - {announcement['headline']}", colour=embed_colour)
            embed.add_field(name='Announcement Type',
                            value=announcement['announcementTypes'][0], inline=True)
            embed.add_field(name='Announcement Date',
                            value=announcement['date'], inline=True)
            embed.add_field(name='Price Sensitive',
                            value=str(announcement['isPriceSensitive']), inline=True)
            embed.add_field(name='Document URL',
                            value=f"https://cdn-api.markitdigital.com/apiman-gateway/ASX/asx-research/1.0/file/{announcement['documentKey']}?access_token=83ff96335c2d45a094df02a206a39ff4", inline=True)
            webhook.send(embed=embed)
            conn.commit()
        else:
            print("repeat")

conn.close()
