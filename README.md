# Slack Job Crawler

This repository intended to crawl job postings from DataTalks.club and post into static website

## Prequsities

In a simple terms, app will only be able to view messages that are sent to #jobs channel. 

To be able to read messages from the channel we will need following permissions
* **channels:read** -> This scope lets your app retrieve a list of all the public channels in a workspace so that we can pick one to retrieve a message from.
* **channels:history** -> This scope lets your app view all the messages within any public channel in a workspace.

