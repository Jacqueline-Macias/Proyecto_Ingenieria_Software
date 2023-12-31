import customtkinter
import tkinter
from tkinter import ttk, messagebox

import Conexion_SQL

class window_provider:
    def __init__(self,window):
        self.window = window
        self.frame_menu = customtkinter.CTkFrame(self.window,width=100, height=430)
        self.frame_menu.place(x=10,y=10)

        self.btn_empleado = customtkinter.CTkButton(self.frame_menu,text="Empleado",command=self.Empleado,width=80,height=50)
        self.btn_empleado.place(x=10,y=10)

        self.btn_proveedor = customtkinter.CTkButton(self.frame_menu, text="Proveedor", command=self.Proveedor, width=80, height=50)
        self.btn_proveedor.place(x=10, y=70)

        self.btn_platillo = customtkinter.CTkButton(self.frame_menu, text="Platillo", command=self.Platillo,width=80, height=50)
        self.btn_platillo.place(x=10, y=130)

        self.btn_insumo = customtkinter.CTkButton(self.frame_menu, text="Insumo", command=self.Insumo,width=80, height=50)
        self.btn_insumo.place(x=10, y=190)

        self.btn_comanda = customtkinter.CTkButton(self.frame_menu, text="Comanda", command=self.Comanda,width=80, height=50)
        self.btn_comanda.place(x=10, y=250)

        self.table_provider = Conexion_SQL.provider('localhost','root','10122002','3306','foodsoft')
    
    def state_btn_Menu(self,btn_state):
        self.btn_empleado.configure(state = btn_state)
        self.btn_proveedor.configure(state=btn_state)
        self.btn_platillo.configure(state = btn_state)
        self.btn_insumo.configure(state=btn_state)
        self.btn_comanda.configure(state = btn_state)
        
    
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

                txt_id_provider.insert(0,key)
                txt_name_product.insert(0,values[0])
                txt_stock_mi_product.insert(0,values[1])
                txt_stock_ma_product.insert(0,values[2])
                txt_precio_in_product.insert(0,values[3])

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

                txt_id_provider.insert(0, key)
                txt_name_product.insert(0, values[0])
                txt_stock_mi_product.insert(0, values[1])
                txt_stock_ma_product.insert(0, values[2])
                txt_precio_in_product.insert(0, values[3])

                option = messagebox.askquestion('Eliminar',f'¿Seguro que quiere eliminar {key} : {values[0]}')
                if option == 'yes':
                    self.table_provider.delete(key)
                    clear_table()
                    add_table()

                clear_txt()
                state_text('disabled')
                state_btn('normal')
                btn_save_product.configure(state='disabled')
                btn_cancel_product.configure(state='disabled')

        def save():
            if self.band_modifier_product:
                self.table_product.modifier(txt_id_provider.get(),txt_name_product.get(),txt_stock_mi_product.get(), txt_stock_ma_product.get(), txt_precio_in_product.get())
            else:
                self.table_product.Add(txt_id_provider.get(),txt_name_product.get(),txt_stock_mi_product.get(), txt_stock_ma_product.get(), txt_precio_in_product.get())
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

        btn_delete = customtkinter.CTkButton(frame_product, text="Pedido", width=60, command=delete)
        btn_delete.place(x=310, y=10)

        btn_delete = customtkinter.CTkButton(frame_product, text="Merma", width=60, command=delete)
        btn_delete.place(x=400, y=10)

        lbl_name = customtkinter.CTkLabel(frame_product, text="Nombre:")
        lbl_name.place(x=10,y=70)
        txt_name_product = customtkinter.CTkEntry(frame_product,width=60)
        txt_name_product.place(x=30,y=70)

        lbl_stock_mi = customtkinter.CTkLabel(frame_product, text="Stock min:")
        lbl_stock_mi.place(x=120, y=70)
        txt_stock_mi_product = customtkinter.CTkEntry(frame_product)
        txt_stock_mi_product.place(x=190, y=70)

        lbl_stock_ma_product = customtkinter.CTkLabel(frame_product, text="Stock max:")
        lbl_stock_ma_product.place(x=10,y=110)
        txt_stock_ma_product = customtkinter.CTkEntry(frame_product, width=200)
        txt_stock_ma_product.place(x=80,y=110)

        lbl_id_provider = customtkinter.CTkLabel(frame_product, text="ID proveedor:")
        lbl_id_provider.place(x=10, y=150)
        txt_id_provider = customtkinter.CTkEntry(frame_product,width=200)
        txt_id_provider.place(x=80, y=150)

        lbl_precio_in_product = customtkinter.CTkLabel(frame_product, text="Precio:")
        lbl_precio_in_product.place(x=10, y=190)
        txt_precio_in_product = customtkinter.CTkEntry(frame_product, width=200)
        txt_precio_in_product.place(x=80, y=190)


        btn_save_product = customtkinter.CTkButton(frame_product,text="guardar",width=100,height=50,command=save)
        btn_save_product.place(x=300,y=130)

        btn_cancel_product = customtkinter.CTkButton(frame_product, text="cancelar", width=100, height=50, command=cancel)
        btn_cancel_product.place(x=300, y=190)

        table = ttk.Treeview(frame_product,columns=('col1','col2','col3','col4','col5'))
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
        btn_cancel_product.configure(state='disabled')
        btn_save_product.configure(state='disabled')

        self.window.update()

    def Comanda(self):
        pass


if __name__ == "__main__":
    window = customtkinter.CTk()
    window.geometry("600x450")
    window.title("FoodSoft")

    app = window_provider(window)

    window.mainloop()