from flask import Flask, jsonify, request
from database import SessionLocal, CVE

app = Flask(__name__)

@app.route("/cves/list", methods=["GET"])
def list_cves():
    db = SessionLocal()
    cves = db.query(CVE).all()
    db.close()
    return jsonify([{
        "id": cve.id,
        "cve_id": cve.cve_id,
        "description": cve.description,
        "published_date": cve.published_date,
        "last_modified_date": cve.last_modified_date,
        "base_score": cve.base_score
    } for cve in cves])

@app.route("/cves/<cve_id>", methods=["GET"])
def get_cve(cve_id):
    db = SessionLocal()
    cve = db.query(CVE).filter(CVE.cve_id == cve_id).first()
    db.close()
    if cve:
        return jsonify({
            "id": cve.id,
            "cve_id": cve.cve_id,
            "description": cve.description,
            "published_date": cve.published_date,
            "last_modified_date": cve.last_modified_date,
            "base_score": cve.base_score
        })
    else:
        return jsonify({"error": "CVE not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)
