# -*- coding: utf-8 -*-
import utils
import traceback
from tweet_func import *

conn = MySQLdb.connect(
    host='localhost', user=config.DATABASE_USER, passwd=config.DATABASE_PASS, db=config.DATABASE_NAME,
    charset='utf8mb4')

def tweet():

    ## Tableが無ければ作成する
    cur = conn.cursor()

    cur.execute(
        "create table if not exists Exercise ("
        "id INTEGER PRIMARY KEY AUTO_INCREMENT,"
        "time_stamp TIMESTAMP NOT NULL DEFAULT (NOW() + INTERVAL 9 HOUR ),"
        "tweeted_time TIMESTAMP NOT NULL,"
        "kcal INTEGER NOT NULL ,"
        "user_name TEXT NOT NULL ,"
        "user_screen_name TEXT NOT NULL ,"
        "tweet_id BIGINT NOT NULL UNIQUE)"
    )
    conn.commit()

    api = auth_twitter()

    print("画像を検索")
    tweet_ranking(api)

def lambda_handler(event=None, context=None):
    try:
        tweet()
    except (Exception,tweepy.error.TweepError) as e:
        traceback.print_exc()
        utils.send_mail("An error has occurred.",  traceback.format_exc())
        raise e
    except:
        traceback.print_exc()
        utils.send_mail("An error has occurred.",  traceback.format_exc())
    return {
        'statusCode': 200
    }

lambda_handler()