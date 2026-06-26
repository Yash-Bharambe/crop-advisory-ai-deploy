import os
import random
import shutil
from tqdm import tqdm


# ===============================
# PATHS
# ===============================

SOURCE_TRAIN = "datasets/ip102/classification/train"
SOURCE_VAL = "datasets/ip102/classification/val"

OUTPUT = "datasets/ip102_balanced"

TRAIN_OUT = os.path.join(OUTPUT, "train")
VAL_OUT = os.path.join(OUTPUT, "val")


# ===============================
# SETTINGS
# ===============================

MAX_IMAGES_PER_CLASS = 300

random.seed(42)


# ===============================
# CREATE FOLDERS
# ===============================

os.makedirs(TRAIN_OUT, exist_ok=True)
os.makedirs(VAL_OUT, exist_ok=True)


# ===============================
# BALANCE FUNCTION
# ===============================

def balance_dataset(source, destination):

    classes = sorted(os.listdir(source))

    print("Classes found:", len(classes))


    for cls in tqdm(classes):

        class_path = os.path.join(source, cls)

        if not os.path.isdir(class_path):
            continue


        images = [
            f for f in os.listdir(class_path)
            if f.lower().endswith(
                (".jpg",".jpeg",".png")
            )
        ]


        print(
            f"Class {cls}: {len(images)} images"
        )


        # Keep all if already small
        if len(images) <= MAX_IMAGES_PER_CLASS:
            selected = images

        else:
            selected = random.sample(
                images,
                MAX_IMAGES_PER_CLASS
            )


        # Create output class folder

        output_class = os.path.join(
            destination,
            cls
        )

        os.makedirs(
            output_class,
            exist_ok=True
        )


        # Copy images

        for img in selected:

            src = os.path.join(
                class_path,
                img
            )

            dst = os.path.join(
                output_class,
                img
            )

            shutil.copy2(
                src,
                dst
            )


# ===============================
# RUN
# ===============================

print("\nCreating balanced TRAIN dataset")
balance_dataset(
    SOURCE_TRAIN,
    TRAIN_OUT
)


print("\nCreating balanced VALIDATION dataset")
balance_dataset(
    SOURCE_VAL,
    VAL_OUT
)


print("\nDONE!")
print(
    "Balanced dataset created at:",
    OUTPUT
)