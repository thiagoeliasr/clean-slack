# Clean Slack

This is a simple Python3 script which uses [slack_cleaner2](https://github.com/sgratzl/slack_cleaner2).

## Install

Install requirements from *requirements.txt* with pip

```
pip install -r requirements.txt
```

Set the SLACK_TOKEN in your environment.

If you're using Linux:

```
export SLACK_TOKEN=<your token here>
```

## Usage:

```
python clean.py <channel-1> <channel-2> <channel-n>
```

### Example:


```
python clean.py .*-bot full-channel-name errors-.*
```

