# API Documentation for CVE Tracker

## Endpoints

### 1. List All CVEs
**Endpoint**: `/cves/list`  
**Method**: `GET`  
**Description**: Retrieves a list of all CVEs.  

### 2. Get CVE Details
**Endpoint**: `/cves/<cve_id>`  
**Method**: `GET`  
**Description**: Retrieves details of a specific CVE based on its ID.  

### 3. Filter CVEs
**Endpoint**: `/cves/filter`  
**Method**: `GET`  
**Description**: Retrieves CVEs based on filter parameters.  
**Query Parameters**:  
- `cve_id`: Filter by CVE ID (e.g., `CVE-2023-0001`).  
- `year`: Filter by year (e.g., `2023`).  
- `score_min`: Minimum CVE score.  
- `score_max`: Maximum CVE score.  
- `last_modified_days`: CVEs modified in the last N days.  
