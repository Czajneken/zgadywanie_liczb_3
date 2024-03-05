from flask import Flask, request
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def hello():
    if request.method == "GET":
        return """
            <html>
                <body>
                    <form action="/" method="POST">
                        
                    </form>
                </body>
            </html>
        """
    else:



if __name__ == "__main__":
    app.run(debug=True)
