

# your heading here

from flask import Flask

app = Flask(__name__) # Q0: Where have you seen similar syntax in other langs?

@app.route("/") # Q1: What points of reference do you have for meaning of '/'?
def hello_world():
    print(__name__) # Q2: Where will this print to? Q3: What will it print?
    return "No hablo queso!"  # Q4: Will this appear anywhere? How u know?

app.run()  # Q5: Where have you seen similar constructs in other languages?


'''
DISCO:
QCC:
0. It's reminiscent of Java's Object instantion
1. Probably the root of the file system
2. It'll print to the terminal
3. It'll print __main__
4. It'll appear on the webpage, and we know because we opened the webpage
5. Similar to Java running methods
...
INVESTIGATIVE APPROACH:
We ran the python file through the terminal, and checked the webpage. It said "No hablo queso!" which told us what the return did
'''