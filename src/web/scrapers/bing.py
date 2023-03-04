
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
from .utils.bing import BING_URL, BING_USERAGENT, Classes

from bs4 import BeautifulSoup

from typing import Dict, Any
import requests
import urllib

class Bing(Scraper):

    ei: str = ""

    html_result: str = ""

    headers: Dict[str, Any] = {}
    options: Dict[str, Any] = {}

    def __init__(self, options: Dict[str, Any]):
        self.options = options

        self.headers["Pragma"]           = ""
        self.headers["Keep-Alive"]       = "115"
        self.headers["Connection"]       = "keep-alive"
        self.headers["Accept-Encoding"]  = "gzip,deflate"
        self.headers["User-Agent"]       = BING_USERAGENT
        self.headers["Accept-Language"]  = "en-us,en;q=0.5"
        self.headers["Accept-Charset"]   = "ISO-8859-1,utf-8;q=0.7,*;q=0.7"
        self.headers["Accept"]           = "text/xml,application/xml,application/xhtml+xml,text/html;q=0.9,text/plain;q=0.8,image/png,*/*;q=0.5"

        data = self.get_page_data(self.prepare_search_url())
        self.html_result = Classes.clean_bing_page(data)

    def prepare_search_url(self):
        return f"{BING_URL}/search?source=hp&q={urllib.parse.quote_plus(self.options.get('query'))}&ei={self.ei}&aomd=1&btnK=Google+Search&start={str(self.options.get('start', 0))}"

    def get_page_data(self, url: str) -> str:
        return requests.get(url, verify=False, timeout=10, headers=self.headers).text

    def search(self) -> Dict[str, Dict[str, Any]]:
        soup = BeautifulSoup(self.html_result, 'html.parser')
        return dict(
            dym = self._get_dym(soup),
            results = self._get_results(soup),
            lyrics = self._get_lyrics(soup),
            kno = self._get_kno(soup),
        )

    def _get_kno(self, soup: BeautifulSoup) -> str or None:
        return None

    def _get_lyrics(self, soup: BeautifulSoup) -> str:
        lyrics = ""
        for section in soup.select(Classes.lyrics):
            lyrics += section.getText() + "<br/><br/>"

        return lyrics


    def _get_dym(self, soup: BeautifulSoup) -> dict:
        did_you_mean = soup.select(Classes.did_you_mean)

        if len(did_you_mean):
            return dict( text=did_you_mean[0].getText(), html=str(did_you_mean[0]) )

    def _get_results(self, soup: BeautifulSoup) -> dict:
        results      = []

        urls         = []
        titles       = []
        descriptions = []

        _titles = soup.select(Classes.title)
        for title in _titles:
            if title.style != "-webkit-line-clamp:2":
                titles.append(title.getText())
                urls.append(title.get("href"))

        _descriptions = soup.select(Classes.description)
        for description in _descriptions:
            descriptions.append(str(description))

        urls_len = len(urls)
        titles_len = len(titles)
        descriptions_len = len(descriptions)

        if ((titles_len < urls_len and titles_len < descriptions_len)
            or (urls_len > titles_len)):
            del urls[0]

        urls_len = len(urls)
        inacurate = descriptions_len > len(urls[1:])

        index = 0
        for url in urls:
            if url == "youtube.com" and inacurate and urls_len > 1:
                del url[index]
                del titles[index]

                index -= 1

            index += 1

        for i in range(len(titles)):
            parsed_url = urllib.parse.urlparse(urls[i])

            try:
                results.append(dict(
                    title = titles[i],
                    description = descriptions[i],
                    url = urls[i],
                    host = parsed_url.netloc,
                ))
            except IndexError:
                pass

        return results

