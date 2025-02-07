from flask import Flask, render_template, send_file
from io import BytesIO
import os
import generator

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/instrument/<int:instrument_id>')
def instrument_image(instrument_id):
    images = generator.generate_instrument_images()
    if instrument_id < 1 or instrument_id > len(images):
        return "Instrument not found", 404
    img_io = BytesIO()
    images[instrument_id - 1].save(img_io, 'PNG')
    img_io.seek(0)
    return send_file(img_io, mimetype='image/png')

@app.route('/favicon.ico')
def favicon():
    return send_file(os.path.join(app.root_path, 'static/favicon.ico'), mimetype='image/vnd.microsoft.icon')

if __name__ == '__main__':
    app.run(debug=True)
