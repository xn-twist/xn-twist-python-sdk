#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Python SDK for xn-twist's API."""

import json

import requests


class xnTwist(object):
    """Class for communicating with the xn-twist API."""

    def __init__(self):
        self.api_path = "http://miceandmen.tk:5000/"

    def make_request(self, url):
        """Make and handle a request to the given branch."""
        response = requests.get(url)

        if response.ok:
            return json.loads(response.text)
        else:
            raise RuntimeWarning("Error response from {}".format(url))

    def get_base(self):
        return self.make_request(self.api_path)

    def get_administrators(self):
        return self.make_request(self.api_path + "administrators")

    def get_feed(self):
        return self.make_request(self.api_path + "feed")

    def get_mappings(self):
        return self.make_request(self.api_path + "mappings")

    def get_non_basic_chars(self):
        return self.make_request(self.api_path + "non_basic_characters")

    def get_unmapped_chars(self):
        return self.make_request(self.api_path + "unmapped_characters")

    def get_basic_chars(self):
        return self.make_request(self.api_path + "basic_characters")

    def get_suggested_deprecations(self):
        return self.make_request(self.api_path + "suggested_deprecations")

    def get_depricated_chars(self):
        return self.make_request(self.api_path + "depricated_characters")
