from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <h1>🛒 Online Store</h1>
    <h2>Cloud + DevOps Project</h2>
    <p>Welcome to our online store!</p>
    """


@app.route("/products")
def products():
    return """
    <h2>Products</h2>
    <ul>
        <li>Laptop - ₹50,000</li>
        <li>Smartphone - ₹25,000</li>
        <li>Headphones - ₹2,000</li>
    </ul>
    """


app.run(host="0.0.0.0", port=5000)