from flask import Flask, render_template_string

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template_string("""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Hello World</title>
        <style>
            body {
                height: 100vh;
                margin: 0;
                display: flex;
                justify-content: center;
                align-items: center;
                background: linear-gradient(135deg, #667eea, #764ba2);
                font-family: "Segoe UI", sans-serif;
            }
            .card {
                background: white;
                padding: 40px 60px;
                border-radius: 14px;
                box-shadow: 0 20px 40px rgba(0,0,0,0.2);
                text-align: center;
            }
            h1 {
                margin: 0;
                font-size: 42px;
                color: #333;
            }
            p {
                margin-top: 10px;
                color: #666;
            }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>Hello, World 🌍</h1>
            <p>Powered by Python & Flask</p>
        </div>
    </body>
    </html>
    """)

if __name__ == "__main__":
    app.run(debug=True)
