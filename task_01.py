#!/usr/bin/env/python
# -*- coding: utf-8 -*-
"""creating a list of versus matchups for players
in a tournament."""

def get_matches(players):
    match_list = []
    for index, player in enumerate(players):
        for i in range(index + 1, len(players)):
            match_list.append((player, players[i]))
    return match_list
