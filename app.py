from flask import Flask, render_template, request
import os

app = Flask(__name__)

# The function tries to open the file and read its contents.
# If an exception occurs while opening the file, it attempts to open the file in a different encoding.
# If the file cannot be opened, an error message is displayed to the user. If the file is successfully opened,
# the contents are displayed using a Jinja template called 'file.html'.
@app.route('/')
@app.route('/<filename>')
#The display_file() function takes an optional parameter filename that defaults to 'file1.txt'
def display_file(filename='file1.txt'):
    #Below the start and end variables are obtained from the query string parameters using the request.args.get() method. 
    # If no parameters are found, start is set to 1 and end is not set.
    start = request.args.get('start', 1, type=int)
    end = request.args.get('end', type=int)
    try:
        try:
            with open(filename, 'r', encoding='iso-8859-1') as f:
                lines = f.readlines()[start-1:end]
            
        except:
            
            with open(os.path.join( filename), 'r', encoding='utf-16-le') as f:
                lines = f.readlines()[start-1:end]

        #with open(filename, 'r') as f:
        
        print(lines)
        print(filename)
        return render_template('file.html', lines=lines, filename=filename, start=start, end=end)
    except Exception as e:
        print(f"EXCEPTION : {e}")
        return render_template('error.html', error=e)

#Finally, if the script is run as the main program, the Flask application is started by calling the run() method.
if __name__ == '__main__':
    app.run()
