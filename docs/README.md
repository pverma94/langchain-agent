# LangChain Agent Project

A beginner-friendly project demonstrating the creation of an AI agent using the LangChain framework with OpenAI and Tavily search capabilities.

## Overview
This project builds a conversational AI agent that can answer questions using a search tool and maintain context across interactions. It uses Python, LangChain, OpenAI's GPT-4o-mini, and Tavily's search API.

## Prerequisites
- Python 3.8 or higher
- Git (for version control)
- An OpenAI API key (sign up at [platform.openai.com](https://platform.openai.com/))
- A Tavily API key (sign up at [tavily.com](https://tavily.com/))

## Setup Instructions
1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/langchain-agent.git
   cd langchain-agent

2. Create a Virtual Environment
   ```bash
   python -m venv env
   env\Scripts\activate

3. Install Dependencies
   ```bash 
   pip install -r requirements.txt

4. Configure Environment Variables
   - Create a .env file in the root directory.
   - Add your API keys:
   ```bash
   OPENAI_API_KEY=your-openai-api-key
   TAVILY_API_KEY=your-tavily-api-key

5. Run the Agent
   - The following script will test the agent with sample queries ("What is the capital of France?" and "What is its largest city?").
   ```bash
   python src/agent.py
   
## Usage
   - Modify src/agent.py to add more tools or customize the agent.
   - Use src/test_openai.py to test your OpenAI API connection.
   - Run in a Jupyter Notebook for interactive debugging

## Project Structure
langchain-agent/
├── src/
│   ├── agent.py          # Main AI agent script
│   └── test_openai.py    # OpenAI API test script
├── docs/
│   └── README.md         # Project documentation
├── .env                  # Environment variables (not tracked)
├── .gitignore            # Git ignore file
├── requirements.txt      # Project dependencies
└── LICENSE               # Optional license file

## Contributing
Feel free to fork this repository, make improvements, and submit pull requests. Issues and feature requests are welcome!

## License
MIT License (or choose your preferred license and update accordingly).