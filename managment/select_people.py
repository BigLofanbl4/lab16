#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def sel(surname, people):
    result = []
    for i in people:
        if i.get("surname", "") == surname:
            result.append(i)
    return result