import pytest
from backend.app import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_list_cves(client):
    response = client.get("/cves/list")
    assert response.status_code == 200
    assert isinstance(response.json, list)

def test_get_cve(client):
    response = client.get("/cves/CVE-TEST-1234")
    assert response.status_code in [200, 404]

def test_filter_cves(client):
    """
    Test the /cves/filter endpoint.
    """
    # Test filtering by year
    response = client.get("/cves/filter", query_string={"year": "2023"})
    assert response.status_code == 200
    assert isinstance(response.json, list)

    # Test filtering by score range
    response = client.get("/cves/filter", query_string={"score_min": 5.0, "score_max": 7.5})
    assert response.status_code == 200
    assert isinstance(response.json, list)

    # Test filtering by last modified date
    response = client.get("/cves/filter", query_string={"last_modified_days": 30})
    assert response.status_code == 200
    assert isinstance(response.json, list)
