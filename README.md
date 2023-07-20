# sendbird-python
Python wrapper for the SendBird API

## SendBird? What is SendBird?

SendBird (YC W16) is a company that provides a powerful and flexible chat API that enables companies to launch chat features within their mobile and web applications with minimum effort and maximum effect. 

For more information, check out the [SendBird](http://sendbird.com?source=https://github.com/jpbullalayao/sendbird-python) home page.

## Usage

```python

import sendbird
sendbird.api_token = "..."

# Create open channel
sendbird.OpenChannel.create(name='Name of Channel', channel_url='name_of_channel')

# Retrieve open channel
channel = sendbird.OpenChannel.retrieve('name-of-channel')

# Update a channel
channel.update(name="New Name")

# List open channels
sendbird.OpenChannel.list()

# Delete open channel
channel.delete()
```

The full list of resources that are available via the `sendbird` prefix are as follows:
```
GroupChannel
OpenChannel
User
```

Find more usage documentation at our [wiki](https://github.com/jpbullalayao/sendbird-python/wiki). Note, the documentation is still a work in progress!

## Setup

You will need the `pip`, and the `requests` library installed on your machine in order to develop locally. One way to do this is to install a virtual environment that contains your `requests` package. To do this, see the instructions below. This assumes that you already have `pip` installed.

```
$ pip install --user virtualenv
$ cd sendbird-python
$ python -m venv sendbird-python
$ source env/bin/activate
$ pip install requests
```

## Author's Note
Interested in the progress of this project? Feel free to follow the repo for live updates! 

If you need to get a hold of me regarding this project, feel free to either:
- email me at me@jourdanb.com
- tweet me @professorragna
