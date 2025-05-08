from flask import Flask
from routes.auth import auth_bp  # if using Blueprint

app = Flask(__name__)

# Register your auth blueprint
app.register_blueprint(auth_bp, url_prefix="/api/auth")

@app.route("/")
def index():
    return "Welcome to the User Authentication System!"

if __name__ == "__main__":
    app.run(debug=True)
