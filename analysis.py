#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: @manojpandey
#
# ..
from collections import Counter
import pymongo
import re
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client['precog']
collection = db['data']

TRUMP = re.compile('(trump|donald|donaldtrump|sickhillary)')
HILLARY = re.compile('(hillary|clinton|hillaryclinton|iamwithher|imwithher)')


def find_popularity():
    # ----------------------
    # Hillary:  86543
    # Trump:  123310
    # Total tweets:  130380
    # -----------------------
    h_favor = 0
    t_favor = 0
    # db_max = 100000
    # db_min = 0
    total_valid = 0

    cursor = collection.find({})
    for doc in cursor:
        # db_min += 1
        # if db_min < db_max:
        try:
            text = doc['text']
            total_valid += 1
        except KeyError:
            # print doc['_id']
            pass
        # print text
        h_favor += len(HILLARY.findall(text.lower()))
        t_favor += len(TRUMP.findall(text.lower()))
        # else:
        #     break
    print "Hillary: ", h_favor
    print "Trump: ", t_favor
    print "Total tweets: ", total_valid


def top_10_hashtags():
    # -----------------------------------------------------------------------
    # [(u'trump', 5431), (u'dncleak2', 2924), (u'imwithher', 2321),
    # (u'maga', 2221), (u'hillaryclinton', 2074), (u'dncleaks2', 2041),
    # (u'electionfinalthoughts', 2010), (u'wikileaks', 1547),
    # (u'clinton', 1436), (u'trump2016', 1394), (u'np', 1071),
    # (u'soundcloud', 1068), (u'podestaemails33', 994), (u'trumppence16', 957),
    # (u'draintheswamp', 914), (u'podestaemails', 914), (u'hillary', 914),
    # (u'electionday', 897), (u'trumptrain', 783), (u'election2016', 779),
    # (u'donaldtrump', 680), (u'reno', 558), (u'vote', 545), (u'icymi', 503),
    # (u'spiritcooking', 444), (u'nevertrump', 401), (u'votetrump', 394),
    # (u'ohio', 386), (u'tcot', 373), (u'votetrumppence16', 364),
    # (u'neverhillary', 329), (u'maga3x', 306), (u'dumptrump', 291),
    # (u'fbi', 283), (u'americafirst', 277), (u'vincefoster', 268),
    # (u'virginia', 268), (u'millennials', 264), (u'florida', 257),
    # (u'bernieorbust', 255), (u'crookedhillary', 249), (u'blackvote', 244),
    # (u'nevada', 241), (u'blacklivesmatters', 241), (u'blackmillennials', 239),
    # (u'blacklives', 239), (u'hrc45', 239), (u'makeamericagreatagain', 226),
    # (u'uselections2016', 221), (u'dnc', 213), (u'uselection', 212),
    # (u'pennsylvania', 200), (u'usa', 198), (u'news', 197), (u'gop', 176),
    # (u'imwither', 172), (u'uniteblue', 170), (u'podestaemails31', 168),
    # (u'ronbrown', 166), (u'morningjoe', 163), (u'cnn', 162),
    # (u'strongertogether', 160), (u'riggedsystem', 157), (u'lockherup', 155),
    # (u'comey', 154), (u'riggedelection', 150), (u'americancitizens', 147),
    # (u'michigan', 141), (u'corruptmedia', 133), (u'pa', 132),
    # (u'america', 131), (u'elections2016', 130), (u'p2', 130),
    # (u'dobbs', 127), (u'dncleak', 125), (u'northcarolina', 124),
    # (u'beentheredonethat', 116), (u'hillaryforprison', 115), (u'rt', 113),
    # (u'emabiggestfansladygaga', 113), (u'pjnet', 112), (u'obama', 108),
    # (u'voteblue', 106), (u'austyncrites', 106), (u'mediabias', 105),
    # (u'2a', 102), (u'ctl', 100), (u'iamwithher', 94), (u'votehillary', 91),
    # (u'politics', 91), (u'usa2016', 90), (u'podestaemails32', 88),
    # (u'jobs', 87), (u'blacks4trump', 86), (u'isis', 81),
    # (u'2016election', 81), (u'clintonfoundation', 80), (u'colorado', 77),
    # (u'newhampshire', 76), (u'presidentialelection', 75)]
    # ------------------------------------------------------------------------
    '''
    Traverse through all hashtags in every tweet
    - hashtags are present in the attribute - entities.hashtags
    - return value - array of hashtags, empty is no hashtag
        {"indices":[x,y], "text": <hashtag-text-here>}
    '''
    cursor = collection.find({})
    # db_max = 10
    # db_min = 0
    hashtag_counter = Counter()
    for doc in cursor:
        # db_min += 1
        # if db_min < db_max:
        try:
            hashtag_list = doc['entities']['hashtags']
            if len(hashtag_list) > 0:
                for ht in hashtag_list:
                    hashtag_counter[ht['text'].lower()] += 1
        except KeyError:
            pass
        # else:
            # break
    print hashtag_counter.most_common(10)


def original_vs_retweeted():
    # Original tweets don't have the attribute
    #   retweeted_status
    # Original
    # db.getCollection('data').find({"retweeted_status":{$eq:null}},{}).length()
    # 46216
    # Retweeted
    # db.getCollection('data').find({"retweeted_status":{$ne:null}},{}).length()
    # 91329
    pass


def fav_counts():
    pass
    # find no of tweets greater than a number - ex: 300,000 => Outputs: 1
    # db.getCollection('data').find({'retweeted_status.favorite_count':{$gt:300000}}).length()

    # some queries:
    # gt 300,000 : 1
    # gt 100,000 : 302
    # gt  50,000 : 807
    # gt  10,000 : 7440
    # gt    5000 : 12131
    # gt    1000 : 26731
    # gt     100 : 52079
    # eq       0 : 6490


def tweet_type():
    pass
    # only text: 121693
    # db.getCollection('data').find({'extended_entities':{$eq:null}}).length()
    # OR
    # db.getCollection('data').find({'entities.media.type':{$eq:null}}).length()
    # ----
    # contains Photo: 11046
    # db.getCollection('data').find({'extended_entities.media.type':'photo'}).length()
    # ----
    # contains Video: 4468
    # db.getCollection('data').find({'extended_entities.media.type':'video'}).length()
    # ----


def main():
    pass

if __name__ == '__main__':
    main()
