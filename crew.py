from crewai import  Crew, Process
from agents import blog_reseacher, blog_writer 
from task import  researcher_task, write_task 


crew  = Crew(
    agents=[blog_reseacher, blog_writer],
    tasks=[researcher_task, write_task],
    process=Process.sequential,
    verbose=True, 
    memory= True, 
    cache=True, 
    max_rpm=10,
    share_crew=True
)


# Starting the task execution process 

result = crew.kickoff(inputs={'topic': 'AI vs ML VS DL VS Data Science'})
print(result)

