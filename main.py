from six.moves import urllib
from subprocess import Popen
import os
import sys

try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO

# A boolean flag to allow printer testing.
allow_print_sample = False

# A test pdf to test printer
print_sample = 'http://unec.edu.az/application/uploads/2014/12/pdf-sample.pdf'

# The supported formats
formats = ['pdf',
           'txt',
           'csv']


def print_file(file, remove):
    """
    Prints a file at a certain path.

    :param file: The path of the file.
    :param remove: Should the file be deleted after printing.
    """
    # call the system's lpr command
    p = Popen(["lpr -#1 " + file], shell=True)
    output = p.communicate()[0]
    print(output)

    if remove:
        # delete file
        os.remove(file)


def get_file(path_or_url, type_):
    """
    :param path_or_url: The path of the file or the url.
    :param type_: The file format.
    :return: tuple containing the path to file and a boolean value
             indicating if the file should be deleted or not.
    """
    if path_or_url.startswith('http'):
        if connection_test(path_or_url):
            file = 'temp.' + type_
            urllib.request.urlretrieve(url_to_pdf, file)
            return file, True
        else:
            return None, False
    else:
        return os.path.abspath(path_or_url), False


def validate_file(file):
    """
    Checks if a given file is of a certain format and returns true if it is and which format it is.
    :param file: The file which we are validating.
    :return: isValid (boolean), format (string)
    """
    for format_ in formats:
        if file.endswith('.' + format_):
            return True, format_

    return False, None


def connection_test(url):
    """
    Check if we can reach a url

    :param url: The url to test
    :return: True if successfully connected to the url.
    """
    try:
        urllib.urlopen(url, timeout=1)
        return True
    except urllib.URLError as err:
        return False


if __name__ == '__main__':
    # check if there was an argument passed down
    if len(sys.argv) >= 2:
        url_to_pdf = sys.argv[1]
    # else check if sample printing is allowed
    elif allow_print_sample:
        url_to_pdf = print_sample
    # else do nothing
    else:
        url_to_pdf = ""
        print('Nothing to print!')
        sys.exit(0)

    # validate file format
    validation = validate_file(url_to_pdf)
    if validation[0]:
        data = get_file(url_to_pdf, validation[1])

        if data[0] is not None:
            print_file(data[0], data[1])
        else:
            print('Failed to connect to '+url_to_pdf)
    else:
        print('Invalid file!')
