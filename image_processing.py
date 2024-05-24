from PIL import Image
import pytesseract
import pandas as pd

MY_CONFIG = r"--psm 6 --oem 3"

def get_mark(img):
    data = pytesseract.image_to_string(img, config=MY_CONFIG)
    split_list = data.split("\n")
    data_list = [row.split() for row in split_list if row.strip()]
    data_list.pop(0)
    data_list.pop(0)
    course_codes = []
    credits = []
    gps = []

    for row in data_list:
        if len(row) > 4:  
            course_codes.append(row[1])
            credits.append(row[-4])
            gps.append(row[-2])
        else:
            print(f"Skipping row due to unexpected length: {row}")

    mark_dict = {
        "c_code": course_codes,
        "credit": credits,
        "gp": gps
    }

    mark_data = pd.DataFrame(mark_dict)
    return mark_data

# i = Image.open("test9.jpg")
# print(get_mark(img=i))
