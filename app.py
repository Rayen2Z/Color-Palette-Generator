import streamlit as st
from PIL import Image

import color_palette_generator as cpg


def app():
    st.title('Color Palette Generator')
    uploaded_file = st.file_uploader("Choose an image...", type=['jpg', 'png'])

    if uploaded_file is not None:
        try:
            img = Image.open(uploaded_file)
            # if img.size[0] < 800 or img.size[1] < 800:
            #     st.error('Image size must be at least 800x800 pixels.')
            #     return

            st.image(img, caption='Uploaded Image.', use_column_width=True)

            # Generate color palette
            selected_colors = cpg.get_top_5_colors(cpg.get_top_10_colors(img))

            # Plot image and color palette
            fig = cpg.plot_img_plus_color_palette(img, selected_colors)

            # Display the figure
            st.pyplot(fig)
        except:
            st.error('Invalid image file. Please upload a jpg or png file.')


if __name__ == '__main__':
    app()
