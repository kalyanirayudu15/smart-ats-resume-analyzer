

import re

COMMON_SKILLS = [
    # Programming languages
    "Python", "Java", "C", "C++", "C#", "JavaScript",
    "TypeScript", "PHP", "Ruby", "Go", "Golang", "R",
    "Kotlin", "Swift", "Rust", "Scala", "MATLAB", "Dart",
    "SQL", "PL/SQL", "Bash", "PowerShell",

    # Web development
    "HTML", "HTML5", "CSS", "CSS3", "React", "Angular",
    "Vue.js", "Node.js", "Express.js", "Next.js", "Bootstrap",
    "Tailwind CSS", "jQuery", "REST API", "GraphQL",
    "JSON", "XML", "AJAX", "Web Development",

    # Python frameworks and libraries
    "FastAPI", "Django", "Flask", "Streamlit", "Tkinter",
    "Pydantic", "SQLAlchemy", "Pytest", "Selenium",
    "BeautifulSoup", "Requests", "OpenCV",

    # Databases
    "MySQL", "PostgreSQL", "SQLite", "MongoDB", "Oracle",
    "SQL Server", "Microsoft SQL Server", "Redis", "Cassandra",
    "Firebase", "DynamoDB", "MariaDB", "Database Management",

    # Data science and analytics
    "Pandas", "NumPy", "Matplotlib", "Seaborn", "Plotly",
    "Scikit-learn", "SciPy", "TensorFlow", "PyTorch",
    "Keras", "Machine Learning", "Deep Learning",
    "Natural Language Processing", "NLP", "Computer Vision",
    "Data Analysis", "Data Analytics", "Data Science",
    "Data Visualization", "Statistics", "Probability",
    "Feature Engineering", "Data Cleaning", "Data Preprocessing",
    "Exploratory Data Analysis", "Predictive Modeling",
    "Regression", "Classification", "Clustering",
    "Generative AI", "Large Language Models", "LLM",
    "Prompt Engineering", "Semantic Search",

    # Cloud and DevOps
    "AWS", "Microsoft Azure", "Azure", "Google Cloud",
    "GCP", "Docker", "Kubernetes", "Jenkins", "Terraform",
    "GitHub Actions", "CI/CD", "Linux", "Unix",
    "Nginx", "Apache", "DevOps", "Cloud Computing",

    # Tools and version control
    "Git", "GitHub", "GitLab", "Bitbucket", "Jupyter",
    "Jupyter Notebook", "Anaconda", "VS Code", "Visual Studio Code",
    "Postman", "Swagger", "Power BI", "Tableau", "Excel",
    "Microsoft Excel", "Advanced Excel", "Google Sheets",
    "Microsoft Office", "Figma",

    # Software engineering and testing
    "Object-Oriented Programming", "OOP", "Data Structures",
    "Algorithms", "DBMS", "Operating Systems",
    "Computer Networks", "Software Development",
    "Agile", "Scrum", "SDLC", "Unit Testing",
    "Integration Testing", "Manual Testing", "Automation Testing",
    "API Testing", "Functional Testing", "Regression Testing",
    "Test Cases", "Bug Tracking", "JIRA",
    "Problem Solving", "Debugging",

    # Enterprise systems and other technologies
    "SAP", "SAP HANA", "SAP Business One", "ERP",
    "ERPNext", "Microsoft Dynamics", "Blockchain",
    "Cybersecurity", "Networking", "Data Entry",
    "Technical Support", "Troubleshooting"
]


def extract_skills(text):
    if not text:
        return []

    text = text.lower()
    found_skills = []

    for skill in COMMON_SKILLS:
        pattern = (
            r"(?<!\w)"
            + re.escape(skill.lower())
            + r"(?!\w)"
        )

        if re.search(pattern, text):
            found_skills.append(skill)

    return found_skills