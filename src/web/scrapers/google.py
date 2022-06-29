
#
# The MIT License (MIT)
#
# Copyright (c) 2022 Wonoly
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#

from .template import Scraper
from .utils.google import GOOGLE_URL, GOOGLE_VED, GOOGLE_USERAGENT

from typing import Dict, Any
import requests
import urllib

class Google(Scraper):

    ei: str = ""
    ved: str = ""

    html_result: str = ""

    headers: Dict[str, Any] = {}
    options: Dict[str, Any] = {}

    def __init__(self, options: Dict[str, Any]):
        self.options = options

        self.headers["Pragma"]           = ""
        self.headers["Keep-Alive"]       = "115"
        self.headers["Connection"]       = "keep-alive"
        self.headers["Accept-Encoding"]  = "gzip,deflate"
        self.headers["User-Agent"]       = GOOGLE_USERAGENT
        self.headers["Accept-Language"]  = "en-us,en;q=0.5"
        self.headers["Accept-Charset"]   = "ISO-8859-1,utf-8;q=0.7,*;q=0.7"
        self.headers["Accept"]           = "text/xml,application/xml,application/xhtml+xml,text/html;q=0.9,text/plain;q=0.8,image/png,*/*;q=0.5"

        data = self.get_page_data(GOOGLE_URL);          #    Open google.com ( Might redirect to country specific site e.g. www.google.co.in)
        data = self.get_page_data(f'{GOOGLE_URL}/ncr'); #    Moves back to google.com

        matches = GOOGLE_VED.search(data)

        if matches is not None:
            self.ved = matches[1]

        data = self.get_page_data(
            f'{GOOGLE_URL}/search?source=hp&q='   +
            urllib.parse.quote_plus(options.get("query")) +
            '&ei=' + self.ei + '&aomd=1&btnK=Google+Search&ved='   +
            self.ved + '&start=' + str(options.get("start", 0)))

        self.html_result = self.clean_google(data)

    def get_page_data(self, url: str) -> str:
        return requests.get(url, verify=False, timeout=10, headers=self.headers).text

    def clean_google(self, data):
        return (data
            # Removes classes we don't need:
            .replace("N6jJud MUxGbd lyLwlc", "")
            .replace("YjtGef ExmHv MUxGbd", "")
            .replace("MUxGbd lyLwlc aLF0Z", "")

            # Transforms all possible variations of some classes' name into a
            # fixed string so it's easier to get consistent results:
            # Descriptions: -> MUxGbd yDYNvb
            .replace("yDYNvb lEBKkf", "yDYNvb")
            .replace("VwiC3b MUxGbd yDYNvb", "MUxGbd yDYNvb")

            # Urls: -> C8nzq BmP5tf
            .replace("cz3goc BmP5tf", "C8nzq BmP5tf")

            # Titles: -> yUTMj MBeuO ynAwRc gsrt PpBGzd YcUVQe
            .replace("yUTMj MBeuO ynAwRc PpBGzd YcUVQe", 'yUTMj MBeuO ynAwRc gsrt PpBGzd YcUVQe')
            .replace("oewGkc LeUQr", 'PpBGzd YcUVQe')
            .replace("q8U8x MBeuO", 'yUTMj MBeuO')
            .replace("ynAwRc PpBGzd", 'ynAwRc gsrt PpBGzd'))

    def search(self) -> Dict[str, Dict[str, Any]]:
        print("google crawl")
        return {}
