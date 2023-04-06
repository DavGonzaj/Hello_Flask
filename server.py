from flask import Flask  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/dojo')          # The "@" decorator associates this route with the function immediately following
def dojo():
    return 'Dojo!'  # Return the string 'Hello World!' as a response

@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Sorry! No response. Try again.!'

@app.route('/hello/<name>')          # The "@" decorator associates this route with the function immediately following
def helloName(name):
    return f"Hi {name}!"


@app.route('/repeat/35/hello/')          # The "@" decorator associates this route with the function immediately following
def repeatHello():
    return 'Hello' * 35

@app.route('/repeat/80/bye')          # The "@" decorator associates this route with the function immediately following
def repeatBye():
    return 'bye' * 80

@app.route('/repeat/80/dogs')          # The "@" decorator associates this route with the function immediately following
def repeatDogs():
    return 'dogs' * 99
  
    
if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

#python server.py