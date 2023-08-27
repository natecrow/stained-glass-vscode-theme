python generate-theme-dark.py stained-glass-dark 60 0 30 90 150 210 270 330

# Remove quotes around "true" in generated themes so it becomes a boolean instead of a string
sed -i 's/\"true\"/true/g' *color-theme.json
