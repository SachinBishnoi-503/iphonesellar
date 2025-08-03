import os
import re
import csv

# Path to your price list CSV
PRICE_CSV = "product_price_updates_cleaned.csv"

# Folders containing HTML files
FOLDERS = ["bsb/product", "bsb/category"]  # Adjust if needed

# Load MRP → New Price map
price_map = {}
with open(PRICE_CSV, newline='', encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        mrp = row["product_mrp"].strip().replace("₹", "")
        sale = row["new_selling_price"].strip().replace("₹", "")
        price_map[mrp] = sale

# Function to process each HTML file
def update_prices_in_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    changed = False

    for mrp, new_sale in price_map.items():
        # Match the MRP and sale price, allowing spaces/newlines between spans
        pattern = rf'(<span class="mrp-price line-through">₹{mrp.rstrip("0").rstrip(".")}(?:\.00)?</span>\s*<span class="sell-price">)₹[\d.,]+(</span>)'
        new_content, count = re.subn(pattern, rf'\1₹{new_sale}\2', content)

        if count > 0:
            content = new_content
            changed = True

    # Save if any changes were made
    if changed:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"✅ Updated: {file_path}")

# Walk through all HTML files in target folders
for folder in FOLDERS:
    for root, _, files in os.walk(folder):
        for file in files:
            if file.endswith(".html"):
                update_prices_in_file(os.path.join(root, file))

