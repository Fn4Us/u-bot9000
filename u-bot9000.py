import praw
import random
import threading


reddit = praw.Reddit(client_id="XXXXXXXXXXXXXXXXXXXXX",
                     client_secret="XXXXXXXXXXXXXXXXXXXXX",
                     user_agent="<console:u-bot9000:1.0>",
                     username="u-bot9000",
                     password="XXXXXXXXXXXXXXXXXXXXXX")


print('running')

subreddit = reddit.subreddit("theletterh")
username_to_check = 'NotAlreadyUsed'  # This is blunderful code but I dont want to change it
randomReply = [
    "H and U are both good. HUnion!!!", "I love H, I also love U", "HU 👍",
    "H + U = 👍", "HEIJAK needs U", "H ❤️ U", "𝙃𝙐", "Move aside 𝕏, we have ℍ𝕌",
    "Ƕ", "}·{ ]_[", "HU her? I hardly know her!", "H and U are the best, AMA", "I am ***H***appy this is working, are yo***U***?"
]
newPostReply = ["H is wonderful, and so is U", "H is cool, and so is U"]
newPostFooter = "\n\n ^(I am a bot, and this action was performed automatically. If you think this is a mistake, leave TheLetterH. If you still think this is a mistake, please) [^(contact me here.)](https://www.reddit.com/message/compose/?to=u-bot9000&subject=The%20bot%27s%20broken)"
replies = ["h", "ℋ", "*h*", "**h**", "~~literally anything else~~ h", "h is awesome :]", "h :]", "# h", "# **h**"]


def run():
  try:
    for comment in subreddit.stream.comments(skip_existing=True):
      if comment.author and comment.author.name == "h-bot-model-h" and comment.body in replies:
        random_response = random.choice(randomReply)
        print("new comment")
        comment.reply(random_response)
        print(f"replied with: {random_response}")
  except Exception as e:
    print(e)
    run()


def process_new_posts(subreddit_name):
  subreddit = reddit.subreddit(subreddit_name)
  for submission in subreddit.stream.submissions(skip_existing=True):
    if submission.author and submission.author.name != username_to_check:
      if random.randint(0, 1000) == 1:
        print("JACKPOT")
        submission.reply("Lucky H! This comment has a 1/1000 chance of happeninq!")
      elif random.randint(0, 10000) == 1:
        print("MEGA JACKPOT!!!")
        submission.reply("LUCKY U!!!! THIS COMMENT HAS A 1/10000 CHANCE OF HAPPENINQ!!!")
      else:
        submission.reply(random.choice(newPostReply) , newPostFooter)
      print(f"Replied to the post with ID: {submission.id}")
      print(f"Post Title: {submission.title}")


## Create two threads for concurrent execution of the functions
thread_run = threading.Thread(target=run)
thread_process = threading.Thread(
    target=process_new_posts,
    args=('theletterh', ))  # Pass subreddit_name as a tuple

# Start all threads
thread_run.start()
thread_process.start()

# Wait for all threads to finish
thread_run.join()
thread_process.join()
thread_run.join()
thread_process.join()
