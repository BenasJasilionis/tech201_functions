def movie_rating(age: int):
    if age < 1 or age > 117:
        print("Please enter an age between 1 and 117")
    elif age >= 1 and age < 8:
        print(f"You are {age} and are able to watch U rated films")
    elif age >= 8 and age < 12:
        print(f"Your are {age} and are able to watch U and PG rated films")
    elif age >= 12 and age < 15:
        print(f"Your are {age} and are able to watch U, PG and 12A rated films")
    elif age >= 15 and age < 18:
        print(f"Your are {age} and are able to watch U, PG, 12A and 15 rated films")
    elif age >= 18:
        print(f"Your are {age} and are able to watch any film you like!")
    else:
        print("Please enter a valid age using numbers between 1 and 117")


user_age = int(input("How old are you?"))
movie_rating(user_age)
