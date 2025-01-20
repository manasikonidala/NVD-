from flask import Blueprint, jsonify, request
from database import SessionLocal, CVE

cve_blueprint = Blueprint("cve_api", __name__)

@cve_blueprint.route("/cves/list", methods=["GET"])
def list_cves():
    db = SessionLocal()
    cves = db.query(CVE).all()
    db.close()
    return jsonify([{
        "id": cve.id,
        "cve_id": cve.cve_id,
        "description": cve.description,
        "published_date": str(cve.published_date),
        "last_modified_date": str(cve.last_modified_date),
        "base_score": cve.base_score
    } for cve in cves])

@cve_blueprint.route("/cves/<cve_id>", methods=["GET"])
def get_cve(cve_id):
    db = SessionLocal()
    cve = db.query(CVE).filter(CVE.cve_id == cve_id).first()
    db.close()
    if cve:
        return jsonify({
            "id": cve.id,
            "cve_id": cve.cve_id,
            "description": cve.description,
            "published_date": str(cve.published_date),
            "last_modified_date": str(cve.last_modified_date),
            "base_score": cve.base_score
        })
    return jsonify({"error": "CVE not found"}), 404
@cve_blueprint.route("/cves/filter", methods=["GET"])
def filter_cves():
    """
    API to filter CVEs based on optional parameters:
    - cve_id
    - year
    - score_min and score_max
    - last_modified_days
    """
    cve_id = request.args.get("cve_id")
    year = request.args.get("year")
    score_min = request.args.get("score_min", type=float)
    score_max = request.args.get("score_max", type=float)
    last_modified_days = request.args.get("last_modified_days", type=int)

    db = SessionLocal()
    query = db.query(CVE)

    if cve_id:
        query = query.filter(CVE.cve_id == cve_id)
    if year:
        query = query.filter(CVE.published_date.like(f"{year}-%"))
    if score_min is not None:
        query = query.filter(CVE.base_score >= score_min)
    if score_max is not None:
        query = query.filter(CVE.base_score <= score_max)
    if last_modified_days:
        from datetime import datetime, timedelta
        cutoff_date = datetime.now() - timedelta(days=last_modified_days)
        query = query.filter(CVE.last_modified_date >= cutoff_date)

    results = query.all()
    db.close()
    return jsonify([{
        "id": cve.id,
        "cve_id": cve.cve_id,
        "description": cve.description,
        "published_date": str(cve.published_date),
        "last_modified_date": str(cve.last_modified_date),
        "base_score": cve.base_score
    } for cve in results])
