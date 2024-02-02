#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from managment import *
from datetime import datetime

def main():
    people = []

    while True:
        command = input("Введите команду (add, info, list, exit, help): ").strip().lower()

        match command:
            case "exit":
                break
            
            case "add":
                person = get_person.create()
                people.append(person)
                people.sort(
                    key=lambda x: datetime.strptime(".".join(x["birthday"]), "%d.%m.%Y")
                )

            case "info":
                surname = input("Введите фамилию: ")
                selected = select_people.sel(surname, people)
                display_people(selected)

            case "list":
                display_people.show(people)

            case "help":
                get_instructions.help()

            case _:
                print(f"Неизвестная команда {command}", file=sys.stderr)

if __name__ == "__main__":
    main()