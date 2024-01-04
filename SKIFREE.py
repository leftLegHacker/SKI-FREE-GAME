# We had alot of things done together and everypart was edited by both of us at some point but i tried to get the
# Labled the best i could for what we did

from tkinter import *
import random
from PIL import Image, ImageTk
from time import sleep
root = Tk()
canvas = Canvas(root, width=500, height=800)
# Max
game_over = False
dy = 5

score = 0
score_display = canvas.create_text(480, 10, text="Score: 0", anchor=NE, font=("Helvetica", 15, "bold"), fill="black")

finishLine= canvas.create_rectangle(0,700,500,710, fill="black")

# both of us Max got it in the end to work and edited the images
skier_image = Image.open('skier_body.jpg')
skier_image = skier_image.resize((25, 48))
skier_image = ImageTk.PhotoImage(skier_image)
skier_id = canvas.create_image(237.5, 0, anchor=NW, image=skier_image)

skier1= canvas.create_rectangle(0,0,35,58)
canvas.itemconfig(skier1, state="hidden")  
canvas.move(skier1,237.5,0)


tree_image = Image.open('treeski.jpg')
tree_image = tree_image.resize((40, 40))
tree_image = ImageTk.PhotoImage(tree_image)
#both of us 
tree_id = canvas.create_image(0, 0, anchor=NW, image=tree_image)
tree_id1 = canvas.create_image(0, 0, anchor=NW, image=tree_image)
tree_id2 = canvas.create_image(0, 0, anchor=NW, image=tree_image)
tree_id3 = canvas.create_image(0, 0, anchor=NW, image=tree_image)
tree_id4 = canvas.create_image(0, 0, anchor=NW, image=tree_image)
tree_id5 = canvas.create_image(0, 0, anchor=NW, image=tree_image)
tree_id6 = canvas.create_image(0, 0, anchor=NW, image=tree_image)

# Max
def get_skier_edges():
    global skier  
    skier = canvas.bbox(skier_id)
    return skier

skier_edges = get_skier_edges()
x0 = skier_edges[0]
y0 = skier_edges[1]
x1 = skier_edges[2]
y1 = skier_edges[3]

skier = [x0, y0, x1, y1]

# Dano's Random madness
xT = random.randrange(1,480)
yT = random.randrange(50,100)
xT1 = random.randrange(1,480)
yT1 = random.randrange(100,200)
xT2 = random.randrange(1,500)
yT2 = random.randrange(200,300)
xT3 = random.randrange(1,480)
yT3 = random.randrange(300,400)
xT4 = random.randrange(1,480)
yT4 = random.randrange(400,500)
xT5 = random.randrange(1,480)
yT5 = random.randrange(500,600)
xT6 = random.randrange(1,480)
yT6 = random.randrange(100,680)
xJ = random.randrange(1,480)
yJ = random.randrange(100,350)
xJ1 = random.randrange(1,480)
yJ1 = random.randrange(400,680)


# combanation of both mixed together
tree = canvas.create_rectangle(0,0,40,40)
canvas.itemconfig(tree, state="hidden")  
tree1 = canvas.create_rectangle(0,0,40,40)
canvas.itemconfig(tree1, state="hidden")
tree2 = canvas.create_rectangle(0,0,40,40)
canvas.itemconfig(tree2, state="hidden")
tree3 = canvas.create_rectangle(0,0,40,40)
canvas.itemconfig(tree3, state="hidden")
tree4 = canvas.create_rectangle(0,0,40,40)
canvas.itemconfig(tree4, state="hidden")
tree5 = canvas.create_rectangle(0,0,40,40)
canvas.itemconfig(tree5, state="hidden")
tree6 = canvas.create_rectangle(0,0,40,40)
canvas.itemconfig(tree6, state="hidden")

canvas.move(tree1, xT1,yT1)
canvas.move(tree2, xT2,yT2)
canvas.move(tree3, xT3,yT3)
canvas.move(tree4, xT4,yT4)
canvas.move(tree5, xT5,yT5)
canvas.move(tree6, xT6,yT6)



treeaccy = tree_id
treeaccy1 = tree_id1
treeaccy2 = tree_id2
treeaccy3 = tree_id3
treeaccy4 = tree_id4
treeaccy5 = tree_id5
treeaccy6 = tree_id6

canvas.move(treeaccy1, xT1,yT1)
canvas.move(treeaccy2, xT2,yT2)
canvas.move(treeaccy3, xT3,yT3)
canvas.move(treeaccy4, xT4,yT4)
canvas.move(treeaccy5, xT5,yT5)
canvas.move(treeaccy6, xT6,yT6)


jump = canvas.create_rectangle(0,0,30,5, fill = "grey")
jump1 = canvas.create_rectangle(0,0,30,5, fill = "grey")
canvas.move(jump, xJ,yJ)
canvas.move(jump1, xJ1,yJ1)

#Max worked on skier move with game over banner and button
def skier_move():
    global dy, skier_id, skier1, game_over, score
    if game_over:
        dy = 0
    else:
        canvas.move(skier_id, 0, dy)
        canvas.move(skier1, 0, dy)
   
    canvas.tag_raise(skier_id)

    skier_coords = canvas.coords(skier_id)
    y0 = skier_coords[1]
   
    if not game_over:
        score += 5
        canvas.itemconfig(score_display, text=f"Score: {score}")

    if y0 >= 700:
        canvas.move(skier_id, 0, -700)
        canvas.move(skier1, 0, -700)
        reposition_trees()
   
    root.after(25, skier_move)

    check_collision()
    check_collision1()
    check_collision2()
    check_collision3()
    check_collision4()
    check_collision5()
    check_collision6()
    check_collisionJump()
    check_collisionJump1()


# Max's work! got the repostion of trees to work. i was strugiling with it and he made it happen!!
def reposition_trees():
    global xT, yT, xT1, yT1, xT2, yT2, xT3, yT3, xT4, yT4, xT5, yT5, xT6, yT6

    def check_bounds(x, y):
        x = max(min(x, 500), 0)
        y = max(min(y, 800), 0)
        return x, y

    xT, yT = check_bounds(random.randrange(1, 480), random.randrange(50, 100))
    canvas.move(tree, xT - canvas.coords(tree)[0], yT - canvas.coords(tree)[1])
    canvas.move(treeaccy, xT - canvas.coords(treeaccy)[0], yT- canvas.coords(treeaccy)[1])
   
    xT1, yT1 = check_bounds(random.randrange(1, 480), random.randrange(100, 200))
    canvas.move(tree1, xT1 - canvas.coords(tree1)[0], yT1 - canvas.coords(tree1)[1])
    canvas.move(treeaccy1, xT1 - canvas.coords(treeaccy1)[0], yT1 - canvas.coords(treeaccy1)[1])
   
    xT2, yT2 = check_bounds(random.randrange(1, 500), random.randrange(200, 300))
    canvas.move(tree2, xT2 - canvas.coords(tree2)[0], yT2 - canvas.coords(tree2)[1])
    canvas.move(treeaccy2, xT2 - canvas.coords(treeaccy2)[0], yT2 - canvas.coords(treeaccy2)[1])
   
    xT3, yT3 = check_bounds(random.randrange(1, 480), random.randrange(300, 400))
    canvas.move(tree3, xT3 - canvas.coords(tree3)[0], yT3 - canvas.coords(tree3)[1])
    canvas.move(treeaccy3, xT3 - canvas.coords(treeaccy3)[0], yT3 - canvas.coords(treeaccy3)[1])
   
    xT4, yT4 = check_bounds(random.randrange(1, 480), random.randrange(400, 500))
    canvas.move(tree4, xT4 - canvas.coords(tree4)[0], yT4 - canvas.coords(tree4)[1])
    canvas.move(treeaccy4, xT4 - canvas.coords(treeaccy4)[0], yT4 - canvas.coords(treeaccy4)[1])

    xT5, yT5 = check_bounds(random.randrange(1, 480), random.randrange(500, 600))
    canvas.move(tree5, xT5 - canvas.coords(tree5)[0], yT5 - canvas.coords(tree5)[1])
    canvas.move(treeaccy5, xT5 - canvas.coords(treeaccy5)[0], yT5 - canvas.coords(treeaccy5)[1])
   
    xT6, yT6 = check_bounds(random.randrange(1, 480), random.randrange(100, 680))
    canvas.move(tree6, xT6 - canvas.coords(tree6)[0], yT6 - canvas.coords(tree6)[1])
    canvas.move(treeaccy6, xT6 - canvas.coords(treeaccy6)[0], yT6 - canvas.coords(treeaccy6)[1])
   

# Dano got the player movment then we both added things into the functions
def sL(event):
    global game_over
    if not game_over:
        canvas.move(skier_id, -10, 0)
        canvas.move(skier1, -10, 0)
    canvas.tag_raise(skier_id)

    x0, y0, x1, y1 = canvas.coords(skier1)
    if x0 <= 0:
        canvas.move(skier_id, 0, 0)

    else:
        canvas.move(skier_id, -10, 0)

    x0, y0, x1, y1 = canvas.coords(skier1)
    if x0 <= 0:
        canvas.move(skier1, 0, 0)
    else:
        canvas.move(skier1, -10, 0)

    check_collision()
    check_collision1()
    check_collision2()
    check_collision3()
    check_collision4()
    check_collision5()
    check_collision6()
    check_collisionJump()
    check_collisionJump1()



def sR(event):
    global game_over
    if not game_over:
        canvas.move(skier_id, 10, 0)
        canvas.move(skier1, 10, 0)
    canvas.tag_raise(skier_id)

    x0, y0, x1, y1 = canvas.coords(skier1)
    if x0 <= 0:
        canvas.move(skier_id, 0, 0)

    else:
        canvas.move(skier_id, 10, 0)

    x0, y0, x1, y1 = canvas.coords(skier1)
    if x0 <= 0:
        canvas.move(skier1, 0, 0)
    else:
        canvas.move(skier1, 10, 0)

    check_collision()
    check_collision1()
    check_collision2()
    check_collision3()
    check_collision4()
    check_collision5()
    check_collision6()
    check_collisionJump()
    check_collisionJump1()
   


def sD(event):
    global game_over
    if not game_over:
        canvas.move(skier_id, 0, 10)
        canvas.move(skier1, 0, 10)
    canvas.tag_raise(skier_id)

    x0, y0, x1, y1 = canvas.coords(skier1)
    if x0 <= 0:
        canvas.move(skier1, 0, 0)
                   
    if y0 >= 700:
        canvas.move(skier1,0,-700)
    check_collision()
    check_collision1()
    check_collision2()
    check_collision3()
    check_collision4()
    check_collision5()
    check_collision6()
    check_collisionJump()
    check_collisionJump1()


#max got the collison to work
def check_collision_with_tree():
    global game_over
    skier_coords = canvas.coords(skier1)
    tree_coords = canvas.coords(tree1)

    if (
        skier_coords[0] < tree_coords[2]
        and skier_coords[2] > tree_coords[0]
        and skier_coords[1] < tree_coords[3]
        and skier_coords[3] > tree_coords[1]
    ):
        game_over_text_func()
        game_over = True


#Dano created the copys of collisons and edited thoguh for each one
def check_collision():
    global game_over
    skier_coords = canvas.coords(skier1)
    tree_coords = canvas.coords(tree)

    if (
        skier_coords[0] < tree_coords[2]
        and skier_coords[2] > tree_coords[0]
        and skier_coords[1] < tree_coords[3]
        and skier_coords[3] > tree_coords[1]
    ):
        game_over_text_func()
        game_over = True
       
       
       
def check_collision1():
    global game_over
    skier_coords = canvas.coords(skier1)        
    tree1_coords = canvas.coords(tree1)
    if (
        skier_coords[0] < tree1_coords[2]
        and skier_coords[2] > tree1_coords[0]
        and skier_coords[1] < tree1_coords[3]
        and skier_coords[3] > tree1_coords[1]
    ):
        game_over_text_func()
        game_over = True



def check_collision2():
    global game_over
    skier_coords = canvas.coords(skier1)        
    tree2_coords = canvas.coords(tree2)
    if (
        skier_coords[0] < tree2_coords[2]
        and skier_coords[2] > tree2_coords[0]
        and skier_coords[1] < tree2_coords[3]
        and skier_coords[3] > tree2_coords[1]
    ):
        game_over_text_func()
        game_over = True



def check_collision3():
    global game_over
    skier_coords = canvas.coords(skier1)        
    tree3_coords = canvas.coords(tree3)
    if (
        skier_coords[0] < tree3_coords[2]
        and skier_coords[2] > tree3_coords[0]
        and skier_coords[1] < tree3_coords[3]
        and skier_coords[3] > tree3_coords[1]
    ):
        game_over_text_func()
        game_over = True



def check_collision4():
    global game_over
    skier_coords = canvas.coords(skier1)        
    tree4_coords = canvas.coords(tree4)
    if (
        skier_coords[0] < tree4_coords[2]
        and skier_coords[2] > tree4_coords[0]
        and skier_coords[1] < tree4_coords[3]
        and skier_coords[3] > tree4_coords[1]
    ):
        game_over_text_func()
        game_over = True
   
   
   
def check_collision5():
    global game_over
    skier_coords = canvas.coords(skier1)        
    tree5_coords = canvas.coords(tree5)
    if (
        skier_coords[0] < tree5_coords[2]
        and skier_coords[2] > tree5_coords[0]
        and skier_coords[1] < tree5_coords[3]
        and skier_coords[3] > tree5_coords[1]
    ):
        game_over_text_func()
        game_over = True
       
       

def check_collision6():
    global game_over
    skier_coords = canvas.coords(skier1)        
    tree6_coords = canvas.coords(tree6)
    if (
        skier_coords[0] < tree6_coords[2]
        and skier_coords[2] > tree6_coords[0]
        and skier_coords[1] < tree6_coords[3]
        and skier_coords[3] > tree6_coords[1]
    ):
        game_over_text_func()
        game_over = True
       
       
# dano started jumps and max added bonus and score     
def check_collisionJump():
    global score
    skier_coords = canvas.coords(skier1)        
    jump_coords = canvas.coords(jump)
    if (
        skier_coords[0] < jump_coords[2]
        and skier_coords[2] > jump_coords[0]
        and skier_coords[1] < jump_coords[3]
        and skier_coords[3] > jump_coords[1]
    ):
        canvas.move(skier1,0,100)
        canvas.move(skier_id,0,100)
        score+=1000
        bonus = canvas.create_text(250, 100, text="+1000", font=("Helvetica", 15, "bold"), fill="green")
        canvas.after(1000, lambda: canvas.delete(bonus))



def check_collisionJump1():
    global score
    skier_coords = canvas.coords(skier1)        
    jump1_coords = canvas.coords(jump1)
    if (
        skier_coords[0] < jump1_coords[2]
        and skier_coords[2] > jump1_coords[0]
        and skier_coords[1] < jump1_coords[3]
        and skier_coords[3] > jump1_coords[1]
    ):
        canvas.move(skier1,0,100)
        canvas.move(skier_id,0,100)
        score+=1000
        bonus = canvas.create_text(250, 100, text="+1000", font=("Helvetica", 15, "bold"), fill="green")
        canvas.after(1000, lambda: canvas.delete(bonus))
       
       
       
#Max     
def game_over_text_func():
    canvas.itemconfig(game_over_text, state="normal")
    canvas.itemconfig(retry_button_window, state="normal")
    canvas.itemconfig(quit_button_window, state="normal")
   
   
   
 #Max  
def reset_game():
    global game_over, skier_id, skier1
    game_over = False
    canvas.itemconfig(game_over_text, state="hidden")
    canvas.itemconfig(retry_button_window, state="hidden")
    canvas.itemconfig(quit_button_window, state="hidden")

    canvas.delete(skier_id)
    skier_id = canvas.create_image(237.5, 0, anchor=NW, image=skier_image)
    canvas.move(skier_id, 0, 0)

    canvas.delete(skier1)
    skier1 = canvas.create_rectangle(0, 0, 35, 58)
    canvas.move(skier1, 237.5, 0)
    canvas.itemconfig(skier1, state="hidden")  

    global dy
    dy = 5
    x0, y0, x1, y1 = canvas.coords(skier1)
    canvas.move(skier_id, 0, dy)

    after_id = root.after(25, skier_move)

    root.after_cancel(after_id)
    if y0 >= 700:
        canvas.move(skier_id, 0, -700)
#Max
game_over_text = canvas.create_text(
    250, 400, text="Game Over!", font=("Helvetica", 24, "bold"), state="hidden"
)
retry_button = Button(canvas, text="2 more skip the last", command=reset_game)
quit_button = Button(canvas, text="Time for a beer", command=root.destroy)

retry_button_window = canvas.create_window(150, 450, anchor=NW, window=retry_button, state="hidden")
quit_button_window = canvas.create_window(300, 450, anchor=NW, window=quit_button, state="hidden")
#Dano
skier_move()
canvas.bind("<KeyPress-Down>", sD)
canvas.bind("<KeyPress-Left>", sL)
canvas.bind("<KeyPress-Right>", sR)

canvas.pack()
canvas.focus_set()

root.mainloop()