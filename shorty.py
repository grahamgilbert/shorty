#!/usr/bin/python3
"""
This will take an input json file and produce a static site full of redirections
"""
import json
import os
import sys
import argparse
import shutil


def load_config(config):
    """
    Loads a json file and returns it
    """
    try:
        return json.load(open(config))
    except Exception as e:
        print(e)
        sys.exit(1)


def ensure_dir(output):
    """
    Creates a directory if it does not exist
    """
    if os.path.exists(output):
        shutil.rmtree(output, ignore_errors=True)

    if os.path.exists(output):
        os.removedirs(output)

    os.makedirs(output)


def build_redirect_item(item, template_string, temp_directory):
    """
    Makes a directory and an index.html file with the redirect code in.
    """
    if 'stub' not in item:
        print('Item does not have a stub - exiting')
        sys.exit(1)
    if 'url' not in item:
        print('Item does not have a url - exiting')
        sys.exit(1)

    stub_dir = os.path.join(temp_directory, item['stub'])
    os.makedirs(stub_dir)
    template_string = template_string.replace('THEURL', item['url'])
    with open(os.path.join(stub_dir, 'index.html'), 'w') as html:
        html.write(template_string)


def generate_html(config, output, googleanalytics):
    """
    Builds the html
    """
    template_dir = '/opt/shorty/templates'
    ensure_dir(output)
    if googleanalytics:
        template = os.path.join(template_dir, 'with_google.html')
    else:
        template = os.path.join(template_dir, 'no_google.html')

    with open(template, 'r') as template_file:
        template_string = template_file.read()

    if googleanalytics:
        template_string = template_string.replace('GOOGLEID', googleanalytics)

    for item in config:
        build_redirect_item(item, template_string, output)

    index_in = os.path.join(template_dir, 'index.html')
    index_out = os.path.join(output, 'index.html')

    shutil.copyfile(index_in, index_out)


def main():

    googleanalytics = None

    parser = argparse.ArgumentParser(prog='Shorty',
                                     description='This script will build a static '
                                     'site with javascript redirections.')
    parser.add_argument(
        '-c', '--config', help='Path to your config file. Required.')
    parser.add_argument('-o', '--output', help='Path to output site to. Defaults to '
                        'current working directory.', default=os.getcwd())
    parser.add_argument('-g', '--google-analytics', help='ID for a Google Analytics account '
                        'for tracking. Optional.',
                        default=googleanalytics)
    if len(sys.argv) < 2:
        parser.print_help()
        sys.exit(1)
    args = parser.parse_args()
    config = args.config
    googleanalytics = args.google_analytics
    output = args.output

    parsed_config = load_config(config)
    generate_html(parsed_config, output, googleanalytics)


if __name__ == '__main__':
    main()
