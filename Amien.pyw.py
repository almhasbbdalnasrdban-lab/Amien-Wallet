import tkinter as tk
from tkinter import messagebox
import random
from datetime import datetime

real_transactions = []

# دالة لرسم القلب الذهبي البارز والقوي والمبتسم
def draw_bold_golden_heart(canvas, x=30, y=10):
    # إحداثيات قلب كبير وبارز جداً
    canvas.create_polygon(
        x+70, y+40,
        x+100, y+10,
        x+130, y+40,
        x+140, y+70,
        x+70, y+130,
        x+0,  y+70,
        x+10, y+40,
        x+40, y+10,
        fill="#FFD700", outline="#B8860B", width=4, smooth=True
    )
    # العين الأولى السعيدة
    canvas.create_arc(x+40, y+45, x+60, y+65, start=0, extent=180, style=tk.ARC, width=4, outline="#3B3226")
    # العين الثانية السعيدة
    canvas.create_arc(x+80, y+45, x+100, y+65, start=0, extent=180, style=tk.ARC, width=4, outline="#3B3226")
    # الفم المبتسم العريض
    canvas.create_arc(x+55, y+70, x+85, y+98, start=180, extent=180, fill="#8B0000", outline="#B8860B", width=3)
    # الخدود الوردية البارزة
    canvas.create_oval(x+30, y+62, x+45, y+77, fill="#FF69B4", outline="")
    canvas.create_oval(x+95, y+62, x+110, y+77, fill="#FF69B4", outline="")

# 1. نافذة تحويل الأموال
def open_transfer():
    w = tk.Toplevel()
    w.title("تحويل أموال")
    w.geometry("350x380")
    w.config(bg="#3B3226")
    tk.Label(w, text="تحويل أموال", font=("Arial", 16, "bold"), fg="#FFD700", bg="#3B3226").pack(pady=15)
    tk.Label(w, text="رقم المستلم:", font=("Arial", 11, "bold"), fg="white", bg="#3B3226").pack(anchor="e", padx=30)
    ep = tk.Entry(w, font=("Arial", 13), justify="right")
    ep.pack(pady=5, padx=30, fill="x")
    tk.Label(w, text="المبلغ (ر.ي):", font=("Arial", 11, "bold"), fg="white", bg="#3B3226").pack(anchor="e", padx=30, pady=(10, 0))
    ea = tk.Entry(w, font=("Arial", 13), justify="right")
    ea.pack(pady=5, padx=30, fill="x")
    
    def send():
        if ep.get()=="" or ea.get()=="":
            messagebox.showerror("خطأ", "أدخل البيانات كاملة")
        else:
            trans_no = random.randint(100000, 999999)
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M")
            real_transactions.append(f"[{current_time}] تحويل {ea.get()} ر.ي إلى {ep.get()} (رقم: {trans_no})")
            messagebox.showinfo("نجاح الحوالة", f"تم تحويل {ea.get()} ر.ي بنجاح إلى {ep.get()}\n\nرقم الحوالة: {trans_no}")
            w.destroy()
            
    tk.Button(w, text="تأكيد التحويل", font=("Arial", 12, "bold"), bg="#FFD700", fg="#3B3226", command=send).pack(pady=20, padx=30, fill="x")

# 2. نافذة تسديد الفواتير والاتصالات
def open_bills():
    w = tk.Toplevel()
    w.title("تسديد الفواتير والخدمات")
    w.geometry("350x400")
    w.config(bg="#3B3226")
    tk.Label(w, text="تسديد الفواتير والاتصالات", font=("Arial", 15, "bold"), fg="#FFD700", bg="#3B3226").pack(pady=15)
    tk.Label(w, text="اختر الخدمة:", font=("Arial", 11, "bold"), fg="white", bg="#3B3226").pack(anchor="e", padx=30)
    service_var = tk.StringVar(w)
    service_var.set("يمن موبايل")
    services = ["يمن موبايل", "سبأفون", "YOU / MTN", "كهرباء / ماء"]
    popupMenu = tk.OptionMenu(w, service_var, *services)
    popupMenu.config(font=("Arial", 11), bg="white", width=20)
    popupMenu.pack(pady=5, padx=30)
    
    tk.Label(w, text="رقم الاشتراك / الهاتف:", font=("Arial", 11, "bold"), fg="white", bg="#3B3226").pack(anchor="e", padx=30, pady=(10, 0))
    eb = tk.Entry(w, font=("Arial", 13), justify="right")
    eb.pack(pady=5, padx=30, fill="x")
    tk.Label(w, text="المبلغ (ر.ي):", font=("Arial", 11, "bold"), fg="white", bg="#3B3226").pack(anchor="e", padx=30, pady=(10, 0))
    eamt = tk.Entry(w, font=("Arial", 13), justify="right")
    eamt.pack(pady=5, padx=30, fill="x")
    
    def pay_bill():
        if eb.get()=="" or eamt.get()=="":
            messagebox.showerror("خطأ", "أدخل بيانات الفاتورة كاملة")
        else:
            bill_no = random.randint(1000000, 9999999)
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M")
            real_transactions.append(f"[{current_time}] سداد فاتورة {service_var.get()}: {eamt.get()} ر.ي (رقم: {bill_no})")
            messagebox.showinfo("نجاح التسديد", f"تم تسديد فاتورة ({service_var.get()}) بقيمة {eamt.get()} ر.ي بنجاح\n\nرقم عملية السداد: {bill_no}")
            w.destroy()
            
    tk.Button(w, text="دفع الفاتورة", font=("Arial", 12, "bold"), bg="#FFD700", fg="#3B3226", command=pay_bill).pack(pady=20, padx=30, fill="x")

# 3. نافذة خدمات المودم والبريد والهاتف الثابت
def open_landline_internet():
    w = tk.Toplevel()
    w.title("خدمات الهاتف الثابت والإنترنت")
    w.geometry("380x420")
    w.config(bg="#3B3226")
    tk.Label(w, text="سداد الهاتف الثابت والبريد والمودم", font=("Arial", 14, "bold"), fg="#FFD700", bg="#3B3226").pack(pady=15)
    tk.Label(w, text="اختر الخدمة:", font=("Arial", 11, "bold"), fg="white", bg="#3B3226").pack(anchor="e", padx=30)
    net_var = tk.StringVar(w)
    net_var.set("إنترنت ADSL (يمن نت)")
    net_services = ["إنترنت ADSL (يمن نت)", "الهاتف الثابت (منزلي)", "خدمات البريد وتوفير البريد"]
    net_menu = tk.OptionMenu(w, net_var, *net_services)
    net_menu.config(font=("Arial", 11), bg="white", width=22)
    net_menu.pack(pady=5, padx=30)
    
    tk.Label(w, text="رقم الحساب / الهاتف الثابت:", font=("Arial", 11, "bold"), fg="white", bg="#3B3226").pack(anchor="e", padx=30, pady=(10, 0))
    e_num = tk.Entry(w, font=("Arial", 13), justify="right")
    e_num.pack(pady=5, padx=30, fill="x")
    tk.Label(w, text="المبلغ (ر.ي):", font=("Arial", 11, "bold"), fg="white", bg="#3B3226").pack(anchor="e", padx=30, pady=(10, 0))
    e_amt = tk.Entry(w, font=("Arial", 13), justify="right")
    e_amt.pack(pady=5, padx=30, fill="x")
    
    def pay_net():
        if e_num.get()=="" or e_amt.get()=="":
            messagebox.showerror("خطأ", "الرجاء إدخال رقم الحساب والمبلغ كاملة")
        else:
            op_no = random.randint(200000, 999999)
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M")
            real_transactions.append(f"[{current_time}] سداد {net_var.get()}: {e_amt.get()} ر.ي (رقم: {op_no})")
            messagebox.showinfo("نجاح السداد", f"تم تسديد اشتراك ({net_var.get()}) رقم: {e_num.get()}\nالمبلغ: {e_amt.get()} ر.ي\n\nرقم العملية: {op_no}")
            w.destroy()
            
    tk.Button(w, text="تأكيد سداد الخدمة", font=("Arial", 12, "bold"), bg="#FFD700", fg="#3B3226", command=pay_net).pack(pady=20, padx=30, fill="x")

# 4. نافذة دفع المشتريات
def open_merchant_pay():
    w = tk.Toplevel()
    w.title("دفع المشتريات والرسوم للمنشآت")
    w.geometry("350x420")
    w.config(bg="#3B3226")
    tk.Label(w, text="دفع للمنشآت والتجار والجامعات", font=("Arial", 14, "bold"), fg="#FFD700", bg="#3B3226").pack(pady=15)
    tk.Label(w, text="رقم المنشأة (6 أرقام ويبدأ بـ 15):", font=("Arial", 11, "bold"), fg="white", bg="#3B3226").pack(anchor="e", padx=30)
    em = tk.Entry(w, font=("Arial", 13), justify="right")
    em.pack(pady=5, padx=30, fill="x")
    tk.Label(w, text="المبلغ (ر.ي):", font=("Arial", 11, "bold"), fg="white", bg="#3B3226").pack(anchor="e", padx=30, pady=(10, 0))
    emoney = tk.Entry(w, font=("Arial", 13), justify="right")
    emoney.pack(pady=5, padx=30, fill="x")
    
    def pay_merchant():
        entered_code = em.get().strip()
        if entered_code == "" or emoney.get() == "":
            messagebox.showerror("خطأ", "الرجاء إدخال رقم المنشأة والمبلغ كاملة")
        elif not entered_code.isdigit() or len(entered_code) != 6 or not entered_code.startswith("15"):
            messagebox.showerror("خطأ أمني", "رقم المنشأة غير صحيح!\nيجب أن يتكون رقم الاشتراك من 6 أرقام ويبدأ بالرمز (15).")
        else:
            pay_no = random.randint(500000, 999999)
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M")
            real_transactions.append(f"[{current_time}] دفع مشتريات منشأة {entered_code}: {emoney.get()} ر.ي")
            messagebox.showinfo("نجاح الدفع", f"تم دفع {emoney.get()} ر.ي بنجاح إلى المنشأة رقم: ({entered_code})\n\nرقم عملية الشراء: {pay_no}")
            w.destroy()
            
    tk.Button(w, text="تأكيد الدفع للمنشأة", font=("Arial", 12, "bold"), bg="#FFD700", fg="#3B3226", command=pay_merchant).pack(pady=20, padx=30, fill="x")

# 5. نافذة إيداع الرصيد
def open_deposit():
    w = tk.Toplevel()
    w.title("إيداع رصيد للمشتركين")
    w.geometry("380x480")
    w.config(bg="#3B3226")
    tk.Label(w, text="إيداع رصيد مشترك في الأمين", font=("Arial", 15, "bold"), fg="#FFD700", bg="#3B3226").pack(pady=15)
    tk.Label(w, text="رقم جوال المودِع (المشترك):", font=("Arial", 10, "bold"), fg="white", bg="#3B3226").pack(anchor="e", padx=30)
    e_depositor = tk.Entry(w, font=("Arial", 12), justify="right")
    e_depositor.pack(pady=3, padx=30, fill="x")
    tk.Label(w, text="رقم جوال المشترك (المستفيد):", font=("Arial", 10, "bold"), fg="white", bg="#3B3226").pack(anchor="e", padx=30, pady=(8, 0))
    e_beneficiary = tk.Entry(w, font=("Arial", 12), justify="right")
    e_beneficiary.pack(pady=3, padx=30, fill="x")
    tk.Label(w, text="المبلغ المراد إيداعه (ر.ي):", font=("Arial", 10, "bold"), fg="white", bg="#3B3226").pack(anchor="e", padx=30, pady=(8, 0))
    edep = tk.Entry(w, font=("Arial", 12), justify="right")
    edep.pack(pady=3, padx=30, fill="x")
    
    def confirm_deposit():
        dep_phone = e_depositor.get().strip()
        ben_phone = e_beneficiary.get().strip()
        amount = edep.get().strip()
        
        if dep_phone == "" or ben_phone == "" or amount == "":
            messagebox.showerror("خطأ", "يرجى تعبئة جميع الحقول المطلوبة")
        elif len(dep_phone) < 9 or len(ben_phone) < 9:
            messagebox.showerror("خطأ في البيانات", "يرجى كتابة أرقام جوال صحيحة ومكتملة")
        else:
            dep_no = random.randint(1000000, 9999999)
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M")
            real_transactions.append(f"[{current_time}] إيداع مبلغ {amount} ر.ي للمشترك {ben_phone} (رقم: {dep_no})")
            msg = (f"تمت عملية الإيداع بنجاح! 📥\n\n"
                   f"• المودِع: {dep_phone}\n"
                   f"• حساب المشترك (المستفيد): {ben_phone}\n"
                   f"• المبلغ المودع: {amount} ر.ي\n"
                   f"• رقم عملية الإيداع: {dep_no}\n\n"
                   f"تم إرسال إشعار بالمخرجات إلى رقم المشترك ({ben_phone}).")
            messagebox.showinfo("نجاح الإيداع", msg)
            w.destroy()
            
    tk.Button(w, text="تأكيد الإيداع وإرسال الإشعار", font=("Arial", 11, "bold"), bg="#FFD700", fg="#3B3226", command=confirm_deposit).pack(pady=20, padx=30, fill="x")

# 6. نافذة كشف الحساب
def open_statement():
    w = tk.Toplevel()
    w.title("كشف الحساب والعمليات")
    w.geometry("420x460")
    w.config(bg="#3B3226")
    tk.Label(w, text="سجل العمليات الحقيقية وكشف الحساب", font=("Arial", 15, "bold"), fg="#FFD700", bg="#3B3226").pack(pady=15)
    
    frame_list = tk.Frame(w, bg="white")
    frame_list.pack(pady=5, padx=25, fill="both", expand=True)
    
    scrollbar = tk.Scrollbar(frame_list)
    scrollbar.pack(side=tk.LEFT, fill=tk.Y)
    
    statement_box = tk.Listbox(frame_list, font=("Arial", 10), yscrollcommand=scrollbar.set, justify="right")
    statement_box.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
    scrollbar.config(command=statement_box.yview)
    
    if len(real_transactions) == 0:
        statement_box.insert(tk.END, "لا توجد أي عمليات منفذة حتى الآن.")
    else:
        for op in real_transactions:
            statement_box.insert(tk.END, " • " + op)
        
    tk.Button(w, text="إغلاق", font=("Arial", 11, "bold"), bg="#8B0000", fg="white", command=w.destroy).pack(pady=15, padx=30, fill="x")

# الشاشة الرئيسية للمحفظة
def go_main():
    if pe.get()=="" or pi.get()=="":
        messagebox.showerror("خطأ", "أدخل رقم الجوال ورمز الحماية")
        return
    rt.destroy()
    m = tk.Tk()
    m.title("محفظة الأمين - الرئيسية")
    m.geometry("400x680")
    m.config(bg="white")
    
    # رسم القلب الذهبي البارز والقوي في الرئيسية
    canvas_main = tk.Canvas(m, width=200, height=130, bg="white", highlightthickness=0)
    canvas_main.pack(pady=(10, 0))
    draw_bold_golden_heart(canvas_main, x=25, y=5)
    
    tk.Label(m, text="محفظة الأمين", font=("Arial", 16, "bold"), fg="#B8860B", bg="white").pack(pady=2)
    tk.Label(m, text="تسهيل وحماية", font=("Arial", 11, "bold"), fg="#D4AF37", bg="white").pack(pady=(0, 5))
    
    fr = tk.Frame(m, bg="#F9F6EE", bd=1, relief="solid")
    fr.pack(pady=5, padx=30, fill="x")
    tk.Label(fr, text="الرصيد المتاح", font=("Arial", 11), fg="#555", bg="#F9F6EE").pack(pady=2)
    tk.Label(fr, text="250,000 ر.ي", font=("Arial", 18, "bold"), fg="#B8860B", bg="#F9F6EE").pack(pady=3)
    
    btn_bg = "#FFFFFF"
    btn_fg = "#3B3226"
    
    tk.Button(m, text="💸 تحويل أموال", font=("Arial", 11, "bold"), bg=btn_bg, fg=btn_fg, bd=2, relief="solid", command=open_transfer).pack(pady=3, padx=40, fill="x")
    tk.Button(m, text="📱 تسديد فواتير الاتصالات", font=("Arial", 11, "bold"), bg=btn_bg, fg=btn_fg, bd=2, relief="solid", command=open_bills).pack(pady=3, padx=40, fill="x")
    tk.Button(m, text="📞 خدمات المودم والبريد والثابت", font=("Arial", 11, "bold"), bg=btn_bg, fg=btn_fg, bd=2, relief="solid", command=open_landline_internet).pack(pady=3, padx=40, fill="x")
    tk.Button(m, text="🛒 دفع المشتريات والجامعات", font=("Arial", 11, "bold"), bg=btn_bg, fg=btn_fg, bd=2, relief="solid", command=open_merchant_pay).pack(pady=3, padx=40, fill="x")
    tk.Button(m, text="📥 إيداع رصيد المشتركين", font=("Arial", 11, "bold"), bg=btn_bg, fg=btn_fg, bd=2, relief="solid", command=open_deposit).pack(pady=3, padx=40, fill="x")
    tk.Button(m, text="📄 كشف الحساب والعمليات", font=("Arial", 11, "bold"), bg=btn_bg, fg=btn_fg, bd=2, relief="solid", command=open_statement).pack(pady=3, padx=40, fill="x")
    
    tk.Button(m, text="🚪 تسجيل الخروج", font=("Arial", 11, "bold"), bg="#8B0000", fg="white", command=m.destroy).pack(pady=8, padx=60, fill="x")
    m.mainloop()

# شاشة تسجيل الدخول الأولى
rt = tk.Tk()
rt.title("محفظة الأمين - تسجيل الدخول")
rt.geometry("400x580")
rt.config(bg="white")

# رسم القلب الذهبي البارز والقوي في شاشة الدخول
canvas_login = tk.Canvas(rt, width=200, height=130, bg="white", highlightthickness=0)
canvas_login.pack(pady=(15, 0))
draw_bold_golden_heart(canvas_login, x=25, y=5)

tk.Label(rt, text="محفظة الأمين", font=("Arial", 20, "bold"), fg="#B8860B", bg="white").pack(pady=2)
tk.Label(rt, text="تسهيل وحماية", font=("Arial", 12, "bold"), fg="#D4AF37", bg="white").pack(pady=(0, 10))

tk.Label(rt, text="رقم الجوال:", font=("Arial", 11, "bold"), fg="#3B3226", bg="white").pack(anchor="e", padx=40)
pe = tk.Entry(rt, font=("Arial", 13), justify="right", bd=2, relief="solid")
pe.pack(pady=5, padx=40, fill="x")

tk.Label(rt, text="رمز الحماية (PIN):", font=("Arial", 11, "bold"), fg="#3B3226", bg="white").pack(anchor="e", padx=40, pady=(8, 0))
pi = tk.Entry(rt, font=("Arial", 13), show="*", justify="right", bd=2, relief="solid")
pi.pack(pady=5, padx=40, fill="x")

tk.Button(rt, text="تسجيل الدخول", font=("Arial", 13, "bold"), bg="#FFD700", fg="#3B3226", command=go_main).pack(pady=20, padx=40, fill="x")

rt.mainloop()
