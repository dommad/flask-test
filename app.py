from flask import Flask, render_template
import plotly.express as px
import json
import plotly

app = Flask(__name__)

# Route for the homepage
@app.route('/')
def index():
    # Create a sample Plotly chart (example: bar chart)
    data = {
        'Category': ['A', 'B', 'C', 'D'],
        'Value': [30, 20, 50, 40]
    }
    fig = px.bar(data, x='Category', y='Value', title='Simple Bar Chart')

    # Convert the Plotly figure to JSON for the frontend
    graph_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template('index.html', graph_json=graph_json)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
