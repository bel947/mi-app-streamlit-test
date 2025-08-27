# -*- coding: utf-8 -*-
"""
Created on Wed Aug 27 13:09:12 2025

@author: anabel.hernandez
"""

import streamlit as st
import pandas as pd

# Cargar los datos
df = pd.read_csv('ventas.csv')

# Mostrar en la web
st.title("Mi app de ventas")
st.write(df)