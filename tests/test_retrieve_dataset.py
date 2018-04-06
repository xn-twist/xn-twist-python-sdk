#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pytest

from xn_twist_python_sdk import xn_twist_python


@pytest.fixture
def xn():
    xn = xn_twist_python.XnTwistSDK()
    return xn


def test_retrieve_dataset(xn):
    """Test the auto-formating of the mappings branch."""
    # get the dataset
    dataset = xn.retrieve_dataset()
    assert len(dataset) > 85
    assert len(dataset['a']) == 10


def test_zero_limit(xn):
    """Test the auto-formating of the mappings branch."""
    # get the dataset
    dataset = xn.retrieve_dataset(limit=0)
    assert len(dataset) > 85
    assert len(dataset['a']) >= 42
