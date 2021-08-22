# Rosie

<p align="center">
	<br/>
    <img src="https://public-assets-f8h.s3.amazonaws.com/clipart3278228-removebg-preview.png" alt="Logo" width="256" height="256">
  </p>

<details open="open">
  <summary>Table of Contents</summary>
  <ol>
  	<li>
    	<a href="#about">About</a>
        <ul>
        	<li><a href="#what-is-it">What is it</a></li>
        	<li><a href="#why-use-it">Why use it</a></li>
            <li><a href="#built-with">Built with</a></li>
        </ul>
  	</li>
    <li>
    	<a href="#description">Description</a>
        <ul>
          <li><a href="#about">About</a></li>
          <li><a href="#models">Models</a></li>
        </ul>
    </li>
    <li>
      <a href="#running-it">Running It</a>
      <ul>
        <li><a href="#testing-locally">Testing Locally</a></li>
        <li><a href="#testing-the-server">Testing The Server</a></li>
      </ul>
    </li>
  </ol>
</details>

## About

### What is it
A chatbot framework built with Spacy and Flask.

### Why use it

### Built with
* Python 3.9
* Flask
* Spacy


### Models

* Chatbot
* Intent
* Phrase
* User


## Running It

### Running Locally

**Pizzaria example (Portuguese - Brazil)**
```txt
pipenv shell
python -m spacy download pt_core_news_lg
python examples/pizzaria_pt.py
```

### Running The Server

*Postman collection in the docs folder*
```txt
pipenv shell
python app.py
```

<br>
