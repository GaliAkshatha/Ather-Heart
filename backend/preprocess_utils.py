class MissingFieldError(Exception):
    """Raised when required patient fields are missing or invalid so the
    Flask layer can return a clean 400 instead of a raw 500 crash."""
    pass


def convert_input_types(data):
    if not isinstance(data, dict):
        raise MissingFieldError("Expected a JSON object of patient fields")

    clean = {}
    for k, v in data.items():
        if v is None or v == "":
            # Leave genuinely missing values as None rather than silently
            # keeping an empty string, which would crash the scaler later.
            clean[k] = None
            continue
        try:
            clean[k] = float(v)
        except (TypeError, ValueError):
            clean[k] = v
    return clean


def calculate_bmi_if_missing(data):
    if ("BMI" not in data or data.get("BMI") in ["", None, 0]) and \
       ("Height" in data and "Weight" in data):
        h = data.get("Height")
        w = data.get("Weight")

        if h in [None, "", 0] or w in [None, "", 0]:
            raise MissingFieldError("Height and Weight are required to calculate BMI")

        try:
            h = float(h)
            w = float(w)
        except (TypeError, ValueError):
            raise MissingFieldError("Height and Weight must be numeric")

        if h <= 0:
            raise MissingFieldError("Height must be greater than 0")

        data["BMI"] = w / ((h / 100) ** 2)

    return data
