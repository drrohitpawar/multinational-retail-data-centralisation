import subprocess

#list of files in the data folder
file_list = ['card_data.py', 'event_data.py', 'orders_data.py', 'products_data.py', 'store_data.py', 'users_data.py']
 
if __name__ == '__main__':
  #run all the files in the data column
  for file in file_list:
    subprocess.run(['python', 'scripts/' + file])