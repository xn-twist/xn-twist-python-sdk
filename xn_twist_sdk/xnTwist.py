#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Python SDK for XN-Twist's API."""

import json

import requests


class xnTwist(object):
    """Class for communicating with the XN-Twist API."""

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
        """Make ``GET`` request to the base api branch (``/``)."""
        return self.make_request(self.api_path)

    def get_administrators(self):
        """
        Make ``GET`` request to branch with admin users (``/administrators``).
        """
        return self.make_request(self.api_path + "administrators")

    def get_feed(self):
        """
        Make ``GET`` request to branch with recently classified characters
        (``/feed``).
        """
        return self.make_request(self.api_path + "feed")

    def get_mappings(self):
        """
        Make ``GET`` request to branch with character mappings (``/mappings``).
        """
        return self.make_request(self.api_path + "mappings")

    def get_non_basic_chars(self):
        """
        Make ``GET`` request to branch with the list of non-basic characters
        that may be used to spoof latin characters (``/non_basic_characters``).
        """
        return self.make_request(self.api_path + "non_basic_characters")

    def get_unmapped_chars(self):
        """
        Make ``GET`` request to branch with list of non-basic characters that
        have not been mapped to any basic characters
        (``/unmapped_characters``).
        """
        return self.make_request(self.api_path + "unmapped_characters")

    def get_basic_chars(self):
        """
        Make ``GET`` request to branch with basic characters
        (``/basic_characters``).
        """
        return self.make_request(self.api_path + "basic_characters")

    def get_suggested_deprecations(self):
        """
        Make ``GET`` request to branch with non-basic characters that have
        been suggested for deprecation (``/suggested_deprecations``).
        """
        return self.make_request(self.api_path + "suggested_deprecations")

    def get_depricated_chars(self):
        """
        Make ``GET`` request to branch with the non-basic characters that have
        been deprecated (``/depricated_characters``).
        """
        return self.make_request(self.api_path + "depricated_characters")
