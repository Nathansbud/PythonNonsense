"""
[Lesson 5: Functions]

We've all heard of functions...in math. For example:

f(x) = x + 5.

What happens when you put 5 into this function?
"""
#Objective
"""
Just kidding, it's trivial -- the answer is, well, f(5) = 10. But what does it MEAN for that process to take place? How did your program just...know what to do when you asked it to input a 5? What I'm trying to ask (in the hopes of inciting an artificial aha! moment) is what are the parts of a function that enable this to work?

Continuing with our math example, this function has 4 components, and we will extrapolate these components out to explain functions in programming:
    - Name
    - Arguments
    - Code
    - Return Type

The first element is simple -- the name our of function is f. Our function didn't need to be f -- you've no doubt seen functions like g(x), h(x), a(x)... -- but this function is called f. Math people really like to use SHORT NAMES because they are SHORT-SIGHTED. Just kidding, it's because everything is hand-written and it's easier to write f(x) = x + 5 than it is i_would_like_to_add_five_to_my_number(x) = x + 5.

In programming, with the magic of a) autocomplete and b) the fact that you want other people to read your code, we have no such silly succinctness quota for function names (usually). Instead, what we strive for (and the same is true for variable names) is VERBOSITY. It should be (somewhat) clear what your function does by looking at its name. 

By that logic, f is a horrible function name -- if I asked you what f does, you could look at its code to say "ah, well it gives me back x + 5", but there's no way in heck JUST f is telling you that. But, if say we changed it to add_5(x) = x + 5, suddenly you have a much better idea of what it does.

Names, in programming, are very important. A well-named function is the difference between a Google Search and a programmer nodding in understanding without needing to look anything up. Good names save time, good names save brain power, and good names have almost certainly saved lives in the past.

The structure of a programming function (or method, or sub-procedure, I will call them functions) is NOT as simple as it is in mathematics, though it's close:
"""
#Example:
def function_name(arg):
    pass #We're using the "pass" keyword here as introduced in L2 -- because a function expects code, not having anything there will throw an error, so we use pass to say "hey there will be code here, but not right now.

"""
See what just happened there? We made our function called function_name, and give it the variable "arg". Except, when we're talking to a function, we don't call it a variable, like you would if you just saw:

arg = 10

But instead, it's called an "argument" (or function argument). Arguments let you pass data to a function, in order to well, do things with them. Usually, this involves manipulating the argument in the "body" of the function in order to "return" some data (or change some data, or print some data) but we'll get back to what that all means later.

Let's, for a second, define our math function again, but let's do it in a way that is a lot more readable--we're programmers, after all. 
"""
#Example:
def add_5(number):
    return number + 5

"""
See that? We've defined our function (add_5), given it an argument (number), and then does something to our argument (number + 5). Except, hang on, what's this funny "return" keyword? 

Remember in the last lesson how we used that input and print? Those, as you might've guessed, were functions (I may have called them out of habit accidentally). They took in your argument (a string in both cases). In the print case, that's fine -- you give it a string, it outputs that string to the console, all is good. But, in the input case, that's not quite what happens. 

The line input("Input temperature: ") does, of course, print "Input temperature: " to the console. But, where does the data you type go? Why does the line:

    temperature = input("Input a temperature: ")

Give you a temperature variable? The answer, as you may have guessed from my reverse introduction, is the keyword RETURN. The input function RETURNS the value of your input. Our originally f(x) RETURNS x + 5 (hence, why you can know that f(5) = 10 -- 10 is returned). And, naturally, add_5(number) returns number + 5. But what about print?
"""
#Objective: Define a variable and set it equal to a print function, similar to how you set things equal to an input...then print it out
#NOTE: DON'T HOVER OVER THE YELLOW LINE (Or do if you want Pycharm to spoil the answer huehue)


"""
If you hovered over the line (you dirty cheater) or tested it for yourself, you may have seen the same thing: the function print returns "None." Weird, huh? Well, not really -- print is designed to, well, print to the console. Why would it need to return anything?

"None" is a keyword in python used to denote...well, nothing. None's type is NoneType (haha), and it's often used as a way to note that something hasn't been defined yet, i.e.:

    x = None
    print(x + 5) #TypeError; 

Let's get back to the whole function deal, and define our "return" a little more robustly: the return value of your function is what the function gives back when the function is called. This can be just about anything under the sun (any type, any value)...it can even be another function (which is kinda unique to Python)! 

The type of what a function returns is generally referred to as its RETURN TYPE. Remember the casting ordeal from the previous function? input's return type is a STRING, and add_5's return type is a FLOAT. But, add_5 is kind of a restrictive function, isn't it? Kind of a niche thing to know you're ONLY going to want to add 5...why don't we make add_5 a little more comprehensive -- let's make an add function.

In math, most functions (in high school, at least) are "single-variable" functions. That is to say, f(x) is a function named f that takes in a single argument called x. You may have seen functions with two variables like f(x, y) = x^2 + y^2), or even some really crazy ones with 3, 4, 5...these are called multi-variable functions, which encompasses the majority of programming functions.

The functions you've seen up until now were single-variable functions. But, there's nothing to stop us from making a function with 10 arguments:
"""
#Example: Test function with 10 args
def test_function(a1, a2, a3, a4, a5, a6, a7, a8, a9, a10):
    print(a1, a2, a3, a4, a5, a6, a7, a8, a9, a10)
"""
See that? This function has 10 arguments, and, curiously, NO return type. There's no "return print(a1, a2...)" or return anything else. This function, test_function, has a return type of one!

Now, you've got functions, arguments, and return types...how do we make a function do something? Why, by calling it of course!

To call a function, you use a pair of parenthesis. 
"""


