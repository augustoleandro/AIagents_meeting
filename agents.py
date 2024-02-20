from textwrap import dedent
from crewai import Agent

from tools.ExaSearchTool import ExaSearchTool

class MeetingPreparationAgents():
	def research_agent(self):
		return Agent(
			role='Especialista em Pesquisa',
			goal='Conduza todo o processo de pesquisa sobre as pessoas e empresas participantes da reunião.',
			tools=ExaSearchTool.tools(),
			backstory=dedent("""\
					Como Especialista em Pesquisa, sua missão é descobrir informações detalhadas
					sobre as pessoas e empresas que participam da reunião. Suas percepções
					estabelecerão as bases para a preparação estratégica da reunião."""),
			verbose=True
		)

	def industry_analysis_agent(self):
		return Agent(
			role='Analista de Indústria',
			goal='Analisar as tendências, desafios e oportunidades da indústria.',
			tools=ExaSearchTool.tools(),
			backstory=dedent("""\
					Como Analista de Indústria, sua análise identificará as principais tendências,
					desafios enfrentados pela indústria e oportunidades potenciais que
					poderiam ser aproveitadas durante a reunião para vantagem estratégica."""),
			verbose=True
		)

	def meeting_strategy_agent(self):
		return Agent(
			role='Estrategista de Reunião',
			goal='Desenvolver pontos de discussão, perguntas e visões estratégicas para a reunião.',
			tools=ExaSearchTool.tools(),
			backstory=dedent("""\
					Como Estrategista de Reunião, sua experiência orientará o desenvolvimento
					de pontos de discussão, perguntas perspicazes e visões estratégicas
					para garantir que os objetivos da reunião sejam alcançados."""),
			verbose=True
		)

	def summary_and_briefing_agent(self):
		return Agent(
			role='Coordenador de Resumo e Briefing',
			goal='Consolidar a pesquisa, análise e insights estratégicos.',
			tools=ExaSearchTool.tools(),
			backstory=dedent("""\
					Coordenador de Resumo e Briefing, seu papel é consolidar a pesquisa,
					análise e insights estratégicos."""),
			verbose=True
		)