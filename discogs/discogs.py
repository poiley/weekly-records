import os
import discogs_client

KEY_AUTH    = os.environ['DISCOGS_AUTH']
KEY_SECRET  = os.environ['DISCOGS_SECRET']

client = discogs_client.Client('weekly/0.1')

client.set_consumer_key(KEY_AUTH, KEY_SECRET)

authorize_url = client.get_authorize_url()