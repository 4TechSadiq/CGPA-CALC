from PIL import Image
import pytesseract
import pandas as pd

MY_CONFIG = r"--psm 6 --oem 3"

def get_mark(img):
    data = pytesseract.image_to_string(img,config=MY_CONFIG)
    split_list = data.split("\n")
    data_list = [split_list[i].split(" ") for i in range(0,len(split_list))]
    
    course_codes = [row[1] for row in data_list if len(row)>1]
    credit = [row[-4] for row in data_list if len(row)>1]
    gp = [row[-2] for row in data_list if len(row)>1]

    mark_dict = {
        "c_code": course_codes,
        "credit": credit,
        "gp": gp
    }

    mark_data = pd.DataFrame(mark_dict)
    return mark_data

# i = Image.open("test8.jpg")
# print(get_mark(img=i))