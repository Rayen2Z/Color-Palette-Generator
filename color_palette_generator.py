import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from skimage.color import rgb2lab, lab2rgb

def read_image(img_path):
    img = Image.open(img_path)
    max_size = (800, 800)
    img.thumbnail(max_size, Image.Resampling.LANCZOS)
    return img

def get_colors(img, n_colors):
    pixels = np.array(img).reshape(-1, 3)
    unique_pixels, counts = np.unique(pixels, return_counts=True, axis=0)
    n_colors = min(n_colors, len(unique_pixels))

    if n_colors == len(unique_pixels):
        return unique_pixels

    unique_pixels = rgb2lab(unique_pixels.reshape(1, -1, 3)).reshape(-1, 3)
    kmeans = KMeans(n_clusters=n_colors, init='k-means++', n_init=10, random_state=42)
    kmeans.fit(unique_pixels, sample_weight=counts)
    colors = kmeans.cluster_centers_
    colors = lab2rgb(colors.reshape(1, -1, 3)).reshape(-1, 3) * 255
    colors = colors.round(0).astype(int)
    return colors

def plot_colors(colors, title):
    fig, ax = plt.subplots(1, 1, figsize=(5, 2), subplot_kw=dict(xticks=[], yticks=[], frame_on=False))
    for sp in ax.spines.values():
        sp.set_visible(False)
    plt.imshow([colors], aspect='equal')
    plt.title(title)
    plt.show()

def plot_img_plus_color_palette(img, colors):
    fig = plt.figure(figsize=(10, 10), dpi=80)
    grid = plt.GridSpec(5, 1, hspace=0)
    plt.subplots_adjust(left=0, bottom=0, right=1, top=1, wspace=0, hspace=0)
    axs0 = fig.add_subplot(grid[:4, :])
    axs0.imshow(img, aspect='equal')
    axs0.axis('off')
    axs1 = fig.add_subplot(grid[4, :])
    axs1.imshow([colors], aspect='auto')
    axs1.axis('off')
    return fig, (axs0, axs1)

