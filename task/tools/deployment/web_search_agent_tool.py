from typing import Any

from task.tools.deployment.base_agent_tool import BaseAgentTool


class WebSearchAgentTool(BaseAgentTool):

    #TODO:
    # Provide implementations of deployment_name (in core config), name, description and parameters.
    # Don't forget to mark them as @property

    @property
    def deployment_name(self) -> str:
        return "web-search-agent"
    
    @property
    def name(self) -> str:
        return "web-search-agent-tool"
    
    @property
    def description(self) -> str:
        return "Tool to call Web Search Agent, that can perform web search and find information in web for you. It is powerful tool that can be used in different scenarios, for example, when you need to find some information in web and then use this information in calculation or content management or code execution, or when you need to find some information in web and then share it with other agents."

    # Parameters:
    #   - prompt: string. Required.
    #   - propagate_history: boolean
    @property
    def parameters(self) -> dict[str, Any]:
        return {
            "type": "object",
            "properties": {
                "prompt": {
                    "type": "string",
                    "description": "The prompt for the Web Search Agent. Here you need to provide the full prompt with instructions and question for the agent. You can use this tool to call agent with different prompts, for example, you can call agent with prompt that is focused on finding some information in web and then use this information in calculation, and another time with prompt that is focused on finding some information in web and then use this information in content management, it depends on your scenario.",
                },
                "propagate_history": {
                    "type": "boolean",
                    "description": "Whether to propagate the history of communication between this agent and the agent that we are calling. It means that if you set it to true, you will have history of communication between this agent and called agent in tool_call_history in custom content of assistant messages. It can be useful when you want to keep context of communication between agents, for example, when you have complex task with multiple steps and you want to keep context of this task in whole process."
                }
            },
            "required": ["prompt"]
        }
