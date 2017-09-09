#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tests for xn-twist's Python SDK."""

import json

import pytest

from xn_twist_python_sdk import xn_twist_python


@pytest.fixture
def xn():
    xn = xn_twist_python.XnTwistSDK()
    return xn


def test_get_requests(xn):
    """Test GET requests to XN-Twist's API."""
    base_response = xn.get_branch()
    # make assertions to ensure that the base_response was received and all branches are listed
    assert("administrators" in json.dumps(base_response))
    assert("mappings" in json.dumps(base_response))
    assert("basic_characters" in json.dumps(base_response))
    assert("feed" in json.dumps(base_response))
    assert("non_basic_characters" in json.dumps(base_response))
    assert("suggested_deprecations" in json.dumps(base_response))
    assert("unmapped_characters" in json.dumps(base_response))
    assert("deprecated_characters" in json.dumps(base_response))
    assert("high_scores" in json.dumps(base_response))

    response = None
    try:
        response = xn.get_branch('administrators')
    except RuntimeWarning:
        assert("null" in json.dumps(response))
    else:
        raise RuntimeError("Able to reach admin branch w/o authentication!")

    response = xn.get_branch('feed')
    assert('"title": "feed"' in json.dumps(response))

    response = xn.get_branch('mappings')
    assert('"title": "mappings"' in json.dumps(response))

    response = xn.get_branch('non_basic_characters')
    assert('"title": "non_basic_characters"' in json.dumps(response))

    response = xn.get_branch('unmapped_characters')
    assert('"title": "unmapped_characters"' in json.dumps(response))

    response = xn.get_branch('basic_characters')
    assert('"title": "basic_characters"' in json.dumps(response))

    response = xn.get_branch('suggested_deprecations')
    assert('"title": "suggested_deprecations"' in json.dumps(response))

    response = xn.get_branch('deprecated_characters')
    assert('"title": "deprecated_characters"' in json.dumps(response))

    response = xn.get_branch('high_scores')
    assert('"title": "high_scores"' in json.dumps(response))


def test_mappings_format(xn):
    """Test the auto-formating of the mappings branch."""
    # get the dataset
    dataset = xn.retrieve_dataset()

    # make sure the dataset is valid json
    dataset_string = json.dumps(dataset)
    new_dataset = json.loads(dataset_string)

    # make sure the two 'versions' of the dataset are the same
    assert(dataset == new_dataset)
