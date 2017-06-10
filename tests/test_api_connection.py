#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tests for xn-twist's Python SDK."""

import json

import pytest

from xn_twist_sdk import xnTwist


@pytest.fixture
def xn():
    xn = xnTwist.xnTwist()
    return xn


def test_get_requests(xn):
    """Test GET requests to XN-Twist's API."""
    base_response = xn.get_base()
    assert("administrators" in json.dumps(base_response) and
           "feed" in json.dumps(base_response))

    response = None
    try:
        response = xn.get_administrators()
    except RuntimeWarning:
        assert("null" in json.dumps(response))
    else:
        raise RuntimeError("Able to reach admin branch w/o authentication!")

    response = xn.get_feed()
    assert('"title": "feed"' in json.dumps(response))

    response = xn.get_mappings()
    assert('"title": "mappings"' in json.dumps(response))

    response = xn.get_non_basic_chars()
    assert('"title": "non_basic_characters"' in json.dumps(response))

    response = xn.get_unmapped_chars()
    assert('"title": "unmapped_characters"' in json.dumps(response))

    response = xn.get_basic_chars()
    assert('"title": "basic_characters"' in json.dumps(response))

    response = xn.get_suggested_deprecations()
    assert('"title": "suggested_deprecations"' in json.dumps(response))

    response = xn.get_depricated_chars()
    assert('"title": "depricated_characters"' in json.dumps(response))


def test_mappings_format(xn):
    """Test the auto-formating of the mappings branch."""
    # get the dataset
    dataset = xn.retrieve_dataset()

    # make sure the dataset is valid json
    dataset_string = json.dumps(dataset)
    new_dataset = json.loads(dataset_string)

    # make sure the two 'versions' of the dataset are the same
    assert(dataset == new_dataset)
