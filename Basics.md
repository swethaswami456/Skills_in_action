Great skill to learn. A webpage is essentially a collection of files that a web browser (Chrome, Edge, Firefox, etc.) reads and displays.

# 1. What is a Webpage?

A webpage is what you see in a browser, like:

* Google homepage
* Amazon product page
* Your company's website

A website is a collection of webpages.

Example:

```text
website.com
│
├── Home Page
├── About Page
├── Contact Page
└── Products Page
```

***

# 2. Core Technologies of Web Development

Every webpage is built using three main technologies:

## HTML (Structure)

Defines the content.

```
<h1>Welcome</h1>
<p>This is my first webpage.</p>
```
## CSS (Styling)

Makes the webpage look attractive.

Example:

```css
h1 {
    color: blue;
    font-size: 40px;
}
```

Think of CSS as paint, furniture, and decorations.

***

## JavaScript (Behavior)

Adds interactivity.

Example:

```javascript
button.onclick = function() {
    alert("Hello!");
}
```

Think of JavaScript as electricity and automation.

***

# 3. Basic File Formats

## HTML File

Extension:

```text
.html
```

Examples:

```text
index.html
about.html
contact.html
```

***

## CSS File

Extension:

```text
.css
```

Example:

```text
style.css
```

***

## JavaScript File

Extension:

```text
.js
```

Example:

```text
script.js
```

***

# 4. Typical Project Structure

```text
MyWebsite/
│
├── index.html
├── css/
│   └── style.css
│
├── js/
│   └── script.js
│
└── images/
    ├── logo.png
    └── banner.jpg
```

***

Create a file called:

```text
index.html
```

Add:

# 5. Your First Webpage

index.html file
``` 
<!DOCTYPE html>
<html>
<head>
    <title>My First Page</title>
</head>
<body>
    <h1>Hello World!</h1>
    <p>Welcome to web development.</p>
</body>
</html>
```



---


# 6. Adding CSS

Create:

```text
style.css
```

```css
body {
    background-color: lightblue;
    font-family: Arial;
}

h1 {
    color: darkblue;
}
```

Connect it to HTML:
```
<head>
    style.css
</head>
```

# 7. Adding JavaScript

Create:

```text
script.js
```

```javascript
alert("Page Loaded!");
```

Connect it:
```
<body>

    <h1>Hello World</h1>

    script.js
</body>
```

# 8. Frontend vs Backend

## Frontend

What users see.

Technologies:

* HTML
* CSS
* JavaScript
* React
* Angular
* Vue

Example:

```text
Buttons
Forms
Menus
Images
```

***

## Backend

Processes data behind the scenes.

Technologies:

* Node.js
* Python
* Java
* C#
* PHP

Handles:

* Login
* Database operations
* Sending emails
* Business logic

***

# 9. Databases

Store application data.

Examples:

* MySQL
* PostgreSQL
* SQL Server
* MongoDB

Example:

```text
Customer Name
Email
Phone
Orders
```

***

# 10. Modern Web Development Stack

A common stack today:

```text
Frontend
    React

Backend
    Node.js

Database
    MongoDB
```

Or:

```text
Frontend
    React

Backend
    Python (Django/FastAPI)

Database
    PostgreSQL
```

***

# 11. How a Website Works

```text
User
  |
Browser
  |
Internet
  |
Web Server
  |
Database
```

Flow:

1. User enters URL.
2. Browser sends request.
3. Server processes request.
4. Database returns data.
5. Server sends HTML/CSS/JS.
6. Browser renders webpage.

***

# 12. Useful Tools

### Code Editor

* Visual Studio Code (most popular)
* Sublime Text

### Browser

* Google Chrome
* Microsoft Edge

### Version Control

* Git
* GitHub

***

# 13. Learning Roadmap

### Beginner

✅ HTML\
✅ CSS\
✅ JavaScript

### Intermediate

✅ Responsive Design\
✅ Git & GitHub\
✅ APIs\
✅ React

### Advanced

✅ Backend Development\
✅ Databases\
✅ Authentication\
✅ Cloud Deployment (Azure, AWS)

***

# Sample Complete Webpage
```
<!DOCTYPE html>
<html>
<head>
    <title>My Website</title>

    <style>
        body {
            font-family: Arial;
            text-align: center;
        }

        button {
            padding: 10px 20px;
        }
    </style>
</head>

<body>

<h1>Welcome</h1>

<button onclick="sayHello()">
    Click Me
</button>

<script>
function sayHello() {
    alert("Hello Swetha!");
}
</script>

</body>
</html>

```

Save as `index.html` and open it in a browser. That's a complete, working webpage.

If you'd like, I can also explain **how web hosting, domains, GitHub Pages, React, and modern web app architecture fit together** with a simple diagram.
