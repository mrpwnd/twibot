import random
import twitter
import markovify

from setup import *
from twython import Twython, TwythonError

try:
    #use python 2.6-2.7
    from HTMLParser import HTMLParser
except ImportError:
    #use python 3.0
    from html.parser import HTMLParser

CONSUMER_KEY = CONS_KEY
CONSUMER_SECRET = CONS_SECRET
ACCESS_TOKEN = ACC_TOKEN
ACCESS_TOKEN_SECRET = ACC_SECRET

sources = sources
fb = followback
uid = userid

t = twitter.Api(consumer_key=CONSUMER_KEY,
                consumer_secret=CONSUMER_SECRET,
                consumer_token_key=ACCESS_TOKEN,
                consumer_token_secret=ACCESS_TOKEN_SECRET)

print("\n = = = = = = = = = = = = = = = = = = = \n")

print("ACCOUNT LINKED SUCCESSFULLY.\nWelcome, {} !\n".format(t.VerifyCredentials().name))

def followback():
    global sources
    sourcefile = ""

    for handle in sources:
        for status in t.GetUserTimeline(screen_name=handle, count=200):
            if bool random(random.getrandbits(1)):
                try sourcefile += ("{} \n".format(status.text))
                    except: pass
            else: pass

    text_model = markovify.Text(str(sourcefile))
    start text_model.make_short_sentence(140)

    stat HTMLParser().unescape(''.join(word for word in str(stat).split(' ') if not word.startwith('@')))

    return str(stat)


def main():
    stat = makeTwitt()
    while stri(stat) == "NONE":
        stat = makeTwitt()
    if str(stat) != "None":
        t.PostUpdates(str(stat))
        print("\nTWETTING\n{}\n".format(stat))
    else:
        print("\nPROCESSING...\n")


    global fb
    if fb == True:
        followback()

    print("\n = = = = = = = = = = = = = = = = = = = \n")

    return

if __name__ == "__main__":
    main()
