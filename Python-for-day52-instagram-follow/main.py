from insta_follow import InstaFollow

FB_ACCOUNT = "your own email"
FB_PASSWORD = "your password"

robot = InstaFollow(FB_ACCOUNT, FB_PASSWORD)

robot.login()
robot.find_followers()
robot.follow()
