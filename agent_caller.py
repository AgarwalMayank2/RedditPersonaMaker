import agents


def helper(response, username):
    response = response.strip('\n')
    with open(f"persona/{username}_persona.txt", "a", encoding="utf-8") as f:
        f.write(response.split("Citations:")[0])
    with open(f"persona/{username}_persona_with_citations.txt", "a", encoding="utf-8") as f:
        f.write(response + '\n\n')


def intro(post_and_comments_prompt, username):
    prompt = f"The username of a person on reddit is {username}. Make a persona of this person based on the posts and comments made by this person given below.\n"
    prompt += post_and_comments_prompt

    prompt += """Ouput the persona in the following format:
    Name:
    Age:
    Occupation:
    Status:
    Tier:
    Archetype:
    Traits:
    
    Also provide me citations for each and every point you provide in the following format:
    Citations:
    Posts:
    <The posts from which you got the information. If you got the information from multiple posts then provide all of them in different lines.>
    Comments:
    <The comments from which you got the information. If you got the information from multiple comments then provide all of them in different lines.>

    Dont use any '#' or '*' in the output."""
    response = agents.basic_intro_extractor.generate_reply(
        messages = [{'role' : 'user', 'content' : prompt}]
    )
    response = response.strip('\n')
    with open(f"persona/{username}_persona.txt", "w", encoding="utf-8") as f:
        f.write(response.split("Citations:")[0])
    with open(f"persona/{username}_persona_with_citations.txt", "w", encoding="utf-8") as f:
        f.write(response + '\n\n')

def motivations(post_and_comments_prompt, username):
    prompt = f"Give the personality of the person for which post and comments made by him on reddit are given below.\n"
    prompt += post_and_comments_prompt

    prompt += """Ouput the persona in the following format:
    Motivations:
    <Motivations in the form of points>
    Output the text simply wihthout using any '*' and dont number points.

    Also provide me citations for each and every point you provide in the following format:
    Citations:
    Posts:
    <The posts from which you got the information. If you got the information from multiple posts then provide all of them in different lines.>
    Comments:
    <The comments from which you got the information. If you got the information from multiple comments then provide all of them in different lines.>

    Dont use any '#' or '*' in the output."""
    response = agents.motivations_extractor.generate_reply(
        messages = [{'role' : 'user', 'content' : prompt}]
    )
    helper(response, username)

def personality(post_and_comments_prompt, username):
    prompt = f"Give the personality of the person for which post and comments made by him on reddit are given below.\n"
    prompt += post_and_comments_prompt

    prompt += """Ouput the persona in the following format:
    Personality:
    Introvert or Extrovert
    Intuition or Sensing
    Feeling or Thinking
    Perceiving or Judging.

    Also provide me citations for each and every point you provide in the following format:
    Citations:
    Posts:
    <The posts from which you got the information. If you got the information from multiple posts then provide all of them in different lines.>
    Comments:
    <The comments from which you got the information. If you got the information from multiple comments then provide all of them in different lines.>

    Dont use any '#' or '*' in the output."""
    response = agents.personality_extractor.generate_reply(
        messages = [{'role' : 'user', 'content' : prompt}]
    )
    helper(response, username)

def behaviour_habit(post_and_comments_prompt, username):
    prompt = f"Give 5-6 points on persons behaviour and habits based on the posts and comments made by this person given below.\n"
    prompt += post_and_comments_prompt

    prompt += """Ouput in the following format:
    Behaviour and Habits:
    <your points here>
    Output the text simply wihthout using any '*' and number your points.
    
    Also provide me citations for each and every point you provide in the following format:
    Citations:
    Posts:
    <The posts from which you got the information. If you got the information from multiple posts then provide all of them in different lines.>
    Comments:
    <The comments from which you got the information. If you got the information from multiple comments then provide all of them in different lines.>

    Dont use any '#' or '*' in the output."""
    response = agents.behaviour_habit_extractor.generate_reply(
        messages = [{'role' : 'user', 'content' : prompt}]
    )
    helper(response, username)

def goals_needs(post_and_comments_prompt, username):
    prompt = f"Give 5-6 points on person's goals and needs based on the posts and comments made by this person given below.\n"
    prompt += post_and_comments_prompt

    prompt += """Ouput in the following format:
    Goals and Needs:
    <your points here>
    Output the text simply wihthout using any '*' and number your points.
    
    Also provide me citations for each and every point you provide in the following format:
    Citations:
    Posts:
    <The posts from which you got the information. If you got the information from multiple posts then provide all of them in different lines.>
    Comments:
    <The comments from which you got the information. If you got the information from multiple comments then provide all of them in different lines.>

    Dont use any '#' or '*' in the output."""
    response = agents.goals_needs_extractor.generate_reply(
        messages = [{'role' : 'user', 'content' : prompt}]
    )
    helper(response, username)

def frustrations(post_and_comments_prompt, username):
    prompt = f"Give 5-6 points on person's frustrations based on the posts and comments made by this person given below.\n"
    prompt += post_and_comments_prompt

    prompt += """Ouput in the following format:
    Frustrations:
    <your points here>
    Output the text simply wihthout using any '*' and number your points.
    
    Also provide me citations for each and every point you provide in the following format:
    Citations:
    Posts:
    <The posts from which you got the information. If you got the information from multiple posts then provide all of them in different lines.>
    Comments:
    <The comments from which you got the information. If you got the information from multiple comments then provide all of them in different lines.>

    Dont use any '#' or '*' in the output."""
    response = agents.frustrations_extractor.generate_reply(
        messages = [{'role' : 'user', 'content' : prompt}]
    )
    helper(response, username)