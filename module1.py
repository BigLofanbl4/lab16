#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def func():
    def form_str(lst):
        res = "<ol>\n"
        for i in lst:
            res += f"<li>{i}</li>\n"
        res += "</ol>"
        return res

    return form_str

