from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

def get_airport_info(icao):
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="lentokentta_tietokanta"
    )
    cursor = connection.cursor(dictionary=True)
    query = "SELECT ident AS ICAO, name AS Name, municipality AS Municipality FROM airport WHERE ident = %s"
    cursor.execute(query, (icao,))
    result = cursor.fetchone()
    cursor.close()
    connection.close()
    return result

@app.route('/kenttä/<icao>', methods=['GET'])
def airport_info(icao):
    data = get_airport_info(icao)
    if data:
        return jsonify(data)
    else:
        return jsonify({"error": "Airport not found"}), 404

if __name__ == '__main__':
    app.run(port=3000)
