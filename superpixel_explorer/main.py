from skimage.io import imread
from skimage.segmentation import slic, mark_boundaries
import streamlit as st


n_segments = st.sidebar.slider("Number of Segments", min_value=1, max_value=300, value=100)
compactness = st.sidebar.slider("Compactness", min_value=1, max_value=100, value=10)
files = st.sidebar.file_uploader("Image", accept_multiple_files=True)

for file in files:
    image = imread(file)
    segments = slic(image, n_segments=n_segments, compactness=compactness, start_label=0)
    st.image(mark_boundaries(image, segments))
