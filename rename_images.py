import os
import shutil

base_dir = r"d:\Website\Diamondpearlhotel\img\rooms"

# The mapping from create_pages.py
room_mappings = [
    {
        "id": "studioking",
        "old_folder": "studioking-5Pic",
        "images": {
            "studioking-bed.jpg": "thumbnail.jpg",
            "studioking-bed-2.jpg": "gallery-1.jpg",
            "studioking-bed-TV.jpg": "gallery-2.jpg",
            "studioking-bathroom.jpg": "gallery-3.jpg"
        }
    },
    {
        "id": "deluxeking",
        "old_folder": "deluxeking-4Pic",
        "images": {
            "deluxeking-bed.jpg": "thumbnail.jpg",
            "deluxeking-bed-2.jpg": "gallery-1.jpg",
            "deluxeking-tv.jpg": "gallery-2.jpg",
            "deluxeking-bathroom.jpg": "gallery-3.jpg"
        }
    },
    {
        "id": "deluxetwincityview",
        "old_folder": "deluxetwincityview-5pic",
        "images": {
            "deluxetwincityview-bed.jpg": "thumbnail.jpg",
            "deluxetwincityview-bed-2.jpg": "gallery-1.jpg",
            "deluxetwincityview-bed-3.jpg": "gallery-2.jpg",
            "deluxetwincityview-amenities.jpg": "gallery-3.jpg"
        }
    },
    {
        "id": "deluxeriverview",
        "old_folder": "deluxetwinriverview-6Pic",
        "images": {
            "deluxetwincityview-bed.jpg": "thumbnail.jpg",
            "deluxetwincityview-bed-2.jpg": "gallery-1.jpg",
            "deluxetwincityview-bed-3.jpg": "gallery-2.jpg",
            "deluxetwincityview-tv.jpg": "gallery-3.jpg"
        }
    }
]

# Step 1: Rename the folders to the new IDs
for room in room_mappings:
    old_path = os.path.join(base_dir, room['old_folder'])
    new_path = os.path.join(base_dir, room['id'])
    
    if os.path.exists(old_path):
        os.rename(old_path, new_path)
        print(f"Renamed {room['old_folder']} to {room['id']}")
    else:
        print(f"Folder {room['old_folder']} not found (maybe already renamed?)")

# Step 2: Create a copy of studioking for executivesuite if it doesn't exist
studioking_path = os.path.join(base_dir, "studioking")
executivesuite_path = os.path.join(base_dir, "executivesuite")
if os.path.exists(studioking_path) and not os.path.exists(executivesuite_path):
    shutil.copytree(studioking_path, executivesuite_path)
    print("Created executivesuite folder by copying studioking")
    # Add mapping for executivesuite so we rename its files too
    room_mappings.append({
        "id": "executivesuite",
        "old_folder": "executivesuite",
        "images": room_mappings[0]["images"] # same original names as studioking before rename
    })

# Step 3: Rename the files inside the new folders
# Note: we need to handle executivesuite which uses the original studioking image names since it was copied before files were renamed
# Actually wait, if I copy studioking BEFORE renaming its files, then the files in executivesuite still have the old names. Yes.
for room in room_mappings:
    folder_path = os.path.join(base_dir, room['id'])
    if not os.path.exists(folder_path):
        continue
        
    for old_img, new_img in room['images'].items():
        old_img_path = os.path.join(folder_path, old_img)
        new_img_path = os.path.join(folder_path, new_img)
        
        if os.path.exists(old_img_path):
            os.rename(old_img_path, new_img_path)
            print(f"Renamed {old_img} to {new_img} in {room['id']}")
        else:
            print(f"Image {old_img} not found in {room['id']}")
