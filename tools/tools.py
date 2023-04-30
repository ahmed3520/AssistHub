from langchain.agents.tools import Tool
from langchain.chat_models import ChatOpenAI
from langchain.schema import (HumanMessage, SystemMessage)
import requests
import os
import pprint

pp = pprint.PrettyPrinter(depth=2)


class Tools():

  def __init__(self) -> None:
    self.tools = [
      Tool(
        name="Calculate Fibonacci",
        func=self.calculate_fibonacci,
        description=
        "Use this tool to calculate the Fibonacci sequence up to the given number."
      )
    ]

  def calculate_fibonacci(self, input):
    try:
      n = int(input)
      if n < 0:
        return "Please enter a non-negative integer."

      fib = [0, 1]
      while len(fib) < n + 1:
        fib.append(fib[-1] + fib[-2])

      return fib

    except ValueError:
      return "Please enter a valid integer."

  def add_tool(self, name, func, description):
    tool = Tool(name=name, func=func, description=description)
    self.tools.append(tool)
