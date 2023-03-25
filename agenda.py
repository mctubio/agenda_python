import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb
from tkinter import scrolledtext as st
import contactos

class Agenda_Contactos:
    def __init__(self):
        self.contacto1 = contactos.Contactos()
        self.ventana = tk.Tk()
        self.ventana.title('Agenda de contactos')

        self.cuaderno = ttk.Notebook(self.ventana)
        self.nuevo_contacto()
        self.buscar_por_apellido()
        self.agenda_completa()

        self.cuaderno.grid(column=0, row=0,pady=10)

        self.ventana.mainloop()
    
    def nuevo_contacto(self):
        #encabezado de la pestaña
        self.pagina01 = ttk.Frame(self.cuaderno)
        self.cuaderno.add(self.pagina01, text = 'Nuevo contacto')
        self.labelframe01 = ttk.LabelFrame(self.pagina01, text ='Contactos')
        self.labelframe01.grid(column=0, row=0, padx=10, pady=10)

        #Codigo
        self.label01 = ttk.Label(self.labelframe01, text= 'Código')
        self.label01.grid(column=0, row=0, padx=5, pady=15, sticky='e')
        self.codigo_nuevo = tk.StringVar()
        self.entry_codigo = ttk.Entry(self.labelframe01, textvariable=self.codigo_nuevo, width=30)
        self.entry_codigo.grid(column=1, row=0, padx=5, pady=15, sticky='w')
        
        #Nombre
        self.label02 = ttk.Label(self.labelframe01, text= 'Nombre')
        self.label02.grid(column=0, row=1, padx=5, pady=15, sticky='e')
        self.nombre_nuevo = tk.StringVar()
        self.entry_nombre = ttk.Entry(self.labelframe01, textvariable=self.nombre_nuevo, width=50)
        self.entry_nombre.grid(column=1, row=1, padx=5, pady=15, sticky='w')

        #Apellido
        self.label03 = ttk.Label(self.labelframe01, text= 'Apellido')
        self.label03.grid(column=0, row=2, padx=5, pady=15, sticky='e')
        self.apellido_nuevo = tk.StringVar()
        self.entry_apellido = ttk.Entry(self.labelframe01, textvariable=self.apellido_nuevo, width=50)
        self.entry_apellido.grid(column=1, row=2, padx=5, pady=15, sticky='w')

        #Telefono
        self.label04 = ttk.Label(self.labelframe01, text= 'Teléfono')
        self.label04.grid(column=0, row=3, padx=5, pady=15, sticky='e')
        self.telefono_nuevo = tk.StringVar()
        self.entry_telefono = ttk.Entry(self.labelframe01, textvariable=self.telefono_nuevo, width=20)
        self.entry_telefono.grid(column=1, row=3, padx=5, pady=15, sticky='w')

        #email
        self.label05 = ttk.Label(self.labelframe01, text= 'e-mail')
        self.label05.grid(column=0, row=4, padx=5, pady=15, sticky='e')
        self.email_nuevo = tk.StringVar()
        self.entry_mail = ttk.Entry(self.labelframe01, textvariable=self.email_nuevo, width=50)
        self.entry_mail.grid(column=1, row=4, padx=5, pady=15, sticky='w')

        #calle
        self.label06 = ttk.Label(self.labelframe01, text= 'Calle')
        self.label06.grid(column=2, row=1, padx=5, pady=15, sticky='e')
        self.calle_nuevo = tk.StringVar()
        self.entry_calle = ttk.Entry(self.labelframe01, textvariable=self.calle_nuevo, width=50)
        self.entry_calle.grid(column=3, row=1, padx=5, pady=15, sticky='w')

        #numero calle
        self.label07 = ttk.Label(self.labelframe01, text= 'Numero')
        self.label07.grid(column=2, row=2, padx=5, pady=15, sticky='e')
        self.num_calle_nuevo = tk.StringVar()
        self.entry_num_calle = ttk.Entry(self.labelframe01, textvariable=self.num_calle_nuevo, width=15)
        self.entry_num_calle.grid(column=3, row=2, padx=5, pady=15, sticky='w')

        #piso
        self.label08 = ttk.Label(self.labelframe01, text= 'Piso')
        self.label08.grid(column=2, row=3, padx=5, pady=15, sticky='e')
        self.piso_nuevo = tk.StringVar()
        self.entry_piso = ttk.Entry(self.labelframe01, textvariable=self.piso_nuevo, width=15)
        self.entry_piso.grid(column=3, row=3, padx=5, pady=15, sticky='w')

        #depto
        self.label08 = ttk.Label(self.labelframe01, text= 'Departamento')
        self.label08.grid(column=2, row=4, padx=5, pady=15, sticky='e')
        self.depto_nuevo = tk.StringVar()
        self.entry_depto = ttk.Entry(self.labelframe01, textvariable=self.depto_nuevo, width=15)
        self.entry_depto.grid(column=3, row=4, padx=5, pady=15, sticky='w')

        #comentario
        self.label08 = ttk.Label(self.labelframe01, text= 'Comentario')
        self.label08.grid(column=0, row=5, padx=5, pady=25, sticky='e')
        self.comentario_nuevo = tk.StringVar()
        self.entry_comentario = ttk.Entry(self.labelframe01, textvariable=self.comentario_nuevo, width=120)
        self.entry_comentario.grid(column=1, row=5, padx=5, pady=25, columnspan=3, sticky='w')

        #boton
        self.boton01 = ttk.Button(self.labelframe01, text='Guardar', command=self.guardar)
        self.boton01.grid(column=3, row=6, padx=10, pady=10, columnspan=2)

    def guardar(self):
        datos = (self.nombre_nuevo.get(), self.apellido_nuevo.get(), self.telefono_nuevo.get())
        self.contacto1.agendado(datos)
        mb.showinfo('Información', 'Nuevo contacto guardado')
        self.nombre_nuevo.set('')
        self.apellido_nuevo.set('')
        self.telefono_nuevo.set('')

    def buscar_por_apellido(self):
        self.pagina02 = ttk.Frame(self.cuaderno)
        self.cuaderno.add(self.pagina02, text = 'Buscar contacto')
        self.labelframe02 = ttk.LabelFrame(self.pagina02, text ='Contactos')
        self.labelframe02.grid(column=0, row=0, padx=10, pady=10)

        self.label01 = ttk.Label(self.labelframe02, text= 'Apellido')
        self.label01.grid(column=0, row=0, padx=3, pady=5)
        self.apellido = tk.StringVar()
        self.entry_apellido = ttk.Entry(self.labelframe02, textvariable=self.apellido, width=25)
        self.entry_apellido.grid(column=1, row=0, padx=3, pady=5)
        
        self.scrolledtext01 =st.ScrolledText(self.labelframe02)
        self.scrolledtext01.grid(column=3, row=1,padx=10, pady=10)

        self.boton02 = ttk.Button(self.labelframe02, text='Consultar', command=self.busqueda)
        self.boton02.grid(column=3, row=0, padx=10, pady=10)

    def busqueda(self):
        datos = (self.apellido.get(), )
        respuesta = self.contacto1.consulta(datos)
        self.scrolledtext01.delete('1.0',tk.END)
        if len(respuesta) > 0:
            for fila in respuesta:
                self.scrolledtext01.insert(tk.END, 'Apellido:'+ str(fila[2]) + '\nNombre:' + str(fila[1]) + '\nTeléfono:' + str(fila[3])+ '\n\n-----\n\n')
        else:
            self.apellido.set('')
            mb.showinfo('Información', 'No se encontró')

    def agenda_completa(self):
        self.pagina03 = ttk.Frame(self.cuaderno)
        self.cuaderno.add(self.pagina03, text = 'Lista de contactos')
        self.labelframe03 = ttk.LabelFrame(self.pagina03, text ='Contactos')
        self.labelframe03.grid(column=0, row=0, padx=10, pady=10)

        self.boton03 = ttk.Button(self.labelframe03, text='Mostrar', command=self.lista)
        self.boton03.grid(column=0, row=0, padx=10, pady=10)

        self.scrolledtext02 = st.ScrolledText(self.labelframe03, width=75, heigh=25)
        self.scrolledtext02.grid(column=0, row=1, padx=10, pady=10)


    def lista(self):
        respuesta = self.contacto1.agenda_completa()
        self.scrolledtext02.delete('1.0', tk.END)
        for fila in respuesta:
            self.scrolledtext02.insert(tk.END, 'Apellido:'+ str(fila[1]) + '\nNombre:' + str(fila[0]) + '\nTeléfono:' + str(fila[2])+ '\n-*-*-*-*-*-\n')

    


agenda_incial = Agenda_Contactos()