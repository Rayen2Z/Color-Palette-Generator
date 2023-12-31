# 🎨 Color Palette Generator 🎨

This project implements a simple color palette generator using machine learning techniques and serves as a perfect opportunity to explore and test the capabilities of Streamlit, an interactive web application framework for Python. 

The objective of this project is to leverage Streamlit's features and functionalities to create a user-friendly web interface for generating visually appealing color palettes. You can try it [here](https://color-palette-generator-rt.streamlit.app/).

The color palette generator uses a KMeans clustering algorithm to identify the most dominant colors in an image. The image is first resized to a standard size to reduce computation time, and then the RGB values of each pixel are extracted and flattened into a 2D array. This array is then fed into the KMeans algorithm, which partitions the pixels into clusters based on their color similarity. The centroids of these clusters represent the dominant colors in the image and are used to generate the color palette.

By deploying the machine learning model on Streamlit, users can easily experiment with different input images, explore the generated palettes, and experience the seamless interactivity provided by Streamlit. 

This project showcases the integration of machine learning and web development, making it an ideal playground to test and explore the potential of Streamlit in real-world applications.

## Future Updates
I am currently working on expanding the capabilities of the color palette generator to accept video inputs. This will allow users to generate color palettes based on the dominant colors in a video, providing a unique and dynamic way to explore color schemes.

In addition, I am also focusing on enhancing the user experience of the Streamlit app. I am exploring different ways to make the interface more intuitive and user-friendly, and am open to feedback and suggestions.

## Examples : 

&nbsp;  
![téléchargement](https://github.com/Rayen2Z/Color-Palette-Generator/assets/93148057/3bb44840-f3a4-44d7-8aac-7c64d31a3de5)
&nbsp;  

&nbsp;  
![output](https://github.com/Rayen2Z/Color-Palette-Generator/assets/93148057/1d858c6a-2502-4388-942d-05ba24355c7c)
&nbsp; 

&nbsp;  
![téléchargement (1)](https://github.com/Rayen2Z/Color-Palette-Generator/assets/93148057/da564eed-4c95-4f03-8948-4655bfad9cdb)
&nbsp;  
