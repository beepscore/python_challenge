#!/usr/bin/env python3

import codecs


class FileUtils:

    def get_file_string(self, filename):
        """ read contents of file and return a string
        If can't read file or file is empty return None
        """
        # note text_file is a file object, not a string
        text_file = open(filename)
        file_string = text_file.read()
        text_file.close()
        # http://stackoverflow.com/questions/4020539/process-escape-sequences-in-a-string-in-python
        decoded_string = codecs.decode(file_string, 'unicode_escape')
        return decoded_string
