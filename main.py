# Recreate the plot with Russian labels and make requested adjustments
plt.figure(figsize=(8, 6))

# Plot data
plt.plot(df['N'], df['N^2'], label='N^2', marker='s', color='blue')
plt.plot(df['N'], df['N*log2N'], label='N*log2N', marker='d', color='orange')
plt.plot(df['N'], df['qsort'], label='qsort', marker='v', color='yellow')
plt.plot(df['N'], df['sortS'], label='sortS', marker='^', color='green')

# Set logarithmic scale for Y-axis
plt.yscale('log')

# Add labels and title in Russian
plt.xlabel('')
plt.ylabel('')
plt.title('Логарифмическая шкала по оси Y')

# Move the label for N to the top
plt.xticks(ticks=df['N'], labels=[f'{n}' if n != 5000 else f'N={n}' for n in df['N']])

# Add a legend in Russian
plt.legend()

# Show grid
plt.grid(True)

# Save and display the plot
output_image_path = "/mnt/data/sorting_graph_russian.png"
plt.savefig(output_image_path)

output_image_path
