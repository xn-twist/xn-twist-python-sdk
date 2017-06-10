#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tests for xn-twist's Python SDK."""

import json

from xn_twist_sdk import xnTwist


def test_sdk_calls():
    xn = xnTwist.xnTwist()
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
