# Part 2

# user inputs number of books purchased
books_purchased = int(input("Enter the number of books you've purchased this month: "))

# starting if block with any integer input less than 0
if books_purchased < 0:
    print("That's not possible.")
# if number of books purchased is 0
elif books_purchased == 0:
    print("You've purchased {} books this month which means you've earned 0 points.".format(books_purchased))
# created a second block here to get rid of the 's' in books
elif books_purchased == 1:
    print("You've purchased {} book this month which means you've earned 0 points.".format(books_purchased))
# if user purchased 2 or 3 books
elif 2 <= books_purchased <= 3:
    print("You've purchased {} books this month which means you've earned 5 points!".format(books_purchased))
# if user purchased 4 or 5 books
elif 4 <= books_purchased <= 5:
    print("You've purchased {} books this month which means you've earned 15 points!".format(books_purchased))
# if user purchased 6 or 7 books
elif 6 <= books_purchased <= 7:
    print("You've purchased {} books this month which means you've earned 30 points!".format(books_purchased))
# for any other integer inputted which in this case is anything >= 8
else:
    print("You've purchased {} books this month which means you've earned 60 points! Great work!".format(books_purchased))

