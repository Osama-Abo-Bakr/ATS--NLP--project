keywords_dict = {
    "Data Science": [
        "Machine Learning", "Data Analysis", "Python", "Pandas", "NumPy",
        "Scikit-learn", "Deep Learning", "Statistics", "Data Visualization",
        "SQL", "TensorFlow", "Jupyter Notebook", "Big Data", "Data Wrangling"
    ],
    "HR": [
        "Talent Acquisition", "Recruitment", "Onboarding", "HR Policies",
        "Employee Engagement", "Payroll", "Performance Management", "HRIS",
        "Training and Development", "Labor Laws", "Conflict Resolution", "Workforce Planning"
    ],
    "Advocate": [
        "Legal Research", "Litigation", "Case Law", "Drafting", "Contracts",
        "Civil Law", "Criminal Law", "Court Procedures", "Legal Advice",
        "Negotiation", "Arbitration", "Legal Compliance"
    ],
    "Arts": [
        "Visual Arts", "Creative Design", "Painting", "Sculpture", "Art History",
        "Exhibition", "Adobe Photoshop", "Illustration", "Concept Development",
        "Portfolio", "Mixed Media", "Graphic Design"
    ],
    "Web Designing": [
        "HTML", "CSS", "JavaScript", "Responsive Design", "UI/UX", "Adobe XD",
        "Figma", "Bootstrap", "Web Accessibility", "SEO", "jQuery",
        "Wireframes", "Frontend Development"
    ],
    "Mechanical Engineer": [
        "AutoCAD", "SolidWorks", "Thermodynamics", "CAD/CAM", "HVAC",
        "Manufacturing Processes", "Mechanical Design", "FEA", "Engineering Drawing",
        "Product Development", "Quality Control", "Maintenance"
    ],
    "Sales": [
        "Lead Generation", "CRM", "Cold Calling", "Sales Funnel", "Negotiation",
        "B2B Sales", "Sales Strategy", "Market Research", "Client Relationship",
        "Sales Forecasting", "Business Development"
    ],
    "Health and fitness": [
        "Personal Training", "Nutrition", "Exercise Physiology", "Weight Management",
        "Workout Plans", "Physical Fitness", "Wellness Coaching", "CPR Certification",
        "Strength Training", "Group Training"
    ],
    "Civil Engineer": [
        "AutoCAD", "Structural Analysis", "Construction Management", "Site Supervision",
        "Concrete Technology", "Estimation", "Project Planning", "Building Codes",
        "Surveying", "Safety Management", "Design Software", "Quantity Takeoff"
    ],
    "Java Developer": [
        "Java", "Spring Boot", "Hibernate", "REST API", "Microservices",
        "JDBC", "Maven", "Multithreading", "OOP", "JSP", "Servlets",
        "JUnit", "Tomcat"
    ],
    "Business Analyst": [
        "Business Analysis", "Requirement Gathering", "Stakeholder Management",
        "Agile", "JIRA", "Use Cases", "Process Modeling", "Data Analysis",
        "SQL", "Wireframes", "SWOT Analysis", "Documentation"
    ],
    "SAP Developer": [
        "SAP ABAP", "SAP Fiori", "SAP HANA", "BAPI", "BADI", "ALV Reports",
        "SmartForms", "RFC", "Data Dictionary", "SAP Modules", "Workflow",
        "Enhancements"
    ],
    "Automation Testing": [
        "Selenium", "TestNG", "JUnit", "Automation Scripts", "WebDriver",
        "CI/CD", "Maven", "Bug Tracking", "Page Object Model", "Test Automation",
        "API Testing"
    ],
    "Electrical Engineering": [
        "Circuit Design", "Power Systems", "PLC", "SCADA", "Embedded Systems",
        "Microcontrollers", "MATLAB", "Load Flow Analysis", "Control Systems",
        "Electrical Safety", "Renewable Energy", "Energy Auditing"
    ],
    "Operations Manager": [
        "Operations Management", "Inventory Control", "Process Improvement",
        "Supply Chain", "Logistics", "Lean Management", "KPI Tracking",
        "Team Leadership", "Cost Reduction", "Scheduling", "Vendor Management"
    ],
    "Python Developer": [
        "Python", "Flask", "Django", "OOP", "REST APIs", "Pandas", "NumPy",
        "Web Scraping", "SQLAlchemy", "Git", "Unit Testing", "Multithreading"
    ],
    "DevOps Engineer": [
        "CI/CD", "Jenkins", "Docker", "Kubernetes", "Terraform", "AWS",
        "Monitoring", "Linux", "Shell Scripting", "Ansible", "Git", "Agile"
    ],
    "Network Security Engineer": [
        "Network Security", "Firewall", "IDS/IPS", "VPN", "SIEM", "Penetration Testing",
        "Threat Analysis", "Incident Response", "TCP/IP", "Encryption", "SOC", "Compliance"
    ],
    "PMO": [
        "Project Management", "Risk Management", "Resource Planning", "PMO Processes",
        "Stakeholder Communication", "Budget Management", "MS Project", "Agile",
        "Reporting", "Governance", "Timeline Tracking"
    ],
    "Database": [
        "SQL", "MySQL", "PostgreSQL", "Oracle", "Database Design", "Normalization",
        "Stored Procedures", "Indexing", "Data Backup", "Triggers", "ER Diagrams", "NoSQL"
    ],
    "Hadoop": [
        "Hadoop", "HDFS", "MapReduce", "Hive", "Pig", "Spark", "YARN", "Big Data",
        "Sqoop", "Oozie", "Data Lake", "Cloudera", "HBase"
    ],
    "ETL Developer": [
        "ETL", "Informatica", "SSIS", "Data Warehousing", "SQL", "Data Mapping",
        "Data Cleansing", "Data Integration", "Workflow Design", "Data Pipeline"
    ],
    "DotNet Developer": [
        ".NET", "C#", "ASP.NET", "MVC", "Entity Framework", "LINQ",
        "SQL Server", "WPF", "Web API", "Visual Studio", "Razor", "XAML"
    ],
    "Blockchain": [
        "Blockchain", "Ethereum", "Solidity", "Smart Contracts", "Web3", "Cryptography",
        "Decentralized Apps", "Consensus Algorithms", "IPFS", "Hyperledger", "Truffle", "Metamask"
    ],
    "Testing": [
        "Manual Testing", "Automation Testing", "Test Cases", "Bug Reporting",
        "Functional Testing", "Regression Testing", "Performance Testing",
        "JIRA", "Selenium", "Quality Assurance", "Test Plans"
    ]
}


class_labels = ['Advocate', 'Arts', 'Automation Testing', 'Blockchain',
                    'Business Analyst', 'Civil Engineer', 'Data Science',
                    'Database', 'DevOps Engineer', 'DotNet Developer',
                    'ETL Developer', 'Electrical Engineering', 'HR', 'Hadoop',
                    'Health and fitness', 'Java Developer', 'Mechanical Engineer', 
                    'Network Security Engineer', 'Operations Manager', 'PMO',
                    'Python Developer', 'SAP Developer', 'Sales', 'Testing', 'Web Designing']