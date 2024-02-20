import os, re
from dotenv import load_dotenv
from exa_py import Exa
from langchain.agents import tool
from typing import List

load_dotenv()


class ExaSearchTool:
	@tool
	def search(query: str):
		"""Search for a webpage based on the query."""
		print("search")
		search = ExaSearchTool._exa().search(f"{query}", use_autoprompt=True, num_results=3)
		return str(search)

	@tool
	def find_similar(url: str):
		"""Search for webpages similar to a given URL.
		The url passed in should be a URL returned from `search`.
		"""
		print("find_similar")
		return ExaSearchTool._exa().find_similar(url, num_results=3)

	@tool
	def get_contents(ids: str):
		"""Get the contents of a webpage.
		The ids must be passed in as a list, a list of ids returned from `search`.
		"""
		ids = re.findall(r"ID: (\S+)", ids)
		contents = str(ExaSearchTool._exa().get_contents(ids=ids, text=True))
		contents = contents.split("URL:")
		contents = [content[:1000] for content in contents]
		return "\n\n".join(contents)

	def tools():
		return [ExaSearchTool.search, ExaSearchTool.find_similar, ExaSearchTool.get_contents]

	def _exa():
		return Exa(api_key=os.getenv("EXA_API_KEY"))


