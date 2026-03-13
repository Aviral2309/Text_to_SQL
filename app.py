from flask import Flask, render_template, request, jsonify
import pymysql
from utils.sql_chain import generate_sql_query

app = Flask(__name__)

# Database connection
connection = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    database="text_to_sql",
    cursorclass=pymysql.cursors.DictCursor
)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/query", methods=["POST"])
def query():

    data = request.get_json()
    question = data["question"]

    try:

        sql_query = generate_sql_query(question)

        with connection.cursor() as cursor:
            cursor.execute(sql_query)
            result = cursor.fetchall()

        return jsonify({
            "sql_query": sql_query,
            "result": result
        })

    except Exception as e:
        return jsonify({
            "error": str(e)
        })


if __name__ == "__main__":
    app.run(debug=True)