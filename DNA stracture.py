import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.lines import Line2D  # Import Line2D explicitly

# Function to generate DNA helix coordinates
def generate_dna_helix(n_turns=2, n_points_per_turn=1000, radius=1, helix_pitch=2 * np.pi):
    t = np.linspace(0, n_turns * 2 * np.pi, n_points_per_turn * n_turns)
    x = radius * np.cos(t)
    y = radius * np.sin(t)
    z = helix_pitch * t / (2 * np.pi)
    return x, y, z

# Generate DNA helix coordinates
x, y, z = generate_dna_helix()

# Generate a random DNA sequence for one strand
dna_sequence = ''.join(np.random.choice(['A', 'T', 'G', 'C'], size=len(x)))

# Generate the complementary strand
complementary_base_pairs = {'A': 'T', 'T': 'A', 'G': 'C', 'C': 'G'}
complementary_sequence = ''.join([complementary_base_pairs[base] for base in dna_sequence])

# Define colors for base pairs
base_colors = {'A': 'blue', 'T': 'red', 'G': 'green', 'C': 'yellow'}

# Plot the DNA helix for both strands with colors and annotations
fig = plt.figure(figsize=(8, 12))  # Adjust the figure size here
ax = fig.add_subplot(111, projection='3d')

# Plot the phosphodiester bonds
for i in range(len(x) - 1):
    ax.plot([x[i], x[i + 1]], [y[i], y[i + 1]], [z[i], z[i + 1]], color='black')

# Plot the first strand
for i in range(len(x)):
    ax.plot([x[i], x[i]], [y[i], y[i]], [z[i], z[i] + 1], color=base_colors[dna_sequence[i]])
    ax.text(x[i], y[i], z[i] + 1, dna_sequence[i], color='black')

    # Represent double bond for AT pairs
    if dna_sequence[i] == 'A' and complementary_sequence[i] == 'T':
        ax.plot([x[i], x[i]], [y[i], y[i]], [z[i] + 1, z[i] + 2], color='black')

# Plot the second strand
for i in range(len(x)):
    ax.plot([x[i], x[i]], [y[i], y[i]], [z[i] + 2, z[i] + 3], color=base_colors[complementary_sequence[i]])
    ax.text(x[i], y[i], z[i] + 3, complementary_sequence[i], color='black')

    # Represent triple bond for GC pairs
    if dna_sequence[i] == 'G' and complementary_sequence[i] == 'C':
        ax.plot([x[i], x[i]], [y[i], y[i]], [z[i] + 3, z[i] + 4], color='black')

# Create a custom legend
legend_elements = [Line2D([0], [0], marker='o', color='w', label='A',
                          markerfacecolor='blue', markersize=10),
                   Line2D([0], [0], marker='o', color='w', label='T',
                          markerfacecolor='red', markersize=10),
                   Line2D([0], [0], marker='o', color='w', label='G',
                          markerfacecolor='green', markersize=10),
                   Line2D([0], [0], marker='o', color='w', label='C',
                          markerfacecolor='yellow', markersize=10)]

# Add legend to the plot
ax.legend(handles=legend_elements, loc='upper right', title='Base Pairs')

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Double Helix Structure of DNA with Base Pair Annotations and Bonds')
plt.show()
