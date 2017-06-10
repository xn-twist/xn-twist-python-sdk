#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Python SDK for XN-Twist's API."""

import json

import requests


class xnTwist(object):
    """Class for communicating with the XN-Twist API."""

    def __init__(self):
        self.api_path = "http://miceandmen.tk:5000/"

    def _make_get_request(self, url):
        """Make and handle a ``GET`` request to the given url."""
        response = requests.get(url)

        if response.ok:
            return json.loads(response.text)
        else:
            raise RuntimeWarning("Error response from {}".format(url))

    def retrieve_dataset(self):
        """Pull data from the ``/mappings`` branch and format it for use with
        the xn-twist algorithm."""
        dataset = {}

        # make a request to the ``mappings`` branch
        r = self.get_mappings()

        # iterate through each of the mappings
        for mapping in r['_items']:
            # if the character is not in the dataset, create a new entry
            if mapping['character'] not in dataset.keys():
                dataset[mapping['character']] = list()

            # add each potential spoof of the current character to the dataset
            for potential_spoof in mapping['potential_spoofs']:
                dataset[mapping['character']].append(
                    potential_spoof['spoof_character'])

        return dataset

    def get_base(self):
        """Make ``GET`` request to the base api branch (``/``)."""
        return self._make_get_request(self.api_path)

    def get_administrators(self):
        """
        Make ``GET`` request to branch with admin users (``/administrators``).
        """
        return self._make_get_request(self.api_path + "administrators")

    def get_feed(self):
        """
        Make ``GET`` request to branch with recently classified characters
        (``/feed``).
        """
        return self._make_get_request(self.api_path + "feed")

    def get_mappings(self):
        """
        Make ``GET`` request to branch with character mappings (``/mappings``).
        """
        return self._make_get_request(self.api_path + "mappings")

    def get_non_basic_chars(self):
        """
        Make ``GET`` request to branch with the list of non-basic characters
        that may be used to spoof latin characters (``/non_basic_characters``).
        """
        return self._make_get_request(self.api_path + "non_basic_characters")

    def get_unmapped_chars(self):
        """
        Make ``GET`` request to branch with list of non-basic characters that
        have not been mapped to any basic characters
        (``/unmapped_characters``).
        """
        return self._make_get_request(self.api_path + "unmapped_characters")

    def get_basic_chars(self):
        """
        Make ``GET`` request to branch with basic characters
        (``/basic_characters``).
        """
        return self._make_get_request(self.api_path + "basic_characters")

    def get_suggested_deprecations(self):
        """
        Make ``GET`` request to branch with non-basic characters that have
        been suggested for deprecation (``/suggested_deprecations``).
        """
        return self._make_get_request(self.api_path + "suggested_deprecations")

    def get_depricated_chars(self):
        """
        Make ``GET`` request to branch with the non-basic characters that have
        been deprecated (``/depricated_characters``).
        """
        return self._make_get_request(self.api_path + "depricated_characters")
