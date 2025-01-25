import nest_asyncio
nest_asyncio.apply()

import os
from dotenv import load_dotenv
from flask import Flask, request, jsonify, render_template
from werkzeug.utils import secure_filename
from llama_parse import LlamaParse

load_dotenv()

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['MAX_CONTENT_LENGTH'] = 10 * 1024 * 1024  # 10MB limit

os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/parse-pdf', methods=['POST'])
def parse_pdf():
    if 'pdf' not in request.files:
        return jsonify({'error': 'No file uploaded'}), 400
    
    file = request.files['pdf']
    
    if file.filename == '':
        return jsonify({'error': 'Empty filename'}), 400
    
    filename = secure_filename(file.filename)
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(filepath)
    
    try:
        parser = LlamaParse(
            result_type="markdown",
            parsing_instruction="Extract only the meaningful content from the document",
            api_key=os.getenv("LLAMA_CLOUD_API_KEY") # <-- LLAMA Cloud API Key HERE
        )
        
        # parse document
        documents = parser.load_data(filepath)
        
        # format response
        parsed_content = []
        for doc in documents:
            parsed_content.append(doc.text_resource.text)
            parsed_content.append('-' * 50)
        
        return jsonify({'content': parsed_content})
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
    finally:
        # remove file setelah parsing
        if os.path.exists(filepath):
            os.remove(filepath)

if __name__ == '__main__':
    app.run(debug=True)