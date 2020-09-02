#! /usr/bin/python3
"""
Tool to check if any of added files contains Geo tag.

By default, this tool runs git command to find added files. For testing
purpose, you can explictly give file names to check.

If any of the files contain Geo tag, this script exits with an error,
i.e. exit code != 0

External dependency:
    git
    exiftool
"""

__author__ = 'Issei Suzuki'
__copyright__ = 'Copyright 2020, Issei Suzuki'
__credits__ = ['Issei Suzuki']
__license__ = 'MIT'
__version__ = '0.0.2'
__status__ = 'Prototype'

import argparse
import re
import subprocess
from typing import Any
from typing import Iterator
from typing import Optional
from typing import Sequence

verbose = 0

class CalledProcessError(RuntimeError):
    pass


def cmd_output(*cmd: str, retcode: Optional[int] = 0, **kwargs: Any) -> str:
    if verbose > 1:
        print(' cmd:', cmd);
    kwargs.setdefault('stdout', subprocess.PIPE)
    kwargs.setdefault('stderr', subprocess.PIPE)
    proc = subprocess.Popen(cmd, **kwargs)
    stdout, stderr = proc.communicate()
    stdout = stdout.decode()
    if retcode is not None and proc.returncode != retcode:
        raise CalledProcessError(cmd, retcode, proc.returncode, stdout, stderr)
    return stdout


def git_added_files() -> Sequence[str]:
    cmd = ('git', 'diff', '--staged', '--name-only', '--diff-filter=A')
    files = cmd_output(*cmd).splitlines()
    if verbose > 0:
        print('git_added_files:')
        print('\t' + '\n\t'.join(files))
    return files


def is_geotagged(filename: str) -> bool:
    """
    Check if the file contains Geo tag.

    Returns:
        bool: True if the given file contains Geo tag, False otherwise.

    Args:
        filename: Path to the file.

    Raises:
        CalledProcessError: Failed to execute exiftool to retrive EXIF information
            of the given file.
    """
    cmd = ('exiftool', filename)
    for s in cmd_output(*cmd).splitlines():
        if re.match('GPS ', s):
            return True
    return False


def is_jpeg_file(filename: str) -> bool:
    f = filename.lower()
    return f.endswith('.jpg') or f.endswith('.jpeg')


def filter_jpeg_files(filenames: Iterator[str]) -> Iterator[str]:
    return filter(is_jpeg_file, filenames)


def find_geotagged_files(filenames: Iterator[str]) -> Iterator[str]:
    jpeg_files = list(filter_jpeg_files(filenames))
    if verbose > 0:
        print('Test targets (filtered):')
        print('\t' + '\n\t'.join(jpeg_files))
    return filter(is_geotagged, jpeg_files)


def main(argv: Optional[Sequence[str]] = None) -> int:
    global verbose

    parser = argparse.ArgumentParser()
    parser.add_argument(
        'filenames', nargs='*',
        help='Filenames pre-commit believes are changed.',
    )
    parser.add_argument('--verbose', '-v', action='count', default=0,
        help='Output verbose message.')
    args = parser.parse_args(argv)
    verbose = args.verbose
    filenames = args.filenames[:]
    if len(filenames) == 0:
        filenames += git_added_files()
    if verbose > 0:
        print('Test targets (raw):')
        print('\t' + '\n\t'.join(filenames))

    geotaggled_files = list(find_geotagged_files(filenames))
    if len(geotaggled_files) == 0:
        return 0

    print('Found files containing Geo tag:')
    print('\t' + '\n\t'.join(geotaggled_files))
    return 1


if __name__ == '__main__':
    exit(main())
