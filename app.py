import streamlit as st
import requests
from PIL import Image
import io

# ── Configuración de página ──────────────────────────────────────────────────
st.set_page_config(
    page_title="RAWG Videogames Analytics",
    page_icon="🎮",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ── URL base de la API ───────────────────────────────────────────────────────
BASE_URL = "http://13.53.112.155:8000"  


# ── Sidebar ──────────────────────────────────────────────────────────────────
with st.sidebar:
    st.title("🎮 RAWG.analytics")
    st.caption("VIDEOGAMES INTELLIGENCE")

    seccion = st.radio(
        "Navegación",
        ["🏠 Inicio", "🎯 Predictor de Éxito", "📊 Visualizaciones", "💬 Consultas"],
        label_visibility="collapsed"
    )

    st.divider()
    st.caption("API: FastAPI + XGBoost · Gemini 2.5 Flash · PostgreSQL RDS")
    st.caption("Infra: AWS EC2 · Lambda · Secrets Manager")


# ── Página: Inicio ───────────────────────────────────────────────────────────
if seccion == "🏠 Inicio":

    st.title("Videogames Analytics")
    st.subheader("End-to-end Data Engineering & ML system · AWS · ~20.000 juegos")

    st.divider()

    col1, col2, col3, col4 = st.columns(4)
    with col1: st.metric("Juegos en BD", "~20.000")
    with col2: st.metric("Accuracy modelo", "86%")
    with col3: st.metric("Endpoints API", "4")
    with col4: st.metric("Tablas", "10")

    st.divider()

    col_a, col_b = st.columns(2)
    with col_a:
        with st.container(border=True):
            st.subheader("🎯 Predictor de Éxito")
            st.write("Introduce las características de un videojuego y el modelo XGBoost predice si será un éxito.")

        with st.container(border=True):
            st.subheader("📊 Visualizaciones")
            st.write("Haz preguntas en lenguaje natural y obtén gráficos generados automáticamente por Gemini AI.")

    with col_b:
        with st.container(border=True):
            st.subheader("💬 Consultas")
            st.write("Pregunta sobre los datos en español o inglés y obtén respuestas en lenguaje natural.")

        with st.container(border=True):
            st.subheader("⚙️ Stack técnico")
            st.write("FastAPI · XGBoost · Gemini 2.5 Flash · PostgreSQL · AWS EC2 · Lambda · Secrets Manager")


# ── Página: Predictor ────────────────────────────────────────────────────────
elif seccion == "🎯 Predictor de Éxito":

    st.header("🎯 Predictor de Éxito")
    st.write("Introduce las características del videojuego para predecir si será un éxito.")

    with st.form("predict_form"):
        col1, col2, col3 = st.columns(3)

        with col1:
            num_platforms     = st.number_input("Plataformas", min_value=1, max_value=50, value=3)
            num_stores        = st.number_input("Tiendas", min_value=1, max_value=20, value=2)
            num_genres        = st.number_input("Géneros", min_value=1, max_value=20, value=2)
            num_tags          = st.number_input("Tags", min_value=1, max_value=100, value=10)

        with col2:
            years_since_release = st.number_input("Años desde lanzamiento", min_value=0, max_value=40, value=2)
            recency_score       = st.number_input("Recency score", min_value=0, max_value=10, value=2)
            release_year        = st.number_input("Año de lanzamiento", min_value=1980, max_value=2025, value=2022)
            esrb_name           = st.selectbox("Clasificación ESRB", [
                "Everyone", "Everyone 10+", "Teen", "Mature", "Adults Only", "Rating Pending"
            ])

        with col3:
            has_multiplayer  = st.selectbox("¿Tiene multijugador?", [("Sí", 1), ("No", 0)], format_func=lambda x: x[0])
            has_singleplayer = st.selectbox("¿Tiene un jugador?",   [("Sí", 1), ("No", 0)], format_func=lambda x: x[0])
            is_indie         = st.selectbox("¿Es indie?",           [("No", 0), ("Sí", 1)], format_func=lambda x: x[0])

        submitted = st.form_submit_button("🔮 Predecir")

    if submitted:
        payload = {
            "num_platforms": num_platforms, "num_stores": num_stores,
            "num_genres": num_genres, "num_tags": num_tags,
            "years_since_release": years_since_release, "recency_score": recency_score,
            "esrb_name": esrb_name, "release_year": release_year,
            "has_multiplayer": has_multiplayer[1],
            "has_singleplayer": has_singleplayer[1],
            "is_indie": is_indie[1]
        }
        with st.spinner("Consultando el modelo..."):
            try:
                response = requests.post(f"{BASE_URL}/predict", json=payload, timeout=10)
                data = response.json()

                st.divider()
                col_res, col_prob = st.columns([1, 2])

                with col_res:
                    # st.success = caja verde, st.error = caja roja
                    if data["prediction_class"] == 1:
                        st.success(f"✦ {data['prediction']}")
                    else:
                        st.error(f"✗ {data['prediction']}")
                    st.write(f"Confianza: **{data['confidence']}**")

                with col_prob:
                    prob = data["probability_success"]
                    st.write("Probabilidad de éxito")
                    st.progress(prob)                          # barra de progreso nativa
                    st.metric("", f"{prob*100:.1f}%")

            except Exception as e:
                st.error(f"Error al conectar con la API: {e}")


# ── Página: Visualizaciones ──────────────────────────────────────────────────
elif seccion == "📊 Visualizaciones":

    st.header("📊 Visualizaciones")
    st.write("Haz una pregunta en lenguaje natural y obtén un gráfico generado automáticamente.")

    ejemplos = [
        "Top 10 géneros con más juegos",
        "Evolución de juegos lanzados por año desde 2015",
        "Plataformas más populares",
        "Rating promedio por género",
        "Top 10 stores con más juegos",
    ]

    pregunta_visual = st.selectbox("💡 Ejemplos", ["Escribe tu propia pregunta..."] + ejemplos)
    if pregunta_visual == "Escribe tu propia pregunta...":
        pregunta_visual = st.text_input("Tu pregunta:", placeholder="Top 10 géneros con más juegos")

    if st.button("📈 Generar gráfico"):
        if pregunta_visual:
            with st.spinner("Generando visualización con Gemini AI..."):
                try:
                    response = requests.get(
                        f"{BASE_URL}/ask-visual-image",
                        params={"question": pregunta_visual},
                        timeout=30
                    )
                    if response.status_code == 200:
                        img = Image.open(io.BytesIO(response.content))
                        st.image(img, use_container_width=True)
                    else:
                        st.error(f"Error {response.status_code}: {response.text}")
                except Exception as e:
                    st.error(f"Error al conectar con la API: {e}")
        else:
            st.warning("Escribe una pregunta primero.")


# ── Página: Consultas ────────────────────────────────────────────────────────
elif seccion == "💬 Consultas":

    st.header("💬 Consultas en lenguaje natural")
    st.write("Pregunta sobre los datos y obtén una respuesta en lenguaje natural.")

    ejemplos_text = [
        "¿Cuál es el juego mejor valorado?",
        "¿Cuántos juegos hay en total?",
        "¿Qué género tiene mejor rating promedio?",
        "¿Cuáles son los 5 juegos con más playtime?",
        "¿Qué desarrolladora tiene más juegos?",
    ]

    pregunta_text = st.selectbox("💡 Ejemplos", ["Escribe tu propia pregunta..."] + ejemplos_text)
    if pregunta_text == "Escribe tu propia pregunta...":
        pregunta_text = st.text_input("Tu pregunta:", placeholder="¿Cuántos juegos hay en total?")

    mostrar_sql = st.checkbox("Mostrar SQL generado", value=False)

    if st.button("🔍 Consultar"):
        if pregunta_text:
            with st.spinner("Consultando con Gemini AI..."):
                try:
                    response = requests.get(
                        f"{BASE_URL}/ask-text",
                        params={"question": pregunta_text},
                        timeout=30
                    )
                    data = response.json()
                    if response.status_code == 200:
                        # st.info = caja azul informativa
                        st.info(data.get("answer", "Sin respuesta"))

                        if mostrar_sql and data.get("sql_generated"):
                            st.caption("SQL GENERADO POR GEMINI AI")
                            st.code(data["sql_generated"], language="sql")

                        st.caption(f"Filas devueltas: {data.get('rows_count', '—')}")
                    else:
                        st.error(f"Error: {data.get('detail', 'Error desconocido')}")
                except Exception as e:
                    st.error(f"Error al conectar con la API: {e}")
        else:
            st.warning("Escribe una pregunta primero.")