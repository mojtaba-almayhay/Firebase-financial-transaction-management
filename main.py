from tkinter import CENTER,END,DISABLED,NORMAL
from tkinter import ttk,messagebox
import config.db as db
from datetime import datetime
from PIL import Image
import customtkinter
from os import path
import json
import sys
import re


#================THEME============#
with open("config/settings.json", "r") as settings_file:
    settings = json.load(settings_file)
customtkinter.set_appearance_mode(settings["theme"])
customtkinter.set_default_color_theme(settings["color_theme"])


#============HOME=====================#
app = customtkinter.CTk() 
app.title("مكتب معاملات مالية")
app.minsize(850,655)
app.geometry('850x650+360+110')
app.iconbitmap('config/images/ico_logo.ico')   

#=============Work====================#
heading_frame = customtkinter.CTkFrame(master=app,corner_radius=5)
heading_frame.pack(padx=0,pady=0, ipadx=0, ipady=0,fill="x",anchor="n")

def dev_serch():
    button_serch.configure(state=DISABLED) 
    label.pack_forget()
    button_serch.pack_forget()

    
    def def_button_serch_exit():
        button_serch.configure(state=NORMAL)
        button_serch_exit.pack_forget()
        entry_scherch_new.pack_forget()
        button_serch.pack(padx=20,expand=True,side="left")
        label.pack(padx=20,side='left')
        displayAllsu_customers()
        
        
    button_serch_exit = customtkinter.CTkButton(master=heading_frame,text="الغاء",width=120,corner_radius=7,fg_color='#cc0a0a',font=customtkinter.CTkFont(family="Robot", size=15, weight="bold"),command=def_button_serch_exit)
    button_serch_exit.pack(padx=20,expand=True,side="left")
    
    
    
    var_scherch_new = customtkinter.StringVar()
    entry_scherch_new = customtkinter.CTkEntry(master=heading_frame,width=500, textvariable=var_scherch_new,justify="center")
    entry_scherch_new.pack(padx=20,expand=True,side="left")
    
    
    def get_data(*args):
        serarch_str = var_scherch_new.get()
        tre.delete(*tre.get_children())        
        ii = 1
        for element in db.serch_user():
            if (re.match(serarch_str,element["name"],re.IGNORECASE)) : 
                tre.insert("",END,values=(element["sum"],element["phone"],element["name"],ii,element["id"]))
                ii = ii+1
    def my_upd(my_widget):
        my_w = my_widget.widget
        try:
            index = int(my_w.curselection()[0])
            value = my_w.get(index)
            var_scherch_new.set(value)
            tre.delete(*tre.get_children())
        except Exception as e:
            if str(e) == "tuple index out of range":
                pass
            elif str(e) == "'Treeview' object has no attribute 'curselection'":
                pass
            else:
                messagebox.showerror("حدث خطا",f"The5555 {e}")
    tre.bind("<<TreeviewSelect>>",my_upd)
    var_scherch_new.trace('w',get_data)

    tre.bind('<<TreeviewSelect>>',Get_Data_customers)
    
button_serch = customtkinter.CTkButton(master=heading_frame,text="بحث",width=120,corner_radius=7,font=customtkinter.CTkFont(family="Robot", size=15, weight="bold"),command=dev_serch)
button_serch.pack(padx=20,expand=True,side="left")

label = customtkinter.CTkLabel(master=heading_frame, text="المهندس مجتبى المياحي",font=customtkinter.CTkFont(family="Robot", size=25, weight="bold"))
label.pack(padx=20,side='left')

image_logo = customtkinter.CTkImage(light_image=Image.open(path.join("config/images/logo.png")), size=(150 ,100))
label_image_logo = customtkinter.CTkLabel(master=heading_frame, image=image_logo, text='')
label_image_logo.pack(padx=20,expand=True,side="right")

main_frame = customtkinter.CTkFrame(master=app,corner_radius=10,fg_color='transparent')
main_frame.pack(padx=0,pady=0, ipadx=5, ipady=5,fill="both",expand=True)

left_frame = customtkinter.CTkFrame(master=main_frame,corner_radius=5)
left_frame.pack_forget()

right_frame = customtkinter.CTkFrame(master=main_frame,corner_radius=5)
right_frame.pack(padx=15,pady=14, ipadx=2, ipady=2,fill="both",side="right")

top_frame = customtkinter.CTkFrame(master=left_frame,corner_radius=5)
top_frame.pack(padx=0,pady=0, ipadx=5, ipady=5,fill="both",side="top",expand=True)

tre = ttk.Treeview(top_frame, columns=(1,2,3,4), show='headings')
tre.heading(1, text='المجموع',anchor=CENTER)
tre.column('1',anchor=CENTER)
tre.heading(2, text='رقم الهاتف',anchor=CENTER)
tre.column('2',anchor=CENTER)
tre.heading(3, text='الاسم',anchor=CENTER)
tre.column('3',anchor=CENTER)
tre.heading(4, text='ت',anchor=CENTER)
tre.column('4',anchor=CENTER)

style = ttk.Style()
style.theme_use("clam")

tre.pack(padx=0,pady=0, ipadx=0, ipady=0,fill="both",expand=True)#
left_frame.pack(padx=15,pady=15, ipadx=0, ipady=0,fill="both",expand=True,side="left")

def Get_Data_customers(event):
    selected_rowcu = tre.focus()
    item = tre.item(selected_rowcu)
    if item['values']  == "":
        pass
    else :
        global data
        data = item['values']

def displayAllsu_customers():
    tre.delete(*tre.get_children())
    try:
        ii = 1
        for row in db.serch_user():
            tre.insert("",END,values=(row["sum"],row["phone"],row["name"],ii,row["id"]))
            ii = ii+1
    except Exception as e:
        if "'NoneType' object is not iterable" == str(e):
            pass
        else:
            messagebox.showwarning('حدث خطأ',f'{e}') 

displayAllsu_customers()
tre.bind('<<TreeviewSelect>>',Get_Data_customers)

def dev_button1():
    Gone_home_right()
    
    lable_names_new = customtkinter.CTkLabel(master=right_frame, text="الاسم",font=customtkinter.CTkFont(family="Robot", size=18, weight="bold"))
    lable_names_new.pack(padx=0, pady=0,expand=True)
    
    var_names_new = customtkinter.StringVar()
    entry_name_new = customtkinter.CTkEntry(master=right_frame,width=180, textvariable=var_names_new,justify="center")
    entry_name_new.pack(padx=0, pady=0,expand=True)
    
    lable_phone_new = customtkinter.CTkLabel(master=right_frame, text="رقم الهاتف",font=customtkinter.CTkFont(family="Robot", size=18, weight="bold"))
    lable_phone_new.pack(padx=0, pady=0,expand=True)
    
    var_phone_new = customtkinter.StringVar()
    entry_phone_new = customtkinter.CTkEntry(master=right_frame,width=180, textvariable=var_phone_new,justify="center")
    entry_phone_new.pack(padx=0, pady=0,expand=True)
    
    def dev_sava_add():
        name  = var_names_new.get()
        try:
            int(var_phone_new.get())
            phone = var_phone_new.get()
            if name == "":
                messagebox.showerror("حدث خطا","حقل الاسم فارغ")
            elif phone == "":
                messagebox.showerror("حدث خطا","حقل رقم الهاتف فارغ")
            elif len(phone) != 11:
                messagebox.showerror("حدث خطا","رقم الهاتف خطا ")
            else:
                db.inset_user(name,str(phone))
                displayAllsu_customers()
                dev_cance_add()
        except Exception as e:
            if "invalid literal for int()" in str(e):
                messagebox.showerror("حدث خطا","رقم الهاتف غير صحيح")
    button_sava = customtkinter.CTkButton(master=right_frame,text="حفظ",width=180,corner_radius=7,font=customtkinter.CTkFont(family="Robot", size=15, weight="bold"),command=dev_sava_add)
    button_sava.pack(padx=20, pady=5,expand=True)
    
    def dev_cance_add():
        lable_names_new.pack_forget()
        entry_name_new.pack_forget()
        lable_phone_new.pack_forget()
        entry_phone_new.pack_forget()
        button_sava.pack_forget()
        button_cance_add.pack_forget()
        Show_home_right()


    button_cance_add = customtkinter.CTkButton(master=right_frame,text="الغاء",width=180,fg_color='#cc0a0a',corner_radius=7,font=customtkinter.CTkFont(family="Robot", size=15, weight="bold"),command=dev_cance_add)
    button_cance_add.pack(padx=20, pady=5,expand=True)
button1 = customtkinter.CTkButton(master=right_frame,text="اضافة",corner_radius=7,font=customtkinter.CTkFont(family="Robot", size=15, weight="bold"),command=dev_button1)
button1.pack(padx=20, pady=25,expand=True)

def dev_buttondele():
    try:
        data
        if messagebox.askyesno("رسالة تاكيد", f"هل انت مأكد من حذف {data[2]} ؟") == True:
            db.delet_user(data[4])
            displayAllsu_customers()
        else:
            pass
    except Exception as e:
        if str(e) == "name 'data' is not defined":
            messagebox.showerror("حدث خطا","يرجى تحديد احد المستخدمين")
buttondele = customtkinter.CTkButton(master=right_frame,text="حذف",fg_color='#cc0a0a',corner_radius=7,font=customtkinter.CTkFont(family="Robot", size=15, weight="bold"),command=dev_buttondele)
buttondele.pack(padx=20, pady=25,expand=True)

def dev_button2():
    try:
        data
        Gone_home_right()
        
        lable_names_new = customtkinter.CTkLabel(master=right_frame, text="الاسم",font=customtkinter.CTkFont(family="Robot", size=18, weight="bold"))
        lable_names_new.pack(padx=0, pady=0,expand=True)
        
        var_names_new = customtkinter.StringVar()
        var_names_new.set(data[2])
        entry_name_new = customtkinter.CTkEntry(master=right_frame,width=180, textvariable=var_names_new,justify="center")
        entry_name_new.pack(padx=0, pady=0,expand=True)
        
        lable_phone_new = customtkinter.CTkLabel(master=right_frame, text="رقم الهاتف",font=customtkinter.CTkFont(family="Robot", size=18, weight="bold"))
        lable_phone_new.pack(padx=0, pady=0,expand=True)
        
        var_phone_new = customtkinter.StringVar()
        var_phone_new.set(data[1])
        entry_phone_new = customtkinter.CTkEntry(master=right_frame,width=180, textvariable=var_phone_new,justify="center")
        entry_phone_new.pack(padx=0, pady=0,expand=True)
        
        def dev_sava_add():
            name  = var_names_new.get()
            try:
                int(var_phone_new.get())
                phone = var_phone_new.get()
                if name == "":
                    messagebox.showerror("حدث خطا","حقل الاسم فارغ")
                elif phone == "":
                    messagebox.showerror("حدث خطا","حقل رقم الهاتف فارغ")
                elif len(phone) != 11:
                    messagebox.showerror("حدث خطا","رقم الهاتف خطا ")
                else:
                    db.updata_user(data[4],name,phone)
                    displayAllsu_customers()
                    dev_cance_add()
                    
            except Exception as e:
                if "invalid literal for int()" in str(e):
                    messagebox.showerror("حدث خطا","رقم الهاتف غير صحيح")
                else:
                    messagebox.showerror("حدث خطا",f"{e}")
        button_sava = customtkinter.CTkButton(master=right_frame,text="حفظ التغيرات",width=180,corner_radius=7,font=customtkinter.CTkFont(family="Robot", size=15, weight="bold"),command=dev_sava_add)
        button_sava.pack(padx=20, pady=5,expand=True)
        
        def dev_cance_add():
            lable_names_new.pack_forget()
            entry_name_new.pack_forget()
            lable_phone_new.pack_forget()
            entry_phone_new.pack_forget()
            button_sava.pack_forget()
            button_cance_add.pack_forget()
            Show_home_right()
            buttondele.pack(padx=20, pady=30,expand=True)
        button_cance_add = customtkinter.CTkButton(master=right_frame,text="الغاء",width=180,fg_color='#cc0a0a',corner_radius=7,font=customtkinter.CTkFont(family="Robot", size=15, weight="bold"),command=dev_cance_add)
        button_cance_add.pack(padx=20, pady=5,expand=True)
    except Exception as e:
        if str(e) == "name 'data' is not defined":
            messagebox.showerror("حدث خطا","يرجى تحديد احد المستخدمين")
            
button2 = customtkinter.CTkButton(master=right_frame,text="تعديل",corner_radius=7,font=customtkinter.CTkFont(family="Robot", size=15, weight="bold"),command=dev_button2)
button2.pack(padx=20, pady=25,expand=True)

def dev_button3():
    try:
        data
        tre.pack_forget()
        tre_mala = ttk.Treeview(top_frame, columns=(1,2,3,4,5), show='headings')
        tre_mala.heading(1, text='النوع',anchor=CENTER)
        tre_mala.column('1',anchor=CENTER)
        tre_mala.heading(2, text='التاريخ',anchor=CENTER)
        tre_mala.column('2',anchor=CENTER)
        tre_mala.heading(3, text='التفاصيل',anchor=CENTER)
        tre_mala.column('3',anchor=CENTER)
        tre_mala.heading(4, text='المبلغ',anchor=CENTER)
        tre_mala.column('4',anchor=CENTER)
        
        tre_mala.heading(5, text='ت',anchor=CENTER)
        tre_mala.column('5',anchor=CENTER)
        
        tre_mala.pack(padx=0,pady=0, ipadx=0, ipady=0,fill="both",expand=True)
        
        def displayAllsu_mala():
            tre_mala.delete(*tre_mala.get_children())
            try:
                ii = 1
                for row in db.serch_mamal(data[4]):
                    tre_mala.insert("",END,values=(row["type"],row["time"],row["not"],row["amount"],ii))
                    ii = ii+1
            except Exception as e:
                    messagebox.showwarning('حدث خطأ',f'{e}') 
        displayAllsu_mala()
        
        try:
            Gone_home_heading()
        except Exception as e :
            if "list.remove(x): x not in list" == str(e):
                pass

            
        Sum_label = customtkinter.CTkLabel(master=heading_frame, text=data[0],font=customtkinter.CTkFont(family="Robot", size=25, weight="bold"))
        Sum_label.pack(pady=5,expand=True,side="left",ipady=10)
        
        name_label = customtkinter.CTkLabel(master=heading_frame, text=data[2],font=customtkinter.CTkFont(family="Robot", size=25, weight="bold"))
        name_label.pack(pady=5,expand=True,side="left",ipady=10)
        
        Gone_home_right()
        

        from PIL import Image
        your_image = customtkinter.CTkImage(light_image=Image.open(path.join("config/images/logo.png")), size=(150 ,150))
        label_image = customtkinter.CTkLabel(master=right_frame, image=your_image, text='')
        label_image.pack(padx=1, pady=20,expand=True)
        
        def def_button_1():
            label_image.pack_forget()
            button_1.pack_forget()
            button_2.pack_forget()

            list_data =  {'text':"اعطيت","sum":data[0]}
            def def_option_menu(text:str):
                list_data['text'] = text
            option_menu = customtkinter.CTkOptionMenu(right_frame, values=["اعطيت", "اخذت"],width=180,command=def_option_menu,anchor=CENTER)
            option_menu.pack(padx=0, pady=0,expand=True)
            
            lable_mm_new = customtkinter.CTkLabel(master=right_frame, text="المبلغ",font=customtkinter.CTkFont(family="Robot", size=18, weight="bold"))
            lable_mm_new.pack(padx=0, pady=0,expand=True)
            var_mm_new = customtkinter.StringVar()
            entry_mm_new = customtkinter.CTkEntry(master=right_frame,width=180, textvariable=var_mm_new,justify="center")
            entry_mm_new.pack(padx=0, pady=0,expand=True)
            
            lable_tt_new = customtkinter.CTkLabel(master=right_frame, text="التفاصيل",font=customtkinter.CTkFont(family="Robot", size=18, weight="bold"))
            lable_tt_new.pack(padx=0, pady=0,expand=True)
            var_tt_new = customtkinter.StringVar()
            var_tt_new.set('لا يوجد')
            entry_tt_new = customtkinter.CTkEntry(master=right_frame,width=180, textvariable=var_tt_new,justify="center")
            entry_tt_new.pack(padx=0, pady=0,expand=True)
            
            lable_ta_new = customtkinter.CTkLabel(master=right_frame, text="التاريخ",font=customtkinter.CTkFont(family="Robot", size=18, weight="bold"))
            lable_ta_new.pack(padx=0, pady=0,expand=True)
            var_ta_new = customtkinter.StringVar()
            app_date = datetime.now()
            var_ta_new.set(app_date.strftime('%Y-%m-%d'))
            entry_ta_new = customtkinter.CTkEntry(master=right_frame,width=180, textvariable=var_ta_new,justify="center")
            entry_ta_new.pack(padx=0, pady=0,expand=True)
            
            def dev__add():
                try:
                    int(var_mm_new.get())
                    if var_mm_new.get() == "":
                        messagebox.showerror("حدث خطأ","لا يمكن ترك حقل المبلغ فارغا")
                    else:
                        db.inset_mamal(list_data['text'],var_mm_new.get(),var_tt_new.get(),var_ta_new.get(),data[4])
                        if list_data["text"] == "اعطيت":
                            suum = list_data["sum"] + int(var_mm_new.get())
                            db.updata_user_sum(data[4],suum)
                            Sum_label.configure(text=suum)
                        else:
                            suum = list_data["sum"] - int(var_mm_new.get())
                            db.updata_user_sum(data[4],suum)
                            Sum_label.configure(text=suum)
                        dev_can_add()
                        displayAllsu_customers()
                        displayAllsu_mala()
                        
                        
                        
                except Exception as e:
                    if str(e) == "invalid literal for int() with base 10: ''":
                        messagebox.showerror("حدث خطأ","لا يمكن ترك حقل المبلغ فارغ")
                        
                    elif str(e) == f"invalid literal for int() with base 10: '{var_mm_new.get()}'":
                        messagebox.showerror("حدث خطأ",f"لا يعتبر {var_mm_new.get()}  مبلغ رقمي")
                
            
            button_add = customtkinter.CTkButton(master=right_frame,text="اضافة",width=180,corner_radius=7,font=customtkinter.CTkFont(family="Robot", size=15, weight="bold"),command=dev__add)
            button_add.pack(padx=20, pady=5,expand=True)
            
            def dev_can_add():
                option_menu.destroy()
                lable_mm_new.destroy()
                entry_mm_new.destroy()
                lable_tt_new.destroy()
                entry_tt_new.destroy()
                lable_ta_new.destroy()
                entry_ta_new.destroy()
                button_add.destroy()
                button_can_add.destroy()
                label_image.pack(padx=20, pady=30,expand=True)
                button_1.pack(padx=20, pady=30,expand=True)
                button_2.pack(padx=20, pady=10,expand=True)
            button_can_add = customtkinter.CTkButton(master=right_frame,text="الغاء",width=180,fg_color='#cc0a0a',corner_radius=7,font=customtkinter.CTkFont(family="Robot", size=15, weight="bold"),command=dev_can_add)
            button_can_add.pack(padx=20, pady=5,expand=True)
        
        button_1 = customtkinter.CTkButton(master=right_frame,text="اضافة جديدة",corner_radius=7,font=customtkinter.CTkFont(family="Robot", size=15, weight="bold"),command=def_button_1)
        button_1.pack(padx=20, pady=30,expand=True)
        
        def def_button_2():
            button_1.pack_forget()
            button_2.pack_forget()
            label_image.pack_forget()
            Sum_label.pack_forget()
            name_label.pack_forget()
            tre_mala.pack_forget()
            Show_home_heading()
            Show_home_right()
            
            
            tre.pack(padx=0,pady=0, ipadx=0, ipady=0,fill="both",expand=True)
            left_frame.pack(padx=15,pady=15, ipadx=0, ipady=0,fill="both",expand=True,side="left")

        button_2 = customtkinter.CTkButton(master=right_frame,text="الغاء",corner_radius=7,fg_color='#cc0a0a',font=customtkinter.CTkFont(family="Robot", size=15, weight="bold"),command=def_button_2)
        button_2.pack(padx=20, pady=10,expand=True)
    except Exception as e:
        if str(e) == "name 'data' is not defined":
            messagebox.showerror("حدث خطا","يرجى تحديد احد المستخدمين")
button3 = customtkinter.CTkButton(master=right_frame,text="تقرير",corner_radius=7,font=customtkinter.CTkFont(family="Robot", size=15, weight="bold"),command=dev_button3)
button3.pack(padx=20, pady=25,expand=True)

deias_hom = customtkinter.CTkLabel(master=right_frame,text='')
deias_hom.pack(padx=20, pady=10,expand=True)#####

def Setting():
    app.title("Setting Opsion")
    app.iconbitmap('config/images/settings.ico')
    heading_frame.pack_forget()
    main_frame.pack_forget()
    
    app_setting = customtkinter.CTkFrame(master=app,fg_color='transparent')
    app_setting.pack(fill="both",expand=True)
    
    frame_top = customtkinter.CTkFrame(master=app_setting,fg_color='transparent')
    frame_top.pack(fill="both",expand=True,side="top")

    frame_left_top = customtkinter.CTkFrame(master=frame_top,fg_color='transparent')
    frame_left_top.pack(fill="both",expand=True,side="left")


    frame1_top =  customtkinter.CTkFrame(master=frame_left_top,fg_color='transparent')
    frame1_top.pack(fill="both",expand=True,side="top")
    theme_lbel = customtkinter.CTkLabel(master=frame1_top,text="Theme : ")
    theme_lbel.pack(fill="both",expand=True,side="left")
    def change_theme(new_theme_mode:str):
        settings["theme"] = new_theme_mode
        f = open("config/settings.json","w")
        json.dump(settings,f,indent=4)
        customtkinter.set_appearance_mode(new_theme_mode)
    theme_combo = customtkinter.CTkOptionMenu(frame1_top, values=["Light", "Dark", "System"],command=change_theme,anchor=CENTER)
    theme_combo.pack(expand=True,side="right")
    
    frame1_bom =  customtkinter.CTkFrame(master=frame_left_top,fg_color='transparent')
    frame1_bom.pack(fill="both",expand=True,side="bottom")
    color_theme_lbel = customtkinter.CTkLabel(master=frame1_bom,text="Color Theme : ")
    color_theme_lbel.pack(expand=True,side="left")
        

    def change_theme_color(new_theme_color:str):
        settings["color_theme"] = new_theme_color
        f = open("config/settings.json","w")
        json.dump(settings,f,indent=4)
        customtkinter.set_default_color_theme(new_theme_color)
    color_theme_combo = customtkinter.CTkOptionMenu(frame1_bom, values=["blue", "dark-blue", "green"],command=change_theme_color,anchor=CENTER)
    color_theme_combo.pack(expand=True,side="right")
    color_theme_combo.set(settings["color_theme"])
    
    
    frame_right_top = customtkinter.CTkFrame(master=frame_top,fg_color='transparent')
    frame_right_top.pack(fill="both",expand=True,side="right")
    setting_image = customtkinter.CTkImage(light_image=Image.open(path.join("config/images/settings.ico")), size=(250 ,250))
    label_setting = customtkinter.CTkLabel(master=frame_right_top, image=setting_image, text='')
    label_setting.pack(expand=True)
    
    
    #===========================================
    frame_bo = customtkinter.CTkFrame(master=app_setting,fg_color='transparent')
    frame_bo.pack(fill="both",expand=True,side="bottom")

    frame_left_bo = customtkinter.CTkFrame(master=frame_bo,fg_color='transparent')
    frame_left_bo.pack(fill="both",expand=True,side="left")
    setting2_image = customtkinter.CTkImage(light_image=Image.open(path.join("config/images/logo.png")), size=(350 , 350))
    label_setting2 = customtkinter.CTkLabel(master=frame_left_bo, image=setting2_image, text='')
    label_setting2.pack(expand=True)
    
    
    
    frame_right_bo = customtkinter.CTkFrame(master=frame_bo,fg_color='transparent')
    frame_right_bo.pack(fill="both",expand=True,side="right")
    
    
    def def_button_save():
        pass
    button_save = customtkinter.CTkButton(master=frame_right_bo,text="حفظ التغيرات",corner_radius=7,font=customtkinter.CTkFont(family="Robot", size=15, weight="bold"),command=def_button_save)
    button_save.pack(expand=True)

    def def_button_exit():
        app_setting.pack_forget()
        heading_frame.pack(padx=0,pady=0, ipadx=0, ipady=0,fill="x",anchor="n")
        main_frame.pack(padx=0,pady=0, ipadx=5, ipady=5,fill="both",expand=True)
    button_exit = customtkinter.CTkButton(master=frame_right_bo,text="الغاء",corner_radius=7,fg_color='#cc0a0a',font=customtkinter.CTkFont(family="Robot", size=15, weight="bold"),command=def_button_exit)
    
    
    
    
    
    button_exit.pack(expand=True)

button4 = customtkinter.CTkButton(master=right_frame,text="الاعدادات",corner_radius=7,fg_color='#cc0a0a',font=customtkinter.CTkFont(family="Robot", size=15, weight="bold"),command=Setting)
button4.pack(padx=20, pady=25,expand=True)

def Main_del():
    if messagebox.askyesno("رسالة تاكيد", "هل انت مأكد من خروج التطبيق ؟") == True:
        app.destroy()
        sys.exit(0)
    else:
        pass
app.protocol('WM_DELETE_WINDOW', Main_del)
button5 = customtkinter.CTkButton(master=right_frame,text="الخروج",corner_radius=7,fg_color='#cc0a0a',font=customtkinter.CTkFont(family="Robot", size=15, weight="bold"),command=Main_del)
button5.pack(padx=20, pady=25,expand=True)

#===================DEF Show or Gone================#
def Gone_home_right():
    buttondele.pack_forget()
    button1.pack_forget()
    button2.pack_forget()
    button3.pack_forget()
    button4.pack_forget()
    button5.pack_forget()
    deias_hom.pack_forget()
    
def Show_home_right():
    button1.pack(padx=20, pady=25,expand=True)
    buttondele.pack(padx=20, pady=25,expand=True)
    button2.pack(padx=20, pady=25,expand=True)
    button3.pack(padx=20, pady=25,expand=True)
    deias_hom.pack(padx=20, pady=10,expand=True)
    button4.pack(padx=20, pady=25,expand=True)
    button5.pack(padx=20, pady=25,expand=True)

def Gone_home_heading():
    label.pack_forget()
    label_image_logo.pack_forget()
    button_serch.pack_forget()

def Show_home_heading():
    button_serch.pack(padx=20,expand=True,side="left")
    label.pack(padx=20,side='left')
    label_image_logo.pack(padx=20,expand=True,side="right")
    
app.mainloop()