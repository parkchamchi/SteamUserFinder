# Steam User Finder
Crawls the `steamcommunity.com` and fetch the list of users using the username.

## Usage
```
python steamuserfinder.py "example username" -e -w
```

```
usage: steamuserfinder.py [-h] [-e] [-w] username

positional arguments:
  username

optional arguments:
  -h, --help        show this help message and exit
  -e, --exact       Return accounts whose usernames exactly match (on the stdout)
  -w, --write_html  Write the HTML file on the output/
```

With `-w`, an HTML file is generated in `output/`.

## Limitations
- This only fetches the first 10,000 users (500 pages) of the query results.