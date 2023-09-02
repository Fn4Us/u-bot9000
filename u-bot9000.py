import praw
import random
import threading
from keep_alive import keep_alive

reddit = praw.Reddit(
    client_id="W1T_uV33O1NvXwmtVbwH-Q",
    client_secret="#####################",
    user_agent="<console:u-bot9000:1.0>",
    username="u-bot9000",
    password="############")

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

keep_alive() # Do you need to know?

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
            submission.reply(reply_text)
            print(f"Replied to the post with ID: {submission.id}")
            print(f"Post Title: {submission.title}")

def reply_to_specific_phrase(username_to_check):
    try:
        for comment in reddit.inbox.comment_replies(skip_existing=True, stream=True):
            if comment.parent().author == username_to_check:
                body = comment.body  # Get the reply's body text
                response = None  # Initialize response as None
                
                # Check if the reply contains specific phrases and set the response accordingly
                if "!a_useless_name" in body:
                    response = "Its a joke \n \n It seems you forgot the I in ai"
                elif "!anarchy" in body:
                    response = "Qooqle en passant \n \nHoly Hell!\n \nNew response just dropped\n \nActual Zombie!\n \n Call the exorcist!\n \nPawn storm incoming!\n \nQueen sacrifice, anyone?\n \nBishop takes a vacation, never comes back."
                elif "good bot" in body.lower():
                    response = "Thanks bro, good human"
                elif "!github" in body:
                    response = "https://github.com/Fn4Us/u-bot9000/tree/main"
                
                # If a response is set, reply to the reply
                if response:
                    comment.reply(response)
                    print(f"Replied to {comment.author.name}'s reply with: {response}")
    except Exception as e:
        print(e)

# Create two threads for concurrent execution of the functions
thread_run = threading.Thread(target=run)
thread_process = threading.Thread(target=process_new_posts, args=('theletterh', 'H is cool, and so is U \n\n ^(I am a bot, and this action was performed automatically. If you think this is a mistake, leave TheLetterH. If you still think this is a mistake, please) [^(contact me here.)](https://www.reddit.com/message/compose/?to=u-bot9000)'))
thread_specific_phrase = threading.Thread(target=reply_to_specific_phrase, args=("target_redditor",))

# Start all threads
thread_run.start()
thread_process.start()
thread_specific_phrase.start()

# Wait for all threads to finish
thread_run.join()
thread_process.join()
thread_specific_phrase.join()
