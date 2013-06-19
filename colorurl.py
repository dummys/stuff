# -*- coding: utf-8 -*-

#
#    colorurl.py - Color url in weechat
#    Copyright (C) 2013 dummys  - http://www.twitter.com/dummys1337
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

SCRIPT_NAME = 'colorurl'
SCRIPT_AUTHOR = 'dummys <dummys1337@gmail.com>'
SCRIPT_VERSION = '1'
SCRIPT_LICENSE = 'GPL'
SCRIPT_DESC = 'Colorize url in weechat'

try:
    import weechat

except ImportError:
    print('This script must be run under WeeChat.')
    print('Get WeeChat now at: http://www.weechat.org/')

try:
    import re

except ImportError as message:
    print('Missing package(s) for %s: %s' % (SCRIPT_NAME, message))

# Default settings for the plugin.
# You can set it dynamically with /set plugins.var.python.colorurl.color [yourcolor]
defaults = {'color': 'lightgreen'}


def is_valid_url(url):
    """
    Used to detect if there is an url in the message. Return a list of urls.
    """
    regex = re.compile(
        r'https?://\S+', re.IGNORECASE)
    return url is not None and regex.findall(url)


def modifier_url(data, modifier, modifier_data, string):
    """
    Function to rewrite the url in color.
    """
    urlz = is_valid_url(string)
    if urlz:
        text = ' '.join(urlz)
        colorz = weechat.color(weechat.config_get_plugin('color'))
        string = string.replace(text, '%s%s%s' % (colorz, text, weechat.color('reset')))
    return '%s' % string


if __name__ == "__main__":
    weechat.register(SCRIPT_NAME, SCRIPT_AUTHOR, SCRIPT_VERSION, SCRIPT_LICENSE, SCRIPT_DESC, "", "")

    for k, v in defaults.iteritems():
        if not weechat.config_is_set_plugin(k):
            weechat.config_set_plugin(k, v)

    weechat.hook_modifier('weechat_print', 'modifier_url', '')
