import openai
import os
from dotenv import load_dotenv

from crewai import Crew

from tasks import MeetingPreparationTasks
from agents import MeetingPreparationAgents


load_dotenv() 

openai.api_key = os.getenv('OPENAI_API_KEY')

tasks = MeetingPreparationTasks()
agents = MeetingPreparationAgents()

openai.api_key = os.getenv('OPENAI_API_KEY')

print("## Seja bem-vindo ao Agente de Reuniões ##")
print("------------------------------------")

participants = input("Quem são os participantes da reunião?\n")
context = input("Qual é o contexto da reunião?\n")
objective = input("Qual é o objetivo da reunião?\n")

# print(f"participants: {participants} | context: {context} | objective: {objective}")

researcher_agent = agents.research_agent()
industry_analyst_agent = agents.industry_analysis_agent()
meeting_strategy_agent = agents.meeting_strategy_agent()
summary_and_briefing_agent = agents.summary_and_briefing_agent()

research = tasks.research_task(researcher_agent, participants, context)
industry_analysis = tasks.industry_analysis_task(industry_analyst_agent, participants, context)
meeting_strategy = tasks.meeting_strategy_task(meeting_strategy_agent, context, objective)
summary_and_briefing = tasks.summary_and_briefing_task(summary_and_briefing_agent, context, objective)

crew = Crew(
    agents=[
        researcher_agent, 
        industry_analyst_agent,
        meeting_strategy_agent, 
        summary_and_briefing_agent
    ], 
    tasks=[
        research, 
        industry_analysis,
        meeting_strategy,
        summary_and_briefing
    ]
)

game = crew.kickoff()

print("## Resultado ##")
print(game)