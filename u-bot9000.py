import praw
import random
import threading
from keep_alive import keep_alive

reddit = praw.Reddit(
    client_id="W1T_uV33O1NvXwmtVbwH-Q",
    client_secret="############################",
    user_agent="<console:u-bot9000:1.0>",
    username="u-bot9000",
    password="#################")

subreddit_data = [
    {'name': 'theletterh', 'reply_text': 'H is cool, and so is U \n\n ^(I am a bot, and this action was performed automatically. If you think this is a mistake, leave TheLetterH. If you still think this is a mistake, please) [^(contact me here.)](https://www.reddit.com/message/compose/?to=u-bot9000)'},
    {'name': 'theletteru', 'reply_text': 'egg'}
]

username_to_check = 'u-bot9000'

randomReply = [
  "H and U are both good. HU UNION!!!",
  "I love H, I also love U",
  "HU 👍",
  "H + U = 👍",
  "HEIJAK needs U",
  "H ❤️ U",
  "𝙃𝙐",
  "Move aside 𝕏, we have ℍ𝕌"
]

keep_alive()

def run():
    try:
      for comment in reddit.redditor("h-bot-model-h").stream.comments(skip_existing=True):
         random_response = random.choice(randomReply)
         print("new comment")
         comment.reply(random_response)
         print(f"replied with: {random_response}")
    except Exception as e:
      print(e)
      run()
run()
def process_new_posts(subreddit_name, reply_text):
    subreddit = reddit.subreddit(subreddit_name)
    for submission in subreddit.stream.submissions(skip_existing=True):
        if submission.author and submission.author.name != username_to_check: #This code is useless it already skips_existing
            submission.reply(reply_text)
            print(f"Replied to the post with ID: {submission.id}")
            print(f"Post Title: {submission.title}")

# Create two threads for both of the functions
thread_run = threading.Thread(target=run)
thread_process = threading.Thread(target=process_new_posts, args=('theletterh', 'H is cool, and so is U \n\n ^(I am a bot, and this action was performed automatically. If you think this is a mistake, leave TheLetterH. If you still think this is a mistake, please) [^(contact me here.)](https://www.reddit.com/message/compose/?to=u-bot9000)'))

# Start both
thread_run.start()
thread_process.start()

# Wait for both threads to finish
thread_run.join()
thread_process.join()
