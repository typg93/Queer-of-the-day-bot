'''
get_tweets.py: mash together a random tweet
10 September 2020
Vicki Langer (@vicki_langer)
'''

from random import choice

from tweet_nouns import nouns
from tweet_adjectives import adjectives
from tweet_labels import labels

from article_determiner import get_indefinite_article

adjective = choice(adjectives)
label = choice(labels)
noun = choice(nouns)
article = get_indefinite_article(adjective)


def get_tweet():
    tweet_to_send = f"today's queerness is {article} {adjective} {label} {noun}"

    return tweet_to_send
