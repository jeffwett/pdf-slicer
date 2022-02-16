# PDF Slicer 
- Python API for splitting a PDF into JPG images
- Can specify DPI

## Sample usage
```
curl  --request POST --data-binary "@file.pdf" http://localhost:5000/pdf_to_jpgs?dpi=400 
```

## Output
```
{ 
  "page_count": 12,
  "pages": [
    base64EncodedJPG,
    ...
  ] 
}
```
- To decode JPG use `base64.b64decode(base64EncodedJPG)` 


## Install instructions (Ubuntu)
```
sudo apt-get update
sudo apt-get -y install python3-pip
pip3 install flask waitress pdf2image
sudo apt-get install -y poppler-utils
sudo add-apt-repository -y ppa:alex-p/tesseract-ocr5
sudo apt install -y tesseract-ocr
```
## Run server
### production
```python3 app.py``` 
### development: 
```flask run```

