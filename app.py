import streamlit as st
import pandas as pd
import duckdb as db

data = {"a": [1, 2, 3], "b": [4, 5, 6]}
df = pd.DataFrame(data)
st.dataframe(df)

q = st.text_area(label="Rentrer la query que vous souhaitez exécuter sachant que la table master ci-dessus est intitulée 'df':"
                 ,value="SELECT * FROM df"
                 )
st.write(f"Voici la requête renseignée : {q}")

df_query = db.sql(str(q)).df()
st.dataframe(df_query)
