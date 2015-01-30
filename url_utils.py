#!/usr/bin/env python3

import urllib.request


class UrlUtils:
    """
    Utilities to make http request, convert response, get "mess" at end
    """

    def get_response(self, url):
        # response type is bytes
        # https://docs.python.org/3/library/urllib.request.html
        response = urllib.request.urlopen(url).read()
        return response

    def string_from_bytes(self, a_bytes):
        # http://stackoverflow.com/questions/606191/convert-bytes-to-a-python-string
        return a_bytes.decode("utf-8")

    def get_mess_and_trailer(self, content, leader):
        components_split_at_leader = content.split(leader)
        mess_and_trailer = components_split_at_leader[-1]
        return mess_and_trailer

    def get_mess(self, content, leader, trailer):
        mess_and_trailer = self.get_mess_and_trailer(content, leader)
        components_split_at_trailer = mess_and_trailer.split(trailer)
        mess = components_split_at_trailer[-2]
        return mess
