"""
Lesson 2: Variables & Conditionals

Welcome to Lesson 2 of Zack Teaches Programming, where we will cover variables and conditionals. But first, a little bit of terminology.

In CS, as in math, variables are the meat and potatoes of the work you will do.

In Python (at the level that you need to concern yourself with) variables have 3 components: Name, Value, and Type
    - The name of a variable is, well, its name. Think X in math...this is what you use to refer to the variable. "Defining" is the act of creating a variable is called "defining" a variable
    - The value of a variable is what it actually represents (i.e. 10, "Park"). "Assigning" act of giving a variable a value is called "assigning" a value to that variable.
    - The type of a variable is what it "means"--is it a whole number (integer)? A word or sentence (string)? A list of decimals (float array)? Python is what is known as a "dynamically typed" language--more on this in a second.

For now, let us define and assign a value to our very first variable. In Python, this has 3 components:
    - The name, written on the LEFT side of the operation
    - An equals sign, used to ASSIGN a value to our named variable
    - The value, written on the RIGHT side of the operation

For example, creating a variable then printing it might look like:

    name = "Zack Amiton"
    age = 17
    print(username, age)

This would, presumably, print "Alex Park" and 10 to the console. You REFER to a variable by its NAME, which passes its VALUE to whatever you are using it for. Names cannot start with numbers, and are case sensitive (x is not equal to X); otherwise, they can be whatever you want.
"""
#Objective: Define your own name and age variable, and print them to the console



"""
Now, types. Python is a dynamically typed language, meaning that although every variable HAS a type, you don't define it explicitly. 

In the above example, name, which had the value "Zack Amiton" is what is known as a "string" (as in, string of characters). A string can hold as many characters as you want. 

Age, which had the value 17, is what is known as an "int" (as in integer). Integers can represent any whole number (more or less, there is an upper and lower limit but that's not too important right now).

The other main types you will likely deal with are:
    - bool (short for "boolean"): This represents a question, and can have the value True or False
        - Ex: is_adult = True
    - float (short for floating point number): This represents a decimal value, i.e. 1.5, 9.12341...
        - Ex: pi = 3.14159265
    - list (also known as an array): This holds a "list" of other variables, like [1, 2, 3, 4, 5], but we'll return to this one later 
        - Ex: colors = ["Red", "Orange", "Yellow", "Green", "Blue", "Indigo", "Violet"]
    - dict (short for dictionary): This holds a "key-value pair" but we'll return to this one later
        - Ex: person = {"Name":"Park", "Age":20, "Nationality":"Korean"}

Assigning a value to a variable AUTOMATICALLY defines its type--but this type might not always be what you want. More of this later.

The value (metaphorically speaking) of a variable is their ability to change. Not every kind of variable can be changed, but those that can are called "mutable." For instance, maybe I was sick of being called Zack Amiton, and wanted to go by Jacques Emerson from now on. All you need to do is...well, assign a new value to name:

    name = "Jacques Emerson"
    
In Python, type is not linked to a variable—-name is CURRENTLY a string, but if I assigned a number to it (name = 5), it is now an int. This is not true of all languages (i.e. in Java, you explicitly assign a type, like int age = 10, and the program doesn't let you assign a string to that variable).
"""
#Objective: Try changing your name/age to something else, and print it



"""
Following along? Cool. You've gotten your name, your age...but let's see if you are, in fact, an adult. How else will we determine whether to let you into a bar or...god forbid...watch content you must be an adult for (which nobody has ever lied on).

For this, we must bring return to our friend the boolean (mentioned above), and introduce a new idea: conditionals. 

A conditional, by nature, is a question--you are asking the program to evaluate an "expression" and see whether it is True or False. This is known as a "logical expression" or a "boolean expression," and for this we need 3 new keywords: if, else, and elif.

Let's say you, being you, want to enter a bar which...I dunno, exists as a program. I, the bouncer, have to scan this patron's age, asking the question: are you older than 21? Or, to define the problem more concretely: is your age ≥ 21? IF age IS ≥ 21, THEN I would probably let you in...ELSE if you aren't, THEN I would probably yell at you to scram. And, since I'm a concerned bouncer, if you're under the age of 10, I'm get REAL mad and call your parents

See what I did there? How subtle...let's translate that statement into code.
"""
#Objective: Comment out and run the following code; what do you think would happen?
"""
age = 20
if age >= 21:
    print("You are, in fact, an adult! Welcome inside...")
elif age < 10:
    print("Now you've done it, I'm gonna call your parents!")
else:
    print("You aren't drinking age, scram!")
"""

"""
In the above statement, you can see our components at work: 
    - if defines that you are about to ask a question
    - age >= 21 is our question, or our boolean expression, asking if AGE is GREATER THAN OR EQUAL TO 21. The boolean operators are:
        - == (is equal to), != (is not equal to)
        - > (greater than), >= (greater than or equal to)
        - < (less than), <= (less than or equal to)
    - : (colon) acts as our then, defining that we are about to say what happens next 
    - elif is short for else if, and defines an "alternate" if statement. In other words, if your age >= 21, then do the first thing, ELSE IF your age is < 10 (meaning your age was NOT >= 21), do the second thing. It executes the statements in order of encounter
    - else acts as our fall through case. if age is NOT greater than or equal to 21, then else is executed
    
In Python, TABS act as the means of breaking up chunks of code. Notice that the print statement is on the next line, and tabbed in by one. This is not just a style thing--this is how Python knows you are inside an if/else. Or, more formally, a "block" of code

Let's combine these things to have a quick final objective: a fahrenheit -> celsius converter.
"""
#Objective: Fahrenheit-Celsius Converter
#For this, I'm going to break out of block comment and leave some notes NEXT to code. I'm also going to introduce a simple new keyword, input("string"), which asks for user input. Type in a temperature value when asked by the console and hit enter.

#Celsius -> Fahrenheit: 9/5*TEMPERATURE + 32
#Fahrenheit -> Celsius: 5/9*(TEMPERATURE - 32)

#Let's make this a 2-way converter...we want a way to check if our code is FAHRENHEIT or CELSIUS to see which formula to use
is_celsius = True #Change this from True to False to test converting both ways
temperature = input("Input your temperature: ")
if is_celsius is True:
    #pass is a keyword which essentially tells Python, "hey, there will be code here, but just like, not now." It does nothing, but you NEED code after your if/else statements

    #Put a print statement here that will convert your temperature to fahrenheit, as in this case, the temperature is given in celsius

    pass
else:
    #Put a print statement here that will convert your temperature to celsius, as in this case, the temperature is given in fahrenheit
    pass

#To test your output is working correctly, try the input 42 from Celsius -> Fahrenheit (which should give 107.6), and 42 from Celsius to Fahrenheit (which should give 5.55555...)


"""
And thus concludes lesson 2!
"""
#End of Lesson








