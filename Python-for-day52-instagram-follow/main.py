from insta_follow import InstaFollow

FB_ACCOUNT = "smallouforme@gmail.com"
FB_PASSWORD = "078376266SMALLou"

robot = InstaFollow(FB_ACCOUNT, FB_PASSWORD)

robot.login()
robot.find_followers()
robot.follow()
