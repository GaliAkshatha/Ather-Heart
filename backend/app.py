import logging
import os
import uuid

from flask import Flask, request, jsonify
from flask_cors import CORS
from werkzeug.utils import secure_filename

from predict import predict_patient, predict_doctor
from ocr_utils import extract_text_from_image, extract_lab_values
from preprocess_utils import convert_input_types, calculate_bmi_if_missing, MissingFieldError

# ----------------------------
# LOGGING
# ----------------------------
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("ather-heart")

app = Flask(__name__)

# ----------------------------
# CORS
# Restrict to configured frontend origin(s) in production. Falls back to "*"
# only when no origin is configured, so local/dev usage still works.
# ----------------------------
ALLOWED_ORIGINS = os.environ.get("ALLOWED_ORIGINS", "*")
CORS(app, origins=[o.strip() for o in ALLOWED_ORIGINS.split(",")] if ALLOWED_ORIGINS != "*" else "*")

# ----------------------------
# UPLOAD FOLDER CHECK
# ----------------------------
UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), "uploads")
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg", "webp", "bmp", "tiff"}
MAX_CONTENT_LENGTH = 10 * 1024 * 1024  # 10 MB upload cap
app.config["MAX_CONTENT_LENGTH"] = MAX_CONTENT_LENGTH


def _allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


# =========================================================
# 1. OCR UPLOAD ROUTE
# =========================================================
@app.route("/api/ocr/upload", methods=["POST"])
def ocr_upload():
    file = request.files.get("file")
    if not file or file.filename == "":
        return jsonify({"error": "No file provided"}), 400

    if not _allowed_file(file.filename):
        return jsonify({"error": "Unsupported file type. Allowed: " + ", ".join(sorted(ALLOWED_EXTENSIONS))}), 400

    # secure_filename strips path separators/traversal sequences; we also
    # prefix a uuid so concurrent uploads with the same name can't collide
    # or overwrite one another.
    safe_name = secure_filename(file.filename)
    unique_name = f"{uuid.uuid4().hex}_{safe_name}"
    file_path = os.path.join(UPLOAD_FOLDER, unique_name)

    try:
        file.save(file_path)
        text = extract_text_from_image(file_path)
        extracted, missing = extract_lab_values(text)
    except Exception:
        logger.exception("OCR processing failed")
        return jsonify({"error": "Failed to process the uploaded image. Please try a clearer image."}), 422
    finally:
        # Don't retain uploaded lab report images longer than needed.
        try:
            if os.path.exists(file_path):
                os.remove(file_path)
        except OSError:
            logger.warning("Could not remove temp upload file %s", file_path)

    return jsonify({
        "extracted": extracted,
        "missing_fields": missing,
        "raw_text": text
    })


# =========================================================
# 2. PATIENT PREDICTION
# =========================================================
@app.route("/api/predict/patient", methods=["POST"])
def patient_predict():
    data = request.get_json(silent=True)
    if not data or not isinstance(data, dict):
        return jsonify({"error": "Request body must be a JSON object of patient fields"}), 400

    try:
        input_data = convert_input_types(data)
        input_data = calculate_bmi_if_missing(input_data)
        result = predict_patient(input_data)
    except MissingFieldError as e:
        return jsonify({"error": str(e)}), 400
    except Exception:
        logger.exception("Patient prediction failed")
        return jsonify({"error": "Could not generate a prediction from the provided data."}), 422

    return jsonify(result)


# =========================================================
# 3. DOCTOR PREDICTION (SHAP RAW)
# =========================================================
@app.route("/api/predict/doctor", methods=["POST"])
def doctor_predict():
    data = request.get_json(silent=True)
    if not data or not isinstance(data, dict):
        return jsonify({"error": "Request body must be a JSON object of patient fields"}), 400

    try:
        input_data = convert_input_types(data)
        input_data = calculate_bmi_if_missing(input_data)
        result = predict_doctor(input_data)
    except MissingFieldError as e:
        return jsonify({"error": str(e)}), 400
    except Exception:
        logger.exception("Doctor prediction failed")
        return jsonify({"error": "Could not generate a prediction from the provided data."}), 422

    return jsonify(result)


# =========================================================
# 4. SIMPLE TEST ROUTE
# =========================================================
@app.route("/api/patients", methods=["GET"])
def test():
    return jsonify([])


# =========================================================
# HEALTH CHECK (used by Render / uptime monitors)
# =========================================================
@app.route("/api/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"})


# =========================================================
# JSON ERROR HANDLERS (so 404/413/500 return JSON, not HTML,
# which is what the frontend expects to parse)
# =========================================================
@app.errorhandler(404)
def not_found(e):
    return jsonify({"error": "Not found"}), 404


@app.errorhandler(413)
def too_large(e):
    return jsonify({"error": "Uploaded file is too large (max 10MB)"}), 413


@app.errorhandler(500)
def server_error(e):
    logger.exception("Unhandled server error")
    return jsonify({"error": "Internal server error"}), 500


# =========================================================
# RUN FLASK (local dev only — Render/production uses gunicorn,
# see Procfile: `gunicorn app:app`)
# =========================================================
if __name__ == "__main__":
    debug_mode = os.environ.get("FLASK_DEBUG", "false").lower() == "true"
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=debug_mode, host="0.0.0.0", port=port)
