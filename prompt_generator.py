import random
import os

def generate_random_prompt():
    """
    Function to generate a random prompt
    """
    # Define categories and prompts
    categories = ["Turn", "Create", "Apply", "Make", "Generate", "Transform"]
    actions = ["a photo", "an image", "a picture"]
    effects = ["into a painting", "into a sketch", "from daytime to nighttime",
               "with a vintage filter", "like a watercolor painting", "into a mosaic",
               "into an abstract interpretation", "with a comic book style",
               "into pixel art", "into a stained glass design", "with a surreal effect",
               "into a pencil drawing", "with a futuristic filter"]
    
    # Generate a random prompt
    prompt = f"{random.choice(categories)} {random.choice(actions)} {random.choice(effects)}"
    return prompt

# Generate a random prompt for each image in the image_data directory and store in style_prompt directory
image_dir = './image_data'
image_paths = [f'{image_dir}/{image}' for image in os.listdir(image_dir)]

for image_path in image_paths:
    prompt = generate_random_prompt()
    with open(f'style_prompt/{os.path.basename(image_path).split(".")[0]}.txt', 'w') as f:
        f.write(prompt)
        print(f"Generated prompt for {os.path.basename(image_path)}: {prompt}")