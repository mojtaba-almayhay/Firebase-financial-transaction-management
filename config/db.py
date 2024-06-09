from tkinter import messagebox
import firebase_admin
from firebase_admin import credentials,db
import sys

cred = credentials.Certificate("config/data_service.json")
firebase_admin.initialize_app(cred,{"databaseURL":"YOUR_URL_FIREBASE"})#======
re = db.reference("/users")

def serch_user():
    try:
        da = re.get()
        info_user = []
        for use in da:
            info_user.append({
                "id":use,
                "name":da[use]['info']['name'],
                "phone":da[use]['info']['phone'],
                "sum":da[use]['info']['sum']
                })
        return info_user

    except Exception as e:
        if "HTTPSConnectionPool(host='oauth2.googleapis.com', port=443)" in str(e):
            if messagebox.askyesno('حدث خطأ', 'لا يوجد اتصال بالانترنيت يرجى اعادة لمحاولة') == True:
               serch_user()
            else:
               sys.exit(0)    
        else:
            if "'NoneType' object is not iterable" == str(e):
                pass
            else:
                messagebox.showerror('حدث خطأ',f'{e}')

def inset_user(NAMEE,PHONE):
    try:
        re.push({"info":{'name': NAMEE,'phone' : PHONE,"sum":0}})
    except Exception as e:
        if "HTTPSConnectionPool(host='oauth2.googleapis.com', port=443)" in str(e):
            if messagebox.askyesno('حدث خطأ', 'لا يوجد اتصال بالانترنيت يرجى اعادة لمحاولة') == True:
                inset_user(NAMEE,PHONE)
            else:
                sys.exit(0)    
        else:
            messagebox.showerror('حدث خطأ',f'{e}')

def updata_user_sum(id,sum):
    try:
        ad = re.get()[id]['data']
        da = re.get()[id]['info']
        re.update({id:{
            "info":{"name":da['name'],"phone":da["phone"],"sum":sum},
            "data":ad
            }})
    except Exception as e:
        if str(e) == "'data'":
            da = re.get()[id]['info']
            re.update({id:{"info":{"name":da['name'],"phone":da["phone"],"sum":sum}}})
        else:
            messagebox.showerror("حدث خطأ",f"{e}")

def updata_user(id,NAMEE,PHONE):
    try:
        ad = re.get()[id]['data']
        da = re.get()[id]['info']
        re.update({id:{
            "info":{"name":NAMEE,"phone":PHONE,"sum":da['sum']},
            "data":ad,
            }})
    except Exception as e:
        if str(e) == "'data'":
            da = re.get()[id]['info']
            re.update({id:{"info":{"name":NAMEE,"phone":PHONE,"sum":da['sum']}}})
        else:
            messagebox.showerror("حدث خطأ",f"{e}")

def delet_user(id_user):
    de = db.reference(f"/users/{id_user}")
    de.delete()

#============MAMLA============#
def inset_mamal(TYPE,MABLG,NOTE,DATA,ID_USER):
    pu = db.reference(f"/users/{ID_USER}/data")
    pu.push({"type":TYPE,"amount":MABLG,"not":NOTE,"time":DATA})

def serch_mamal(ID_USER):
    try:
        da = re.get()[ID_USER]["data"]
        info_user = []
        for use in da:
            info_user.append({"amount":da[use]['amount'],"not":da[use]['not'],"time":da[use]['time'],"type":da[use]['type']})
        
        return info_user
    except Exception as e:
        if "HTTPSConnectionPool(host='oauth2.googleapis.com', port=443)" in str(e):
            if messagebox.askyesno('حدث خطأ', 'لا يوجد اتصال بالانترنيت يرجى اعادة لمحاولة') == True:
                sys.exit(0)
            else:
                serch_mamal()
        elif str(e) == "'data'":
            return []
        else:
            messagebox.showerror("حدث خطأ",f"{e}")