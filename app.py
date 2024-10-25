from flask import Flask, render_template, request, jsonify
import subprocess

app = Flask(__name__)

def generate_text_with_llama(prompt):
    command = ["ollama", "run", "llama3.2"]
    
    try:
        process = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, encoding='utf-8')
        output, error = process.communicate(input=prompt)
        if output:
            return output.strip()
        if error:
            return f"Error occurred: {error.strip()}"
    
    except Exception as e:
        return f"An exception occurred: {str(e)}"

def count_words(text):
    return len(text.split())

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    prompt = request.form['prompt']
    word_limit = int(request.form['wordLimit'])
    word_count = count_words(prompt)

    if word_count > word_limit:
        return jsonify({"blog_content": f"Error: Prompt exceeds the {word_limit}-word limit."})

    blog_content = generate_text_with_llama(prompt)
    return jsonify({"blog_content": blog_content})

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5050)
