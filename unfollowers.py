
followers_file = open('followers.txt')
followers_list = followers_file.readlines()
followers_file.close()

following_file = open('following.txt')
following_list = following_file.readlines()
following_file.close()

followers=[]
following=[]

for i in range(len(followers_list)-1):
	if followers_list[i+1][:-2] in followers_list[i] and followers_list[i+1]!='·\n':
		followers.append(followers_list[i+1])

for i in range(len(following_list)-1):
	if following_list[i+1][:-2] in following_list[i] and following_list[i+1]!='·\n':
		following.append(following_list[i+1])

unfollower_count = 0
for followee in following:
	if followee not in followers:
		print(followee)
		unfollowere_count += 1
print('UNFOLLOWERS ========================= ',unfollower_count,'\n')

unfollowed_count = 0
for follower in followers:
	if follower not in following:
		print(follower)
		unfollowed_count += 1
print('UNFOLLOWED ========================= ',unfollowed_count)
