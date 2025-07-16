import post_comment_extractor
import agent_caller

profile_link = input("Enter the Reddit profile link: ")
username = profile_link.strip("/").split("/")[-1]

posts, comments = post_comment_extractor.get_posts_comments(username)

post_and_comments_prompt = "Here are the posts made by the user:-\n"
for post in posts[:30]:
    post_and_comments_prompt += f"Post title: {post['title']}, Post content: {post['body']} \n"

post_and_comments_prompt += "Here are the comments made by the user and the post title and content of which comment was made:-\n"
for comment in comments[:30]:
    post_and_comments_prompt += f"Comment: {comment['comment']}, Post title: {comment['post_title']}, Post content: {comment['post_body']} \n"
print(username)
agent_caller.intro(post_and_comments_prompt, username)
agent_caller.motivations(post_and_comments_prompt, username)
agent_caller.personality(post_and_comments_prompt, username)
agent_caller.behaviour_habit(post_and_comments_prompt, username)
agent_caller.goals_needs(post_and_comments_prompt, username)
agent_caller.frustrations(post_and_comments_prompt, username)

