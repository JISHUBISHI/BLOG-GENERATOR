function generateBlog() {
    const prompt = document.getElementById('prompt').value;
    const wordLimit = document.getElementById('wordLimit').value;
    const generateButton = document.getElementById('generateButton');

    if (!prompt) {
        alert('Please enter a prompt.');
        return;
    }

    // Show loading state
    generateButton.disabled = true;
    generateButton.innerHTML = `<span class="spinner"></span> Generating...`;

    fetch('/generate', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: `prompt=${encodeURIComponent(prompt)}&wordLimit=${encodeURIComponent(wordLimit)}`
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('blogContent').textContent = data.blog_content;
        
        // Reset button to its original state
        generateButton.disabled = false;
        generateButton.innerHTML = 'Generate Blog';
    })
    .catch(error => {
        console.error('Error:', error);

        // Reset button if there's an error
        generateButton.disabled = false;
        generateButton.innerHTML = 'Generate Blog';
    });
}
