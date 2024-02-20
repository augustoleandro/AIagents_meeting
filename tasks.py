from textwrap import dedent
from crewai import Task

class MeetingPreparationTasks():
	def research_task(self, agent, participants, context):
		return Task(
			description=dedent(f"""\
				Conduza uma pesquisa abrangente sobre cada um dos indivíduos e empresas
				envolvidos na reunião. Reúna informações sobre notícias recentes,
				conquistas, histórico profissional e quaisquer atividades comerciais
				relevantes.

				Participantes: {participants}
				Contexto da Reunião: {context}"""),
			expected_output=dedent("""\
				Um relatório detalhado resumindo as principais descobertas sobre cada
				participante e empresa, destacando informações relevantes para a reunião."""),
			async_execution=True,
			agent=agent
		)

	def industry_analysis_task(self, agent, participants, context):
		return Task(
			description=dedent(f"""\
				Analise as tendências, desafios e oportunidades da indústria atual
				relevantes para o contexto da reunião. Considere relatórios de mercado,
				desenvolvimentos recentes e opiniões de especialistas para fornecer
		      	uma visão abrangente do cenário da indústria.

				Participantes: {participants}
				Contexto da Reunião: {context}"""),
			expected_output=dedent("""\
				Uma análise perspicaz que identifica as principais tendências, desafios
				e oportunidades potenciais."""),
			async_execution=True,
			agent=agent
		)

	def meeting_strategy_task(self, agent, context, objective):
		return Task(
			description=dedent(f"""\
				Desenvolva pontos de discussão estratégicos, perguntas perspicazes e
				ângulos de discussão para a reunião com base na pesquisa e análise
				da indústria realizada.
		      
				Contexto da Reunião: {context}
				Objetivo da Reunião: {objective}"""),
			expected_output=dedent("""\
				Complete report with a list of key talking points, strategic questions
				to ask to help achieve the meetings objective during the meeting."""),
			agent=agent
		)

	def summary_and_briefing_task(self, agent, context, objective):
		return Task(
			description=dedent(f"""\
				Resuma todas as descobertas da pesquisa, análise da indústria e
				pontos de discussão estratégicos em um documento de resumo abrangente
				para a reunião. Garanta que o resumo seja fácil de digerir e
				equipado com todas as informações e estratégias necessárias.

				Contexto da Reunião: {context}
				Objetivo da Reunião: {objective}"""),
			expected_output=dedent("""\
				Um documento de briefing bem estruturado que inclui seções para
				bios dos participantes, visão geral da indústria, pontos de discussão
				e recomendações estratégicas."""),
			agent=agent
		)