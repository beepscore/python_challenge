#!/usr/bin/env python3

import file_utils
import url_utils


class Puzzle6:
    """
    test_puzzle5.py explains puzzle6 starting url

    http://www.pythonchallenge.com/pc/def/channel.html

    page shows a partially zipped/unzipped zipper
    html has a comment?
    <html> <!-- <-- zip -->
    http://www.htmlhelp.com/reference/wilbur/misc/comment.html
    Is this a deliberately malformed comment?
    Is zip file somehow hidden or embedded in html or jpg?
    No, wrong approach.

    Page source tile "now there are pairs"
    Unzip something?

    http://www.pythonchallenge.com/pc/def/zip.html
    Says "yes. find the zip".
    I saved web page to get associated files.
    I don't see anything in style.css

    looked for a hint
    http://www.intelligentgeek.com/home/blog/pythonchallenge6

    downloaded
    http://www.pythonchallenge.com/pc/def/channel.zip
    then expanded manually, could do it programmatically.
    """

    def __init__(self):
        self.puzzle_url = "http://www.pythonchallenge.com/pc/def/channel.html"
        self.zip_url = "http://www.pythonchallenge.com/pc/def/channel.zip"
        self.url_utils = url_utils.UrlUtils()

    def download_and_write_zip(self):
        response_bytes = self.url_utils.get_response(self.zip_url)
        filename = "./test/channel.zip"
        file_utils.FileUtils().write_bytes_to_filename(response_bytes,
                                                       filename)
