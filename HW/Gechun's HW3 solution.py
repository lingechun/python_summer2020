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

# Create user objects
ps = api.get_user('WUSTLPoliSci')

# Create a list of follower ids
ps_followers = ps.followers_ids()
# Check if the length of this list equal to her number of followers
len(ps_followers)
ps.followers_count # they are equal! it is 469 followers


# Create a list to store each follower's number of tweets
tweets = []
# Create another list to store each follower's number of followers
followers = []
for follower_id in ps_followers[0:5]:
	user = api.get_user(follower_id)
    tweets.append(user.statuses_count)
    followers.append(user.followers_count)
# Get the index of the largest number in tweets
index_active = tweets.index(max(tweets))
# According to the index, we find the most active follower
active_follower_id = ps_followers[index_active]
active_follower = api.get_user(active_follower_id)
active_follower.name

# Get the index of the largest number in followers
index_popular = followers.index(max(followers))
# According to the index, we find the most popular follower
popular_follower_id = ps_followers[index_popular]
popular_follower = api.get_user(popular_follower_id)
popular_follower.name

# Create a list of friend ids
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
for friend_id in ps_friends[0:20]:
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
    print(active_friend_layman.name)

if len(friend_expert_ids) == 0:
    print('No expert friend.')
else:
    # Get the index of the largest number in friend_expert_tweets
    index_active = friend_expert_tweets.index(max(friend_expert_tweets))
    # According to the index, we find the most active expert friend
    active_friend_expert_id = friend_expert_ids[index_active]
    active_friend_expert = api.get_user(active_friend_expert_id)
    print(active_friend_expert.name)

if len(friend_celebrity_ids) == 0:
	print('No celebrity friend.')
else:
    # Get the index of the largest number in friend_celebrity_tweets
    index_active = friend_celebrity_tweets.index(max(friend_celebrity_tweets))
    # According to the index, we find the most active expert friend
    active_friend_celebrity_id = friend_celebrity_ids[index_active]
    active_friend_celebrity = api.get_user(active_friend_celebrity_id)
    print(active_friend_celebrity.name)


# Get the index of the largest number in friend_followers
index_popular = friend_followers.index(max(friend_followers))
# According to the index, we find the most popular friend
popular_friend_id = ps_friends[index_popular]
popular_friend = api.get_user(popular_friend_id)
popular_friend.name


# Limit the friends to laymen and experts
limit_friends = friend_layman_ids + friend_expert_ids
# Limit the followers to laymen and experts
limit_followers = []
for follower_id in ps_followers[0:20]:
	user = api.get_user(follower_id)
	if user.followers_count <= 1000:
       limit_followers.append(follower_id)
    else:
    	continue


# Find the most active one among followers and followers' followers
for follower_id in limit_followers:
	user = api.get_user(follower_id)
	limit_followers_followers.append(user.followers_ids())


tweets.append(user.statuses_count)
    followers.append(user.followers_count)



tweets.append(user.statuses_count)
followers.append(user.followers_count)





