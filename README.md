# Shorty

Shorty is a statically generated URL shortener. It is suggested that this is combined with something like S3 and CloudFront and a CI tool to deploy it. It supports sending analytics to Google.

## Usage

It is suggested that this is run via the Docker image, but it's only dependency is Python 3.

``` bash
docker run --rm -ti \
    -v `pwd`/output:/tmp/output \
    -v `pwd`/config.json:/config.json \
    grahamgilbert/shorty:latest /usr/local/bin/shorty \
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
