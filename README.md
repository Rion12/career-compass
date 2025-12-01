# Career Compass

![Diagram](./arch_diagram.png)


A multi-agent system built with Google Agent Development Kit (ADK) to help students find universities, check eligibility, calculate budgets, and manage applications with Human-in-the-Loop validation.

## Features

- **Career Advisor**: Initial consultation and geopolitical safety checks
- **University Researcher**: Search universities based on criteria
- **Financial Planner**: Detailed budget calculations
- **Application Manager**: Document validation (HITL) and application tracking

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Configure API key in `.env`:
```
GOOGLE_API_KEY=your_api_key_here
```

3. Run the application:
```bash
python run.py
```

## Architecture

See [architecture_description.md](architecture_description.md) for detailed system architecture.

## Project Structure

```
career_compass/
├── agent.py              # Root agent
├── prompt.py             # System prompts
├── sub_agents/
│   ├── advisor/          # Career Advisor
│   ├── researcher/       # University Researcher
│   ├── finance/          # Financial Planner
│   └── application/      # Application Manager
└── tools/
    └── adk_tools.py      # Shared tools
```


