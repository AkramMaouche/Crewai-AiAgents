from crewai import Crew, Task
from agents import blog_reseacher, blog_writer 
from tools import yt_Tool 


researcher_task = Task(
    agent= blog_reseacher, 
    description= ('identify the video {topic}'
    "get detailed information about the video from the youtube channels" ),
    expected_output="A comprehensive 3 paragraph long report base on the {topic} of video content  ",
    tools= [yt_Tool]
    )

write_task = Task(
    agent= blog_writer, 
    description= ("get the information from the youtube channels on the topic {topic}" ),
    expected_output=" Summarize the info from the yutube channel video on the topic {topic} and create the content for the blog",
    tools= [yt_Tool],
    async_execution= False  
    output_file= 'new-blog-post.md '
    )
