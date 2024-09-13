/* Basic styles */
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
    background-color: #f5f5f5;
    color: #333;
}

header, nav, section, article, aside, footer {
    margin: 20px;
    padding: 20px;
    border: 1px solid #ccc;
    background-color: #fff;
    border-radius: 5px;
    box-shadow: 0 0 10px rgba(0,0,0,0.1);
}

/* Header styles */
header {
    background-color: #4CAF50;
    color: white;
}

header h1 {
    margin: 0;
}

/* Navigation styles */
nav ul {
    list-style-type: none;
    padding: 0;
    margin: 0;
}

nav ul li {
    display: inline;
    margin-right: 10px;
}

nav ul li a {
    color: white;
    text-decoration: none;
    padding: 10px 15px;
    background-color: #333;
    border-radius: 5px;
}

nav ul li a:hover {
    background-color: #555;
}

/* Section and article styles */
section {
    margin-bottom: 20px;
}

article {
    margin-bottom: 20px;
}

/* Text content styles */
p {
    line-height: 1.6;
}

blockquote {
    margin: 20px 0;
    padding: 10px 20px;
    background-color: #f9f9f9;
    border-left: 5px solid #ccc;
}

pre {
    background-color: #f4f4f4;
    padding: 10px;
    border: 1px solid #ddd;
    overflow-x: auto;
}

ol, ul {
    margin: 10px 0;
    padding: 0 0 0 40px;
}

dl {
    margin: 20px 0;
}

figure {
    margin: 20px 0;
}

figcaption {
    text-align: center;
    font-style: italic;
}

/* Form styles */
form {
    margin: 20px 0;
}

fieldset {
    border: 1px solid #ccc;
    padding: 10px;
    margin-bottom: 20px;
    border-radius: 5px;
}

legend {
    font-weight: bold;
}

label {
    display: block;
    margin-bottom: 5px;
}

input[type="text"],
input[type="email"],
textarea {
    width: 100%;
    padding: 10px;
    margin-bottom: 10px;
    border: 1px solid #ccc;
    border-radius: 5px;
}

input[type="color"],
input[type="submit"] {
    display: block;
    margin: 10px 0;
}

/* Details and dialog styles */
details {
    margin: 20px 0;
}

dialog {
    border: none;
    padding: 20px;
    border-radius: 5px;
    background-color: #f9f9f9;
    box-shadow: 0 0 10px rgba(0,0,0,0.1);
}

/* Table styles */
table {
    width: 100%;
    border-collapse: collapse;
    margin-bottom: 20px;
}

table, th, td {
    border: 1px solid #ddd;
    padding: 10px;
}

thead {
    background-color: #f9f9f9;
}

caption {
    font-weight: bold;
    margin-bottom: 10px;
}

/* Multimedia styles */
audio, video {
    display: block;
    margin: 20px 0;
}

embed {
    display: block;
    margin: 20px 0;
}

/* Aside styles */
aside {
    background-color: #f4f4f4;
    padding: 20px;
    border-radius: 5px;
    box-shadow: 0 0 10px rgba(0,0,0,0.1);
}

/* Footer styles */
footer {
    background-color: #333;
    color: white;
    text-align: center;
    padding: 20px;
    position: relative;
}

footer p {
    margin: 0;
}

/* Responsive styles */
@media (max-width: 768px) {
    nav ul li {
        display: block;
        margin: 5px 0;
    }

    input[type="text"],
    input[type="email"],
    textarea {
        width: 100%;
    }
}
