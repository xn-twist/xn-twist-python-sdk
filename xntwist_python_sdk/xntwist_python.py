#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Python SDK for XN-Twist's API."""

try:
    import ConfigParser
except:
    import configparser as ConfigParser
import sys

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
        r = self.get_branch('mappings')

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

    def get_branch(self, api_branch=None):
        """Make ``GET`` request to the given api branch."""
        if api_branch == None:
            return self.requester.make_get_request(self.api_path)
        else:
            return self.requester.make_get_request(self.api_path + api_branch)

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

    def delete_item(self, item_json, api_branch):
        """
        Make ``DELETE`` request to delete the given item from the given api branch.
        """
        # find the id and etag
        item_id = item_json['_id']
        item_etag = item_json['_etag']

        header = {
            'If-Match': item_etag
        }

        return self.requester.make_delete_request(self.api_path + api_branch +
                                                  "/{}".format(item_id),
                                                  self.auth, header)
