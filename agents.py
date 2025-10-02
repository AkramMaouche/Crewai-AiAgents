from crewai import Agent 
from tools import tool
import os 
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

llm  =  ChatGoogleGenerativeAI(model = 'Gemeni-1.5-flash',
                               verbose = True,
                               temperature = 0.5,
                               google_api_key = os.getenv('GOOGLE_API_KEY'))

## Create a Senior blog content Creator 
blog_reseacher = Agent(
    role= 'Blog Reasearcher From Youtube videos',
    verbose= True,
    backstory=('Expert in Undrstanding videos in Ai DataScience, '
    'Machine learning and Generative Ai '),
    allow_delegation=True,
    memory =True,
    tools=[tool],
    llm=llm ,
    goal= 'get the relevent video content for topic {topic} from Yt channel '
    )


## Create a blog writer agent with YT tool 


blog_writer = Agent(
    role = "Blog writer",
    goal='Narrate compelling tech stories about the video {topic} from YT channel',
    verbose=True,
    memory=True,
    backstory= ("With a fair for simplifying complex topics, you craft " 
    "engaging narratives that captivate and educate , bringing new" 
    "discovries to light is an accessible manner"
    ),
    llm=llm,
    tools=[tool],
    allow_delegation=False 

)