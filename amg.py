#!/usr/bin/env python

import logging, logging.config
import urllib2, urlparse
import sys, threading, Queue, time, argparse
from collections import Counter
import config

if __name__ == '__main__':
    # parse command line arguments
    parser = argparse.ArgumentParser(description='fdfdfdfd')
    parser.add_argument('url', type=str, help='base URL where WordPress is installed')

    parser.add_argument('-u', '--username', default=config.username,
                        help="username (default: " + str(config.username) + ")")

    parser.add_argument('-w', '--wordlist', default=config.wordlist,
                        help="username (default: " + str(config.username) + ")")

    args = parser.parse_args()
    config.url = args.url
    config.username = args.username
    config.wordlist = args.wordlist

    # logger configuration
    logging.config.fileConfig("amg.conf")
    logger = logging.getLogger("amg")

logger.info("Target URL: %s", config.url)  # check URL and user (if user not set, enumerate usernames)
logger.info("Checking URL & username...")

usernames = []
if config.username:
    usernames.append(config.username)

logger.info("Users: %s", usernames)  # check URL and user (if user not set, enumerate usernames)

# load login check tasks into queue
logger.debug("Loading wordlist...")

file = open(config.wordlist, "r")

wordlist = file.readlines()

count = Counter(wordlist)

print count
for line in wordlist:
    print line


def worker():
    """thread worker function"""
    print 'Worker'
    return


threads = []
for i in range(5):
    t = threading.Thread(target=worker)
    threads.append(t)
    t.start()
