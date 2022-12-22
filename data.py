import pandas as pd
import os
import cv2

def data_frame(data_frame: pd.DataFrame, directory_obj: str, name: str):
    data = os.listdir(directory_obj)

    if data_frame.empty:
        count = 0
    else:
        data_list = data_frame["Class"].tolist()
        data_list = list(set(data_list))
        count = len(data_list)

    for i in data:
        path = f"{directory_obj}\{i}"
        data_frame2 = pd.DataFrame({"Class": name, "path": [path], "tag": count})
        data_frame = pd.concat([data_frame, data_frame2], ignore_index = True)

    print(data_frame)
    return data_frame




def main():
    """Separates code blocks."""
    df = pd.DataFrame()

    df = data_frame(df, "D:\Lab Python\Lab_1\dataset\ rose", "rose")
    df = data_frame(df, "D:\Lab Python\Lab_1\dataset\ tulip", "tulip")



if __name__ == "__main__":
	main()

 # D:\Lab Python\Lab_1\dataset\ rose
 # D:\Lab Python\Lab_1\dataset\ tulip