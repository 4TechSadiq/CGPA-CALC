import pandas as pd
from PIL import Image
from image_processing import get_mark

# image = Image.open("test8.jpg")
# data_frame = get_mark(image)

def cgpa(data: pd.DataFrame):
    cred_x_mark = 0
    cred_t = 0
    try:
        for i in range(1, len(data)):
            try:
                cred = int(data.iloc[i][1])
                mark = float(data.iloc[i][2])
            except ValueError:
                # Skip rows with non-numeric credit or GP
                continue
            cred_t += cred
            cred_x_mark += cred * mark
        cgpa = cred_x_mark / cred_t if cred_t != 0 else 0
        print(cgpa)
        return cgpa
    except Exception as e:
        return f"Error: {str(e)}"

