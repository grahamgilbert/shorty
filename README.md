# Shorty

Shorty is a statically generated URL shortener. It is suggested that this is combined with something like S3 and CloudFront and a CI tool to deploy it. It supports sending analytics to Google.

## Usage

``` bash
python3 shorty.py \
    --config=/config.json \
    --output=/tmp/output/site \
    --google-analytics='GA-ABC12343-Y'
```

### Config file format

``` json
[
    {
        "stub": "",
        "url": "https://grahamgilbert.com/"
    },
    {
        "stub": "blog",
        "url": "https://grahamgilbert.com"
    },
    {
        "stub": "crypt",
        "url": "https://github.com/grahamgilbert/crypt"
    }
]
```

Use an empty string for `stub` to redirect the site root (`/`). If no root entry is
configured, Shorty uses the default index page. Root redirects use the same
template and optional analytics as other redirects.

## Development

Use the Python version series in `.python-version`. CI selects the latest stable
patch release in that series. Shorty has no third-party runtime dependencies.
Install the pinned lint dependencies before running the checks:

``` bash
python3 -m venv venv
. venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements-dev.txt
./test.sh
```
