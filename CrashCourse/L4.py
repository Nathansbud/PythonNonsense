"""
[Lesson 4: Loops! Loops! Loops! Loops! Loops!]

If you thought lists were magical (and indeed, I often do, then wait until you get a handle on loops!

Loops, in essence, combine conditionals from lesson 2 and lists from lesson 3, to solve a problem you may have run into a bit last lesson: how do I do something x amount of times without having to retype the same function over and over?

If you recall adding "Dork" to the names list, you likely did:

    names.append("Dork")
    names.append("Dork")
    names.append("Dork")
    names.append("Dork")
    names.append("Dork")

To add 5 dorks. Which, sure, it WORKS, but...programming is supposed to automate your life, isn't it? It feels silly copying and pasting the same line again and again...if only you could, say, LOOP THROUGH those things.

Obviously, since this lesson is called loops (loops, loops, loops), we're getting to that. But, hold your horses.

What, at its core, does "looping" mean? Looping (or iterating) is a programming concept which essentially means to do something repeatedly, as its name might imply. That said, there's a bit more to it -- namely, how long do you loop for?

There are 2 main types of loops, and a couple different versions of those loops:
    - while loop
    - for loop

While loops, which we'll look at first, are essentially just a conditional statement (think lesson 2). They are defined using the keyword "while" and given a condition during which they should continue looping.

In plain english, and using the bar example from lesson 2, we could use a while loop to simulate a person desperately trying to get into a bar each year. Each year, their age increases by 1, but we still have to check whether or not that person is <21 to see if they can be let in.

To construct this loop, let's make a simple example while loop:
"""
#NOTE: you can hit the red stop button to stop a program from running)
#Example: While loop with an incrementing "age" variable
age = 10
while age < 21:
    print(str(age) + "? Too young!") #Note: str(number) is a way to turn a number (age, an int, in this case) into a string; int and string can't be added together otherwise
    age = age + 1 #Note: the simplified form age += 1 can also be used to do this
print(str(age) + "? Sure, you can enter the bar!")
"""
Running the above code, you should hopefully have a handle on how the while loop is working:
    - while tells the program to loop WHILE some condition is true
    - age < 21 is the condition -- the code inside the while loop program will loop forever so long as age is < 21, and stop the moment it is true
    - : (colon) is the then, just like it is for the conditionals in lesson 2

Tracing what is happening, age starts at 10. Age < 21, so we enter the while loop, print out that the person is too young, and increase age by 1. This repeats WHILE age is < 21, and then once that final age = age + 1 occurs, age = 21 (so age < 21 is FALSE) and therefore we exit the loop, printing that "sure you can enter" message.

For the sake of learning, modify the above loop by COMMENTING OUT the line: 
    
    age = age + 1
    
What happened? 

If my programming spidey senses are correct (and indeed, you may have expected this), then "10? Too young!" printed a bazillion times before you got fed up and hit stop. Why?

This is what's called an infinite loop -- while loops will loop while their CONDITION is true. In other words, nothing is changing age, so age is always < 21, so you will be trapped inside of that loop forever. Muahaha. 

In other words, always make sure you modify the variable being checked by your condition SOMEHOW. If all else fails, there's also another keyword you can look to, called break. Try replacing the line:
    
    age = age + 1

With the line

    break

What happens when you ran the program?
 
If my sensei senses are spot-on, you had one "10? Too young!" and then a "10? Sure, you can enter the bar!" Except, age was still < 21. How did we leave the loop? 

Break immediately terminates the loop whenever it is encountered. This is not usually good form unless you're doing it for a specific reason (for now, I'd avoid using the break keyword), but it's good to be aware of. 

For the sake of practice, try writing your own while loop -- i'll give you a count variable to work off of.
"""
#Objective: Make a while loop that prints the numbers 0 to 100!
count = 1



"""
Now, back to that pesky names 5x append call. Let's use a while loop to simplify that!
"""
#Objective: Use a while loop to recreate the ["Jacques", "Park", "John", "Jack", "Dork", "Dork", "Dork", "Dork", "Dork", "Dork"] list!
names = ["Jacques", "Park", "John", "Jack", "Dork"]
#We want to append 5 dorks to this list. Let's do that using a while loop!



"""
So, to summarize: while loops! They loop "forever" until their condition is no longer true, and you should always make sure you modify the variable being checked in the condition (or, if all else fails, yeet yourself outta there with a break call).

But, while loops, as great as they are, kinda feel like opening a bike lock with a pair of bolt cutters rather than a key. Sure, it gets the job done -- you've unlocked your bike lock, sorta -- but they're imprecise, and kinda overkill. You don't always WANT the power of (potential) infinity on your hands. Maybe you just, well, want to loop 5 times! Surely, there's a way to do that...

Introducing, the for loop! Whereas the while loop loops WHILE some condition is true, for loops loop FOR some number of iterations. 

For loops are loops which introduce some variable -- referred to as the index or the element -- which is then automatically changes each time the loop runs through. Whereas with your while loop, you defined some count variable and increased it, in the for loop...well, it's a bit different.

There are two variants of the for loop. The first, the "for i" loop, is not very "Pythonic" -- that is to say, it's a convention that is not as clean and nice as Python usually is. It's more typical of languages like Java/C++ than it is of Python, but as somebody who learned to program in Java, it's what I feel makes "more" sense in terms of learning about for loops.


The "for i" for loop takes the following form:

    for i in range(start_value, end_value, change_by): 
        print(i)
    #Note: change_by is assumed to be 1, so omit it unless you want to change i by more than 1 each loop
    #Note: i is arbitrary -- it is simply a variable name, but convention is to use i. If you have nested for loops (loops inside of loops), the convention is to go i, then j, then k, then ...
    
Where, to use math language, i has the domain [start_value, end_value)...in other words, it loops from start_value (inclusive) to end_value (exclusive), being increased by change_by for each iteration of the loop. This loop is identical in function to:
    
    i = start_value
    while i < end_value:
        print(i)
        i += change_by   

In other words, for loops and while loops can largely accomplish the same things -- the tool you choose depends on what you're trying to do. In this case, for loops are nice because they provide you an index (i) with which to use to do things.
"""
#Objective: Make a for loop that prints the numbers 0 to 100 (this should be simpler than the while loop version)



"""
Now, you're ready for a classic programming challenge -- although to do introduce it, I need to tell you about a really handy operator: modulo.

The modulo operator (%) returns the "remainder" of a division operation, like you used to do in ES/MS and then kinda stopped doing. So, 10/3 has a reminder of 1, 100/14 has a remainder of 2, 1000/1000 has a remainder of 0, that sorta thing.

To get this remainder, you do 
    
    NUMBER % DIVIDING_NUMBER

Which returns the remainder -- 10 % 3 returns 1 (10 / 3 has a remainder of 1), 5 % 5 returns 0 (5 / 5 has remainder 0), 100 % 99 has a remainder 1...try this out for yourself!
"""
#Objective: Use a for loop to print the remainder, or modulo result, of dividing check (given below) by all the numbers from 1 -> 100
check = 100



"""
Now you're REALLY ready for a classic programming challenge: The FizzBuzz challenge.

FizzBuzz is a programming challenge where:
    - Every time you reach a number divisible by 3 (having 0 as the modulo remainder), you print "Fizz"
    - Every time you reach a number divisible by 5 (having 0 as the modulo remainder), you print "Buzz"
    - If BOTH of these are true, you print "FizzBuzz" 

First, though, a slightly simpler challenge that should give you the inspiration:
"""
#Objective 1: Use a for loop and the modulo operator to code the FizzBuzz challenge!





#Objective 2: Use a for loop to check whether or not the numbers from 0 -> 100 are EVEN...don't forget your good friend, the if statement (which can be put inside a for loop)!
#(Hint: A number is either even or odd...which is TWO different states...)



"""
Congrats, you're a real programmer now! That's a classic (very very beginner) programming puzzle...I'd give you the diamond puzzle, but I don't hate you that much yet.

So, for i loop...you might not get how it differs from the while loop THAT drastically -- and indeed, functionally it doesn't -- but it has an advantage I haven't yet touched upon yet. Remember our good friends from Lesson 3? That's right, baby, lists are back, and back with a vengeance.

Programming classes don't touch upon lists without loops -- it's sacrilege. For loops (generally) start at 0, lists generally start at 0, and there's a reason for that. You got a list of 10 things you wanna loop through? Let's see...how could you use a loop to do that...OH WAIT:
    
"""
# Ignore this line -- I didn't want to type out ["Name 0", "Name 1", "Name 2", ..., "Name 99"] -- or don't ignore it and look up "generator" in the documentation, they're magical
name_list = [f"Name {i}" for i in range(100)]
#Objective: Comment out and run this example code to have your mind blown
# for i in range(len(name_list)):
#   print(name_list[i])

"""
Did you see it? Did you see the magic? That's right, baby, you can use the count variable of a for loop as the index for a list! They're like two peas in a pod! The main use case of lists (besides doing something x amount of times) is being able to easily loop through lists! 

If you were wondering why the upper range bound was exclusive (i.e. for i in range(10) means i takes on the values 0-9, but not 10), this is why: lists start at 0, so you wouldn't WANT to do list[upper_bound], you want list[upper_bound - 1] as the final value. Magic. Friggin magic.

Now you've seen the magic...it's time to wield it, baby.
"""
#Objective 1: Construct a for loop to change every name in name_list to "Park" (because programmers are nothing if not self-centered)





#Object 2: Construct a for loop to...loop BACKWARDS through your name list (maybe comment out the above thing, since everything being named Park would make it hard to tell)
#Hint: Remember the "change_by" in the original for loop explanation up above...




"""
Feeling kinda steady? All that was the first kind of for loop -- the for i loop. Now that you've got your sea legs under ya, let's take a look at the other kind: for each loops.

I'll admit -- I used to hate these, when I first learned Python. I didn't get them. Now, I use them about 30x more often than a for i loop, so believe me when I say they rock.

Where for i loops are used for a range of numbers, for each loops are used to loop over elements of a list (and technically for i loops are for each loops in Python yada yada yada you don't need to know that yet).

For each loops are similar looking to for i loops, except instead of using the silly range(start, end, count) thing, you just loop over a list:
    
    names = ["Name", "Nombre", "Nomenclature"]
    for name in names:
        print(name)

Clean? Elegant? Beautiful? Yes. Yes to all of the above. 
"""
#Objective: Add up all the scores in the following list that AREN'T DIVISIBLE BY 3 using a for each loop
scores = [100, 24, 12938, 129, 1230, 24, 5, 1239, 29, 12039, 23, 4215, 12, 456, 1239, 123, 91283, 452, 1249, 129, 42, 7, 7, 1293, 3, 3, 3, 3, 3, 3, 3, 1239]
total = 0

"""
And with that, baby, you've seen lists and loops!
"""
#End of Lesson