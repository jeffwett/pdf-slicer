from flask import Flask, request
import hashlib
import json
import base64
app = Flask(__name__)
from pdf2image import convert_from_bytes

import tempfile
import shutil
import pdb

@app.route("/check")
def check():
    return json.dumps({})

@app.route("/pdf_to_jpgs", methods = ['POST'])
def pdf_to_jpgs():
    from pdf2image import convert_from_path

    pdf_data = request.data

    if pdf_data == '' or pdf_data == None:
        return json.dumps({"page_count": 0, "pages": []})

    dpi = request.args.get("dpi", default=200)

    images = convert_from_bytes(pdf_data, dpi=dpi)

    with tempfile.TemporaryDirectory() as dirpath:
        filename = lambda page: dirpath + str(page) +'.jpg'

        for i in range(len(images)):
            # Save pages as images in the pdf
            images[i].save(filename(i), 'JPEG')
        out = {}
        out['page_count'] = len(images)
        out['pages'] = []

        for i in range(len(images)):
            with open(filename(i), "rb") as page_image_file:
                file_d = page_image_file.read()
                file_e = base64.encodebytes(file_d).decode("ascii")
                out['pages'].append(file_e)
        return json.dumps(out)

if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)
