import streamlit as st

st.set_page_config(page_title="Estado de Sesión", page_icon="🧠")

st.markdown("# Estado de Sesión (Session State)")
st.sidebar.header("Estado de Sesión")

st.write(
    """
    Streamlit ejecuta todo el script de Python cada vez que interactúas con un widget.
    Esto significa que las variables se reinician. `st.session_state` soluciona esto permitiendo persistir datos entre ejecuciones.
    """
)

st.header("1. El problema")
st.write("Intenta incrementar este contador. Verás que si interactúas con otro botón (como el de abajo), el valor puede perderse si no se guarda.")

count = 0
increment = st.button('Incrementar Contador Simple')
if increment:
    count += 1

st.write('Contador simple = ', count)

st.divider()

st.header("2. La solución: Session State")
st.write("Este contador usa `st.session_state` para recordar su valor.")

# Inicializar el estado si no existe
if 'contador_real' not in st.session_state:  
    st.session_state.contador_real = 0

def incrementar_contador():
    st.session_state.contador_real += 1

st.button('Incrementar Contador Real', on_click=incrementar_contador)

st.write('Contador Real = ', st.session_state.contador_real)
st.write(f"Valor en session_state: {st.session_state.contador_real}")

st.divider()

st.header("3. Ejercicio: Lista de tareas")
st.write("Escribe una tarea y presiona Enter para agregarla a la lista.")

if 'tareas' not in st.session_state:
    st.session_state.tareas = []

nueva_tarea = st.text_input("Nueva tarea", key="input_tarea")

if st.button("Agregar tarea") and nueva_tarea:
    st.session_state.tareas.append(nueva_tarea)
    st.success(f"Tarea '*{nueva_tarea}*' agregada!")

st.write("### Tus Tareas:")
for i, tarea in enumerate(st.session_state.tareas):
    st.write(f"{i + 1}. {tarea}")

if st.button("Limpiar lista"):
    st.session_state.tareas = []
    st.rerun()
