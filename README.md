# RedditPersonaMaker

For a given reddit user profile link, a persona will be made for that user after analysing the user's posts and comments.

## To run the project:-
1. Install all the modules from the `requirements.txt` file.
2. Make a Reddit app and fill the credential details in `.env` file. You can make a reddit app from the link provided:- https://www.reddit.com/prefs/apps
3. Generate a groq API key and update in the `API_KEY` section of `.env` file.
4. Run the `main.py` file.

To change the LLM, navigate to `agents.py` file and change the LLM in `llm_config` section in top.

For a given user, two txt files will be create in the persona folder. One will be `<username>_persona.txt` and other `<username>_persona_with_citations.txt` which also contains the citations for each charactersitics of the persona.

PS: The profile links should follow the format: **https://www.reddit.com/user/<username>/**

You can find sample persona for the user https://www.reddit.com/user/kojied/ and https://www.reddit.com/user/Hungry-Move-6603/comments/ in the persona folder.
