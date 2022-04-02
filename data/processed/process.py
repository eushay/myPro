from read_clean_data import Process_data

def process_raw_data():
    processed_data = Process_data()
    processed_data.read_data()
    processed_data.delete_dups()
    df_columns = processed_data.get_columns()
    df = processed_data.set_index('date')
    return df

if __name__ == '__main__':
    df = process_raw_data()