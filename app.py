from flask import Flask, request, render_template_string

app = Flask(__name__)
tickets = []

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        ticket = {
            "id": len(tickets) + 1,
            "title": request.form["title"],
            "description": request.form["description"]
        }
        tickets.append(ticket)
    return render_template_string('''
        <h1>ITSM Ticketing System</h1>
        <form method="post">
            Title: <input name="title" required><br>
            Description: <textarea name="description" required></textarea><br>
            <input type="submit" value="Submit Ticket">
        </form>
        <h2>Existing Tickets:</h2>
        <ul>
        {% for ticket in tickets %}
            <li>{{ ticket.id }} - {{ ticket.title }}: {{ ticket.description }}</li>
        {% endfor %}
        </ul>
    ''', tickets=tickets)

if __name__ == "__main__":
    app.run(debug=True)
