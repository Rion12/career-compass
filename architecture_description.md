# Architecture

Core to Career Compass is the `Career_Compass` root agent -- a prime example of a multi-agent system. It's not a monolithic application but an ecosystem of specialized agents, each contributing to a different stage of the university selection and application process. This modular approach, facilitated by Google's Agent Development Kit, allows for a sophisticated and robust workflow. The central orchestrator of this system is the `Career_Compass` agent.

The `Career_Compass` agent is constructed using the [Agent] class from the Google ADK. Its definition highlights several key parameters: the name, the model it uses for its reasoning capabilities (`gemini-2.5-flash-lite`), and a detailed instruction set that governs its behavior. Crucially, it also defines the `sub_agents` it can delegate tasks to.

The real power of the `Career_Compass` lies in its team of specialized sub-agents, each an expert in its domain.

## Career Advisor: `Career_Advisor`

This agent is responsible for the initial user intake and providing geopolitical advice. It acts as the first point of contact, understanding the student's preferences for course, location, and budget. To ensure student safety, it utilizes the [check_geopolitics] tool to assess the stability and safety of preferred study destinations.

## University Researcher: `University_Researcher`

Once the student's preferences are clear, the `University_Researcher` takes over. This agent is an expert in academic institutions, capable of finding universities that match the user's specific criteria. It uses the [search_universities] tool to scan a database of institutions, filtering by course, location, and other factors to present a curated list of options.

## Financial Planner: `Financial_Planner`

The `Financial_Planner` is a specialized agent that handles the financial aspects of studying abroad. It takes a selected university and the user's budget to provide a detailed cost breakdown. Using the [calculate_budget] tool, it estimates tuition fees, living costs, and other expenses, helping the student understand the financial feasibility of their choice.

## Application Manager: `Application_Manager`

The `Application_Manager` oversees the final stages of the process. It assists with document validation and tracks the application status. This agent implements a Human-in-the-Loop (HITL) workflow using the [validate_sop] tool to review the student's Statement of Purpose and provide feedback. It also uses the [track_application]tool to simulate real-time updates on application progress.

## Essential Tools and Utilities

The `Career_Compass` and its sub-agents are equipped with a variety of tools to perform their tasks effectively.

### Geopolitical Analysis ([check_geopolitics]

A crucial tool for the Advisor agent, allowing it to retrieve up-to-date safety and stability information for various countries, ensuring students make informed decisions about where to study.

### University Search ([search_universities])

This tool powers the Researcher agent, enabling it to query a structured dataset of universities based on multiple parameters like course interest and location preference.

### Budget Calculation ([calculate_budget])

Used by the Financial Planner, this tool performs the necessary calculations to provide a comprehensive financial overview, including tuition and living expenses.

### Document Validation ([validate_sop])

A key component of the Application Manager, this tool simulates an automated review of the Statement of Purpose, ensuring it meets basic length and quality requirements before submission.

### Application Tracking ([track_application])

This tool allows the Application Manager to provide simulated status updates for submitted applications, adding a layer of realism to the user experience.
