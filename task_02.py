#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Implementing something that resembles the structure of a
login or authentication screen."""

import authentication
import getpass

def login(username, maxattempts=3):
    valid = False
    current_attempts = 0
    false = "Incorrect username or password. You have {} attempts left!"
    while current_attempts < maxattempts:
        password = getpass.getpass()
        valid = authentication.authenticate(username, password)
        if valid == True:
            return valid
        else:
            current_attempts += 1
            print false.format(maxattempts - current_attempts)
    return valid
