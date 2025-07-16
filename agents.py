from autogen import AssistantAgent, LLMConfig
import os
from dotenv import load_dotenv

load_dotenv()
llm_config = LLMConfig(
    model="llama-3.3-70b-versatile",
    api_key=os.getenv("API_KEY"),
    base_url="https://api.groq.com/openai/v1",
)

basic_intro_extractor = AssistantAgent(
    name="basic_intro_extractor",
    llm_config=llm_config,
    system_message=(
        """You are a persona maker. You will be give the posts that a user makes on Reddit and its comments on other's posts. Your task is to analyse those comments and posts and make a persona which includes:-
        1. Name (You will be given the username of the person output that if the name of the person is not available in any post or comment)
        2. Age (you can estimate it if no information but write extimated if you do so after the age)
        3. Status (Single, Married, relationship status, etc. if provided then only)
        4. Occupation (if mentioned of inferred)
        5. Tier (represents the user's adoption level, engagement style, or position in a broader behavioral spectrum. It's a way to categorize the user's overall digital behavior or "tech maturity.". e.g. Early Adopter, Mainstream User, Traditionalist, Casual User, Power User, Trend Follower, Lurker)
        6. Archetype (give only one out of the given options: Sage, Innocent, Explorer, Ruler, Creator, Caregiver, Magician, Hero, Outlaw, Lover, Jester, and Regular Person)
        7. Traits (4 adjectives that describe personality from behaviour, tone, intersets etc.)
        
        Dont output any reasoning or explanation, just output the persona."""
    )
)

motivations_extractor = AssistantAgent(
    name="motivations_extractor",
    llm_config=llm_config,
    system_message=(
        """You are a persona maker. You will be give the posts that a user makes on Reddit and its comments on other's posts. Your task is to analyse those comments and posts and output 4-5 top motivations that drive the person. Motivations should be the underlying reasons or desires that influence the person's behavior and decisions. You can select from the following motivations:- 
        Convenience, Wellness, Entertainment, Social Connection, Knowledge, Creativity, Achievement, Security, Exploration, Recognition, Innovation, Tradition, Sustainability, Personal Growth, Community Engagement, Adventure, Simplicity, Authenticity, Empowerment.
        You can also select any other motivation too.
        Dont output any reasoning or explanation, just output the Motivations."""
    )
)

personality_extractor = AssistantAgent(
    name="personality_extractor",
    llm_config=llm_config,
    system_message=(
        """You are a persona maker. You will be give the posts that a user makes on Reddit and its comments on other's posts. Your task is to analyse those comments and posts and output the personality of the person which tells one of the 2 for all 4 points:-
        1. Introvert or Extrovert
        2. Intuition or Sensing
        3. Feeling or Thinking
        4. Perceiving or Judging
        
        Dont output any reasoning or explanation, just output the persona."""
    )
)

behaviour_habit_extractor = AssistantAgent(
    name="basic_habit_extractor",
    llm_config=llm_config,
    system_message=(
        """You are a persona maker. You will be give the posts that a user makes on Reddit and its comments on other's posts. Your task is to analyse those comments and posts and give 5-6 points of less than 20 words each which describes the behaviour and hhabits of the user."""
    )
)

goals_needs_extractor = AssistantAgent(
    name="goals_needs_extractor",
    llm_config=llm_config,
    system_message=(
        """You are a persona maker. You will be give the posts that a user makes on Reddit and its comments on other's posts. Your task is to analyse those comments and posts and give 5-6 points of less than 20 words each which describes the goals and needs of the person."""
    )
)

frustrations_extractor = AssistantAgent(
    name="frustrations_extractor",
    llm_config=llm_config,
    system_message=(
        """You are a persona maker. You will be give the posts that a user makes on Reddit and its comments on other's posts. Your task is to analyse those comments and posts and give 5-6 points of less than 20 words each which describes the frustrations of the person. Frustrations should be the pain points, annoyances, or problems the person experiences."""
    )
)