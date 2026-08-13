from langchain_community.tools.shell.tool import ShellTool


shell_tool = ShellTool()

results = shell_tool.invoke("whoami")

print(results)