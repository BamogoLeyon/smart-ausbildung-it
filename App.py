from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>SmartAusbildung</h1>
    <h2>IT Ausbildung in Deutschland</h2>
    <p>Diese Plattform hilft internationalen Bewerbern, 
    eine passende IT-Ausbildung in Deutschland zu finden.</p>

    <h3>Beliebte IT-Berufe:</h3>
    <ul>
        <li>Fachinformatiker/in - Anwendungsentwicklung</li>
        <li>Fachinformatiker/in - Systemintegration</li>
        <li>IT-Systemelektroniker/in</li>
    </ul>
    """

if __name__ == "__main__":
    app.run()
