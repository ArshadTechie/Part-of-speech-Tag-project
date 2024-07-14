<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>
  <h1>Parts of Speech Tagger with Streamlit</h1>

  <p>This project implements a Parts of Speech (POS) Tagger using Streamlit, a Python framework for creating interactive web applications. The POS Tagger identifies the grammatical parts of words in a sentence using a pre-trained neural network model.</p>

  <h2>Features</h2>
  <ul>
    <li><strong>Input Sentence Tagging</strong>: Enter a sentence to see the parts of speech tagged for each word.</li>
    <li><strong>Individual Word Tagging</strong>: Check the part of speech tag for a specific word in the input sentence.</li>
    <li><strong>Example Selection</strong>: Choose from pre-defined examples or enter your own sentence for tagging.</li>
    <li><strong>Interactive Interface</strong>: Navigate between different functionalities using the sidebar navigation.</li>
  </ul>

  <h2>Technologies Used</h2>
  <ul>
    <li>Python</li>
    <li>Streamlit</li>
    <li>Keras (for loading and using the pre-trained model)</li>
    <li>NumPy (for numerical operations and array handling)</li>
    <li>Pickle (for serializing and deserializing Python objects)</li>
  </ul>

  <h2>Getting Started</h2>

  <h3>Prerequisites</h3>
  <ul>
    <li>Python 3.6+</li>
    <li>Install necessary Python packages:</li>
  </ul>

  <pre><code>pip install streamlit keras numpy</code></pre>

  <h3>Installation</h3>
  <ol>
    <li>Clone the repository:</li>
  </ol>

  <pre><code>git clone https://github.com/your-username/pos-tagger-streamlit.git</code></pre>

  <ol start="2">
    <li>Navigate to the project directory:</li>
  </ol>

  <pre><code>cd pos-tagger-streamlit</code></pre>

  <ol start="3">
    <li>Run the Streamlit application:</li>
  </ol>

  <pre><code>streamlit run app.py</code></pre>

  <h2>Usage</h2>
  <ul>
    <li><strong>Home Page</strong>: Enter a sentence in the text input or choose an example from the dropdown menu. Click "Submit" to see the parts of speech tagged.</li>
    <li><strong>Individual Word Page</strong>: Navigate to this page to check the part of speech tag for a specific word from the previously entered sentence.</li>
  </ul>
  <h2>Contributing</h2>
  <p>Contributions are welcome! Please fork the repository and create a pull request with your suggested changes.</p>

  <h2>Acknowledgments</h2>
  <ul>
    <li>Special thanks to <a href="https://streamlit.io/">Streamlit</a> for making it easy to create interactive web apps with Python.</li>
    <li>The POS Tagger model is based on a neural network trained using Keras.</li>
  </ul>
</body>
</html>
