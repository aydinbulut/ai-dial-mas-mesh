from typing import Any

from task.tools.deployment.base_agent_tool import BaseAgentTool


class ContentManagementAgentTool(BaseAgentTool):

    # TODO:
    # Provide implementations of deployment_name (in core config), name, description and parameters.
    # Don't forget to mark them as @property

    @property
    def deployment_name(self) -> str:
        return "content-management-agent"

    @property
    def name(self) -> str:
        return "content-management-agent-tool"

    @property
    def description(self) -> str:
        return "Tool to call Content Management Agent, that can perform content management tasks, such as saving content to content management system, updating content in content management system, deleting content from content management system and sharing content with other agents. It is powerful tool that can be used in different scenarios, for example, when you need to save some information to content management system and then share it with other agents, or when you need to update some information in content management system and then share it with other agents, or when you need to delete some information from content management system and then share it with other agents."

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
                    "description": "The prompt for the Content Management Agent. Here you need to provide the full prompt with instructions and question for the agent. You can use this tool to call agent with different prompts, for example, you can call agent with prompt that is focused on saving content to content management system, and another time with prompt that is focused on updating content in content management system, it depends on your scenario.",
                },
                "propagate_history": {
                    "type": "boolean",
                    "description": "Whether to propagate the history of communication between this agent and the agent that we are calling. It means that if you set it to true, you will have history of communication between this agent and called agent in tool_call_history in custom content of assistant messages. It can be useful when you want to keep context of communication between agents, for example, when you have complex content management task with multiple steps and you want to keep context of this task in whole process."
                }
            },
            "required": ["prompt"]
        }
