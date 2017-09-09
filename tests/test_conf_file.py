#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Test to make sure that the XN-Twist SDK can properly pull from a config file."""

import os

from xn_twist_python_sdk import xn_twist_python


def test_config_file_reading():
    """Make sure that the SDK can properly read from configuration files."""
    config_file_path = os.path.abspath(os.path.join(os.path.dirname(__file__),
                                                    './xn.conf.test'))
    # initialize the SDK with a conf file
    xn = xn_twist_python.XnTwistSDK(config_file_path)

    # make sure the config file was properly read
    assert xn.auth.username == "John Doe"
    assert xn.auth.password == "Test"
