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


def dimension(data_frame: pd.DataFrame):
    width_list = []
    height_list = []
    channels_list = []

    for i in data_frame.path:
        img = cv2.imread(i)
        width_list.append(img.shape[0])
        height_list.append(img.shape[1])
        channels_list.append(img.shape[2])

    data_frame["width"] = pd.Series(width_list)
    data_frame["height"] = pd.Series(height_list)
    data_frame["channels"] = pd.Series(channels_list)

    print(data_frame)
    return data_frame


def stat(data_frame: pd.DataFrame):
    print(data_frame.describe())
    if data_frame.tag.mean() == 0.5:
        print("Набор является сбалансированным\n")
    else:
        print("Набор не является сбалансированным\n"")

        def new_data_frame(data_frame: pd.DataFrame, class_tag: int):
            data_frame2 = pd.DataFrame()
            data_frame2 = data_frame[data_frame.tag == class_tag]
            print(data_frame2)
            return data_frame2


def main():
    """Separates code blocks."""
    df = pd.DataFrame()

    df = data_frame(df, "D:\Lab Python\Lab_1\dataset\ rose", "rose")
    df = data_frame(df, "D:\Lab Python\Lab_1\dataset\ tulip", "tulip")

    df = dimension(df)

    stat(df)

    df2 = pd.DataFrame()
    df2 = new_data_frame(df, 5)



if __name__ == "__main__":
	main()

 # D:\Lab Python\Lab_1\dataset\ rose
 # D:\Lab Python\Lab_1\dataset\ tulip