import requests

# Get series information for KXHIGHNY
#url = "https://api.elections.kalshi.com/trade-api/v2/series/KXHIGHNY"
url = "https://api.elections.kalshi.com/trade-api/v2/markets?series_ticker=KXNBAGAME"
response = requests.get(url)
series_data = response.json()


# Get all past markets for the NBA Games series
markets_url = f"https://external-api.kalshi.com/trade-api/v2/markets?series_ticker=KXNBAGAME"
markets_response = requests.get(markets_url)
markets_data = markets_response.json()

# Get event information for the NBA Games series
event_ticker = markets_data['markets'][0]['event_ticker']
event_url = f"https://external-api.kalshi.com/trade-api/v2/events?series_ticker=KXNBAGAME"
event_response = requests.get(event_url)
event_data = event_response.json()
event_titles = []


# Output all outcomes of games that have been played: Indiana wins, Los Angeles wins, etc.
for i in range(0, len(markets_data['markets'])):
    market = markets_data['markets'][i]
    print()
    print(f"- {market['ticker']}: {market['title']}")
    print(f"  Event: {event_data['events'][i]['title']}")
    print(f"  Yes Price: ${market['yes_bid_dollars']} | Volume: {market['volume_fp']}")
    print()
    

"""
# Get details for a specific event if you have its ticker

if markets_data['markets']:
    
    # Let's get details for the first market's event

    print(f"Event Details:")
    print(f"Title: {event_data['event']['title']}")
    print(f"Category: {event_data['event']['category']}")
    pass
"""
