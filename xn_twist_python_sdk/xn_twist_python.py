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
        self.api_path = "https://xntwist.hightower.space:2053/"
        # initialize a Requester object
        self.requester = Requester()
        # set the path to the config file (if any)
        self.config_file_path = config_file_path

        if self.config_file_path is not None:
            username, password = _read_config_file(config_file_path)
            self.auth = HTTPBasicAuth(username, password)

    def retrieve_dataset(self, limit=10):
        """Pull data from the ``/mappings`` branch and format it for use with
        the xn-twist algorithm. The limit sets the maximum number of spoofs that should be returned for each character. A limit of zero will return all of the spoofs."""
        dataset = dict()

        # make a request to the ``mappings`` branch
        r = self.get_branch('mappings')

        # iterate through each of the mappings
        for mapping in r['_items']:
            if limit == 0:
                # create a list of the spoofs sorted by votes
                sorted_list = sorted(mapping['potential_spoofs'], key=lambda spoof: spoof['votes'], reverse=True)
            else:
                # create a list of the spoofs sorted by votes
                sorted_list = sorted(mapping['potential_spoofs'], key=lambda spoof: spoof['votes'], reverse=True)[:limit]
            dataset[mapping['character']] = [spoof_character['spoof_character'] for spoof_character in sorted_list]

        return dataset

    def get_branch(self, api_branch=None):
        """Make ``GET`` request to the given api branch."""
        if api_branch == None:
            return self.requester.make_get_request(self.api_path)
        else:
            return self.requester.make_get_request(self.api_path + api_branch)

    def add_item(self, data, api_branch):
        """
        Make ``POST`` request to add an item to the given branch.
        """
        return self.requester.make_post_request(self.api_path + api_branch,
                                                self.auth, data)

    def update_item(self, item_json, new_data, api_branch):
        """
        Make ``PUT`` request to update an item on the given branch.
        """
        # find the id and etag
        item_id = item_json['_id']
        item_etag = item_json['_etag']

        header = {
            'If-Match': item_etag
        }

        return self.requester.make_put_request(self.api_path + api_branch +
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
