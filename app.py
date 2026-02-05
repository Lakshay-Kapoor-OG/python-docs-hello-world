from flask import Flask, render_template_string

app = Flask(__name__)

@app.route("/")
def home():
    return render_template_string("""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Mini Flask App</title>
        <style>
            body {
                font-family: Arial;
                text-align: center;
                margin-top: 100px;
            }
            button {
                padding: 10px 20px;
                font-size: 16px;
                cursor: pointer;
            }
        </style>
    </head>
    <body>
        <h1>👋 Hello from Flask</h1>
        <p id="text">Click the button</p>
        <button onclick="changeText()">Click Me</button>

        <script>
            function changeText() {
                document.getElementById("text").innerHTML = "🎉 Button Clicked!";
            }
        </script>
    </body>
    </html>
    """)

if __name__ == "__main__":
    app.run(debug=True)
