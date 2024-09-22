import streamlit as st
import pandas as pd
import numpy as np
from pathlib import Path
import matplotlib.pyplot as plt

st.title("Bike counters")

DATE_COLUMN = "date"


@st.cache_data
def load_data():
    data = pd.read_parquet(Path("data") / "train.parquet")
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis="columns", inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data


data_load_state = st.text("Loading data...")
data = load_data()
data_load_state.text("Done! (using st.cache_data)")

if st.checkbox("Show raw data"):
    st.subheader("Raw data")
    st.write(data)

st.subheader("Bike count a Sebastopol")
# Appliquer le filtre pour le graphique
mask = (
    (data["counter_name"] == "Totem 73 boulevard de Sébastopol S-N")
    & (data["date"] > pd.to_datetime("2021/03/01"))
    & (data["date"] < pd.to_datetime("2021/03/08"))
)

# Créer le graphique
fig, ax = plt.subplots(figsize=(10, 4))
data[mask].plot(x="date", y="bike_count", ax=ax)
ax.set_title("Comptage de vélos du 73 boulevard de Sébastopol (1-8 mars 2021)")
ax.set_xlabel("Date")
ax.set_ylabel("Nombre de vélos")

# Afficher le graphique dans Streamlit
st.pyplot(fig)
