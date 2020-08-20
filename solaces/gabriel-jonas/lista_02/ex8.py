def show_stars (row):
    print ("```")
    screen = "*"
    for i in range(row):
        print (screen)
        screen = screen + "*"
    print ("```")

show_stars(3)