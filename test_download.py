import unittest
from unittest import mock

import io
import sys
import urllib.request as request

BUFF_SIZE = 1024


def download_length(response, output, length):
    times = length // BUFF_SIZE
    if length % BUFF_SIZE > 0:
        times += 1
    for time in range(times):
        output.write(response.read(BUFF_SIZE))
        print("Download %d" % (((time * BUFF_SIZE)/length) * 100))


def download(response, output):
    total_downloaded = 0
    while True:
        data = response.read(BUFF_SIZE)
        total_downloaded += len(data)
        if not data:
            break
        output.write(data)
        print("Downloaded {bytes}".format(bytes=total_downloaded))

class DownloadTest(unittest.TestCase):
    def test_download_with_known_length(self):
        response = mock.MagicMock()
        response.read = mock.MagicMock(side_effect=['Data']*2)

        output = mock.MagicMock()
        download_length(response, output, 1025)

        calls = [mock.call(BUFF_SIZE), mock.call(BUFF_SIZE)]

        response.read.assert_has_calls(calls)

        calls = [mock.call('Data'), mock.call('Data')]

        output.write.assert_has_calls(calls)

    def test_download_with_no_length(self):
        response = mock.MagicMock()
        response.read = mock.MagicMock(side_effect=['data', 'more data', ''])

        output = mock.MagicMock()
        output.write = mock.MagicMock()

        download(response, output)

        calls = [mock.call(BUFF_SIZE), mock.call(BUFF_SIZE), mock.call(BUFF_SIZE)]

        response.read.assert_has_calls(calls)

        calls = [mock.call('data'), mock.call('more data')]

        output.write.assert_has_calls(calls)
