import streamlit as st
import random

st.subheader("Ejercicio 1: Saludo simple")
saludo = st.text_input("Escribe tu nombre aqui 👇", )
if saludo.strip() != "":
    st.write(f"¡Hola, {saludo}!")


# st.subheader
st.divider()

st.subheader("Ejercicio 2: Calculadora de producto")
num1= st.number_input("Escribe el primer numero", step=1, placeholder="Digita un numero aqui")
num2= st.number_input("Escribe el segundo numero", step=1, placeholder="Digita otro numero aqui")

st.write(num1 * num2)
if num1 > 100 or num2 > 100:
    st.warning("Números grandes.")

st.divider()
st.subheader("Ejercicio 3: Convertidor de Temperatura (Radio Buttons)")

seleccion = st.radio(
    "Selecciona tu tipo de conversion:",
    [":blue[Celsius a Fahrenheit]",":red[Fahrenheit a Celsius]"],
    index=None,
    )

temperatura = st.number_input("Ingrese la temperatura en números", step=1, placeholder="Digita un numero aqui")

celcius = 0
farenheit = 0

if seleccion == ":blue[Celsius a Fahrenheit]":
    resultado = (temperatura * 9/5) + 32
    st.write("Resultado: ", resultado, "°F")
elif seleccion == ":red[Fahrenheit a Celsius]":
    resultado = (temperatura - 32) * 5/9
    st.write("Resultado: ", resultado, "°C")



st.divider()
st.subheader("Ejercicio 4: Galeria de mascotas (Tabs)")

tab1, tab2, tab3 = st.tabs(["Gatos", "Perros", "Aves"])

with tab1:
    st.header("Meow!")
    st.image("img/gatos.jpg")
    if st.button("Me gusta", key="btn_gatos"):
        st.toast("Te gusta estos gatos", icon="👍")
with tab2:
    st.header("Guaf!")
    st.image("img/perros.png")
    if st.button("Me gusta", key="btn_perros"):
        st.toast("Te gusta estos perros", icon="👍")
with tab3:
    st.header("Cruk!")
    st.image("img/aves.avif")
    if st.button("Me gusta", key="btn_aves"):
        st.toast("Te gusta estos loros", icon="👍")


st.divider()
st.subheader("Ejercicio 5: Caja de comentarios (Formulario)")

with st.form("formulario"):
    asunto = st.text_input("Asunto")
    texto = st.text_area("Escriba su mensaje")
    boton = st.form_submit_button("Enviar")

    if boton:
        if texto.strip() != "":
            st.write(f"**Asunto:** {asunto} \n\n **Mensaje:** {texto}"
            )
        #elif asunto.strip()  == "":
            #st.error("El asunto no puede ir vacio")
        elif texto.strip()  == "":
            st.error("El texto no puede ir vacio")
            

st.divider()
st.subheader("Ejercicio 6: Login Simulado (Session State)")


if 'login' not in st.session_state:
    st.session_state.login = False

if not st.session_state.login:
    usuario = st.text_input("Ingrese el usuario")
    contrasena = st.text_input("Ingrese la contraseña", type="password")

    if st.button("Ingresar"):
        if usuario == "admin" and contrasena == "1234":
            st.session_state.login = True
            st.session_state.usuario = usuario
            st.success("Sesión iniciada correctamente!")
            st.rerun()
        else:
            st.error("Los credenciales son inválidos")

else:
    st.write(f'Bienvenido {st.session_state.usuario}')
    if st.button("Cerrar sesion"):
        st.session_state.login = False
        st.rerun()


st.divider()
st.subheader("Ejercicio 7: Lista de compras (Session State)")

agregar = st.text_input("Ingrese un producto", key= 'input_productos')

mensaje = ('Lista vacia')
if 'productos' not in st.session_state:
    st.session_state.productos = []


if st.button('Agregar'):
    st.session_state.productos.append(agregar)
    st.success(f'Nuevo producto agregado:  {agregar}')
    st.write("Productos agregados: ")

if st.button('Limpiar Lista'):
    st.session_state.productos = []
if not st.session_state.productos:
    st.info(mensaje)
for i, producto in enumerate(st.session_state.productos):
    st.write(f'{i+1}. {producto}')


# if not st.session_state.productos:
#     st.info(mensaje)
    



st.divider()
st.subheader('Ejercicio 8: Gráfico interactivo')

rango = st.slider('Desliza para enumerar',10,100,10)

numeros_aleatorios = [random.randint(0,1000) for _ in range(rango)]

st.write('Los numeros son: ')
for i, num in enumerate(numeros_aleatorios, start=1):
    st.write(f"{i}. {num}")

st.line_chart(numeros_aleatorios)
st.button("Regenerar")