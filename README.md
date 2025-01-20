# NVD-Assesment
Project Overview
The CVE Tracker is a web application that retrieves vulnerability data from the NVD API, processes it, and displays it in an interactive user interface. It allows users to:

View a list of CVEs.
Search for CVEs by ID, year, or score.
Sync and store CVE data in a local database.
View details of a specific CVE.
Features
Fetch CVE data from the NVD API and store it in a database.
Perform data cleansing and handle missing data fields.
Expose APIs for listing and filtering CVEs.
Frontend UI with:
Interactive tables.
Dynamic navigation for CVE details.
Periodic data synchronization support.
Project Structure
graphql
Copy code
project-folder/
│
├── backend/
│   ├── app.py                 # Flask app and route definitions
│   ├── database.py            # Database schema and configuration
│   └── api/
│       ├── cve_api.py         # Flask API endpoints for CVEs
│       └── utils.py           # Utilities for fetching and syncing CVE data
│       |__sync_service.py
├── frontend/
│   ├── index.html             # Main CVE list UI
│   ├── cve_details.html       # CVE details UI
│   ├── styles.css             # CSS for styling the UI
│   └── script.js              # JavaScript for frontend interactions
│
├── tests/
│   └── test_api.py            # Unit tests for backend APIs
│
├── requirements.txt           # Python dependencies
└── README.md                  # Project documentation
TECHNOLOGIES USED:
BACKEND:
Python 3.x
Flask (REST API framework)
SQLAlchemy (ORM for database management)
SQLite (Database)
FRONTEND:
HTML, CSS, JavaScript
Fetch API for HTTP requests
Testing
Pytest
####
Step 1: Clone the Repository
Clone the project repository to your local machine:

bash
Copy code
git clone <repository-url>
cd project-folder
Step 2: Set Up the Backend
Install Dependencies:
bash
Copy code
pip install -r requirements.txt
Initialize the Database: Run the following script to create the cve_data.db database:
bash
Copy code
python backend/database.py
Step 3: Run the Backend Server
Start the Flask server:
bash
Copy code
python backend/app.py
Open your browser and visit:
http://127.0.0.1:5000/cves/list – To list all CVEs (API endpoint).
http://127.0.0.1:5000/cves/<cve_id> – To fetch a specific CVE (replace <cve_id> with an actual CVE ID).
Step 4: Sync CVE Data
Open the Python REPL:
bash
Copy code
python
Run the following commands to fetch and store CVE data:
python
Copy code
from backend.api.utils import sync_cves
sync_cves()
Step 5: Set Up the Frontend
Navigate to the frontend directory:
bash
Copy code
cd frontend
Start a local HTTP server:
bash
Copy code
python -m http.server 8000
Open your browser and visit:
http://127.0.0.1:8000/index.html – Main CVE list page.
Step 6: Run Tests
Run all unit tests using pytest:
bash
Copy code
pytest

LISTING ALL THE CVE details.

LISTING ALL THE CVE details.
OUTPUTS:
##one test case failed
![image alt](https://github.com/manasikonidala/NVD-assesment/blob/335d9cafb5658f7e7dc9d8ef2eed7ea2767a6414/WhatsApp%20Image%202025-01-11%20at%2017.08.10%20(1).jpeg)
##two test cases passed 
![image alt](https://github.com/manasikonidala/NVD-assesment/blob/bafd726fb0ebed05c8130ecc0746a51e0d5d72c5/WhatsApp%20Image%202025-01-11%20at%2017.08.10.jpeg)
##two test cases failed
![image alt](https://github.com/manasikonidala/NVD-assesment/blob/5f3ffb89f0e3c2d616ef399ee0ff8086fcfd00d4/WhatsApp%20Image%202025-01-11%20at%2017.08.11%20(1).jpeg)
##two cases passed
![image alt](https://github.com/manasikonidala/NVD-assesment/blob/9414044c59a1b53c42097a42d25e1e2cb874f03d/WhatsApp%20Image%202025-01-11%20at%2017.08.12.jpeg)
#display of cve data outputs
![image alt](https://github.com/manasikonidala/NVD-assesment/blob/86d768a3c76f93dce1a2c7867bd022ac18d47ea8/WhatsApp%20Image%202025-01-11%20at%2017.08.27.jpeg)




