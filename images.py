import os
import re
import shutil

# Paths
posts_dir = r"C:\Users\sehza\Documents\ThOfficialDevBlogs\content\posts"
attachments_dir = r"C:\Users\sehza\Documents\notes\Attachments"
static_images_dir = r"C:\Users\sehza\Documents\ThOfficialDevBlogs\static\images"

# Ensure destination exists
os.makedirs(static_images_dir, exist_ok=True)

# Step 1: Process each markdown file in the posts directory
for filename in os.listdir(posts_dir):
    if filename.endswith(".md"):
        filepath = os.path.join(posts_dir, filename)
        
        with open(filepath, "r", encoding="utf-8") as file:
            content = file.read()
        
        # Step 2: Find all image links [[image.png]]
        images = re.findall(r'\[\[([^]]*\.(?:png|jpg|jpeg|gif|webp))\]\]', content, flags=re.IGNORECASE)
        
        # Step 3: Replace links + copy images
        for image in images:
            markdown_image = f"![Image Description](/images/{image.replace(' ', '%20')})"
            content = content.replace(f"[[{image}]]", markdown_image)
            
            image_source = os.path.join(attachments_dir, image)
            print("Looking for:", image_source)
            
            if os.path.exists(image_source):
                shutil.copy(image_source, static_images_dir)
                print("Copied:", image_source)
            else:
                print("⚠️ Not found:", image_source)

        # Step 4: Write updated content
        with open(filepath, "w", encoding="utf-8") as file:
            file.write(content)

print("✅ Markdown files processed and images copied successfully.")
