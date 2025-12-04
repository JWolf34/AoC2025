import datetime
import requests
import os

def fetchInput(day, year):
    
    print(f"Fetching input for Day {day} of year {year}...")
    session_is = getSession()
    cookies_are = dict(session=session_is)
    headers = {"User-Agent": "johnmwolf34@gmail.com"}
    r = requests.get(f"https://adventofcode.com/{year}/day/{day}/input",headers=headers,cookies=cookies_are)

    try:
        input = open(f"day{day}/input.txt", 'a')
        input.write(r.text)
        input.close()
        print("Fetched! Happy coding :)")
    except FileNotFoundError as e:
        print("Error occurred when fetching today's input. Is it not the Advent of Code?")
        print(e)


def getSession():
    return os.getenv("SESSION")

if __name__ == "__main__":
    DAY = 4
    YEAR = 2025
    fetchInput(day= DAY, year= YEAR)


    