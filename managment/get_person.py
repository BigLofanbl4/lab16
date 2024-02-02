#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def create():
    person = {}
    person["surname"] = input("Введите фамилию: ")
    person["name"] = input("Введите имя: ")
    person["zodiac"] = input("Введите знак зодиака: ")
    person["birthday"] = input("Дата рождения (число.месяц.год):").split(".")
    return person