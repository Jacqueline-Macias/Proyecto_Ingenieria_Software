import customtkinter
import tkinter
from tkinter import ttk, messagebox
from datetime import date

import Conexion_SQL
import image
import contra

class window_provider:
    def __init__(self,window,id):
        self.window = window
        self.id = id
        self.frame_menu = customtkinter.CTkFrame(self.window,width=100, height=430)
        self.frame_menu.place(x=10,y=10)

        self.btn_empleado = customtkinter.CTkButton(self.frame_menu,text="",image=image.open_image("Image\\employe.png",50,50),command=self.Empleado,width=80,height=50)
        self.btn_empleado.place(x=10,y=10)

        self.btn_proveedor = customtkinter.CTkButton(self.frame_menu, text="", image=image.open_image(
            "Image\\local.png", 50, 50), command=self.Proveedor, width=80, height=50)
        self.btn_proveedor.place(x=10, y=70)

        self.btn_platillo = customtkinter.CTkButton(self.frame_menu, text="", image=image.open_image("Image\\restaurant.png", 50, 50), command=self.Platillo, width=80, height=50)
        self.btn_platillo.place(x=10, y=130)

        self.btn_insumo = customtkinter.CTkButton(
            self.frame_menu, text="", image=image.open_image("Image\\grocery.png", 50, 50), command=self.Insumo, width=80, height=50)
        self.btn_insumo.place(x=10, y=190)

        self.btn_comanda = customtkinter.CTkButton(
            self.frame_menu, text="", image=image.open_image("Image\\order.png", 50, 50), command=self.Comanda, width=80, height=50)
        self.btn_comanda.place(x=10, y=250)

        self.btn_report = customtkinter.CTkButton(self.frame_menu, text="", image=image.open_image("Image\\search.png", 50, 50), command=self.report, width=80, height=50)
        self.btn_report.place(x=10, y=310)

        self.table_provider = Conexion_SQL.provider('localhost','root',contra.contraseña(),'3306','foodsoft')
        self.table_product = Conexion_SQL.supply('localhost','root',contra.contraseña(),'3306','foodsoft')
        self.table_order = Conexion_SQL.order('localhost', 'root', contra.contraseña(), '3306', 'foodsoft')
    
    def state_btn_Menu(self,btn_state):
        self.btn_empleado.configure(state=btn_state)
        self.btn_proveedor.configure(state=btn_state)
        self.btn_platillo.configure(state=btn_state)
        self.btn_insumo.configure(state=btn_state)
        self.btn_comanda.configure(state=btn_state)
        self.btn_report.configure(state=btn_state)
        
    
    def Empleado(self):
        pass

    def Proveedor(self):
        frame_provider = customtkinter.CTkFrame(self.window, width=470, height=430)
        frame_provider.place(x=120, y=10)
        self.band_modifier_provider = False

        def state_text(text_state):
            txt_id_provider.configure(state=text_state)
            txt_name_provider.configure(state=text_state)
            txt_phone_provider.configure(state=text_state)
            txt_email_provider.configure(state=text_state)
            txt_type_provider.configure(state=text_state)
            txt_rfc_provider.configure(state=text_state)

        def state_btn(btn_state):
            btn_add.configure(state=btn_state)
            btn_modifier.configure(state=btn_state)
            btn_delete.configure(state=btn_state)

        def add_table():
            provider = self.table_provider.select_all()
            for count in provider:
                table.insert("",tkinter.END, text=count[0],values=[count[1],count[2],count[3],count[4],count[5]])

        def clear_table():
            register = table.get_children()
            for count_register in register:
                table.delete(count_register)

        def clear_txt():
            txt_id_provider.delete(0,customtkinter.END)
            txt_name_provider.delete(0,customtkinter.END)
            txt_phone_provider.delete(0,customtkinter.END)
            txt_email_provider.delete(0,customtkinter.END)
            txt_type_provider.delete(0,customtkinter.END)
            txt_rfc_provider.delete(0,customtkinter.END)

        def add():
            self.band_modifier_provider = False
            state_btn("disabled")
            state_text("normal")
            btn_save_provider.configure(state='normal')
            btn_cancel_provider.configure(state='normal')

        def modifier():
            select = table.focus()
            key = table.item(select,'text')

            if key == '':
                messagebox.showerror("Modificar","Selecciona un elemento")
            else:
                self.band_modifier_provider = True
                state_text('normal')
                values = table.item(select,'values')

                txt_id_provider.insert(0,key)
                txt_name_provider.insert(0,values[0])
                txt_phone_provider.insert(0,values[1])
                txt_email_provider.insert(0,values[2])
                txt_type_provider.insert(0,values[3])
                txt_rfc_provider.insert(0,values[4])

                state_btn('disabled')
                btn_cancel_provider.configure(state='normal')
                btn_save_provider.configure(state='normal')

        def delete():
            select = table.focus()
            key = table.item(select, 'text')

            if key == '':
                messagebox.showerror("Eliminar", "Selecciona un elemento")
            else:
                state_text('normal')
                values = table.item(select, 'values')

                txt_id_provider.insert(0, key)
                txt_name_provider.insert(0, values[0])
                txt_phone_provider.insert(0, values[1])
                txt_email_provider.insert(0, values[2])
                txt_type_provider.insert(0, values[3])
                txt_rfc_provider.insert(0, values[4])

                option = messagebox.askquestion('Eliminar',f'¿Seguro que quiere eliminar {key} : {values[0]}')
                if option == 'yes':
                    self.table_provider.delete(key)
                    clear_table()
                    add_table()

                clear_txt()
                state_text('disabled')
                state_btn('normal')
                btn_save_provider.configure(state='disabled')
                btn_cancel_provider.configure(state='disabled')

        def save():
            if self.band_modifier_provider:
                self.table_provider.modifier(txt_id_provider.get(),txt_name_provider.get(),txt_phone_provider.get(), txt_email_provider.get(), txt_type_provider.get(), txt_rfc_provider.get())
            else:
                self.table_provider.Add(txt_id_provider.get(),txt_name_provider.get(),txt_phone_provider.get(),txt_email_provider.get(),txt_type_provider.get(),txt_rfc_provider.get())
            clear_txt()
            clear_table()
            add_table()
            state_text('disabled')
            state_btn('normal')
            btn_save_provider.configure(state='disabled')
            btn_cancel_provider.configure(state='disabled')

        def cancel():
            option = messagebox.askquestion('Cancelar',"¿Seguro que quiere cancelar?")
            if option == 'yes':
                clear_txt()
                state_text('disabled')
                state_btn('normal')
                btn_save_provider.configure(state='disabled')
                btn_cancel_provider.configure(state='disabled')

        def close():
            frame_provider.destroy()
            self.state_btn_Menu('normal')
        
        btn_close = customtkinter.CTkButton(frame_provider,text="X",width=10,height=10,fg_color="RED",command=close)
        btn_close.place(x=0,y=0)

        btn_add = customtkinter.CTkButton(frame_provider,text="Registar",width=100,command=add)
        btn_add.place(x=70,y=10)

        btn_modifier = customtkinter.CTkButton(frame_provider,text="Modificar",width=100,command=modifier)
        btn_modifier.place(x=180, y=10)

        btn_delete = customtkinter.CTkButton(frame_provider, text="Eliminar", width=100, command=delete)
        btn_delete.place(x=290, y=10)

        lbl_id = customtkinter.CTkLabel(frame_provider, text="ID:")
        lbl_id.place(x=10,y=70)
        txt_id_provider = customtkinter.CTkEntry(frame_provider,width=60)
        txt_id_provider.place(x=30,y=70)

        lbl_name = customtkinter.CTkLabel(frame_provider, text="Proveedor:")
        lbl_name.place(x=120, y=70)
        txt_name_provider = customtkinter.CTkEntry(frame_provider)
        txt_name_provider.place(x=190, y=70)

        lbl_phone_provider = customtkinter.CTkLabel(frame_provider, text="Telefono:")
        lbl_phone_provider.place(x=10,y=110)
        txt_phone_provider = customtkinter.CTkEntry(frame_provider, width=200)
        txt_phone_provider.place(x=80,y=110)

        lbl_email_provider = customtkinter.CTkLabel(frame_provider, text="Correo:")
        lbl_email_provider.place(x=10, y=150)
        txt_email_provider = customtkinter.CTkEntry(frame_provider,width=200)
        txt_email_provider.place(x=80, y=150)

        lbl_type_provider = customtkinter.CTkLabel(frame_provider, text="Cadena:")
        lbl_type_provider.place(x=10, y=190)
        txt_type_provider = customtkinter.CTkEntry(frame_provider, width=200)
        txt_type_provider.place(x=80, y=190)

        lbl_rfc_provider = customtkinter.CTkLabel(frame_provider, text="RFC:")
        lbl_rfc_provider.place(x=10, y=230)
        txt_rfc_provider = customtkinter.CTkEntry(frame_provider, width=200)
        txt_rfc_provider.place(x=80, y=230)

        btn_save_provider = customtkinter.CTkButton(frame_provider,text="guardar",width=100,height=50,command=save)
        btn_save_provider.place(x=300,y=130)

        btn_cancel_provider = customtkinter.CTkButton(frame_provider, text="cancelar", width=100, height=50, command=cancel)
        btn_cancel_provider.place(x=300, y=190)

        table = ttk.Treeview(frame_provider,columns=('col1','col2','col3','col4','col5'))
        table.column("#0",width=10)
        table.column("col1",width=20)
        table.column('col2',width=15)
        table.column('col3',width=20)
        table.column('col4',width=15)
        table.column('col5',width=15)

        table.heading('#0',text="ID")
        table.heading('col1',text='Nombre')
        table.heading('col2',text='Telefono')
        table.heading('col3',text='Email')
        table.heading('col4',text='Cadena')
        table.heading('col5',text='RFC')

        table.place(x=10,y=410,width=680)

        add_table()

        self.state_btn_Menu("disabled")
        state_text("disabled")
        btn_cancel_provider.configure(state='disabled')
        btn_save_provider.configure(state='disabled')

        self.window.update()

    def Platillo(self):
        pass

    def Insumo(self):
        frame_product = customtkinter.CTkFrame(self.window, width=470, height=430)
        frame_product.place(x=120, y=10)
        self.band_modifier_product = False

        def state_text(text_state):
            txt_id_provider.configure(state=text_state)
            txt_name_product.configure(state=text_state)
            txt_stock_mi_product.configure(state=text_state)
            txt_stock_ma_product.configure(state=text_state)
            txt_precio_in_product.configure(state=text_state)
            txt_number.configure(state=text_state)

        def state_btn(btn_state):
            btn_add.configure(state=btn_state)
            btn_modifier.configure(state=btn_state)
            btn_delete.configure(state=btn_state)
            btn_pedido.configure(state=btn_state)
            btn_merma.configure(state=btn_state)

        def add_table():
            provider = self.table_product.select_all()
            for count in provider:
                table.insert("",tkinter.END, text=count[0],values=[count[1],count[2],count[3],count[4],count[5]])

        def clear_table():
            register = table.get_children()
            for count_register in register:
                table.delete(count_register)

        def clear_txt():
            txt_id_provider.set('')
            txt_name_product.delete(0,customtkinter.END)
            txt_stock_mi_product.delete(0,customtkinter.END)
            txt_stock_ma_product.delete(0,customtkinter.END)
            txt_precio_in_product.delete(0,customtkinter.END)

        def add():
            self.band_modifier_product = False
            state_btn("disabled")
            state_text("normal")
            btn_save_product.configure(state='normal')
            btn_cancel_product.configure(state='normal')

        def modifier():
            select = table.focus()
            key = table.item(select,'text')

            if key == '':
                messagebox.showerror("Modificar","Selecciona un elemento")
            else:
                self.band_modifier_product = True
                state_text('normal')
                values = table.item(select,'values')

                provider = self.table_product.Search_id('nombre','proveedor','id_proveedor',int(values[4]))
                txt_name_product.insert(0,key)
                txt_number.insert(0,values[0])
                txt_stock_mi_product.insert(0,values[1])
                txt_stock_ma_product.insert(0,values[2])
                txt_precio_in_product.insert(0,values[3])
                txt_id_provider.set(provider[0])

                state_btn('disabled')
                btn_cancel_product.configure(state='normal')
                btn_save_product.configure(state='normal')

        def delete():
            select = table.focus()
            key = table.item(select, 'text')

            if key == '':
                messagebox.showerror("Eliminar", "Selecciona un elemento")
            else:
                state_text('normal')
                values = table.item(select, 'values')

                provider = self.table_product.Search_id('nombre', 'proveedor', 'id_proveedor', int(values[4]))
                txt_name_product.insert(0, key)
                txt_number.insert(0,values[0])
                txt_stock_mi_product.insert(0, values[1])
                txt_stock_ma_product.insert(0, values[2])
                txt_precio_in_product.insert(0, values[3])
                txt_id_provider.set(provider[0])

                option = messagebox.askquestion('Eliminar',f'¿Seguro que quiere eliminar {key} ')
                if option == 'yes':
                    self.table_product.delete(key)
                    clear_table()
                    add_table()

                clear_txt()
                state_text('disabled')
                state_btn('normal')
                btn_save_product.configure(state='disabled')
                btn_cancel_product.configure(state='disabled')

        def merma():
            pass

        def save():
            if self.band_modifier_product:
                self.table_product.modifier(txt_number.get(),txt_id_provider.get(),txt_name_product.get(),txt_stock_mi_product.get(), txt_stock_ma_product.get(), txt_precio_in_product.get())
            else:
                self.table_product.Add(txt_id_provider.get(),txt_name_product.get(),txt_number.get(),txt_stock_mi_product.get(), txt_stock_ma_product.get(), txt_precio_in_product.get())
            clear_txt()
            clear_table()
            add_table()
            state_text('disabled')
            state_btn('normal')
            btn_save_product.configure(state='disabled')
            btn_cancel_product.configure(state='disabled')

        def cancel():
            option = messagebox.askquestion('Cancelar',"¿Seguro que quiere cancelar?")
            if option == 'yes':
                clear_txt()
                state_text('disabled')
                state_btn('normal')
                btn_save_product.configure(state='disabled')
                btn_cancel_product.configure(state='disabled')

        def close():
            frame_product.destroy()
            self.state_btn_Menu('normal')
        
        btn_close = customtkinter.CTkButton(frame_product,text="X",width=10,height=10,fg_color="RED",command=close)
        btn_close.place(x=0,y=0)

        btn_add = customtkinter.CTkButton(frame_product,text="Registar",width=60,command=add)
        btn_add.place(x=40,y=10)

        btn_modifier = customtkinter.CTkButton(frame_product,text="Modificar",width=60,command=modifier)
        btn_modifier.place(x=130, y=10)

        btn_delete = customtkinter.CTkButton(frame_product, text="Eliminar", width=60, command=delete)
        btn_delete.place(x=220, y=10)

        btn_pedido = customtkinter.CTkButton(frame_product, text="Pedido", width=60, command=self.order)
        btn_pedido.place(x=310, y=10)

        btn_merma = customtkinter.CTkButton(frame_product, text="Merma", width=60, command=merma)
        btn_merma.place(x=400, y=10)

        lbl_name = customtkinter.CTkLabel(frame_product, text="Nombre:")
        lbl_name.place(x=10,y=70)
        txt_name_product = customtkinter.CTkEntry(frame_product,width=230)
        txt_name_product.place(x=80,y=70)

        lbl_stock_mi = customtkinter.CTkLabel(frame_product, text="Stock min:")
        lbl_stock_mi.place(x=10, y=110)
        txt_stock_mi_product = customtkinter.CTkEntry(frame_product, width=70)
        txt_stock_mi_product.place(x=80, y=110)

        lbl_stock_ma_product = customtkinter.CTkLabel(frame_product, text="Stock max:")
        lbl_stock_ma_product.place(x=170,y=110)
        txt_stock_ma_product = customtkinter.CTkEntry(frame_product, width=70)
        txt_stock_ma_product.place(x=240,y=110)

        values_provider = self.table_provider.select("nombre")
        lbl_id_provider = customtkinter.CTkLabel(frame_product, text="proveedor:")
        lbl_id_provider.place(x= 10, y=190)
        txt_id_provider = customtkinter.CTkOptionMenu(frame_product,width=150,values=values_provider)
        txt_id_provider.place(x=80, y=190)
        txt_id_provider.set("")

        lbl_precio_in_product = customtkinter.CTkLabel(frame_product, text="Precio:")
        lbl_precio_in_product.place(x=10, y=150)
        txt_precio_in_product = customtkinter.CTkEntry(frame_product, width=70)
        txt_precio_in_product.place(x=80, y=150)

        lbl_number= customtkinter.CTkLabel(frame_product, text="Cantidad:")
        lbl_number.place(x=170, y=150)
        txt_number = customtkinter.CTkEntry(frame_product, width=70)
        txt_number.place(x=240, y=150)

        btn_save_product = customtkinter.CTkButton(frame_product,text="guardar",width=100,height=50,command=save)
        btn_save_product.place(x=330,y=90)

        btn_cancel_product = customtkinter.CTkButton(frame_product, text="cancelar", width=100, height=50, command=cancel)
        btn_cancel_product.place(x=330, y=150)

        table = ttk.Treeview(frame_product,columns=('col1','col2','col3','col4','col5'))
        table.column("#0",width=10)
        table.column("col1",width=20)
        table.column('col2',width=15)
        table.column('col3',width=20)
        table.column('col4',width=15)
        table.column('col5',width=15)

        table.heading('#0',text="nombre")
        table.heading('col1',text='cantidad')
        table.heading('col2',text='Stock Min')
        table.heading('col3',text='stock Max')
        table.heading('col4',text='Precio')
        table.heading('col5',text='Provedor')

        table.place(x=10,y=410,width=680)

        add_table()

        self.state_btn_Menu("disabled")
        state_text("disabled")
        btn_cancel_product.configure(state='disabled')
        btn_save_product.configure(state='disabled')

        self.window.update()
    
    def order(self):
        frame_order = customtkinter.CTkFrame(self.window, width=470, height=430)
        frame_order.place(x=120, y=10)

        def add_table():
            provider = self.table_order.view(folio)
            for count in provider:
                name_provider = self.table_provider.Search_id('nombre','proveedor','id_proveedor',int(count[2]))
                table.insert("", tkinter.END, text=count[1], values=[
                             name_provider, count[3],count[4], int(count[3])*float(count[4])])

        def clear_table():
            register = table.get_children()
            for count_register in register:
                table.delete(count_register)

        def clear_txt():
            txt_number.delete(0,customtkinter.END)
            txt_price.delete(0,customtkinter.END)

        def state_btn(btn_state):
            btn_add.configure(state=btn_state)
            btn_remove.configure(state=btn_state)
            btn_order.configure(state=btn_state)

        def state_txt(txt_state):
            txt_price.configure(state=txt_state)
            txt_number.configure(state=txt_state)

        def state_product(product_state):
            txt_product.configure(state=product_state)
            btn_product.configure(state=product_state)

        def state_provider(provider_state):
            txt_cmb_provider.configure(state=provider_state)
            btn_search.configure(state=provider_state)

        def close():
            frame_order.destroy()

        def search():
            if txt_cmb_provider.get() != "":
                try:
                    product = self.table_product.Search("nombre","insumo",'id_proveedor',int(txt_cmb_provider.get()))
                    txt_product.configure(values = product)

                    band = self.table_order.add_order(int(txt_cmb_provider.get()),self.id,date.today())
                    if band:
                        state_btn('normal')
                        state_product('normal')
                        state_provider('disabled')
                except Exception as Ex:
                    messagebox.showerror("Error","Dato no valido")

            else:
                messagebox.showerror("Error","Ingrese el id del proveedor")

        def price_and_number():
            state_txt('normal')
            clear_txt()
            price = self.table_order.Search_id('precio', 'insumo', 'nombre', txt_product.get())

            number = self.table_order.Search_id('cantidad','insumo','nombre',txt_product.get())
            max = self.table_order.Search_id('stock_max','insumo','nombre',txt_product.get())

            number = max[0] - number[0]

            txt_price.insert(0,price[0])
            txt_price.configure(state="disabled")
            txt_number.insert(0,number)

        def add():
            max = self.table_order.Search_id('stock_max','insumo','nombre',txt_product.get())
            number = self.table_order.Search_id('cantidad','insumo','nombre',txt_product.get())
            number = max[0] - (int(txt_number.get())+number[0])
            if number < 0:
                messagebox.showerror("Error","La cantida sobrepasa al maximo")
            elif int(txt_number.get()) < 0:
                messagebox.showerror("Error","La cantidad no puede ser negativa")
            else:
                number_product = self.table_order.Search_id('cantidad','insumo','nombre',txt_product.get())
                number_product = number_product[0] + int(txt_number.get())
                self.table_product.modifier_number(txt_product.get(),number_product)
                product = self.table_order.Search_view(folio, txt_product.get())
                if (product == []):
                    self.table_order.add(folio,txt_product.get(),float(txt_price.get()),int(txt_number.get()))
                else:
                    product = product[0]
                    new_number = int(txt_number.get()) + product[4]
                    new_price = float(txt_price.get()) + product[3]
                    self.table_order.modifier(folio,txt_product.get(),new_price,new_number)

                self.subtotal_order = self.subtotal_order + (int(txt_number.get()) * float(txt_price.get()))
                lbl_subtotal = customtkinter.CTkLabel(frame_order,text=f"Subtotal: {self.subtotal_order}")
                lbl_subtotal.place(x=300,y=120)

                self.iva_order = self.subtotal_order * 0.16
                lbl_IVA = customtkinter.CTkLabel(frame_order,text=f"IVA: {self.iva_order}")
                lbl_IVA.place(x=300,y=140)

                self.total_order = self.subtotal_order + self.iva_order
                lbl_total = customtkinter.CTkLabel(frame_order,text=f"Total: {self.total_order}")
                lbl_total.place(x=300,y=180)
                
                clear_table()
                add_table()
                state_txt('normal')
                clear_txt()
                state_txt("disabled")

        def remove():
            select = table.focus()
            key = table.item(select, 'text')

            if key == '':
                messagebox.showerror("Eliminar", "Selecciona un elemento")
            else:
                values = table.item(select, 'values')
                option = messagebox.askquestion('Eliminar', f'¿Seguro que quiere quitar {key}')
                if option == 'yes':
                    number_product = self.table_order.Search_id('cantidad','insumo','nombre',txt_product.get())
                    number_product = number_product[0] - int(values[2])
                    self.table_product.modifier_number(key,number_product)
                    self.table_order.delete(folio,key)

                    self.subtotal_order = self.subtotal_order - float(values[3])
                    lbl_subtotal = customtkinter.CTkLabel(frame_order,text=f"Subtotal: {self.subtotal_order}")
                    lbl_subtotal.place(x=300,y=120)

                    self.iva_order = self.subtotal_order * 0.16
                    lbl_IVA = customtkinter.CTkLabel(frame_order,text=f"IVA: {self.iva_order}")
                    lbl_IVA.place(x=300,y=140)

                    self.total_order = self.subtotal_order + self.iva_order
                    lbl_total = customtkinter.CTkLabel(frame_order,text=f"Total: {self.total_order}")
                    lbl_total.place(x=300,y=180)

                    clear_txt()
                    clear_table()
                    add_table()


        def order():
            product = self.table_order.Search_view(folio, txt_product.get())
            if (product != []):
                messagebox.showinfo("Pedido",f"El total a pagar sera de {self.total_order}")
                frame_order.destroy()
                self.order()
            else:
                messagebox.showerror("Error","No se ha agregado nada al pedido")

        btn_close = customtkinter.CTkButton(frame_order,text="X",fg_color="RED",width=10,height=10,command=close)
        btn_close.place(x=0,y=0)

        lbl_provider = customtkinter.CTkLabel(frame_order,text="ID proveedor")
        lbl_provider.place(x=10,y=30)
        txt_cmb_provider =  customtkinter.CTkEntry(frame_order, width=150,height=30)
        txt_cmb_provider.place(x=100, y=30)
        btn_search = customtkinter.CTkButton(frame_order, text="", image=image.open_image(
            "Image\\search.png", 30, 30), width=30, height=30, command=search)
        btn_search.place(x=250,y=30)

        lbl_date = customtkinter.CTkLabel(frame_order, width=100,height=30,text=f"Fecha: {date.today()}")
        lbl_date.place(x=300,y=30)

        lbl_product = customtkinter.CTkLabel(frame_order,text="insumo")
        lbl_product.place(x=10,y=100)
        txt_product = customtkinter.CTkOptionMenu(frame_order, width=150, height=30, fg_color="WHITE", text_color="BLACK", button_color="WHITE", values=[])
        txt_product.place(x=80, y=100)
        txt_product.set("")
        btn_product = customtkinter.CTkButton(frame_order, text="", image=image.open_image(
            "Image\\search.png", 30, 30), width=30, height=30, command=price_and_number)
        btn_product.place(x=230, y=100)

        lbl_price = customtkinter.CTkLabel(frame_order, text="Precio")
        lbl_price.place(x=10, y=140)
        txt_price = customtkinter.CTkEntry(frame_order, width=50)
        txt_price.place(x=80, y=140)

        lbl_number = customtkinter.CTkLabel(frame_order, text="Cantidad")
        lbl_number.place(x=10, y=180)
        txt_number = customtkinter.CTkEntry(frame_order, width=50)
        txt_number.place(x=80, y=180)

        folio = len(self.table_order.select_all()) + 1
        lbl_folio = customtkinter.CTkLabel(frame_order,text=f"Folio: {folio}")
        lbl_folio.place(x=300,y=100)

        self.subtotal_order = 0
        lbl_subtotal = customtkinter.CTkLabel(frame_order,text=f"Subtotal: {self.subtotal_order}")
        lbl_subtotal.place(x=300,y=120)

        self.iva_order = 0
        lbl_IVA = customtkinter.CTkLabel(frame_order,text=f"IVA: {self.iva_order}")
        lbl_IVA.place(x=300,y=140)

        lbl = customtkinter.CTkLabel(frame_order,text="------------------------")
        lbl.place(x=300,y=160)

        self.total_order = 0
        lbl_total = customtkinter.CTkLabel(frame_order,text=f"Total: {self.total_order}")
        lbl_total.place(x=300,y=180)

        btn_add = customtkinter.CTkButton(frame_order,text="Agregar",width=60,command=add)
        btn_add.place(x=220,y=230)

        btn_remove = customtkinter.CTkButton(frame_order, text="Quitar", width=60, command=remove)
        btn_remove.place(x=290, y=230)

        btn_order = customtkinter.CTkButton(frame_order,text="Pedido",width=60, command=order)
        btn_order.place(x=360, y=230)

        table = ttk.Treeview(frame_order, columns=('col1', 'col2', 'col3','col4'))
        table.column("#0", width=10)
        table.column("col1", width=20)
        table.column('col2', width=15)
        table.column('col3', width=20)
        table.column('col4', width=20)

        table.heading('#0', text="Producto")
        table.heading('col1', text='Proveedor')
        table.heading('col2', text='Precio')
        table.heading('col3',text='Cantidad')
        table.heading('col4', text='Importe')

        table.place(x=10, y=400, width=680)

        state_txt('disabled')
        state_product('disabled')
        state_btn('disabled')

        self.window.update()

    def Comanda(self):
        pass

    def report(self):
        frame_report = customtkinter.CTkFrame(self.window, width=470, height=430)
        frame_report.place(x=120, y=10)
        self.state_btn_Menu('disabled')
    
        def add_table():
            provider = self.table_order.view(search_id.get())
            for count in provider:
                name_provider = self.table_provider.Search_id('nombre','proveedor','id_proveedor',int(count[2]))
                table.insert("", tkinter.END, text=count[1], values=[
                            name_provider, count[3],count[4], int(count[3])*float(count[4])])
        
        def clear_table():
            register = table.get_children()
            for count_register in register:
                table.delete(count_register)

        def close():
            self.state_btn_Menu('normal')
            frame_report.destroy()
        
        def search():

            if cmb_search.get() == "pedido":

                table.heading('#0', text="Producto")
                table.heading('col1', text='Proveedor')
                table.heading('col2', text='Precio')
                table.heading('col3', text='Cantidad')
                table.heading('col4', text='Importe')

                table.place(x=10, y=150, width=680)

                clear_table()
                add_table()


                frame_report.update()

        search_id = customtkinter.CTkEntry(frame_report,width=200)
        search_id.place(x=10,y=40)
        cmb_search = customtkinter.CTkOptionMenu(frame_report,values=['pedido'],width=100)
        cmb_search.place(x=210,y=40)
        btn_search = customtkinter.CTkButton(frame_report, width=30, height=30, text="", image=image.open_image(
            "Image\\search.png", 30, 30), command=search)
        btn_search.place(x=310,y=40)

        btn_close = customtkinter.CTkButton(frame_report,width=10,height=10,text="X",fg_color="RED",command=close)
        btn_close.place(x=0,y=0)

        table = ttk.Treeview(frame_report, columns=('col1', 'col2', 'col3', 'col4'))
        table.column("#0", width=10)
        table.column("col1", width=20)
        table.column('col2', width=15)
        table.column('col3', width=20)
        table.column('col4', width=20)


        self.window.update()

if __name__ == "__main__":
    window = customtkinter.CTk()
    window.geometry("600x450")
    window.title("FoodSoft")

    app = window_provider(window,1)

    window.mainloop()