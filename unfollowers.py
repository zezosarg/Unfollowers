
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

c=0
for i in following:
	if i not in followers:
		print(i)
		c+=1
print('UNFOLLOWERS ========================= ',c,'\n')

c=0
for i in followers:
	if i not in following:
		print(i)
		c+=1
print('UNFOLLOWED ========================= ',c)
