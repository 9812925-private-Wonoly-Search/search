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

import re

BING_URL = "http://www.bing.com"
BING_USERAGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"

class Classes:
    """A class for tracking obfuscated class names used in Google results that
    are directly referenced in Whoogle's filtering code."""

    title = "#b_results > li.b_algo > h2 > a"
    description = "#b_results > li.b_algo > div.b_caption > p.b_algoSlug"

    lyrics = 'div.ujudUb'
    did_you_mean = "a.gL9Hy"

    kno_panel = dict(
        url = 'div[class="kno-rdesc"] span a',
        type = 'div.SPZz6b div span',
        metadata = 'div.rVusze',
        title = ['TODO'],
        description = 'TODO',
    )

    @staticmethod
    def clean_bing_page(page: str) -> str:
        return (page
            .replace("<span class=\"algoSlug_icon\"", "<span class=\"wonolySearchResultIcon\""))
