def paint_calculation(height,width,cover):
#using math formuals:
    area=height*width
    no_of_cans=area//cover
    print("you need",no_of_cans,"cans of paint the wall")

h=int(input("enter height of wall in metres: "))
w=int(input("enter width of wall in metres: "))
coverage=2
paint_calculation(h,w,coverage)