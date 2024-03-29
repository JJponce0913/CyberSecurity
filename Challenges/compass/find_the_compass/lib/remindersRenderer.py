#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Python Version    : 3.11
# Author           : Mika - @bWlrYQ

from html import escape

class Renderer(object):
    """
    Proof of Concept to one day get rid of Jinja2. Who needs Jinja2 ?
    """
    def __init__(self, coordinates: str):
        # Only a wise administrator can retrieve the coordinates of the compass.
        self.coordinates = coordinates

    def render(self, author, content):
        author = escape(author)
        # content = escape(content)  # We're not using the content variable anymore
        htmlTemplate = "<p><strong>{}</strong>: {}</p>".format(author, self.coordinates)
        try:
            # Use escape for XSS protection
            return htmlTemplate
        except Exception as e:
            print(e)
            return "An error occurred while rendering the reminder."
