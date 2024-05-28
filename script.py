from features import features
from predictor import predict_fake_profile


result = []
profile_pic = int(input('Enter 1 if the account has profile pic otherwise 0: '))
username = input('Enter the username of the account: ')
name = input('Enter the name in the account: ')
description = input('Enter the description of the account: ')
url = int(input('Enter 1 if the account has any external url otherwise 0: '))
private = int(input('Enter 1 if the account is private otherwise 0: '))
post = int(input('Enter the number of posts in the account: '))
followers = int(input('Enter the number of followers in the account: '))
followings = int(input('Enter the number of followings in the account: '))

feature = features(username=username, name=name)

result += [profile_pic]
result += feature
result += [len(description), url, private, post, followers, followings]
print(result)
print('FAKE PROFILE' if predict_fake_profile(result) == 0 else 'REAL PROFILE')
