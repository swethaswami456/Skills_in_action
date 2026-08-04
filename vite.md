Vite is basically a project scaffolding + development tool.
It does two main things:

- Creates the initial project structure for you.
- Provides the local development server (npm run dev) and build process (npm run build).

For example, when you run:

```
npm create vite@latest my-app -- --template react
```

Vite generates something like:

```
my-app/
│
├── src/
│   ├── App.jsx
│   ├── main.jsx
│
├── public/
├── package.json
├── vite.config.js
└── index.html
```

## If you're curious, you can even use React without Vite
Create a single HTML file:

```html
<!DOCTYPE html>
<html>
  <body>
    <div id="root"></div>

    https://unpkg.com/react@18/umd/react.development.js
    https://unpkg.com/react-dom@18/umd/react-dom.development.js

    <script>
      const root = ReactDOM.createRoot(document.getElementById("root"));

      root.render(
        React.createElement("h1", null, "Hello Swetha!")
      );
    </script>
  </body>
</html>
```
