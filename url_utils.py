#!/usr/bin/env python3

import urllib.request


class UrlUtils:
    """
    Utilities to make http request, convert response, get "mess" at end
    """

    def get_response(url):
        # response type is bytes
        # https://docs.python.org/3/library/urllib.request.html
        response = urllib.request.urlopen(url).read()
        return response

    def string_from_bytes(a_bytes):
        # http://stackoverflow.com/questions/606191/convert-bytes-to-a-python-string
        return a_bytes.decode("utf-8")

    def get_mess_and_trailer(content, leader):
        components_split_at_leader = content.split(leader)
        mess_and_trailer = components_split_at_leader[-1]
        return mess_and_trailer

    def get_mess(content, leader, trailer):
        mess_and_trailer = UrlUtils.get_mess_and_trailer(content, leader)
        components_split_at_trailer = mess_and_trailer.split(trailer)
        mess = components_split_at_trailer[-2]
        return mess

    def get_url_from_answer_string(a_string):
        """ this method url encodes a_string to replace space with +
        http://stackoverflow.com/questions/1211229/in-a-url-should-spaces-be-encoded-using-20-or
        http://stackoverflow.com/questions/1634271/url-encoding-the-space-character-or-20
        http://stackoverflow.com/questions/1005676/urls-and-plus-signs
        """
        base_url = "http://www.pythonchallenge.com/pc/def/"
        end_url = urllib.parse.quote_plus(a_string) + ".html"
        url = urllib.parse.urljoin(base_url, end_url)
        return url
