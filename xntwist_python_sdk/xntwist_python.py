#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Python SDK for XN-Twist's API."""

import argparse
try:
    import ConfigParser
except:
    import configparser as ConfigParser
import json

import requests
from requests.auth import HTTPBasicAuth

from .utility import Requester


def _read_config_file(config_file_path):
    """Read the credentials from the given config file."""
    config = ConfigParser.RawConfigParser()
    config.read(config_file_path)

    try:
        username = config.get('xn-twist', 'username')
        password = config.get('xn-twist', 'password')
    except ConfigParser.NoOptionError:
        print('Could not read configuration file.')
        sys.exit(1)
    else:
        return username, password


class XnTwistSDK(object):
    """Class for communicating with the XN-Twist API."""

    def __init__(self, config_file_path=None):
        """."""
        self.api_path = "http://xntwist.tk:5000/"
        # initialize a Requester object
        self.requester = Requester()
        # set the path to the config file (if any)
        self.config_file_path = config_file_path

        if self.config_file_path is not None:
            username, password = _read_config_file(config_file_path)
            self.auth = HTTPBasicAuth(username, password)

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
        return self.requester.make_get_request(self.api_path)

    def get_administrators(self):
        """
        Make ``GET`` request to branch with admin users (``/administrators``).
        """
        return self.requester.make_get_request(self.api_path + "administrators")

    def get_feed(self):
        """
        Make ``GET`` request to branch with recently classified characters
        (``/feed``).
        """
        return self.requester.make_get_request(self.api_path + "feed")

    def get_mappings(self):
        """
        Make ``GET`` request to branch with character mappings (``/mappings``).
        """
        return self.requester.make_get_request(self.api_path + "mappings")

    def get_non_basic_chars(self):
        """
        Make ``GET`` request to branch with the list of non-basic characters
        that may be used to spoof latin characters (``/non_basic_characters``).
        """
        return self.requester.make_get_request(self.api_path + "non_basic_characters")

    def get_unmapped_chars(self):
        """
        Make ``GET`` request to branch with list of non-basic characters that
        have not been mapped to any basic characters
        (``/unmapped_characters``).
        """
        return self.requester.make_get_request(self.api_path + "unmapped_characters")

    def get_basic_chars(self):
        """
        Make ``GET`` request to branch with basic characters
        (``/basic_characters``).
        """
        return self.requester.make_get_request(self.api_path + "basic_characters")

    def get_suggested_deprecations(self):
        """
        Make ``GET`` request to branch with non-basic characters that have
        been suggested for deprecation (``/suggested_deprecations``).
        """
        return self.requester.make_get_request(self.api_path + "suggested_deprecations")

    def get_depricated_chars(self):
        """
        Make ``GET`` request to branch with the non-basic characters that have
        been deprecated (``/depricated_characters``).
        """
        return self.requester.make_get_request(self.api_path + "depricated_characters")

    def add_new_mapping(self, data):
        """
        Make ``POST`` request to mappings branch (``/mappings``).
        """
        return self.requester.make_post_request(self.api_path + "mappings",
                                                self.auth, data)

    def update_existing_mapping(self, item_json, new_data):
        """
        Make ``PUT`` request to mappings branch (``/mappings``) to modify an existing mapping.
        """
        # find the id and etag
        item_id = item_json['_id']
        item_etag = item_json['_etag']

        header = {
            'If-Match': item_etag
        }

        return self.requester.make_put_request(self.api_path + "mappings" +
                                               "/{}".format(item_id),
                                               self.auth, header, new_data)

    def delete_feed_item(self, item_json):
        """
        Make ``POST`` request to mappings branch (``/mappings``).
        """
        # find the id and etag
        item_id = item_json['_id']
        item_etag = item_json['_etag']

        header = {
            'If-Match': item_etag
        }

        return self.requester.make_delete_request(self.api_path + "mappings" +
                                                  "/{}".format(item_id),
                                                  self.auth, header)
