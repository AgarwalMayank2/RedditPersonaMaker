import os
import praw
from dotenv import load_dotenv

load_dotenv()

reddit = praw.Reddit(
    client_id=os.getenv("CLIENT_ID"),
    client_secret=os.getenv("CLIENT_SECRET"),
    user_agent=os.getenv("USER_AGENT")
)

def get_user_data(username):
    redditor = reddit.redditor(username)
    posts = []
    comments = []

    try:
        for post in redditor.submissions.new(limit=50):
            posts.append({
                "title": post.title,
                "body": post.selftext
            })

        for comment in redditor.comments.new(limit=50):
            submission = comment.submission
            comments.append({
                "comment": comment.body,
                "post_title": submission.title,
                "post_body": submission.selftext
            })

    except Exception as e:
        print(f"Error retrieving data: {e}")

    return posts, comments

def get_posts_comments(username):
    posts, comments = get_user_data(username)
    return posts, comments