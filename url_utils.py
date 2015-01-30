#!/usr/bin/env python3

import urllib.request


class UrlUtils:
    """
    Utilities to make http request and convert response
    """

    def get_response(self, url):
        # response type is bytes
        # https://docs.python.org/3/library/urllib.request.html
        response = urllib.request.urlopen(url).read()
        return response

    def string_from_bytes(self, a_bytes):
        # http://stackoverflow.com/questions/606191/convert-bytes-to-a-python-string
        return a_bytes.decode("utf-8")
