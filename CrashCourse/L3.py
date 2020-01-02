"""
[Lesson 3: Lists]

So far, we've covered 2 main concepts:
    - Variables (int, string, float, bool)
    - Conditionals: if, else, elif

Now, it's time for another super crucial programming concepts: lists.

Consider the following situation: you are a classroom teacher, and want to store the names of the 20-odd students in your class. Per our previous example, you COULD (and indeed, novice programmers often DO) do something like so:

    student_one = "Zack"
    student_two = "Park"
    student_three = "John"
    ...
    student_twenty = "Dork"

But, of course, this is silly — you've created twenty variables to represent what is, in essence, a set of the same type of variable. Wouldn't it make more sense to just have a single "names" variable to hold all those?

Introducing: the list! Lists (or arrays, as they are more commonly referred to) are a basic type of "data structure" (a way to store and model data), and they crop up just about everywhere because they are incredibly, incredibly useful. Lists are "types" in the strictest sense (in the same way the strings and ints we encountered before were), but they have some cool features.

Let us define that list of names from before (though for my own sake, we're limiting it to 5 names:
"""
names = ["Zack", "Park", "John", "Jack", "Dork"]
"""
As you can see, we've just made a variable called names (from now on, I will simply use the form names variable) with 5 elements in it: "Zack", "Park", "John", "Jack", "Dork". As all of these elements are strings, convention is to call this...well, a list of strings, naturally.

Arrays have a ton of cool features associated with them. The first of these (and the most frequently used), inherent to the structure of a list, is indexing.

In the above list, you have...well, some elements in a list. Because it's a short list, naturally it's easy to tell how many elements are in it -- but, obviously, not every list does. 

Lists have an inherent "length" (or size) property to them, which can be accessed by using the len(list) function, similar to how we used print("string") and input("string") in the previous lesson. For example, print(len(names)) would print out the number of elements in the above list. Don't believe me? Try it!  
"""
#Objective: Programmatically check the number of elements in our list
print(len(names))
print(names.__len__()) #This method also works, but I'll explain why in a little bit
"""
Tinker with names as you see fit to verify that the above snippet does what you'd expect. So far, a bit contrived, but keep this function in mind because we're about to use it again in a mere moment!

The second aspect of lists that is INCREDIBLY, INCREDIBLY important is...well, indexing! Because, heck, what's the point of storing anything in a list if you can't get it back out! 

The "index" of an object is its position in a list of objects. So, in our above list, names, "Zack" is the 1st element in the list, followed by "Park", by "John", "Jack" -- except, programmers are dorks, and they start counting at 0. So, you say Zack is the 0th element of the list, Park is the 1st, John is the 2nd...

Knowing this, you can access these elements by their indices (or indexes, either is accepted as the plural). The syntax for doing so is list_name[index] -- so names[0] would return "Zack", names[1] returns "Park"...
"""
#Objective 1: Try printing the first element of your names list


#Objective 2: Try printing the LAST element of your names list, USING the len() function (HINT: List indexing starts at 0)



"""
If Objective 2 above went swimmingly for you, congrats! 

If you encountered an angry read error message above -- I presume IndexError, then now is a good time to teach you about error messages. IndexError is what happens when you give an index that is not part of your list -- so, if your list has 10 elements and you ask it for element 200, then...well, there is no element 200, so your program will flip you the bird. If your list has 10 elements and you ask for list[10] then it will also crash -- list[9] is the last element in a 10 element list (and if you still haven't cracked Objective 2, go back to the earlier objective and see what len() is giving you)

Moving on from this, indexing is a way to "access" elements in a list. But, at the same time, everybody makes mistakes, and everybody changes their mind. Luckily, those names aren't set in stone -- this Zack kid is a real pain in my side. Let's change him to something else.

Just like in Lesson 2, when we assigned a value to a variable, we can assign a value to an index of our list (which, itself, is a variable, as a list is just a collection of ordered variables). Of course, this variable does not have its "own" name -- its name would be list[index] -- but we can still assign a value to it in just the same way as:

    name = value

Or, more explicitly

    list[index] = value
    
Try changing that pesky "Zack", the 0th element of the list, to something else -- let's rename him to Jacques.
"""
#Objective: PROGRAMMATICALLY (don't just retype in the above list) change the first element of names from "Zack" to "Jacques", then print that element to verify that it worked



"""
If that worked, your list should now be:
    
    names = ["Jacques", "Park", "John", "Jack", "Dork"]

Progress! You can use indices to access and modify elements of our list, and you can check how long the list is. But what if, say, you're sick of your 5 students? You want a 6th? Obviously, you can go manually type out a new name, but that's BORING. Plus, I want a way to add 10, 100, 100000 names without typing them all out. What if my class has 100000 dorks in it, huh? It's a CS class, so that wouldn't be surprising, but YOU would be the real dork if you manually added them all by modifying the list by hand.

Introducing another function: append! Append, as the name might suggest, will append (add) an element to the end of your list. For example:
 
    nums = [1, 2, 3, 4, 5]
    nums.append(6)
    #nums is now [1, 2, 3, 4, 5, 6]
    
Let's add another dork to the end of our list -- heck, screw that let's add FIVE dorks to the end of our list. You've seen the append syntax above...now let's make it work!
"""
#Objective: Add 5 students named "Dork" to the end of nums using append



"""
If your dorking around worked correctly, your list should now read:
    
    names = ["Jacques", "Park", "John", "Jack", "Dork", "Dork", "Dork", "Dork", "Dork", "Dork"]

But, I think that was one dork too many -- let's remove some dorks, because 6 dorks is a bit overwhelming.

We're going to introduce 2 new functions here: pop(index) and remove(element)
    - pop() is a function which takes in an index to remove, and...yeets it into oblivion. 
    - remove() is a function which takes in an element to remove, and...yeets it into oblivion.

For instance, on our above nums list, let's say we want to get rid of the FIRST element in our list. We could do this by calling pop()!
    
    nums.pop(0)
    #nums should now be [2, 3, 4, 5, 6]

Remove, on the other hand, doesn't remove based on an INDEX, it removes an OBJECT. So, if you want it to remove the 6 from that list, you tell it to!

    nums.remove(6)
    #nums should now be [2, 3, 4, 5]

WARNING: REMOVE DOES NOT REMOVE ALL MATCHING ELEMENTS. It only removes the first object that matches from left to right!

Okay, we've got append, we've got remove, and we've got pop -- seems only natural that we get rid of some dorks, eh? 
"""
#Objective: Use pop and/or remove to get rid of EVERY student named "Dork"




"""
Ah, crap, winter break just ended and a whole bunch of students just arrived -- new students!
"""
new_names = ["New", "Newer", "Newest"]
"""
It simply won't do to have names AND new_names...that's two separate lists! If only there was a simply way to ADD two lists together...that would be simply...+...sorry, I mean PLUS...it would reduce our unnecessarily complexity.

If you couldn't read between the lines there, you can use the + sign (or + operator, as it is called), to join two lists:
"""
#Example: Comment out to see this in action!
# some_nums = [1, 2, 3]
# some_more_nums = [4, 5, 6]
# some_nums = some_nums + some_more_nums
# print(some_nums)
"""
So, if we can easily JOIN our lists...

Why don't we do that for our names & new_names!
"""
#Objective: Join names & new_names!





"""
Lists, indexing, assigning, appending, removing, popping, joining...that seems like a lot of list things!

Let's say we add ONE more function into the list of list functions -- this time, a simple one, though: sum()!

Sum, of course, does not make sense on strings -- you can't sum "Cat" and "Dog". You can, however, sum numbers together. For instance:
    
    summable = [1, 2, 3, 4, 5, 6]
    print(sum(summable))

Should print the sum of a summable list! So, as should be familiar to most people...it's time to do some averaging!

According to the internet, the average monthly temps in Toamasina, Madagascar are:

Jan: 86	
Feb: 86	
March: 86
April: 84	
May: 81	 
June: 79	
July: 77	
August: 77	
September: 79	
October: 81	
November: 82
December: 84

Unfortunately, I have this list of random temperatures that some dork filled with meme and stupid numbers...I'll need you to replace each element with the corresponding monthly temperature -- where first index represents January, and the last represents December -- then average the result and add it to the list of malagasy averages:

"""
#Final Objective: Find the average yearly temperatures in Toamasina, Madagascar, then add it to the list of Madagascar Averages
temperatures = [69, 69, 420, 69, 42, -400, 20, 9001, 80085, 69, 17, 2020]

#Add that average to the end of this list programmatically:


nationwide_temps = []
"""
And...that should be it for lists! But don't think they're going anywhere, because you're about to see a lot of them in Lesson 4!
"""
#End of Lesson

