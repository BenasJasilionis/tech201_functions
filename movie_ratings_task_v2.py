def movie_rating(age):
    if age < 1 or age > 117:
        print("Please enter an age between 1 and 117")
    elif 1 <= age < 8:
        print(f"You are {age} and are able to watch U rated films")
    elif 8 <= age < 12:
        print(f"Your are {age} and are able to watch U and PG rated films")
    elif 12 <= age < 15:
        print(f"Your are {age} and are able to watch U, PG and 12A rated films")
    elif 15 <= age < 18:
        print(f"Your are {age} and are able to watch U, PG, 12A and 15 rated films")
    elif age >= 18:
        print(f"Your are {age} and are able to watch any film you like!")
    else:
        print("Please enter a valid age using numbers between 1 and 117")


user_age = int(input("How old are you?"))
movie_rating(user_age)
