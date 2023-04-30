# AssistHub AI Assistant

The AI Assistant is a customizable project that aims to make human life easier by performing various tasks based on user input and output via voice or chat.
It is designed to work with multiple agents that use Langchain, a language processing and understanding framework, to achieve a common objective. For now, we are building the core of the project which includes creating a user-friendly GUI and developing tools that users can create and add as per their needs.

## Features

- Cross-platform support for Windows, Linux, and Mac OS.
- User-friendly GUI for easy interaction via voice or chat.
- Language processing and understanding using Langchain, which leverages state-of-the-art language models such as OpenAI GPT-3 or GPT-4 and Hugging Face models.
- Customizable with tools that users can create and add as per their needs.

## Tools

Tools are a key feature of this project that allows users to customize the AI assistant as per their requirements.
A tool can be defined as a function or a script that performs a specific task using Langchain. For instance, a tool can be created to fetch the weather forecast, play music, or provide news updates. These tools can be added by the user using an editor in the program without editing the source code. Alternatively, developers can contribute by creating new tools and their functions and submitting them to the project repository.

## Installation

To run the project, follow these steps:

1. Clone the repository: `git clone https://github.com/ahmed3520/AssistHub.git`
2. Navigate to the project directory: `cd AssistHub`
3. Install the required dependencies
   - For the front-end (Electron): `npm install`
   - For the back-end(Python) you need to navigate to `cd backend` and install the dependencies: `pip install -r requirements.txt`
4. Run the project `npm start`

We are welcoming any developer to contribute to this project. Before contributing, please read the code of conduct and the contributing guide and make sure you understand the project idea. You can contribute by creating new tools and their functions, improving the current code, improving the README.md, create testing or reporting issues.

## License

This project is licensed under the Apache License - see the LICENSE file for details.
