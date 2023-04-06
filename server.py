from flask import Flask  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/dojo')          # The "@" decorator associates this route with the function immediately following
def david():
    return 'Dojo!'  # Return the string 'Hello World!' as a response

@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'

@app.route('/say/flask')          # The "@" decorator associates this route with the function immediately following
def flask():
    return 'Hi Flask!'

@app.route('/say/michael')          # The "@" decorator associates this route with the function immediately following
def michael():
    return 'Hi Michael!'
 
@app.route('/say/john')          # The "@" decorator associates this route with the function immediately following
def john():
    return 'Hi John!'

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