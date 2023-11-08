import turtle


def irma_setup():
    """Creates the Turtle and the Screen with the map background
       and coordinate system set to match latitude and longitude.

       :return: a tuple containing the Turtle and the Screen

       DO NOT CHANGE THE CODE IN THIS FUNCTION!
    """
    import tkinter
    turtle.setup(965, 600)  # set size of window to size of map

    wn = turtle.Screen()
    wn.title("Hurricane Irma")

    # kludge to get the map shown as a background image,
    # since wn.bgpic does not allow you to position the image
    canvas = wn.getcanvas()
    turtle.setworldcoordinates(-90, 0, -17.66, 45)  # set the coordinate system to match lat/long

    map_bg_img = tkinter.PhotoImage(file="images/atlantic-basin.png")

    # additional kludge for positioning the background image
    # when setworldcoordinates is used
    canvas.create_image(-1175, -580, anchor=tkinter.NW, image=map_bg_img)

    t = turtle.Turtle()
    wn.register_shape("images/hurricane.gif")
    t.shape("images/hurricane.gif")

    return (t, wn, map_bg_img)

def wind_speed_to_category(wind_speed):
    if 74 <= wind_speed <= 95:
        return 1
    elif 96 <= wind_speed <= 110:
        return 2
    elif 111 <= wind_speed <= 129:
        return 3
    elif 130 <= wind_speed <= 156:
        return 4
    elif 157 <= wind_speed:
        return 5
    else:
        return 0

def hurricane_color(cat):
    if cat == 0:
        return 'White'
    elif cat == 1:
        return 'Blue'
    elif cat == 2:
        return 'Green'
    elif cat == 3:
        return 'Yellow'
    elif cat == 4:
        return 'Orange'
    elif cat == 5:
        return 'Red'

def irma():
    """Animates the path of hurricane Irma
    """
    (t, wn, map_bg_img) = irma_setup()

    # your code to animate Irma here
    t.hideturtle()
    t.penup()

    file_read = open("irma.csv", "r")
    hurricane_changes = file_read.readlines()[1:]

    for change in hurricane_changes:
        this_change = change.split(',')
        hurricane_latitude = float(this_change[2])
        hurricane_longitude = float(this_change[3])
        t.setposition(hurricane_longitude, hurricane_latitude)
        t.showturtle()
        t.pendown()
        hurricane_winds = int(this_change[4])
        hurricane_category = wind_speed_to_category(hurricane_winds)
        t.color(hurricane_color(hurricane_category))
        t.pensize((hurricane_category*3)/2)


# I got the wind speeds for categories from https://www.nhc.noaa.gov/aboutsshws.php

    return (t, wn, map_bg_img)

if __name__ == "__main__":
    (t, wn, map_bg_img) = irma()
    wn.exitonclick()
