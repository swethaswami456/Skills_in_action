# Html - Hyper Text MarkUp Language
# LEARNING Tutorial

## Html Elements
### NESTED HTML
- element inside an element
### Empty elements - `<br>`


HTML TAGNAMES such as html, head, body are `case in-sensitive`
```
- <html>
- <head>  <title> content </title> </head>
- <body> <h1> heading </h1>  <p> Paragraph Ln 1 <br> Paragraph ln 2 </p> </body>
- </html>
```

## Attributes

All HTML elements can have attributes. They are also `case in-sensitive`. But lowercase recommended
- The href attribute of `<a>` specifies the URL of the page the link goes to
- The src attribute of `<img>` specifies the path to the image to be displayed
- The width and height attributes of `<img>` provide size information for images
- The alt attribute of `<img>` provides an alternate text for an image
- The style attribute is used to add styles to an element, such as color, font, size, and more
- The lang attribute of the `<html>` tag declares the language of the Web page
- The title attribute defines some extra information about an element

### The href Attribute
The `<a>` tag defines a hyperlink. The href attribute specifies the URL of the page the link goes to:

- Example
```
<a href="https://www.w3schools.com">Visit W3Schools</a> 
```

### The src Attribute
The `<img>` tag is used to embed an image in an HTML page. The src attribute specifies the path to the image to be displayed:

- Example
```
<img src="img_girl.jpg">
<img src="img_girl.jpg" width="500" height="600">

<img src="img_girl.jpg" alt="Girl with a jacket"> 
<!-- alternate name if image is not displayed -->
```

Eitehr be absolute or relTIVE LINK
- Absolute link - http://www.xyz.com
- Relative link - '/images/img_girl.jpg'

### General Attributes

```
The style Attribute
<p style="color:red;">This is a red paragraph.</p>

The lang Attribute
This is meant to assist search engines and browsers.

<!DOCTYPE html>
<html lang="en">
<html lang="en-US">
<body>

The title Attribute
Hover over a para to see teh title
<p title="I'm a tooltip">This is a paragraph.</p>

Always use a quote
Good:
<a href="https://www.w3schools.com/html/">Visit our HTML tutorial</a>
Bad:
<a href=https://www.w3schools.com/html/>Visit our HTML tutorial</a>
```

## Headings

```
h1 to h6
<h1>..... </h1>
.
.
.
<h6>.....  </h6>
```

## Paragraphs

|Attribute| HTML display |
|------|-----------|
|`<p>` |	Defines a paragraph
|`<hr>` |	Defines a thematic change in the content
|`<br>` |	Inserts a single line break
|`<pre>` |	Defines pre-formatted text

## Style Attribute
- Use the `style` attribute for styling HTML elements
    - Use `background-color` for background color
    - Use `color` for text colors
    - Use `font-family` for text fonts
    - Use `font-size` for text sizes
    - Use `text-align` for text alignment
    - Use `border` fro border
``` html
<tagname(element) style="property:value;">
```

### Background Color
```html
<body style="background-color:powderblue;">
<h1 style="background-color:powderblue;">This is a heading</h1>
<p style="background-color:tomato;">This is a paragraph.</p>
</body>
```

### Text
```html
<h1 style="color:blue;text-align:center;">This is a heading</h1>
<p style="color:red;text-align:center;">This is a paragraph.</p>
```

### Font
```html
<h1 style="font-family:verdana;font-size:300%;border:2px solid Tomato;">This is a heading</h1>
<p style="font-family:courier;font-size:160%;border:2px solid Tomato;">This is a paragraph.</p>
```

## Text Formatting

- `<b>` - Bold text
- `<strong>` - Important text
- `<i>` - Italic text
- `<em>` - Emphasized text
- `<mark>` - Marked text
- `<small>` - Smaller text
- `<del>` - Deleted text
- `<ins>` - Inserted text
- `<sub>` - Subscript text
- `<sup>` - Superscript text

```html
<b> Bold text </b>
<strong> Strong Text - Important text</strong>
<i> Italic text </i>
<em> Emphasized text </em>
<mark> Marked text  </mark>
<small> Smaller text </small>
<del> Deleted text   </del>
<ins> Inserted text   </ins>
<sub> Subscript text   </sub>
<sup> Superscript text   </sup>
```

## Quotations

|Tag	            | Description |
|----               |------|
| `<blockquote>`    | Defines a section that is quoted from another source
| `<q>`	            | Defines a short inline quotation
| `<abbr>`	        | Defines an abbreviation or acronym
| `<address>`	    | Defines contact information for the author/owner of a document
| `<cite>`	        | Defines the title of a work
| `<bdo>`	        | Defines the text direction

```html
<!-- Quotations -->
 <p>Here is a quote from WWF's website:</p>
<blockquote cite="http://www.worldwildlife.org/who/index.html">
For 60 years, WWF has worked to help people and nature thrive. As the world's leading conservation organization, WWF works in nearly 100 countries. At every level, we collaborate with people around the world to develop and deliver innovative solutions that protect communities, wildlife, and the places in which they live.
</blockquote>
<br>
<p>WWF's goal is to: <q>Build a future where people live in harmony with nature.</q></p>
<p>The <abbr title="World Health Organization">WHO</abbr> was founded in 1948.</p>

<address>
Written by John Doe.<br>
Visit us at:<br>
Example.com<br>
Box 564, Disneyland<br>
USA
</address>

<p><cite>The Scream</cite> by Edvard Munch. Painted in 1893.</p>

<bdo dir="rtl">This text will be written from right to left</bdo>
```

## Colours
![alt text](Colours.png)

- Please refer to Style-Attribute topic as well for border colour, Background, text, etc
- Last two have 50% transparency
    - rgba(255, 99, 71, 0.5)
    - hsla(9, 100%, 64%, 0.5)

```html
<h1 style="background-color:rgb(255, 99, 71);">...</h1>
<h1 style="background-color:#ff6347;">...</h1>
<h1 style="background-color:hsl(9, 100%, 64%);">...</h1>

<h1 style="background-color:rgba(255, 99, 71, 0.5);">...</h1>
<h1 style="background-color:hsla(9, 100%, 64%, 0.5);">...</h1>
```


# CSS - Cascading Style Sheets

## CSS saves a lot of work. It can control the layout of multiple web pages all at once.

> Tip: The word cascading means that a style applied to a parent element will also apply to all children elements within the parent. So, if you set the color of the body text to "blue", all headings, paragraphs, and other text elements within the body will also get the same color (unless you specify something else)!

### Ways of having style

- ### Inline - by using the style attribute inside HTML elements
    ```html
    <h1 style="color:blue;">A Blue Heading</h1>
    <p style="color:red;">A red paragraph.</p>
    ```

- ### Internal - by using a `<style>` element in the `<head>` section
    ```html
    <!DOCTYPE html>
    <html>
    <head>
    <style>
    body {background-color: powderblue;}
    h1   {color: blue;}
    p    {color: red;}
    </style>
    </head>
    <body>

    <h1>This is a heading</h1>
    <p>This is a paragraph.</p>

    </body>
    </html>
    ```

- ### External - by using a <link> element to link to an external CSS file
    ```html
    <!DOCTYPE html>
    <html>
    <head>
    <link rel="stylesheet" href="styles.css">
    </head>
    <body>

    <h1>This is a heading</h1>
    <p>This is a paragraph.</p>

    </body>
    </html>
    ```

    Style.css is as below
    ```
    body {
    background-color: powderblue;
    }
    h1 {
    color: blue;
    }
    p {
    color: red;
    }
    ```

    #### Three ways of External link
    ```html
    This example uses a full URL to link to a style sheet:
    <link rel="stylesheet" href="https://www.w3schools.com/html/styles.css">

    This example links to a style sheet located in the html folder on the current web site: 
    <link rel="stylesheet" href="/html/styles.css">

    This example links to a style sheet located in the same folder as the current page:
    <link rel="stylesheet" href="styles.css">
    ```

### Some of CSS Properties

- Use the CSS `color` property for text colors
- Use the CSS `font-family` property for text fonts
- Use the CSS `font-size` property for text sizes
- Use the CSS `border` property for borders
- Use the CSS `padding` property for space inside the border
- Use the CSS `margin` property for space outside the border

```html
p {
  color: red;
  font-family: courier;
  font-size: 160%;
  border: 2px solid powderblue;
  padding: 30px;
  margin: 50px;
}
```


# Links

## Target

The target attribute specifies where to open the linked document.

The target attribute can have one of the following values:

- `_self` - Default. Opens the document in the same window/tab as it was clicked
- `_blank` - Opens the document in a new window or tab
- `_parent` - Opens the document in the parent frame
- `_top` - Opens the document in the full body of the window

```html 
<a href="https://www.w3schools.com/" target="_blank">Visit W3Schools!</a> 
```

## Direct and Indirect Reference

```html 
<a href="_template.html" target="_blank">Visit W3Schools!</a> 
<a href="Scrap_Code/React_Scrap/index.html" target="_blank">Visit W3Schools!</a> 
```

## Image as Link

```html
<h1>The image below is a link. Try to click on it.</h1>

<a href="Scrap_Code/React_Scrap/index.html" target="_blank"><img src="Colours.png" alt="Dental Page Image" style="width:600px;height:450px;"></a>
```

## Button as Link

To use an HTML button as a link, you have to add some JavaScript code.  
JavaScript allows you to specify what happens at certain events, such as a click of a button:
```
<button onclick="document.location='default.asp'">HTML Tutorial</button>
```

## Title of Link - a Tooltip

```
<a href="https://www.w3schools.com/html/" title="Go to W3Schools HTML section">Visit our HTML Tutorial</a>
```

## Link Colours

By default, a link will appear like this (in all browsers):

- An unvisited link is underlined and blue
- A visited link is underlined and purple
- An active link is underlined and red

```css
<style>
a:link {
  color: green;
  background-color: transparent;
  text-decoration: none;
}

a:visited {
  color: pink;
  background-color: transparent;
  text-decoration: none;
}

a:hover {
  color: red;
  background-color: transparent;
  text-decoration: underline;
}

a:active {
  color: yellow;
  background-color: transparent;
  text-decoration: underline;
}
</style>
```

### A link can also be styled as a button, by using CSS:

```css
<style>
a:link, a:visited {
  background-color: #f44336;
  color: white;
  padding: 15px 25px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
}

a:hover, a:active {
  background-color: red;
}
</style>
```


# BookMarks

## `id` for bookmark and then reference it

First, use the `id` attribute to create a bookmark:

```html

<a href="#C4">Jump to Chapter 4</a>

<h2 id="C4">Chapter 4</h2>

You can also add a link to a bookmark on another page:
<a href="html_demo.html#C4">Jump to Chapter 4</a>
```
