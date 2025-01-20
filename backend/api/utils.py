import requests
import logging
import time
import schedule
from datetime import datetime
#from database import SessionLocal, CVE
from ..database import SessionLocal, CVE


API_URL = "https://services.nvd.nist.gov/rest/json/cves/2.0"

'''def fetch_cves(offset=0, limit=100):
    response = requests.get(API_URL, params={"startIndex": offset, "resultsPerPage": limit})
    data = response.json().get("vulnerabilities", [])
    return data'''

'''def sync_cves():
    db = SessionLocal()
    offset = 0
    limit = 100
    while True:
        cve_data = fetch_cves(offset, limit)
        if not cve_data:
            break

        for item in cve_data:
            cve_id = item["cve"]["id"]
            description = item["cve"]["descriptions"][0]["value"]
            published_date = datetime.fromisoformat(item["published"])
            last_modified_date = datetime.fromisoformat(item["lastModified"])
            base_score = item.get("metrics", {}).get("cvssMetricV3", {}).get("cvssData", {}).get("baseScore")

            # Upsert logic
            existing_cve = db.query(CVE).filter(CVE.cve_id == cve_id).first()
            if existing_cve:
                existing_cve.last_modified_date = last_modified_date
                existing_cve.base_score = base_score
            else:
                db.add(CVE(
                    cve_id=cve_id,
                    description=description,
                    published_date=published_date,
                    last_modified_date=last_modified_date,
                    base_score=base_score
                ))
        db.commit()
        offset += limit
    db.close()'''


API_URL = "https://services.nvd.nist.gov/rest/json/cves/2.0"

'''2 def fetch_cves(offset=0, limit=100):
    try:
        # Send the request to the API
        response = requests.get(API_URL, params={"startIndex": offset, "resultsPerPage": limit})

        # Log the response status code and content for debugging
        logging.debug(f"Response status code: {response.status_code}")
        logging.debug(f"Response content: {response.text}")

        # Check if the response is valid and contains JSON
        if response.status_code == 200:
            try:
                data = response.json()
                return data.get("vulnerabilities", [])
            except ValueError as e:
                logging.error(f"Error parsing JSON: {e}")
                return []
        else:
            logging.error(f"Request failed with status code {response.status_code}")
            return []

    except requests.exceptions.RequestException as e:
        logging.error(f"Request failed: {e}")
        return []'''


def fetch_cves(offset=0, limit=100):
    """
    Fetch CVEs from the NVD API with pagination.
    :param offset: The starting index for the data to fetch.
    :param limit: Number of records to fetch in a single request.
    :return: List of CVE data retrieved from the API.
    """
    try:
        response = requests.get(API_URL, params={"startIndex": offset, "resultsPerPage": limit})
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json().get("vulnerabilities", [])
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching CVEs: {e}")
        return []



def sync_cves_in_batches(batch_size=100, period_seconds=3600):
    """
    Synchronize CVE data in batch mode periodically.
    :param batch_size: Number of CVEs to fetch in each batch.
    :param period_seconds: Time period between each sync in seconds.
    """
    def job():
        print("Synchronizing CVEs in batches...")
        sync_cves(batch_size=batch_size)

    # Schedule the job to run periodically
    schedule.every(period_seconds).seconds.do(job)

    print(f"Periodic synchronization scheduled every {period_seconds} seconds.")
    while True:
        schedule.run_pending()
        time.sleep(1)



def sync_cves(batch_size=100):
    """
    Fetch CVE data from the NVD API and synchronize it with the database in batches.
    :param batch_size: Number of records to fetch in each batch.
    """
    db = SessionLocal()
    offset = 0

    while True:
        # Fetch data in chunks using the NVD API
        cve_data = fetch_cves(offset=offset, limit=batch_size)
        if not cve_data:
            print("No more data to fetch.")
            break

        for item in cve_data:
            cve_id = item["cve"]["id"]
            description = item["cve"]["descriptions"][0]["value"]

            # Safely access published and modified dates
            published_date = item.get("published")
            if published_date:
                published_date = datetime.fromisoformat(published_date)
            last_modified_date = item.get("lastModified")
            if last_modified_date:
                last_modified_date = datetime.fromisoformat(last_modified_date)

            # Safely access base score
            base_score = item.get("metrics", {}).get("cvssMetricV3", {}).get("cvssData", {}).get("baseScore")

            # Upsert logic to insert or update the CVE in the database
            existing_cve = db.query(CVE).filter(CVE.cve_id == cve_id).first()
            if existing_cve:
                existing_cve.last_modified_date = last_modified_date
                existing_cve.base_score = base_score
            else:
                db.add(CVE(
                    cve_id=cve_id,
                    description=description,
                    published_date=published_date,
                    last_modified_date=last_modified_date,
                    base_score=base_score
                ))
        db.commit()

        print(f"Fetched and synchronized {batch_size} records starting from offset {offset}.")
        offset += batch_size

    db.close()
