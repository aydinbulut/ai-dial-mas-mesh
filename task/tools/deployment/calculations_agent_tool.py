from typing import Any

from task.tools.deployment.base_agent_tool import BaseAgentTool


class CalculationsAgentTool(BaseAgentTool):

    #TODO:
    # Provide implementations of deployment_name (in core config), name, description and parameters.
    # Don't forget to mark them as @property
    # Parameters:
    #   - prompt: string. Required.
    #   - propagate_history: boolean
    @property
    def deployment_name(self) -> str:
        return "calculations-agent"
    
    @property
    def name(self) -> str:
        return "calculations-agent-tool"
    
    @property
    def description(self) -> str:
        return "Tool to call Calculations Agent, that can perform complex calculations, code execution, content management and web search in one call. It is powerful tool that can be used in different scenarios, for example, when you need to perform complex calculation with multiple steps, or when you need to perform calculation and then save result to content management system and then share it with other agents, or when you need to perform calculation and then find some information in web and then use this information in calculation."
    
    @property
    def parameters(self) -> dict[str, Any]:
        return {
            "type": "object",
            "properties": {
                "prompt": {
                    "type": "string",
                    "description": "The prompt for the Calculations Agent. Here you need to provide the full prompt with instructions and question for the agent. You can use this tool to call agent with different prompts, for example, you can call agent with prompt that is focused on code execution, and another time with prompt that is focused on complex calculations, it depends on your scenario.",
                },
                "propagate_history": {
                    "type": "boolean",
                    "description": "Whether to propagate the history of communication between this agent and the agent that we are calling. It means that if you set it to true, you will have history of communication between this agent and called agent in tool_call_history in custom content of assistant messages. It can be useful when you want to keep context of communication between agents, for example, when you have complex calculation with multiple steps and you want to keep context of this calculation in whole process."
                }
            },
            "required": ["prompt"]
        }