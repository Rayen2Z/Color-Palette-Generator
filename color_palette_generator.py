import numpy as np
from PIL import Image
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler


def read_image(img_path):
    img = Image.open(img_path)
    max_size = (800, 800)
    img.thumbnail(max_size, Image.Resampling.LANCZOS)
    return img


def get_top_10_colors(img):
    pixels = np.array(img).reshape(-1, 3)
    scaler = StandardScaler()
    pixels_scaled = scaler.fit_transform(pixels)
    kmeans = KMeans(n_clusters=10, init='k-means++', n_init=10, random_state=42)
    kmeans.fit(pixels_scaled)
    colors = scaler.inverse_transform(kmeans.cluster_centers_)
    colors = colors.round(0).astype(int)
    return colors


def get_top_5_colors(colors):
    from scipy.spatial.distance import pdist, squareform
    dist_matrix = squareform(pdist(colors))
    selected_colors = []
    for _ in range(5):
        if not selected_colors:
            selected_colors.append(np.argmax(np.min(dist_matrix, axis=0)))
        else:
            remaining_colors = np.delete(np.arange(10), selected_colors)
            min_distances = np.min(dist_matrix[np.ix_(remaining_colors, selected_colors)], axis=1)
            selected_colors.append(remaining_colors[np.argmax(min_distances)])
    selected_colors = colors[selected_colors]
    return selected_colors


def plot_top_10_colors(colors):
    fig, ax = plt.subplots(1, 1, figsize=(5, 2), subplot_kw=dict(xticks=[], yticks=[], frame_on=False))
    for sp in ax.spines.values():
        sp.set_visible(False)
    plt.imshow([colors.astype(int)], aspect='equal')
    plt.show()


def plot_top_5_colours(selected_colors):
    fig, ax = plt.subplots(1, 1, figsize=(5, 2), subplot_kw=dict(xticks=[], yticks=[], frame_on=False))
    for sp in ax.spines.values():
        sp.set_visible(False)
    plt.imshow([selected_colors.astype(int)], aspect='auto')
    plt.show()


def plot_img_plus_color_palette(img, selected_colors):
    fig = plt.figure(figsize=(10, 10), dpi=80)
    grid = plt.GridSpec(5, 1, hspace=0)
    plt.subplots_adjust(left=0, bottom=0, right=1, top=1, wspace=0, hspace=0)
    axs0 = fig.add_subplot(grid[:4, :])
    axs0.imshow(img, aspect='equal')
    axs0.axis('off')
    axs1 = fig.add_subplot(grid[4, :])
    axs1.imshow([selected_colors.astype(int)], aspect='auto')
    axs1.axis('off')
    return fig
