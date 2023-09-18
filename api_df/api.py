"""
api for getting a dataframe, perform some calculations in backend, and returning updated dataframe
run via: python api.py
"""

from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)

def backend(input_df):
    input_df['value'] = input_df['value'] * 3
    return input_df

@app.route('/api/df', methods=['POST'])
def process_dataframe():
    """
    Process incoming DataFrame, perform calculations, and return the updated DataFrame.
    """
    try:
        request_data = request.get_json()

        if len(request_data) == 0:
            return jsonify({'error': 'Empty dataframe'}), 400

        input_df = pd.DataFrame(request_data)

        updated_df = backend(input_df)

        updated_json = updated_df.to_json(orient='records')

        return jsonify({'updated_dataframe': updated_json}), 200

    except Exception as e:
        app.logger.error(f'Error processing DataFrame: {str(e)}')
        return jsonify({'error': 'Internal server error.'}), 500

if __name__ == '__main__':
    app.run(debug=True)
