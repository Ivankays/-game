import tkinter as tk

def del_esc(event):
    root.destroy()

root = tk.Tk()
root.title('Hexxagon')
root.iconphoto(True,  tk.PhotoImage(file='picture/Group 6.png'))
root.geometry("950x700+150+60")
root.resizable(False, False)
root.wm_attributes("-topmost", 1)
root.bind("<Escape>", del_esc)

canvas = tk.Canvas(root, width=950, height=700)
canvas.pack()


photo_list = [
    tk.PhotoImage(file="picture/place.png"), # обычная клетка
    tk.PhotoImage(file="picture/not_place.png"),
    tk.PhotoImage(file="picture/red1.png"),
    tk.PhotoImage(file="picture/blue1.png"),
    tk.PhotoImage(file="picture/red2.png"),
    tk.PhotoImage(file="picture/blue2.png"),
    tk.PhotoImage(file="picture/red3.png"),
    tk.PhotoImage(file="picture/blue3.png"),
    tk.PhotoImage(file="picture/Group 1 (1).png"),
]

with open('lvl2.txt', 'r') as file:
    sizeg = int(file.readline())
    sizev = int(file.readline())
    poz =  [int(x) for x in file.readline().split()]
    poz1 = [int(x) for x in file.readline().split()]
    poz2 = [int(x) for x in file.readline().split()]
    poz3 = [int(x) for x in file.readline().split()]

coordinates = []
place_kol=0
step=1
c=0

def victory():
    gg = canvas.find_withtag('chip')
    canvas.delete('store')
    vr = canvas.find_withtag('red')
    vb = canvas.find_withtag('blue')
    canvas.create_text(830, 50, text=f"Игрок 1: {len(vr)}", font=("Helvetica", 24), fill="red",  tag = 'store')
    canvas.create_text(830, 90, text=f"Игрок 2: {len(vb)}", font=("Helvetica", 24), fill="blue", tag = 'store')
    if len(vb)==0:
        canvas.delete('all')
        button.destroy()  
        canvas.create_text(430, 270, text="Победа красных", font=("Helvetica", 24), fill="red")
    elif len(vr)==0:
        canvas.delete('all')
        button.destroy()  
        canvas.create_text(430, 270, text="Победа синих", font=("Helvetica", 24), fill="blue")
    if len(gg) == 110-1:
        canvas.delete('all')
        button.destroy()  
        if (len(vr) > len(vb)) or vb==0:
            canvas.create_text(950/2, 700/2, text="Победа красных", font=("Helvetica", 24), fill="red")
        elif len(vr) < len(vb) or vr==0:
            canvas.create_text(950/2, 700/2, text="Победа синих", font=("Helvetica", 24), fill="blue")
        else:
            canvas.create_text(950/2, 700/2, text="Ничья", font=("Helvetica", 24), fill="black")
     
def сreat_coord():
    for j in range(sizev):
        for i in range(sizeg):
            coordinates.append([24 + (i * 42), 27 + (j * 74)])
        for i in range(sizeg):
            coordinates.append([45 + (i * 42), 64 + (j * 74)])
сreat_coord()

def сreat_place(): 
    global place_kol
    for i in range(sizeg*sizev*2): 
        if i not in poz:
            canvas.create_image(coordinates[i][0], coordinates[i][1], image=photo_list[0], tag = 'place')
            place_kol+= 1
        else:
            canvas.create_image(coordinates[i][0], coordinates[i][1], image=photo_list[1], tag = 'not_place')
            coordinates[i][0], coordinates[i][1] = -1000,-1000
    
    for i in range(sizeg*sizev*2): 
        if i in poz1:
            canvas.create_image(coordinates[i][0], coordinates[i][1], image=photo_list[2], tag = ('red','chip'))
        if i in poz2:
            canvas.create_image(coordinates[i][0], coordinates[i][1], image=photo_list[3], tag = ('blue','chip'))
        if i in poz3:
            canvas.create_image(coordinates[i][0], coordinates[i][1], image=photo_list[8], tag = ('chip'))
сreat_place()
print(coordinates)

def click_handler(event):
    global for_dell, step
    item=0
    x, y = event.x, event.y
    item = canvas.find_closest(x, y)[0]
    coor = canvas.coords(item)
    for i in range(sizeg*sizev*2):
        if coordinates[i][0]==coor[0] and coordinates[i][1]==coor[1]:
            coor = i
            break

    if step==1 or step==2:
        c=0
        for_not=canvas.gettags(canvas.find_closest(x, y)[0])

        if step==1 and 'red' in for_not:
            for_dell=coor
            click(coor,c)
            step+=1
            
        elif step==2  and 'hod2' in for_not:
            move1(coor,step)
            attack(coor,step)
            step+=1

        elif step==2  and 'hod3' in for_not:
            move2(coor,for_dell,step)
            attack(coor,step)
            step+=1
    
    if step==3 or step==4:
        c=1
        for_not=canvas.gettags(canvas.find_closest(x, y)[0])
        if step==3 and 'blue' in for_not:
            for_dell=coor
            click(coor,c)
            step+=1

        elif step==4 and 'hod2' in for_not:
            move1(coor,step)
            attack(coor,step)
            step+=1

        elif step==4 and 'hod3' in for_not:
            move2(coor,for_dell,step)
            attack(coor,step)
            step+=1
    
    if step==5:
        step=1


def click(coor,c):
    if coor%(sizeg*2)<sizeg:
        k1=-1
        k2=-2
        canvas.create_image(coordinates[coor-k2][0], coordinates[coor-k2][1], image=photo_list[6+c], tag = 'hod3') #центр
        canvas.create_image(coordinates[coor+k2][0], coordinates[coor+k2][1], image=photo_list[6+c], tag = 'hod3')
        canvas.create_image(coordinates[coor+k2+sizeg+sizeg+1][0], coordinates[coor+k2+sizeg+sizeg+1][1], image=photo_list[6+c], tag = 'hod3') #низ
        canvas.create_image(coordinates[coor+k2+sizeg+sizeg+2][0], coordinates[coor+k2+sizeg+sizeg+2][1], image=photo_list[6+c], tag = 'hod3')
        canvas.create_image(coordinates[coor+k2+sizeg+sizeg+3][0], coordinates[coor+k2+sizeg+sizeg+3][1], image=photo_list[6+c], tag = 'hod3')
        canvas.create_image(coordinates[coor+k2-sizeg-sizeg+1][0], coordinates[coor+k2-sizeg-sizeg+1][1], image=photo_list[6+c], tag = 'hod3') #верх
        canvas.create_image(coordinates[coor+k2-sizeg-sizeg+2][0], coordinates[coor+k2-sizeg-sizeg+2][1], image=photo_list[6+c], tag = 'hod3')
        canvas.create_image(coordinates[coor+k2-sizeg-sizeg+3][0], coordinates[coor+k2-sizeg-sizeg+3][1], image=photo_list[6+c], tag = 'hod3')
        canvas.create_image(coordinates[coor+k2+sizeg][0], coordinates[coor+k2+sizeg][1], image=photo_list[6+c], tag = 'hod3') #лево
        canvas.create_image(coordinates[coor+k2-sizeg][0], coordinates[coor+k2-sizeg][1], image=photo_list[6+c], tag = 'hod3')
        canvas.create_image(coordinates[coor-k2+sizeg-1][0], coordinates[coor-k2+sizeg-1][1], image=photo_list[6+c], tag = 'hod3') #право
        canvas.create_image(coordinates[coor-k2-sizeg-1][0], coordinates[coor-k2-sizeg-1][1], image=photo_list[6+c], tag = 'hod3')
        
    else:
        k1=1
        k2=2
        canvas.create_image(coordinates[coor-k2][0], coordinates[coor-k2][1], image=photo_list[6+c], tag = 'hod3')
        canvas.create_image(coordinates[coor+k2][0], coordinates[coor+k2][1], image=photo_list[6+c], tag = 'hod3')
        canvas.create_image(coordinates[coor+k2+sizeg+sizeg-1][0], coordinates[coor+k2+sizeg+sizeg-1][1], image=photo_list[6+c], tag = 'hod3')
        canvas.create_image(coordinates[coor+k2+sizeg+sizeg-2][0], coordinates[coor+k2+sizeg+sizeg-2][1], image=photo_list[6+c], tag = 'hod3')
        canvas.create_image(coordinates[coor+k2+sizeg+sizeg-3][0], coordinates[coor+k2+sizeg+sizeg-3][1], image=photo_list[6+c], tag = 'hod3')
        canvas.create_image(coordinates[coor+k2-sizeg-sizeg-1][0], coordinates[coor+k2-sizeg-sizeg-1][1], image=photo_list[6+c], tag = 'hod3')
        canvas.create_image(coordinates[coor+k2-sizeg-sizeg-2][0], coordinates[coor+k2-sizeg-sizeg-2][1], image=photo_list[6+c], tag = 'hod3')
        canvas.create_image(coordinates[coor+k2-sizeg-sizeg-3][0], coordinates[coor+k2-sizeg-sizeg-3][1], image=photo_list[6+c], tag = 'hod3')
        canvas.create_image(coordinates[coor+k2+sizeg][0], coordinates[coor+k2+sizeg][1], image=photo_list[6+c], tag = 'hod3')
        canvas.create_image(coordinates[coor+k2-sizeg][0], coordinates[coor+k2-sizeg][1], image=photo_list[6+c], tag = 'hod3')
        canvas.create_image(coordinates[coor-k2+sizeg+1][0], coordinates[coor-k2+sizeg+1][1], image=photo_list[6+c], tag = 'hod3')
        canvas.create_image(coordinates[coor-k2-sizeg+1][0], coordinates[coor-k2-sizeg+1][1], image=photo_list[6+c], tag = 'hod3')
    
    canvas.create_image(coordinates[coor-k1][0], coordinates[coor-k1][1], image=photo_list[4+c], tag = 'hod2')
    canvas.create_image(coordinates[coor+k1][0], coordinates[coor+k1][1], image=photo_list[4+c], tag = 'hod2')
    canvas.create_image(coordinates[coor+sizeg][0], coordinates[coor+sizeg][1], image=photo_list[4+c], tag = 'hod2')
    canvas.create_image(coordinates[coor+sizeg+k1][0], coordinates[coor+sizeg+k1][1], image=photo_list[4+c], tag = 'hod2')
    canvas.create_image(coordinates[coor-sizeg][0], coordinates[coor-sizeg][1], image=photo_list[4+c], tag = 'hod2')
    canvas.create_image(coordinates[coor-sizeg+k1][0], coordinates[coor-sizeg+k1][1], image=photo_list[4+c], tag = 'hod2')
    canvas.tag_raise('chip')

def move1(coor,step):
    can = []
    for obj in canvas.find_all():
        obj_x, obj_y = canvas.coords(obj)
        if obj_x == coordinates[coor][0] and obj_y == coordinates[coor][1]:
                can.append(obj)

    if len(can)<=2:
        if step==1 or step==2:
            canvas.create_image(coordinates[coor][0], coordinates[coor][1], image=photo_list[2], tag = ('red','chip'))
        else:
            canvas.create_image(coordinates[coor][0], coordinates[coor][1], image=photo_list[3], tag = ('blue','chip'))
    canvas.delete('hod3','hod2')

def move2(coor,for_dell,step):
    found_objects = []
    for obj in canvas.find_all():
        obj_x, obj_y = canvas.coords(obj)
        if obj_x == coordinates[for_dell][0] and obj_y == coordinates[for_dell][1]:
            found_objects.append(obj)
               
    can = []
    for obj in canvas.find_all():
        obj_x, obj_y = canvas.coords(obj)
        if obj_x == coordinates[coor][0] and obj_y == coordinates[coor][1]:
                can.append(obj)


    if len(can)<=2 and found_objects:
        last_found_object = found_objects.pop()
        if step==1 or step==2:
            canvas.create_image(coordinates[coor][0], coordinates[coor][1], image=photo_list[2], tag = ('red','chip'))
        else:
            canvas.create_image(coordinates[coor][0], coordinates[coor][1], image=photo_list[3], tag = ('blue','chip'))
        canvas.delete(last_found_object) 
    canvas.delete('hod3','hod2')

def attack(coor,step):
    can = []
    for obj in canvas.find_all():
        obj_x, obj_y = canvas.coords(obj)
        if obj_x == coordinates[coor][0] and obj_y == coordinates[coor][1]:
                can.append(obj)

    x=can.pop(0)-1

    can = []
    if coor%(sizeg*2)<sizeg:
        k1=-1
    else:
        k1=1

    for obj in canvas.find_all():
        obj_x, obj_y = canvas.coords(obj)
        if obj_x == coordinates[x-k1][0] and obj_y == coordinates[x-k1][1]:
                can.append(obj)
        elif obj_x == coordinates[x+k1][0] and obj_y == coordinates[x+k1][1]:
                can.append(obj)
        elif obj_x == coordinates[x+sizeg][0] and obj_y == coordinates[x+sizeg][1]:
                can.append(obj)
        elif obj_x == coordinates[x+sizeg+k1][0] and obj_y == coordinates[x+sizeg+k1][1]:
                can.append(obj)
        elif obj_x == coordinates[x-sizeg][0] and obj_y == coordinates[x-sizeg][1]:
                can.append(obj)
        elif obj_x == coordinates[x-sizeg+k1][0] and obj_y == coordinates[x-sizeg+k1][1]:
                can.append(obj) 
    
    for i in can:
        if i > sizeg*sizev*2:
            obj_x, obj_y = map(int, canvas.coords(i))
            for j in coordinates:
                if obj_x==j[0] and obj_y==j[1]:
                    if step==1 or step==2:
                        canvas.create_image(coordinates[coordinates.index(j)][0], coordinates[coordinates.index(j)][1], image=photo_list[2], tag = ('red','chip'))
                    else:
                        canvas.create_image(coordinates[coordinates.index(j)][0], coordinates[coordinates.index(j)][1], image=photo_list[3], tag = ('blue','chip'))
                    canvas.delete(i)
def give_up():
    global step
    canvas.delete('all')
    button.destroy()   
    if step == 1 or step == 2:
        canvas.create_text(950/2, 700/2, text="Победа синих", font=("Helvetica", 24), fill="blue")
    elif step == 3 or step == 4:
        canvas.create_text(950/2, 700/2, text="Победа красных", font=("Helvetica", 24), fill="red")
   

button = tk.Button(root, text="сдаться", command=give_up, width=20, height=2)
button.place(relx=0.97, rely=0.93, anchor=tk.SE)
victory()
canvas.bind("<Button-1>", click_handler)  
root.mainloop()