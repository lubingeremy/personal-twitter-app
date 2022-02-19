import tweepy
import time

access_token = "";
access_token_secret = "";

consumer_key = "";
consumer_secret = ""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# def delete(k):
#     tweetDelete(k)
#     time.sleep(2)
    
def startingPoint(statusId):
    if (statusId == ''):
        return True;
    else:
        return False;

def tweetDelete(k):
    check = False;
    for status in api.user_timeline(user_id="", count=k):
        if (check != True):
            print("Status id is " + str(status.id));
            check = startingPoint(status.id);
            print("check is " + str(check))
            time.sleep(1.5);
            if (check):
                print("----->STARTING POINT REACHED");
                continue
        else:
            api.destroy_status(status.id);
            print(str(status.id) + " deleted");
            time.sleep(1.5);


def tweetDelete2(k):
    tweetCount = 0;
    for status in api.user_timeline(user_id="", count=k, max_id=""):
        api.destroy_status(status.id);
        print(str(status.id) + " deleted");
        tweetCount+=1;
        time.sleep(0.5);

