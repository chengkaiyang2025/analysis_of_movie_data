import os
import gzip
import shutil


def unzip_gz_files(folder_path):
    # 遍历指定文件夹中的所有文件
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.gz'):
                file_path = os.path.join(root, file)
                # 构建解压后的文件路径，去掉 .gz 后缀
                output_file_path = os.path.splitext(file_path)[0]
                try:
                    # 打开 gz 文件进行读取
                    with gzip.open(file_path, 'rb') as f_in:
                        # 打开解压后的文件进行写入
                        with open(output_file_path, 'wb') as f_out:
                            # 将 gz 文件内容复制到解压后的文件
                            shutil.copyfileobj(f_in, f_out)
                    print(f"Successfully unzipped {file_path} to {output_file_path}")
                except Exception as e:
                    print(f"Error unzipping {file_path}: {e}")


if __name__ == "__main__":
    # 指定包含 gz 文件的文件夹路径
    folder_path = 'D:/GITHUB/analysis_of_movie_data/data/imdb'
    unzip_gz_files(folder_path)
