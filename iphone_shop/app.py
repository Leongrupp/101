from flask import Flask, render_template, abort

app = Flask(__name__)

IPHONES = [
    {"slug": "iphone-15-pro-max", "name": "iPhone 15 Pro Max", "price": 1199, "description": "The ultimate iPhone experience with powerful A17 Pro chip and titanium design."},
    {"slug": "iphone-15-pro", "name": "iPhone 15 Pro", "price": 999, "description": "Pro-class performance in a compact form."},
    {"slug": "iphone-15-plus", "name": "iPhone 15 Plus", "price": 899, "description": "Large display with all‑day battery life."},
    {"slug": "iphone-15", "name": "iPhone 15", "price": 799, "description": "The latest iPhone with powerful features and great value."},
    {"slug": "iphone-14", "name": "iPhone 14", "price": 699, "description": "A popular choice with impressive capabilities."},
    {"slug": "iphone-13", "name": "iPhone 13", "price": 599, "description": "Performance and camera in a classic design."},
    {"slug": "iphone-se", "name": "iPhone SE", "price": 429, "description": "Compact and affordable with Touch ID."}
]

@app.route('/')
def index():
    return render_template('index.html', iphones=IPHONES)

@app.route('/iphone/<slug>')
def iphone_detail(slug):
    model = next((i for i in IPHONES if i['slug'] == slug), None)
    if model is None:
        abort(404)
    return render_template('detail.html', model=model)

if __name__ == '__main__':
    app.run(debug=True)
