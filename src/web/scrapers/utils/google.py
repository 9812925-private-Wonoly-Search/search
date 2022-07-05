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

GOOGLE_URL = "http://www.google.com"
GOOGLE_VED = re.compile('/type="submit" data-ved="(.*?)"/')
GOOGLE_USERAGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"

class Classes:
    """A class for tracking obfuscated class names used in Google results that
    are directly referenced in Whoogle's filtering code."""

    title = "div.v7W49e div a h3"
    description = "div.lyLwlc"

    lyrics = 'div.ujudUb'
    did_you_mean = "a.gL9Hy"

    kno_panel = dict(
        url = 'div[class="kno-rdesc"] span a',
        type = 'div.SPZz6b div span',
        metadata = 'div.rVusze',
        title = ['div.BkwXh div', 'div.SPZz6b h2 span'],
        description = 'div[class="kno-rdesc"] span',
    )

    @staticmethod
    def clean_google_page(html: str) -> str:
        return (html
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
