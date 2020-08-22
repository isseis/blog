#! /usr/bin/python3
'''
Tool to publish a draft file in Jekyll.

Usage:
    publish.py -i _drafts/draft_post.md
'''

__author__ = 'Issei Suzuki'
__copyright__ = 'Copyright 2020, Issei Suzuki'
__credits__ = ['Issei Suzuki']
__license__ = 'MIT'
__version__ = '0.0.1'
__status__ = 'Prototype'

import argparse
import os
import re
import sys
import time

verbose = False

def read_draft(name):
    '''Read draft posts.

    Args:
        name:   Path name to the draft markdown file.

    Returns:
        A pair of strings holding front matter and body in string. In case
        'date' is specified in the fton matter, it will be removed.
    '''
    global verbose
    if verbose:
        print('Read draft:', name)

    with open(name, "r") as f:
        # front matter section
        header = []
        s = f.readline()
        if s != '---\n':
            raise ValueError('First line must be "---"')

        # front matter block
        while True:
            s = f.readline()
            if not s:
                raise ValueError('Front matter block is not closed')
            if s == '---\n':
                break
            if re.match(r'date:', s):
                continue
            header.append(s)
        # body
        body = f.read()

    return ''.join(header), body


def get_outfile_path(input_path, publish_time, outdir):
    '''Generate path name for writing the post.

    Args:
        input_path: Path name to the draft markdown file.
        publish_time: Time to publish the article in time.struct_time.
        out_dir: Directory to write published article.
    '''
    return os.path.join(outdir,
            time.strftime("%Y-%m-%d-", publish_time)
            + os.path.basename(input_path))


def publish_article(header, body, publish_time, outfile):
    global verbose
    if verbose:
        print('Write post:', outfile)

    with open(outfile, "w") as f:
        f.write('---\n')
        f.write(header)
        f.write('date:\t')
        f.write(time.strftime('%Y-%m-%d %H:%M:%S %z\n', publish_time))
        f.write('---\n')
        f.write(body)

def main():
    global verbose

    publish_time = time.localtime()

    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', required=True,
            help="draft file name to publish")
    parser.add_argument('-o', '--outdir', default='_posts',
            help='directory to write published article [_posts]')
    parser.add_argument('-v', dest='verbose', action='store_true',
            help="show verbose message")
    args = parser.parse_args()

    # Validate arguments
    verbose = args.verbose

    if re.match(r'\d\d\d\d-\d\d-\d\d-', args.input):
        print('Input file name contains date', '[' + args.input + ']')
        sys.exit(os.EX_USAGE)
    if not re.search(r'\.md$', args.input):
        print('Input file name must end with \'.md\'', '[' + args.input + ']')
        sys.exit(os.EX_USAGE)

    if not os.path.isdir(args.outdir):
        print('Output must be directory', '[' + args.outdir + ']')
        sys.exit(os.EX_USAGE)

    # Do the job!
    header, body = read_draft(args.input)
    outfile = get_outfile_path(args.input, publish_time, args.outdir)
    publish_article(header, body, publish_time, outfile)


if __name__ == "__main__":
    main()
