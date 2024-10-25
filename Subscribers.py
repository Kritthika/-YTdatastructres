class Youtube :
    def __init__(self,username, subscribers=0, subscription=0): 
        self.username = username
        self.subscribers = subscribers
        self.subscription = subscription
    def usersub(self, user):
        user.subscribers+=1
        self.subscription+=1
user1 = Youtube("kRIT")
user2 = Youtube("prad")
user3 = Youtube("kitty")
user1.usersub(user2)
user2.usersub(user1)
user3.usersub(user1)
print(user1.username)
print("User1 subscribers:",user1.subscribers)
print(user2.username)
print("User2 subscribers:",user2.subscribers)