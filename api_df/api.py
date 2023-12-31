"""
api for getting a dataframe, perform some calculations in backend, and returning updated dataframe
run via: python api.py
app is running by default in port 5000 in localhost: http://127.0.0.1:5000/
"""

from flask import Flask, request, jsonify
import pandas as pd
from backend import backendProcess

app = Flask(__name__)


@app.route("/api/df", methods=["POST"])
def process_dataframe() -> tuple:
    """
    process incoming DataFrame, perform calculations and return the updated DataFrame.
    """
    try:
        request_data = request.get_json()

        if len(request_data) == 0:
            return jsonify({"error": "Empty dataframe"}), 400

        input_df = pd.DataFrame(request_data)

        updated_df = backendProcess(input_df)

        updated_json = updated_df.to_json(orient="records")

        return jsonify({"updated_dataframe": updated_json}), 200

    except Exception as e:
        app.logger.error(f"Error processing DataFrame: {str(e)}")
        return jsonify({"error": "Internal server error."}), 500


if __name__ == "__main__":
    """
    main method
    """
    DEBUG = True
    app.run(debug=DEBUG)
