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

# 🎯 Problem Statement (Pain Points)

Students aspiring to study abroad face a complex, overwhelming, and often expensive decision-making process. Key challenges include:

- Difficulty selecting universities based on entrance exam scores, global rankings, job outcomes, part-time work opportunities, tuition fees, and accommodation options.
- Confusion around which course aligns best with career goals.
- High cost associated with studying abroad, including preparation, applications, and paying large sums to career consultants.
- Lack of a faster, more affordable, and transparent approach to planning international education.
- Concerns about employability, especially regarding job opportunities after completing a master’s program.
- Uncertainty about which countries are best suited for specific courses or specializations.
- Difficulty identifying universities with strong niche or specialized programs (e.g., Gaming, AI, Cybersecurity).
- Limited clarity on available scholarships and eligibility requirements across countries and courses.
- Manually sifting through thousands of university websites, course syllabi, and admission criteria is time-consuming, error-prone, and mentally exhausting.
- Students today face a paralyzing mix of **Academic Choice Overload** and **Global Geopolitical Uncertainty**, making high-stakes master’s decisions feel risky and confusing.

---

# 🚀 Solution Statement — *Career Compass*

Career Compass is designed to simplify and accelerate the entire study-abroad decision journey through an intelligent, human-friendly system.

### 🔍 Key Features

- Asks the user about course preferences, study location, duration, mode of study (offline, online, hybrid), and personal constraints in a natural conversational format.
- Collects the user’s educational background and work experience to assess eligibility across programs and countries.
- Provides a list of university options tailored to the user's goals, preferences, and constraints.
- Generates a complete **budget summary**, including:
  - Entrance test fees  
  - Application fees  
  - Visa fees  
  - Tuition fees  
  - Accommodation  
  - Insurance  
  - Scholarships and fee-reduction opportunities  
  - Additional living costs
- Helps students identify countries and universities where their chosen course is strongest.
- Saves time, money, and effort by eliminating the need for expensive consultants and manual research.

---

## ✅ Next Steps

1. **Replace mock data with real-time data**
   - Integrate APIs and reliable data sources to fetch up-to-date information on universities, courses, fees, and scholarships.

2. **Improve the Application Manager Agent workflow**
   - Refine the end-to-end application flow, including shortlisting, tracking deadlines, document checklists, and status updates.

3. **Enhance and refine prompts**
   - Optimize system and user prompts for better context understanding, more accurate recommendations, and a smoother conversational experience.
---





