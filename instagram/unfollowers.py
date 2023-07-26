import instaloader

class Insta_info:

    def __init__(self, username):

        self.username = username
        self.loader = instaloader.Instaloader()
        self.profile = instaloader.Profile.from_username(self.loader.context,self.username)
        
    def get_my_followers(self):
        for followers in self.profile.get_followers():
            with open("followers.txt","a+") as f:
                file = f.write(followers.username+'\n')
        
                print("Writing followers...")
                print(file)
        
    def get_my_followees(self):
         for followees in self.profile.get_followees():
            with open("followees.txt","a+") as f:
                file = f.write(followees.username+'\n')
         
            print("Writing followees...")
            print(file)

    def get_my_unfollowers(self):
        
        followers_file = set(open("followers.txt").readlines())
        followees_file = set(open("followees.txt").readlines())

        unfollowers_set = followees_file.difference(followers_file)
        
        for unfollowers in unfollowers_set:
            print(unfollowers)            


    def Login(self):

        login = self.loader.load_session_from_file(self.username)

        return login

insta_info = Insta_info("chrisgeek_")

insta_info.Login()
'insta_info.get_my_followers() '
'insta_info.get_my_followees()'
insta_info.get_my_unfollowers()




