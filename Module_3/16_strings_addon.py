this_is_string = "Hi there!"

the_same_string = 'Hi there!'

this_is_string == the_same_string # True

text = """This is first line
And second line
Last third line"""

song = '''Jingle bells, jingle bells
Jingle all the way
Oh, what fun it is to ride
In a one horse open sleigh'''

one_line_text_1 = "Textual data in Python is handled with str objects, or strings. Strings are immutable sequences of Unicode code points. String literals are written in a variety of ways: single quotes, double quotes, triple quoted."

one_line_text_2 = "Textual data in Python is handled with str objects," \
                " or strings. Strings are immutable sequences of Unicode" \
                " code points. String literals are written in a variety" \
                " of ways: single quotes, double quotes, triple quoted."

print(one_line_text_1 == one_line_text_2) # True

("spam " "eggs") == "spam eggs"  # True

one_line_text = ("Textual data in Python is handled with str objects,"
                " or strings. Strings are immutable sequences of Unicode"
                " code points. String literals are written in a variety "
                " of ways: single quotes, double quotes, triple quoted.")

query = ("SELECT * "
         "FROM some_table "
         "WHERE condition1 = True "
         "AND condition2 = False")

print("Hello\nWorld")
#Hello
#World

print("Hello\tWorld") # Hello	World
print("Hello my little\rsister") #sistermy little
print("Hello\bWorld") #HellWorld
print("Hello\\World") #Hello\World
print('It\'s a beautiful day') #It's a beautiful day
print("He said, \"Hello\"") #He said, "Hello"




