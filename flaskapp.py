from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return """
    <html>
        <head>
            <style>
                body {
                    background-color: #f0f8ff; /* Light blue background */
                    font-family: Arial, sans-serif;
                    text-align: center;
                    padding: 50px;
                }
                h1 {
                    color: #4CAF50; /* Green text */
                }
            </style>
        </head>
        <body>
            <h1>Hello, world!</h1>
            <p>Test asdads<br>Have a great day!</p>
        </body>
    </html>
    """
    
@app.route('/test')
def stuff():
    return "This is a test"
    
# Print registered routes
print(app.url_map)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1337, debug=True)