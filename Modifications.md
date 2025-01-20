## Modification done in the updated version of code

1)Modified backend/api/utils.py to include batch synchronization functionality.
    ->To run this synchronization,  a script is added to backend/sync_service.py

2)Enhanced the existing API in backend/api/cve_api.py to support search and filter functionality.

3)API_documentation.md file is incorporated

4)Added tests for the new /cves/filter API in tests/test_api.py uder the function test_filter_cves

5)The issue "Consume the CVE information from the CVE API - The script is partially working" is resolved with the updates provided in the sync_cves function and the batch synchronization logic.

6)Accessing CVEs using API - Partially working 
->> this resolved this issue is addressed by the fetch_cves function was updated to include proper handling of pagination using startIndex and resultsPerPage to retrieve CVEs in smaller, manageable chunks.
->>The sync_cves function was updated to retrieve and process all CVEs by iterating over multiple chunks using the updated fetch_cves function.
