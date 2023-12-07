def question_main(question):
    return input(question + " (YES/NO): ").lower() == 'yes'

def result(color_guess):
    print(f"Judging by the answers you've provided, I think your favorite color is... {color_guess.capitalize()}!")

def superluckyguess():
    print("Welcome to Scotts Color guessing game, are you ready?")

    monochromatic = question_main("Is your favorite color a monochromatic shade?")
    warm = question_main("Ah alright, is your favorite color a warmer tone like red, orange or yellow?")
    cool = question_main("Fair enough, how about a cooler tone like blue, green or purple?")

    if monochromatic:
        print("Oh wow, very bland taste, nice!")
        monochromatic_color = input("So it's something tasteless like black or white I assume (Type Black or White)? ")
        print(f"Wow, is it actually {monochromatic_color.capitalize()}? I'm sorry to hear that..")
        result(monochromatic_color)
    else:
        if warm:
            print("Oooh, very cozy!")
            warm_color = ['red', 'yellow', 'orange']

            for color in warm_color:
                if question_main(f"Is your favorite color {color}?"):
                    result(color)
                    return
        elif cool:
            print("A very vibrant choice, I like that!")
            cool_color = ['blue', 'green', 'purple']

            for color in cool_color:
                if question_main(f"Is your favorite color {color}?"):
                    result(color)
                    return

        if not warm and not cool:
            print("Either you're just saying no for fun or you like weirder colors, lets keep going...")
            neutral_colors = ['brown', 'pink', 'gray']

            for color in neutral_colors:
                if question_main(f"Is your favorite color {color}?"):
                    result(color)
                    return

        print("Alright I give up, it's probably something complex like Glaucous or Dead Salmon (yes that's an actual color look it up)")
        user_color = input("What is your favorite color then? ")
        print(f"{user_color.capitalize()}... definitely an interesting choice but who am I to judge?")
        print("It's always... different... when someone has a unique favorite color.")


if __name__ == "__main__":
    superluckyguess()