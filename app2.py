import streamlit as st
import pandas as pd

df_reviews = pd.read_csv("datasets/customer reviews.csv")
df_top100books = pd.read_csv("datasets/Top-100 Trending Books.csv")

df_reviews
