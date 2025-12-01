from google.adk.tools import FunctionTool
import json

# Mock Data
UNIVERSITIES = [
    {
        "name": "Tech Institute of Berlin",
        "location": "Berlin, Germany",
        "courses": ["Computer Science", "Data Science", "AI"],
        "tuition_fees": 1500,
        "living_cost": 900,
        "mode": "Offline",
        "duration": "2 Years"
    },
    {
        "name": "University of Toronto Online",
        "location": "Toronto, Canada",
        "courses": ["Business Analytics", "Computer Science"],
        "tuition_fees": 20000,
        "living_cost": 0,
        "mode": "Online",
        "duration": "1 Year"
    },

    # --- Ireland ---
    {
        "name": "Dublin Tech University",
        "location": "Dublin, Ireland",
        "courses": ["Cybersecurity", "AI", "Cloud Computing"],
        "tuition_fees": 18000,
        "living_cost": 1100,
        "mode": "Offline",
        "duration": "2 Years"
    },
    {
        "name": "Cork Institute of Technology",
        "location": "Cork, Ireland",
        "courses": ["Data Analytics", " Software Engineering"],
        "tuition_fees": 16000,
        "living_cost": 950,
        "mode": "Offline",
        "duration": "1.5 Years"
    },

    # --- USA ---
    {
        "name": "California Digital University",
        "location": "California, USA",
        "courses": ["AI", "Machine Learning", "Robotics"],
        "tuition_fees": 28000,
        "living_cost": 1600,
        "mode": "Offline",
        "duration": "2 Years"
    },
    {
        "name": "New York School of Technology",
        "location": "New York, USA",
        "courses": ["Cybersecurity", "IT Management"],
        "tuition_fees": 30000,
        "living_cost": 1800,
        "mode": "Offline",
        "duration": "2 Years"
    },
    {
        "name": "Seattle Online Tech University",
        "location": "Seattle, USA",
        "courses": ["Cloud Computing", "DevOps"],
        "tuition_fees": 12000,
        "living_cost": 0,
        "mode": "Online",
        "duration": "1 Year"
    },
    {
        "name": "Texas Global Institute",
        "location": "Texas, USA",
        "courses": ["Business Analytics", "Information Systems"],
        "tuition_fees": 20000,
        "living_cost": 1400,
        "mode": "Offline",
        "duration": "1.5 Years"
    },

    # --- Germany ---
    {
        "name": "Munich School of Engineering",
        "location": "Munich, Germany",
        "courses": ["Mechanical Engineering", "AI", "Computer Science"],
        "tuition_fees": 2000,
        "living_cost": 1000,
        "mode": "Offline",
        "duration": "2 Years"
    },
    {
        "name": "Hamburg Applied Sciences University",
        "location": "Hamburg, Germany",
        "courses": ["Data Engineering", "Software Development"],
        "tuition_fees": 2500,
        "living_cost": 950,
        "mode": "Offline",
        "duration": "2 Years"
    },

    # --- France ---
    {
        "name": "Paris Institute of Advanced Computing",
        "location": "Paris, France",
        "courses": ["AI", "Data Science", "Distributed Systems"],
        "tuition_fees": 9000,
        "living_cost": 1200,
        "mode": "Offline",
        "duration": "2 Years"
    },
    {
        "name": "Lyon School of Business Analytics",
        "location": "Lyon, France",
        "courses": ["Business Analytics", "AI"],
        "tuition_fees": 8000,
        "living_cost": 900,
        "mode": "Offline",
        "duration": "1.5 Years"
    },

    # --- UK ---
    {
        "name": "London Global Tech University",
        "location": "London, UK",
        "courses": ["Cybersecurity", "Cloud Computing", "AI"],
        "tuition_fees": 22000,
        "living_cost": 1300,
        "mode": "Offline",
        "duration": "1 Year"
    },
    {
        "name": "Manchester Computing Institute",
        "location": "Manchester, UK",
        "courses": ["Computer Science", "Machine Learning"],
        "tuition_fees": 18000,
        "living_cost": 1000,
        "mode": "Offline",
        "duration": "1 Year"
    },
    {
        "name": "Cardiff Online University",
        "location": "Cardiff, UK",
        "courses": ["Business Analytics", "Tech Management"],
        "tuition_fees": 9000,
        "living_cost": 0,
        "mode": "Online",
        "duration": "1 Year"
    },

    # --- Canada ---
    {
        "name": "Vancouver Institute of Technology",
        "location": "Vancouver, Canada",
        "courses": ["Software Engineering", "AI"],
        "tuition_fees": 21000,
        "living_cost": 1200,
        "mode": "Offline",
        "duration": "2 Years"
    },
    {
        "name": "Montreal Technical University",
        "location": "Montreal, Canada",
        "courses": ["Data Science", "Cloud Computing"],
        "tuition_fees": 18000,
        "living_cost": 850,
        "mode": "Offline",
        "duration": "2 Years"
    },
    {
        "name": "Ottawa Online University",
        "location": "Ottawa, Canada",
        "courses": ["Cybersecurity", "IT Governance"],
        "tuition_fees": 15000,
        "living_cost": 0,
        "mode": "Online",
        "duration": "1 Year"
    },

    # --- Russia ---
    {
        "name": "Moscow Institute of Information Systems",
        "location": "Moscow, Russia",
        "courses": ["Computer Science", "Cybersecurity"],
        "tuition_fees": 3500,
        "living_cost": 600,
        "mode": "Offline",
        "duration": "2 Years"
    },
    {
        "name": "St. Petersburg Technical Academy",
        "location": "St. Petersburg, Russia",
        "courses": ["AI", "Advanced Computing"],
        "tuition_fees": 3000,
        "living_cost": 550,
        "mode": "Offline",
        "duration": "2 Years"
    },

    # --- Ukraine ---
    {
        "name": "Kyiv Polytechnic International",
        "location": "Kyiv, Ukraine",
        "courses": ["Software Engineering", "Cyber Defense"],
        "tuition_fees": 2500,
        "living_cost": 400,
        "mode": "Offline",
        "duration": "2 Years"
    },
    {
        "name": "Lviv Institute of Data & AI",
        "location": "Lviv, Ukraine",
        "courses": ["Data Science", "AI", "Business Intelligence"],
        "tuition_fees": 2300,
        "living_cost": 350,
        "mode": "Offline",
        "duration": "1.5 Years"
    },

    # Extra entries to reach 25
    {
        "name": "Boston Online Global Tech",
        "location": "Boston, USA",
        "courses": ["AI", "Cloud Engineering"],
        "tuition_fees": 15000,
        "living_cost": 0,
        "mode": "Online",
        "duration": "1 Year"
    },
    {
        "name": "Edinburgh School of Computing",
        "location": "Edinburgh, UK",
        "courses": ["AI", "Software Systems"],
        "tuition_fees": 17000,
        "living_cost": 950,
        "mode": "Offline",
        "duration": "1 Year"
    },
    {
        "name": "Toulouse Aerospace & Tech Institute",
        "location": "Toulouse, France",
        "courses": ["Aerospace Computing", "AI"],
        "tuition_fees": 8500,
        "living_cost": 800,
        "mode": "Offline",
        "duration": "2 Years"
    }
]

GEOPOLITICAL_INFO = { "Germany": {
        "summary": "Stable. Safe for students. Strong economy and tech opportunities.",
        "risk_score": 2,
        "visa_friendliness": "Moderate",
        "student_safety_rating": 4.5
    },
    "Canada": {
        "summary": "Very stable. Highly welcoming to international students with strong PR pathways.",
        "risk_score": 2,
        "visa_friendliness": "Easy",
        "student_safety_rating": 4.7
    },
    "Ireland": {
        "summary": "Stable and student-friendly. Strong tech sector growth.",
        "risk_score": 2,
        "visa_friendliness": "Moderate",
        "student_safety_rating": 4.5
    },
    "USA": {
        "summary": "Stable with high opportunities. Safety varies regionally; immigration is competitive.",
        "risk_score": 3,
        "visa_friendliness": "Hard",
        "student_safety_rating": 4.0
    },
    "France": {
        "summary": "Stable overall. Occasional protests but generally safe for students.",
        "risk_score": 3,
        "visa_friendliness": "Moderate",
        "student_safety_rating": 4.2
    },
    "UK": {
        "summary": "Stable, strong universities. Post-Brexit rules stricter but manageable.",
        "risk_score": 3,
        "visa_friendliness": "Moderate",
        "student_safety_rating": 4.3
    },
    "Russia": {
        "summary": "High geopolitical tension. Mixed safety; not ideal for international students.",
        "risk_score": 7,
        "visa_friendliness": "Hard",
        "student_safety_rating": 3.0
    },
    "Ukraine": {
        "summary": "Currently unstable due to ongoing conflict. Not safe for international study.",
        "risk_score": 10,
        "visa_friendliness": "Hard",
        "student_safety_rating": 1.0
    },
    "Australia": {
        "summary": "Very stable. High-quality education and easy student pathways.",
        "risk_score": 2,
        "visa_friendliness": "Easy",
        "student_safety_rating": 4.7
    },
    "Netherlands": {
        "summary": "Stable and safe. Very popular among EU and international students.",
        "risk_score": 2,
        "visa_friendliness": "Moderate",
        "student_safety_rating": 4.6
    },
    "Sweden": {
        "summary": "Extremely safe, stable, innovative environment.",
        "risk_score": 1,
        "visa_friendliness": "Moderate",
        "student_safety_rating": 4.8
    },
    "Finland": {
        "summary": "Highly stable and education-focused. Very safe.",
        "risk_score": 1,
        "visa_friendliness": "Moderate",
        "student_safety_rating": 4.8
    },
    "Norway": {
        "summary": "Very stable and safe with top-tier living standards.",
        "risk_score": 1,
        "visa_friendliness": "Moderate",
        "student_safety_rating": 4.7
    },
    "Denmark": {
        "summary": "Stable and secure. Strong education and innovation culture.",
        "risk_score": 1,
        "visa_friendliness": "Moderate",
        "student_safety_rating": 4.7
    },
    "Japan": {
        "summary": "Stable, safe, technologically advanced.",
        "risk_score": 2,
        "visa_friendliness": "Moderate",
        "student_safety_rating": 4.8
    },
    "South Korea": {
        "summary": "Stable and modern. Excellent tech ecosystem.",
        "risk_score": 3,
        "visa_friendliness": "Moderate",
        "student_safety_rating": 4.5
    },
    "Singapore": {
        "summary": "Very stable, clean, and safe. Globally connected academic ecosystem.",
        "risk_score": 1,
        "visa_friendliness": "Easy",
        "student_safety_rating": 4.9
    },
    "UAE": {
        "summary": "Stable and fast-growing. Very safe for expatriates.",
        "risk_score": 2,
        "visa_friendliness": "Easy",
        "student_safety_rating": 4.8
    },
    "Qatar": {
        "summary": "Stable, wealthy, and modern. Safe for students.",
        "risk_score": 2,
        "visa_friendliness": "Moderate",
        "student_safety_rating": 4.7
    },
    "India": {
        "summary": "Stable with rapid economic growth. Safety varies by region.",
        "risk_score": 4,
        "visa_friendliness": "Easy",
        "student_safety_rating": 3.8
    },
    "China": {
        "summary": "Stable domestically. Growing education sector with increasing research influence.",
        "risk_score": 3,
        "visa_friendliness": "Hard",
        "student_safety_rating": 4.3
    },
    "Italy": {
        "summary": "Stable and relaxed environment. Affordable education.",
        "risk_score": 3,
        "visa_friendliness": "Moderate",
        "student_safety_rating": 4.2
    },
    "Spain": {
        "summary": "Stable, warm, and student-friendly.",
        "risk_score": 3,
        "visa_friendliness": "Moderate",
        "student_safety_rating": 4.4
    }
}

# Functions
def check_geopolitics(location: str) -> str:
    """Checks the geopolitical stability of a given location."""
    print(f"[Tool] Checking geopolitics for: {location}")
    for country, info in GEOPOLITICAL_INFO.items():
        if country.lower() in location.lower():
            return f"{country}: {info}"
    return f"{location}: Stability data not found."

def search_universities(course_interest: str, location_preference: str = "") -> str:
    """Searches for universities based on course interest and optional location."""
    print(f"[Tool] Searching universities for course: {course_interest}, location: {location_preference}")
    matches = []
    for uni in UNIVERSITIES:
        course_match = any(course_interest.lower() in c.lower() for c in uni["courses"])
        loc_match = True
        if location_preference:
            loc_match = location_preference.lower() in uni["location"].lower()
        if course_match and loc_match:
            matches.append(uni)
    return json.dumps(matches)

def calculate_budget(university_name: str, user_budget: float) -> str:
    """Calculates the budget for a specific university."""
    print(f"[Tool] Calculating budget for: {university_name}")
    uni = next((u for u in UNIVERSITIES if u["name"].lower() == university_name.lower()), None)
    if not uni:
        return "University not found."
    tuition = uni["tuition_fees"]
    living = uni["living_cost"] * 12
    total = tuition + living + 2000
    return json.dumps({
        "university": uni["name"],
        "total_cost": total,
        "within_budget": total <= user_budget,
        "breakdown": {"tuition": tuition, "living": living, "misc": 2000}
    })

def validate_sop(sop_text: str) -> str:
    """Validates the Statement of Purpose (SOP)."""
    print(f"[Tool] Validating SOP...")
    if len(sop_text) < 50:
        return "SOP is too short. Please elaborate on your goals."
    return "SOP looks good. Clear and concise."

def track_application(app_id: str) -> str:
    """Tracks the status of an application."""
    print(f"[Tool] Tracking application: {app_id}")
    return "Application Status: Under Review"

# Tool Objects
check_geopolitics_tool = FunctionTool(func=check_geopolitics)
search_universities_tool = FunctionTool(func=search_universities)
calculate_budget_tool = FunctionTool(func=calculate_budget)
validate_sop_tool = FunctionTool(func=validate_sop)
track_application_tool = FunctionTool(func=track_application)
