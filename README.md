# sendbird-python
Python wrapper for the SendBird API, built via Stripe code standards.

## SendBird? What is SendBird?

SendBird (YC W16) is a company that provides a powerful and flexible chat API that enables companies to launch chat features within their mobile and web applications with minimum effort and maximum effect. 

For more information, check out the [SendBird](http://sendbird.com?source=https://github.com/jpbullalayao/sendbird-python) home page.


## Usage

```python

import sendbird
sendbird.api_token = "..."

# Create open channel
sendbird.OpenChannel.create(name='Name of Channel', channel_url='name-of-channel')

# Retrieve open channel
channel = sendbird.OpenChannel.retrieve('name-of-channel')

# Update a channel
channel.update(name="New Name")

# List open channels
sendbird.OpenChannel.list()
```


## Author's Note
Interested in the progress of this project? Feel free to follow the repo for live updates! 

If you need to get a hold of me regarding this project, feel free to either:
- email me at me@jourdanb.com
- tweet me @professorragna
