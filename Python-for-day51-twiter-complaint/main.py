from speed_twitter import TwitterBot

PROMISED_DOWN = 150
PROMISED_UP = 10
TWITTER_ACCOUNT = "your own account"
TWITTER_PASSWORD = "your password"


robot = TwitterBot(TWITTER_ACCOUNT, TWITTER_PASSWORD)
print("Getting your download speed:")
robot.get_internet_speed()
print(f"Down:{robot.down}\nUp:{robot.up}")

if robot.down < PROMISED_DOWN or robot.up < PROMISED_UP:
    TWEET = (f"Hey! ISP, why my internet speed is -> {robot.down}Mbps/{robot.up}Mbps, "
             f"when I pay for {PROMISED_DOWN}Mbps/{PROMISED_UP}Mbps")
    print(f"Whoopee! {robot.down} < {PROMISED_DOWN} = {robot.down < PROMISED_DOWN}\n{robot.up} "
          f"< {PROMISED_UP} = {robot.up < PROMISED_UP}")

    robot.twitter_provider(TWEET)