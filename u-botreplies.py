import praw
import random
import threading
import time
from keep_alive import keep_alive

reddit = praw.Reddit(
    client_id="W1T_uV33O1NvXwmtVbwH-Q",
    client_secret="##################",
    user_agent="<console:u-bot9000:1.0>",
    username="u-bot9000",
    password="#########")

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

keep_alive()

def reply_to_replies():
    try:
        for comment in reddit.inbox.comment_replies():
            if comment.author and comment.author.name != username_to_check:
                # Check if the comment has replies
                comment.refresh()
                replies_to_comment = comment.replies
                
                # Check if there are any replies to the comment
                if not replies_to_comment:
                    body = comment.body  # Get the reply's body text
                    response = None  # Initialize response as None

                    # Check if the body contains specific phrases and set the response accordingly
                    for phrase, reply_text in phrases_and_responses.items():
                        if phrase in body:
                            response = reply_text
                            break  # Exit the loop if a matching phrase is found

                    # Check if a response is set and reply to the comment
                    if response:
                        comment.reply(response)
                        print(f"Replied to {comment.author.name}'s reply with: {response}")

                    # Sleep briefly to avoid rate limiting
                    time.sleep(5)
    
    except Exception as e:
        print(e)


reply_to_replies()
