# Gechun's HW3 solution

import importlib 
import sys
import tweepy 

# Add directory where my key is to system PATH
sys.path.insert(0, '/Users/lingechun/python.summer2020')

# Import items from file
twitter = importlib.import_module('start_twitterAPI')
# Get my twitter API
api = twitter.client

#1(1)
# Create user objects
ps = api.get_user('WUSTLPoliSci')

# Get a list of follower ids
ps_followers = ps.followers_ids()
# Check if the length of this list equal to her number of followers
len(ps_followers)
ps.followers_count # they are equal! it is 469 followers


# Create a list to store each follower's number of tweets
tweets = []
# Create another list to store each follower's number of followers
followers = []
for follower_id in ps_followers:
	user = api.get_user(follower_id)
    tweets.append(user.statuses_count)
    followers.append(user.followers_count)
# Get the index of the largest number in tweets
index_active = tweets.index(max(tweets))
# According to the index, we find the most active follower
active_follower_id = ps_followers[index_active]
active_follower = api.get_user(active_follower_id)
print(active_follower.id, active_follower.name, active_follower.screen_name)
## 810933338 十勝餡粒々@アメリカPh.D.リベンジ tubuann_only

#1(2)
# Get the index of the largest number in followers
index_popular = followers.index(max(followers))
# According to the index, we find the most popular follower
popular_follower_id = ps_followers[index_popular]
popular_follower = api.get_user(popular_follower_id)
print(popular_follower.id, popular_follower.name, popular_follower.screen_name)
## 84653850 Brendan Nyhan BrendanNyhan 

#1(3)
# Get a list of friend ids
ps_friends = api.friends_ids(ps.id)
# # Check if the length of this list equal to her number of followings/friends
len(ps_friends)
ps.friends_count # they are equal! it is 158 followings/friends


# # Create three lists of friends who are layman, expert or celebrity
friend_layman_ids = []
friend_expert_ids = []
friend_celebrity_ids = []
# Create three lists to store layman/expert/celebrity friend's number of tweets
friend_layman_tweets = []
friend_expert_tweets = []
friend_celebrity_tweets = []
# Create a list to store each friend's number of followers
friend_followers = []
for friend_id in ps_friends:
	user = api.get_user(friend_id)
	friend_followers.append(user.followers_count)
	if user.followers_count < 100:
		friend_layman_ids.append(friend_id)
		friend_layman_tweets.append(user.statuses_count)
	elif user.followers_count > 1000:
        friend_celebrity_ids.append(friend_id)
        friend_celebrity_tweets.append(user.statuses_count)
    else:
    	friend_expert_ids.append(friend_id)
    	friend_expert_tweets.append(user.statuses_count)


if len(friend_layman_ids) == 0:
    print('No layman friend.')
else:
	# Get the index of the largest number in friend_layman_tweets
    index_active = friend_layman_tweets.index(max(friend_layman_tweets))
    # According to the index, we find the most active layman friend
    active_friend_layman_id = friend_layman_ids[index_active]
    active_friend_layman = api.get_user(active_friend_layman_id)
    print(active_friend_layman.id, active_friend_layman.name, active_friend_layman.screen_name)
## 764260766 usman falalu usmanfalalu1

if len(friend_expert_ids) == 0:
    print('No expert friend.')
else:
    # Get the index of the largest number in friend_expert_tweets
    index_active = friend_expert_tweets.index(max(friend_expert_tweets))
    # According to the index, we find the most active expert friend
    active_friend_expert_id = friend_expert_ids[index_active]
    active_friend_expert = api.get_user(active_friend_expert_id)
    print(active_friend_expert.id, active_friend_expert.name, active_friend_expert.screen_name)
## 1064533471 Tim... we're doomed prof_nokken

if len(friend_celebrity_ids) == 0:
	print('No celebrity friend.')
else:
    # Get the index of the largest number in friend_celebrity_tweets
    index_active = friend_celebrity_tweets.index(max(friend_celebrity_tweets))
    # According to the index, we find the most active expert friend
    active_friend_celebrity_id = friend_celebrity_ids[index_active]
    active_friend_celebrity = api.get_user(active_friend_celebrity_id)
    print(active_friend_celebrity.id, active_friend_celebrity.name, active_friend_celebrity.screen_name)
## 807095 The New York Times nytimes

#1(4)
# Get the index of the largest number in friend_followers
index_popular = friend_followers.index(max(friend_followers))
# According to the index, we find the most popular friend
popular_friend_id = ps_friends[index_popular]
popular_friend = api.get_user(popular_friend_id)
print(popular_friend.id, popular_friend.name, popular_friend.screen_name)
## 813286 Barack Obama BarackObama

#2(1)
# Limit the followers to laymen and experts
limit_followers = []
for follower_id in ps_followers:
	user = api.get_user(follower_id)
	if user.followers_count <= 1000:
       limit_followers.append(follower_id)
    else:
    	continue

# Find the ids of ps followers' followers
followers_followers = []
for follower_id in limit_followers:
    try:
        user = api.get_user(follower_id)
        followers_followers.append(user.followers_ids())
    except tweepy.TweepError:
        continue

# Combine followers and followers' followers uniquely
followers_followers_flat = []
for i in range(0, len(followers_followers)):
    followers_followers_flat = followers_followers_flat + followers_followers[i]
all_followers = list(set(limit_followers + followers_followers_flat))

# Find the most active one among followers and followers' followers
tweets_ids = {}
for follower_id in all_followers:
    user = api.get_user(follower_id)
    if user.followers_count <= 1000:  # further limit the followers' followers to laymen and experts
        tweets_ids[follower_id] = user.statuses_count
    else:
        continue

active_follower_id = max(tweets_ids, key=tweets_ids.get)
active_follower = api.get_user(active_follower_id)
print(active_follower.id, active_follower.name, active_follower.screen_name)
## 458785593 Corporación GES CorporacionGES


#2(2)
# Limit the friends to laymen and experts
limit_friends = friend_layman_ids + friend_expert_ids

# Find the ids of ps friends' friends
friends_friends = []
for friend_id in limit_friends:
    try:
        friends_friends.append(api.friends_ids(friend_id))
    except tweepy.TweepError:
        continue


# Combine friends and friends' friends uniquely
friends_friends_flat = []
for i in range(0, len(friends_friends)):
    friends_friends_flat = friends_friends_flat + friends_friends[i]
all_friends = list(set(limit_friends + friends_friends_flat))

# Find the most active one among friends and friends' friends
tweets_ids = {}
for friend_id in all_friends:
    user = api.get_user(friend_id)
    if user.followers_count <= 1000:  # further limit the friends' friends to laymen and experts
        tweets_ids[friend_id] = user.statuses_count
    else:
        continue
    

active_friend_id = max(tweets_ids, key=tweets_ids.get)
active_friend = api.get_user(active_friend_id)
print(active_friend.id, active_friend.name, active_friend.screen_name)









