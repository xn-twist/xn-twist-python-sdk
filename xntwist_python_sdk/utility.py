#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Python SDK for XN-Twist's API."""

import json

import requests


class Requester(object):
    """Utility class for the XN-Twist API."""

    def __init__(self):
        """."""
        return

    @staticmethod
    def make_get_request(url):
        """Make and handle a ``GET`` request to the given url."""
        response = requests.get(url)

        if response.ok:
            return json.loads(response.text)
        else:
            raise RuntimeWarning("{} response ".format(response.status_code) +
                                 "from {}: {}".format(url, response.text))

    @staticmethod
    def make_post_request(url, auth=None, data=None):
        """Make and handle a ``POST`` request to the given url."""
        response = requests.post(url, auth=auth, json=data)

        if response.ok:
            return json.loads(response.text)
        else:
            raise RuntimeWarning("{} response ".format(response.status_code) +
                                 "from {}: {}".format(url, response.text))

    @staticmethod
    def make_put_request(url, auth=None, headers=None, data=None):
        """Make and handle a ``PUT`` request to the given url."""
        response = requests.put(url, auth=auth, headers=headers, json=data)

        if response.ok:
            return json.loads(response.text)
        else:
            raise RuntimeWarning("{} response ".format(response.status_code) +
                                 "from {}: {}".format(url, response.text))

    @staticmethod
    def make_delete_request(url, auth=None, headers=None):
        """Make and handle a ``DELETE`` request to the given url."""
        response = requests.delete(url, auth=auth, headers=headers)

        if response.ok:
            return
        else:
            raise RuntimeWarning("{} response ".format(response.status_code) +
                                 "from {}: {}".format(url, response.text))
