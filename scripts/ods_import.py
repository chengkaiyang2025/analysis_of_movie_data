import gzip
import logging
import os
import shutil
import mysql.connector

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
)


class OdsImport:
    table_mapping = {
        'name.basics.tsv': 'ods.ods_imdb_name_basics',
        # 'title.akas.tsv': 'ods.ods_imdb_akas',
        'title.basics.tsv': 'ods.ods_imdb_bas ics',
        'title.crew.tsv': 'ods.ods_imdb_crew',
        'title.episode.tsv': 'ods.ods_imdb_episode',
        'title.ratings.tsv': 'ods.ods_imdb_rating',
    }
    work_path = 'D:/GITHUB/analysis_of_movie_data/data/imdb/gz'
    tsv_path = os.path.join(work_path, 'tsv')
    cnx = mysql.connector.connect(user='root', password='',
                                  host='127.0.0.1',
                                  database='ods')

    # cnx.close()

    def __step_010_init_ods_database(self):
        cursor = self.cnx.cursor()
        try:
            sql_file_path = 'D:/GITHUB/analysis_of_movie_data/code/ods_ddl.sql'
            with open(sql_file_path, 'r', encoding='utf-8') as sql_file:
                sql_content = sql_file.read()
                # 按分号分割 SQL 语句
                statements = sql_content.split(';')
                for statement in statements:
                    if statement.strip():
                        try:
                            cursor.execute(statement)
                            self.cnx.commit()
                            logging.info(f"Successfully executed SQL statement: {statement.strip()[:50]}...")
                        except mysql.connector.Error as err:
                            logging.error(f"Error executing SQL statement: {statement.strip()[:50]}... Error: {err}")
        except Exception as e:
            logging.error(f"Error reading or executing SQL file: {e}")
        finally:
            cursor.close()

    def __step_050_download_from_web(self):
        pass

    def __step_075_ungz(self):
        if not os.path.exists(self.tsv_path):
            os.makedirs(self.tsv_path)
        for root, dirs, files in os.walk(self.work_path):
            for file in files:
                if file.endswith('.gz'):
                    file_path = os.path.join(root, file)
                    # 构建解压后的文件路径，去掉 .gz 后缀
                    output_filename = os.path.splitext(file)[0]
                    output_file_path = os.path.join(self.tsv_path, output_filename)
                    try:
                        # 打开 gz 文件进行读取
                        with gzip.open(file_path, 'rb') as f_in:
                            # 打开解压后的文件进行写入
                            with open(output_file_path, 'wb') as f_out:
                                # 将 gz 文件内容复制到解压后的文件
                                shutil.copyfileobj(f_in, f_out)
                        logging.info(f"Successfully unzipped {file_path} to {output_file_path}")
                    except Exception as e:
                        logging.error(f"Error unzipping {file_path}: {e}")

    def __step_100_import(self):
        cursor = self.cnx.cursor()
        batch_size = 20000
        try:
            # 遍历指定目录下的所有文件
            for filename in os.listdir(self.tsv_path):
                if filename.endswith('.tsv'):
                    file_path = os.path.join(self.tsv_path, filename)
                    if filename in self.table_mapping:
                        table_name = self.table_mapping[filename]
                        try:
                            with open(file_path, 'r', encoding='utf-8') as f:
                                headers = f.readline().strip().split('\t')
                                data_batch = []
                                for line in f:
                                    values = line.strip().split('\t')
                                    data_batch.append(values)
                                    if len(data_batch) == batch_size:
                                        placeholders = ', '.join(['%s'] * len(headers))
                                        insert_query = f"INSERT INTO {table_name} ({', '.join(headers)}) VALUES ({placeholders})"
                                        try:
                                            cursor.executemany(insert_query, data_batch)
                                            self.cnx.commit()
                                            logging.info(
                                                f"Successfully imported a batch of {batch_size} rows from {filename} into {table_name}")
                                        except mysql.connector.Error as err:
                                            logging.error(
                                                f"Error importing a batch from {filename} into {table_name}: {err}. Skipping this batch.")
                                            self.cnx.rollback()
                                        data_batch = []
                                if data_batch:
                                    placeholders = ', '.join(['%s'] * len(headers))
                                    insert_query = f"INSERT INTO {table_name} ({', '.join(headers)}) VALUES ({placeholders})"
                                    try:
                                        cursor.executemany(insert_query, data_batch)
                                        self.cnx.commit()
                                        logging.info(
                                            f"Successfully imported the remaining {len(data_batch)} rows from {filename} into {table_name}")
                                    except mysql.connector.Error as err:
                                        logging.error(
                                            f"Error importing the remaining data from {filename} into {table_name}: {err}. Skipping this batch.")
                                        self.cnx.rollback()
                        except Exception as e:
                            logging.error(f"Error importing {filename} into {table_name}: {e}")
        except Exception as e:
            logging.error(f"An error occurred: {e}")
        finally:
            # 关闭游标和数据库连接
            cursor.close()

    def run(self):
        self.__step_010_init_ods_database()
        # self.__step_075_ungz()
        self.__step_100_import()
        pass

if __name__ == '__main__':
    ODS = OdsImport()
    ODS.run()
