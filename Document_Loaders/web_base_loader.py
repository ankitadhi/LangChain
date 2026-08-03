from langchain_community.document_loaders import WebBaseLoader

loader = WebBaseLoader("https://python.langchain.com")

docs = loader.load()

print(docs[0].page_content[:500])


"""
figuration and file/data utilities can be used.
USER_AGENT environment variable not set, consider setting it to identify your requests.
LangChain overview - Docs by LangChainDocumentation IndexFetch the complete documentation index at: /llms.txtUse this file to discover all available pages before exploring further.Skip to main contentInterrupt is coming to NYC and London this fall. Join the builders, engineers, and teams shaping what's next for agents. Get your tickets →Docs by LangChain home pageBuildSearch...⌘KAsk AIGitHubTry LangSmithTry LangSmithSearch...NavigationLangChain overviewOverviewDeep AgentsLangChainLangGraphIntegr
"""