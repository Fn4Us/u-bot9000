import praw
import random
import threading
import time
from keep_alive import keep_alive

reddit = praw.Reddit(
    client_id="W1T_uV33O1NvXwmtVbwH-Q",
    client_secret="####################",
    user_agent="<console:u-bot9000:1.0>",
    username="u-bot9000",
    password="############")

# List of phrases and their corresponding responses
phrases_and_responses = {
    "!a_useless_name": "Its a joke \n \n It seems you forgot the I in ai",
    "!anarchy": "Qooqle en passant \n \nHoly Hell!\n \nNew response just dropped\n \nActual Zombie!\n \n Call the exorcist!\n \nPawn storm incoming!\n \nQueen sacrifice, anyone?",
    "Good bot": "Thanks! Good human",
    "!github": "https://github.com/Fn4Us/u-bot9000"
}

subreddit_data = [
    {'name': 'theletterh', 'reply_text': 'H is cool, and so is U \n\n ^(I am a bot, and this action was performed automatically. If you think this is a mistake, leave TheLetterH. If you still think this is a mistake, please) [^(contact me here.)](https://www.reddit.com/message/compose/?to=u-bot9000)'},
    {'name': 'theletteru', 'reply_text': 'egg'}
]

username_to_check = 'u-bot9000' # This is blunderful code but I dont want to change it

randomReply = [
    "H and U are both good. HU UNION!!!",
    "I love H, I also love U",
    "HU 👍",
    "H + U = 👍",
    "HEIJAK needs U",
    "H ❤️ U",
    "𝙃𝙐",
    "Move aside 𝕏, we have ℍ𝕌",
    "Ƕ"
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

def process_new_posts(subreddit_name, reply_text):
    subreddit = reddit.subreddit(subreddit_name)
    for submission in subreddit.stream.submissions(skip_existing=True):
        if submission.author and submission.author.name != username_to_check:
            prob = random.randint(0,1000)
            if prob == 1:
              probe = random.randint(0,10)
              if probe == 1:
                print("MEGA JACKPOT!!!")
                comment.reply("LUCKY U!!!! THIS COMMENT HAS A 1/10000 CHANCE OF HAPPENINQ!!!")
              else:
                print("JACKPOT")
                comment.reply("Lucky H! This comment has a 1/1000 chance of happeninq!")
            else:
              submission.reply(reply_text)
            print(f"Replied to the post with ID: {submission.id}")
            print(f"Post Title: {submission.title}")


# Create two threads for concurrent execution of the functions
thread_run = threading.Thread(target=run)
thread_process = threading.Thread(target=process_new_posts, args=('theletterh', 'H is cool, and so is U \n\n ^(I am a bot, and this action was performed automatically. If you think this is a mistake, leave TheLetterH. If you still think this is a mistake, please) [^(contact me here.)](https://www.reddit.com/message/compose/?to=u-bot9000)'))


# Start all threads
thread_run.start()
thread_process.start()


# Wait for all threads to finish
thread_run.join()
thread_process.join()
