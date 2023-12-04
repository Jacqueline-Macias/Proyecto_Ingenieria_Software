import customtkinter

class window_provider:
    def __init__(self,window):
        self.window = window
        self.frame_menu = customtkinter.CTkFrame(self.window,width=100, height=430)
        self.frame_menu.place(x=10,y=10)

        self.btn_empleado = customtkinter.CTkButton(self.frame_menu,text="EM",command=self.Empleado,width=80,height=50)
        self.btn_empleado.place(x=10,y=10)

        self.btn_proveedor = customtkinter.CTkButton(self.frame_menu, text="PRO", command=self.Proveedor, width=80, height=50)
        self.btn_proveedor.place(x=10, y=70)
    
    def state_btn_Menu(self,btn_state):
        self.btn_empleado.configure(state = btn_state)
        self.btn_proveedor.configure(state=btn_state)
        
    
    def Empleado(self):
        pass

    def Proveedor(self):
        self.frame_provider = customtkinter.CTkFrame(self.window, width=470, height=430)
        self.frame_provider.place(x=120, y=10)

        def state_text(text_state):
            self.txt_id_provider.configure(state=text_state)
            self.txt_name_provider.configure(state=text_state)
            self.txt_phone_provier.configure(state=text_state)
            self.txt_type_provier.configure(state=text_state)
            self.txt_rfc_provier.configure(state=text_state)

        def state_btn(btn_state):
            self.btn_add.configure(state=btn_state)
            self.btn_modifier.configure(state=btn_state)
            self.btn_delete.configure(state=btn_state)

        def add():
            state_btn("disabled")
            state_text("normal")

        def modifier():
            pass

        def delete():
            pass

        def save():
            pass

        def cancel():
            pass

        self.btn_add = customtkinter.CTkButton(self.frame_provider,text="Registar",width=100,command=add)
        self.btn_add.place(x=70,y=10)

        self.btn_modifier = customtkinter.CTkButton(self.frame_provider,text="Modificar",width=100,command=modifier)
        self.btn_modifier.place(x=180, y=10)

        self.btn_delete = customtkinter.CTkButton(self.frame_provider, text="Eliminar", width=100, command=delete)
        self.btn_delete.place(x=290, y=10)

        lbl_id = customtkinter.CTkLabel(self.frame_provider, text="ID:")
        lbl_id.place(x=10,y=70)
        self.txt_id_provider = customtkinter.CTkEntry(self.frame_provider,width=60)
        self.txt_id_provider.place(x=30,y=70)

        lbl_name = customtkinter.CTkLabel(self.frame_provider, text="Proveedor:")
        lbl_name.place(x=120, y=70)
        self.txt_name_provider = customtkinter.CTkEntry(self.frame_provider)
        self.txt_name_provider.place(x=190, y=70)

        lbl_phone_provier = customtkinter.CTkLabel(self.frame_provider, text="Telefono:")
        lbl_phone_provier.place(x=10,y=110)
        self.txt_phone_provier = customtkinter.CTkEntry(self.frame_provider, width=200)
        self.txt_phone_provier.place(x=80,y=110)

        lbl_email_provier = customtkinter.CTkLabel(self.frame_provider, text="Correo:")
        lbl_email_provier.place(x=10, y=150)
        self.txt_email_provier = customtkinter.CTkEntry(self.frame_provider,width=200)
        self.txt_email_provier.place(x=80, y=150)

        lbl_type_provier = customtkinter.CTkLabel(self.frame_provider, text="Cadena:")
        lbl_type_provier.place(x=10, y=190)
        self.txt_type_provier = customtkinter.CTkEntry(self.frame_provider, width=200)
        self.txt_type_provier.place(x=80, y=190)

        lbl_rfc_provier = customtkinter.CTkLabel(self.frame_provider, text="RFC:")
        lbl_rfc_provier.place(x=10, y=230)
        self.txt_rfc_provier = customtkinter.CTkEntry(self.frame_provider, width=200)
        self.txt_rfc_provier.place(x=80, y=230)

        self.state_btn_Menu("disabled")
        state_text("disabled")

        self.window.update()

if __name__ == "__main__":
    window = customtkinter.CTk()
    window.geometry("600x450")
    window.title("FoodSoft")

    app = window_provider(window)

    window.mainloop()