# Hospital_Mangement_System
A database-driven Hospital Management System built with Python and MySQL, designed to simplify hospital operations such as patient management, doctor management, appointment scheduling, prescriptions, and billing.



Markdown
# Hospital Management System (HMS)

A modular, CLI-based Hospital Management System built with Python and MySQL following a 3-tier architecture (**Models**, **Services**, and **Menus**).

---

## 📂 Project Structure

```text
.
├── Database/
│   ├── db.py                 # MySQL connection setup & automatic table initializer
│   └── hms_databse.sql       # MySQL schema and tables script
├── menus/                    # CLI user interaction layers
│   ├── admin_menu.py
│   ├── billing_menu.py
│   ├── doctor_menu.py
│   ├── patient_menu.py
│   └── receptionist_menu.py
├── models/                   # Data classes / Entity representations
│   ├── admin.py
│   ├── billing.py
│   ├── doctor.py
│   ├── patient.py
│   └── receptionist.py
├── services/                 # Business logic & MySQL CRUD operations
│   ├── admin_service.py
│   ├── billing_services.py
│   ├── doctor_service.py
│   ├── patient_service.py
│   └── receptionist_service.py
├── main.py                   # Application entry point
└── README.md                 # Project documentation & team workflow
🔀 Branching Strategy (Protecting main)
We enforce a strict 3-Tier Branching Model to ensure stable production code:

🟢 main Branch (Production): Protected! Only contains fully tested, stable releases. Nobody commits or pushes directly to main.

🟡 develop Branch (Staging): Integration environment where all team features come together. Collaborators submit Pull Requests (PRs) here.

🔵 feature/* Branches: Individual workspace branches created by collaborators for assigned tasks.

Plaintext
[ feature/doctor-module ] ──(PR)──> [ develop ] ──(Team Lead Release)──> [ main ]
[ feature/billing-module] ──(PR)──┘
👥 Team Roles & Module Ownership
To prevent merge conflicts, each team member works only inside their assigned files:

👑 Team Lead (You)
Core Responsibilities: Core DB infrastructure, Admin module, entry point, code reviews, and releases (develop -> main).

Assigned Files:

Database/db.py

Database/hms_databse.sql

main.py

models/admin.py | services/admin_service.py | menus/admin_menu.py

💻 Collaborator 1: Doctor Module
Assigned Files:

models/doctor.py

services/doctor_service.py

menus/doctor_menu.py

💻 Collaborator 2: Patient & Receptionist Modules
Assigned Files:

models/patient.py & models/receptionist.py

services/patient_service.py & services/receptionist_service.py

menus/patient_menu.py & menus/receptionist_menu.py

💻 Collaborator 3: Billing Module
Assigned Files:

models/billing.py

services/billing_services.py

menus/billing_menu.py

🛢️ Database Setup & Usage Guide
1. Database Initialization
Make sure your local MySQL server is running. You can import the schema into MySQL Workbench or via terminal:

Bash
mysql -u root -p < Database/hms_databse.sql
2. Configure Local Credentials
Open Database/db.py and set your local MySQL connection parameters:

Python
DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "YOUR_MYSQL_PASSWORD",  # Enter your local MySQL password
    "database": "hms_db"
}
3. Verify DB Connection
Run db.py directly to confirm that your database connection works properly:

Bash
python Database/db.py
(If successful, you will see ✅ Database & tables ready! printed in the console).

🔄 Complete Git Workflow for Collaborators
Rule 0: Golden Rules
🛑 NEVER push to main or develop directly!

🛑 ALWAYS work inside a feature/ branch created from develop.

Step-by-Step Step Workflow
Step 1: Clone & Switch to develop
Bash
git clone <repository-url>
cd <repository-folder>
git checkout develop
git pull origin develop
Step 2: Create a Feature Branch from develop
Name your feature branch after your assigned module:

Bash
# Example for Doctor module contributor
git checkout -b feature/doctor-module

# Example for Billing module contributor
git checkout -b feature/billing-module
Step 3: Work on assigned files & Commit
Only modify files inside your assigned domain.

Bash
git add .
git commit -m "feat(doctor): completed doctor service CRUD operations"
Step 4: Keep your branch updated with develop
Before pushing, ensure your code has the latest changes from develop:

Bash
git fetch origin
git rebase origin/develop
Step 5: Push your Feature Branch
Bash
git push origin feature/your-module-name
Step 6: Create a Pull Request (PR) to develop
Go to GitHub repository.

Click Compare & pull request.

CRITICAL: Set base branch to develop (NOT main).

Request a review from the Team Lead.

🚀 Team Lead Release Protocol (Merging to main)
When all features in develop are tested and verified by the Team Lead:

Bash
# Team Lead merges stable develop code to main
git checkout main
git pull origin main
git merge develop
git push origin main
