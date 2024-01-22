import praw
import random

reddit = praw.Reddit(client_id="XXXXXXXXXXXXXXXXXXXXXXXXXX",
                     client_secret="XXXXXXXXXXXXXXXXXXXXXXXXXXX",
                     user_agent="<console:u-bot9000:1.0>",
                     username="u-bot9000",
                     password="XXXXXXXXXXXXXXXXXXXXXXXXXXX")

print('running')

subreddit = reddit.subreddit("theletteru")

username_to_check = 'NotAlreadyUsed'  # This is blunderful code but I dont want to change it

def process_new_posts(subreddit_name):
  subreddit = reddit.subreddit(subreddit_name)
  for submission in subreddit.stream.submissions(skip_existing=True):
    if submission.author and submission.author.name != username_to_check:
      prob = random.randint(0, 1000)
      if prob == 1:
        probe = random.randint(0, 10000)
        if probe == 1:
          print("MEGA JACKPOT!!!")
          submission.reply(
              "LUCKY U!!!! THIS COMMENT HAS A 1/10000 CHANCE OF HAPPENINQ!!!")
        else:
          print("JACKPOT")
          submission.reply(
              "Lucky U! This comment has a 1/1000 chance of happeninq!")
      else:
        prob = random.randint(0, 2)
        if prob == 1:
          submission.reply(
              "U is the best! H is pretty cool too \n\n ^(I am a bot, and this action was performed automatically. If you think this is a mistake, leave TheLetterU. If you still think this is a mistake, please) [^(contact me here.)](https://www.reddit.com/message/compose/?to=u-bot9000&subject=The%20bot%27s%20broken)"
          )
        else:
          submission.reply(
              "U is really cool, but I also like H \n\n ^(I am a bot, and this action was performed automatically. If you think this is a mistake, leave TheLetterU. If you still think this is a mistake, please) [^(contact me here.)](https://www.reddit.com/message/compose/?to=u-bot9000&subject=The%20bot%27s%20broken)"
          )
      print(f"Replied to the post with ID: {submission.id}")
      print(f"Post Title: {submission.title}")


process_new_posts('theletteru')
