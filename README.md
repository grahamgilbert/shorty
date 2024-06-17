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
        "stub": "blog",
        "url": "https://grahamgilbert.com"
    },
    {
        "stub": "crypt",
        "url": "https://github.com/grahamgilbert/crypt"
    }
]
```
