import streamlit as st
from PIL import Image

import color_palette_generator as cpg

def app():
    st.title('Color Palette Generator')
    uploaded_file = st.file_uploader("Choose an image...", type=['jpg', 'png'])

    n_colors = st.slider('Number of colors in the palette', min_value=1, max_value=10, value=5)

    if uploaded_file is not None:
        try:
            img = Image.open(uploaded_file)
            st.image(img, caption='Uploaded Image.', use_column_width=True)

            # Generate color palette
            selected_colors = cpg.get_colors(img, n_colors)

            # Plot image and color palette
            fig, _ = cpg.plot_img_plus_color_palette(img, selected_colors)

            # Display the figure
            st.pyplot(fig)
        except:
            st.error('Invalid image file. Please upload a jpg or png file.')

if __name__ == '__main__':
    app()
