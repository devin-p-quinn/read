'''
    Reading Time Program
    Devin Quinn
'''

from datetime import date
from datetime import timedelta
from csv import writer
from book import Book
from typing import Tuple
import re
from myCalendar import create_event, update_event


def get_start() -> date:
    '''Gets the start date for reading and returns a datetime obj'''
    pattern = r"(19|20)\d{2}\-(0[1-9]|1[0,1,2])\-(0[1-9]|[12][0-9]|3[01])"
    while True:
        day = input("When do you want to start reading\n"
                    "use format (YYYY-MM-DD)\n")
        match = re.match(pattern, day)
        if bool(match):
            break
        else:
            print("Date format incorrect please try again!\n")
    start = date.fromisoformat(day)

    return start


def get_title() -> str:
    '''Gets the title of the book from user input'''
    title = input("What is the title of the book you want to read?\n")

    return title


def get_author() -> str:
    '''Gets the author of the book from user input'''
    author = input("Who is the author of the book?\n")

    return author


def get_length() -> int:
    '''Gets the length of the book from user input'''
    while True:
        try:
            length = int(input("How long is the book in pages?\n"))
            break
        except ValueError:
            print("Please enter a digit")

    return length


def get_chapters() -> int:
    '''Gets the chapters of the book from user input'''
    while True:
        try:
            chapters = int(input("How long is the book in chapters?\n"))
            break
        except ValueError:
            print("Please enter a digit")

    return chapters


def is_pages() -> bool:
    '''Boolean expression that returns true if the book is measured in pages
    or false if the book is measured in chapters'''
    page_val = True
    while True:
        page_or_chap = input("Do you want to measure you progress by pages "
                             "or chapters?\n")
        if page_or_chap.casefold() == 'pages':
            page_val = True
            break
        elif page_or_chap.casefold() == 'chapters':
            page_val = False
            break
        else:
            print("Input invalid! Please try again.\n")

    return page_val


def get_prog_day(page_chap: bool) -> int:
    '''Gets the number of pages the users wants to read during the week'''
    if page_chap:
        progress = "page"
    else:
        progress = "chapter"
    while True:
        try:
            week_prog = int(
                input(
                    "How many {0}s do you want to read during "
                    "the week\n".format(progress)))
            break
        except ValueError:
            print("Please enter a digit\n")

    return week_prog


def get_prog_end(page_chap: bool) -> int:
    '''Gets the number of pages the users wants to read during the week'''
    if page_chap:
        progress = "page"
    else:
        progress = "chapter"
    while True:
        try:
            end_prog = int(
                input(
                    "How many {0}s do you want to read on the "
                    "weekend\n".format(progress)))
            break
        except ValueError:
            print("Please enter a digit\n")

    return end_prog


def get_current_pos(page_chap: bool) -> int:
    '''Get the current page from the user and returns it as an int'''
    if page_chap:
        progress = "page"
    else:
        progress = "chapter"
    while True:
        try:
            current_pos = int(input("What {0} are you starting "
                                    "on (If starting from the begining "
                                    "enter 0)\n".format(progress)))
            break
        except ValueError:
            print("Please enter a digit\n")

    return current_pos


def read_schedule(variables: list) -> None:
    '''Takes a list of variables and prints the reading schedule'''
    day = variables[0]
    book = variables[1]
    length = variables[2]
    len_day = variables[3]
    len_end = variables[4]
    current = variables[5]
    days = 0
    delta = timedelta(days=1)
    total = length

    if variables[6]:
        progress = "page"
    else:
        progress = "chapter"

    while current < total:
        if day.isoweekday() < 6:
            current = current + len_day
        else:
            current = current + len_end

        if current > total:
            current = total

        print("On {0} read to {1} {2}".format(day.strftime("%A %d %B %Y"),
                                              progress, current))

        new_event = create_event(day, progress, current, book.title)
        update_event(new_event)
        day = day + delta
        length = length - current
        days += 1

    print("It will take {0} days to read {1}".format(days, book.title))

    update = input("Do you want to update the log (Y/N)")

    if update.casefold() == "y":
        update_log(book.title, book.length, day, days)


def update_log(title, pages, date, days) -> None:
    info = [title, pages, date, days]

    with open('read_log.csv', 'a') as f:
        writer_object = writer(f)
        writer_object.writerow(info)
        f.close()


def main():
    '''Main function that gathers variables and puts them in a list'''
    variables = []
    start = get_start()
    variables.append(start)
    title = get_title()
    author = get_author()
    length = get_length()
    chapters = get_chapters()
    book = Book(title, author, length, chapters)
    variables.append(book)
    page_chap = is_pages()
    if page_chap:
        length = book.length
    else:
        length = book.chapters
    week = get_prog_day(page_chap)
    end = get_prog_end(page_chap)
    current = get_current_pos(page_chap)
    variables.append(length)
    variables.append(week)
    variables.append(end)
    variables.append(current)
    variables.append(page_chap)
    read_schedule(variables)


if __name__ == "__main__":
    main()
