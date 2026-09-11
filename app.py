from flask import Flask, jsonify

app = Flask(__name__)

expenses = []


@app.route("/")
def home():
    return jsonify({
        "message": "Welcome to Expense Tracker!",
        "status": "Application is running"
    })


@app.route("/add/<category>/<int:amount>")
def add_expense(category, amount):
    expense = {
        "category": category,
        "amount": amount
    }

    expenses.append(expense)

    return jsonify({
        "message": "Expense added successfully",
        "expense": expense
    })


@app.route("/expenses")
def view_expenses():
    return jsonify(expenses)


@app.route("/total")
def total_expenses():
    total = sum(expense["amount"] for expense in expenses)

    return jsonify({
        "total_expenses": total
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)