import customtkinter
import tkinter
from tkinter import ttk, messagebox

import Conexion_SQL

class window_provider:
    def __init__(self,window):
        self.window = window
        self.frame_menu = customtkinter.CTkFrame(self.window,width=100, height=430)
        self.frame_menu.place(x=10,y=10)

        self.btn_empleado = customtkinter.CTkButton(self.frame_menu,text="EM",command=self.Empleado,width=80,height=50)
        self.btn_empleado.place(x=10,y=10)

        self.btn_proveedor = customtkinter.CTkButton(self.frame_menu, text="PRO", command=self.Proveedor, width=80, height=50)
        self.btn_proveedor.place(x=10, y=70)

        self.table_provider = Conexion_SQL.provider('localhost','root','Ryck-29042001','3306','foodsoft')
    
    def state_btn_Menu(self,btn_state):
        self.btn_empleado.configure(state = btn_state)
        self.btn_proveedor.configure(state=btn_state)
        
    
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

if __name__ == "__main__":
    window = customtkinter.CTk()
    window.geometry("600x450")
    window.title("FoodSoft")

    app = window_provider(window)

    window.mainloop()