# import csv

# filename = "D:\\Download\\cv-corpus-13.0-2023-03-09\\vi\\other_filtered.tsv"
# counts = {}

# with open(filename,errors="ignore") as tsvfile:
#     reader = csv.DictReader(tsvfile, delimiter='\t')
#     # print(reader.)
#     for row in reader:
#         client_id = row["client_id"]
#         if client_id in counts:
#             counts[client_id] += 1
#         else:
#             counts[client_id] = 1

# for client_id, count in counts.items():
#     print(f"{client_id}: {count}")



# import csv

# filename = "D:\\Download\\cv-corpus-13.0-2023-03-09\\vi\\other.tsv"
# counts = {}

# # Create a new filename for the output TSV file
# output_filename = "D:\\Download\\cv-corpus-13.0-2023-03-09\\vi\\other_filtered_30.tsv"

# with open(filename,'r', encoding='utf8') as tsvfile:
#     reader = csv.DictReader(tsvfile, delimiter='\t')
    
#     # Create a new list to store only those rows where the count is less than or equal to 20
#     rows_to_keep = []
#     for row in reader:
#         client_id = row["client_id"]
#         if client_id in counts:
#             counts[client_id] += 1
#         else:
#             counts[client_id] = 1
        
#         # Check if the count is less than or equal to 20 and add the row to the rows_to_keep list
#         if counts[client_id] <= 30:
#             rows_to_keep.append(row)

# # Write only the rows in the rows_to_keep list to the output TSV file
# with open(output_filename, mode='w', newline='', encoding='utf8') as tsvfile:
#     writer = csv.DictWriter(tsvfile, delimiter='\t', fieldnames=reader.fieldnames)
#     writer.writeheader()
#     for row in rows_to_keep:
#         writer.writerow(row)






# import os
# # import shutil
# import csv
# from pydub import AudioSegment
# from pydub.utils import mediainfo
# filename = "D:\\Download\\cv-corpus-13.0-2023-03-09\\vi\\other_filtered_30.tsv"
# # counts = {}

# output_folder="D:\\Download\\cv-corpus-13.0-2023-03-09\\vi\\wavs"
# # Create a new filename for the output TSV file
# # output_filename = "D:\\Download\\cv-corpus-13.0-2023-03-09\\vi\\other_filtered_30.tsv"

# with open(filename,'r', encoding='utf8') as tsvfile:
#     reader = csv.DictReader(tsvfile, delimiter='\t')
    
#     # Create a new list to store only those rows where the count is less than or equal to 20
#     # rows_to_keep = []
#     for row in reader:
#         input_file = row["path"]
#         mp3_file = AudioSegment.from_file('D:\\Download\\cv-corpus-13.0-2023-03-09\\vi\\clips\\'+input_file, format="mp3")


#         channels = mp3_file.channels
#         sample_width = mp3_file.sample_width
#         frame_rate = mp3_file.frame_rate # Set the frame rate to 16000 Hz to match the 64 kbps bitrate



#         base_name, ext = os.path.splitext(input_file)
#         new_file_name = base_name + ".wav"
#         output_file = os.path.join(output_folder, new_file_name)
#         wav_file = mp3_file.set_frame_rate(8000).set_channels(channels).set_sample_width(sample_width)

#         wav_file.export(output_file, format="wav")




# import shutil
# import csv
# import re
# import string

# # def normalize_text(text):
# #         # Remove extra whitespaces
# #     text = re.sub(r'\s+', ' ', text).strip()
# #     # Remove all punctuation marks
# #     punctuation = string.punctuation + "“”‘’"
# #     text = text.translate(str.maketrans("", "", punctuation))
    
# #     return text
# # Open the file for reading
# with open('D:\\Download\\vivos\\test\\prompts.txt', 'r', encoding='utf8') as f:
#     # i=0
#     # Read each line in the file
#     with open('D:\\Download\\cv-corpus-13.0-2023-03-09\\vi\\final4.tsv', 'r', encoding='utf8') as tsvfile:
#         tsvreader = csv.DictReader(tsvfile, delimiter='\t')
        
#         # Open a new TSV file for writing the modified rows
#         with open('D:\\Download\\cv-corpus-13.0-2023-03-09\\vi\\final6.tsv', 'w', newline='', encoding='utf8') as tsvout:
#             tsvwriter = csv.DictWriter(tsvout, delimiter='\t', fieldnames=tsvreader.fieldnames)
#             tsvwriter.writeheader()
            
#             # Loop through each row in the input TSV file
#             for row in tsvreader:
#                 # Check if the value of the 'person' column ends with '.mp3'
#                 # if 'speaker' in row['client_id']:
#                 # row['sentence']= normalize_text(row['sentence'])
#                 client= row['client_id']
#                 if  client.count("_") >= 2:
#                     client="_".join(client.split("_", 2)[:2])

#                     row['client_id']=client
#                     print(client)
#                     # print(second_part)
#                     # print("String contains 2 underscores.")
#                 tsvwriter.writerow(row)







# import csv

# # Open the input file for reading and output file for writing
# with open('D:\\Download\\cv-corpus-13.0-2023-03-09\\vi\\final.tsv', 'r', encoding='utf8') as input_file, open('D:\\Download\\cv-corpus-13.0-2023-03-09\\vi\\final2.tsv', 'w', newline='', encoding='utf8') as output_file:
#     reader = csv.reader(input_file, delimiter='\t')
#     writer = csv.writer(output_file, delimiter='\t')

#     # Get the header row and create a list of indices for the columns to delete
#     header = next(reader)
#     columns_to_delete = [3,4,5,6,7,8,9, 10]  # for example, delete the third and fifth columns
#     new_header = [col for i, col in enumerate(header) if i not in columns_to_delete]

#     # Write the modified header row to the output file
#     writer.writerow(new_header)

#     # Iterate over the remaining rows and write them to the output file with the specified columns removed
#     for row in reader:
#         new_row = [col for i, col in enumerate(row) if i not in columns_to_delete]
#         writer.writerow(new_row)








# import glob
# import os
# import csv
# import shutil
# folder_path = "D:\\Download\\vlsp2020_train_set_02"  # replace with the path to your folder
# search_string = "*speaker*.txt"


# # use glob to find all files that match the search string
# file_list = glob.glob(os.path.join(folder_path, search_string))
# i=0
# # iterate over the file list and print each filename

# # Create a new filename for the output TSV file
# output_filename = "D:\\Download\\cv-corpus-13.0-2023-03-09\\vi\\final4.tsv"

# with open(output_filename, mode='a', newline='', encoding='utf8') as tsvfile:
#     writer = csv.writer(tsvfile, delimiter="\t")
#     for file_path in file_list:
#         base_name, file_name = os.path.split(file_path)
#         wave_file_path= file_path.replace(".txt", ".wav") 


#         with open(file_path, "r",encoding='utf8') as file:
#             file_contents = file.read()

#         # print the file contents
#         # print(file_contents)
#         speaker = file_name.split("_", 2)[0]
#         # print(speaker)
#         wav_name = file_name.replace(".txt", ".wav") 
#         # print(wav_name)
#         new_row = [speaker, wav_name, file_contents]
#         writer.writerow(new_row)

#         shutil.copyfile(wave_file_path,'D:\\Download\\cv-corpus-13.0-2023-03-09\\vi\\wavs\\'+wav_name)





# import os
# import threading
# import wave

# folder_path = "D:\\Download\\cv-corpus-13.0-2023-03-09\\vi\\wavs"  # replace with the path to your folder
# total_duration = 0

# # define a function to read the duration of a WAV file
# def read_wav_duration(file_path):
#     with wave.open(file_path, "r") as file:
#         frames = file.getnframes()
#         rate = file.getframerate()
#         duration = frames / float(rate)
#         return duration

# # define a function to process a single WAV file
# def process_file(file_path):
#     global total_duration
#     duration = read_wav_duration(file_path)
#     total_duration += duration

# # define a function to process multiple WAV files in a thread
# def process_files_in_thread(file_paths):
#     for file_path in file_paths:
#         if file_path.lower().endswith(".wav"):
#             process_file(os.path.join(folder_path, file_path))

# # get a list of all the files in the folder
# file_names = os.listdir(folder_path)

# # divide the list of files into two roughly equal parts
# half = len(file_names) // 2
# files_part1 = file_names[:half]
# files_part2 = file_names[half:]

# # create two threads to process the two parts of the file list
# thread1 = threading.Thread(target=process_files_in_thread, args=(files_part1,))
# thread2 = threading.Thread(target=process_files_in_thread, args=(files_part2,))

# # start the threads
# thread1.start()
# thread2.start()

# # wait for the threads to finish
# thread1.join()
# thread2.join()

# # print the total duration of all WAV files in the folder
# print("Total duration:", total_duration, "seconds")






# import pandas as pd
# import matplotlib.pyplot as plt

# # Read the TSV file into a pandas DataFrame
# df = pd.read_csv('D:\\Download\\cv-corpus-13.0-2023-03-09\\vi\\final6.tsv', sep='\t')

# # Count the number of occurrences of each value in the 'client' column
# unique_clients = df['client_id'].nunique()

# # Print the number of unique clients
# print("Number of unique clients:", unique_clients)






# import concurrent.futures
# import time
# start_time = time.time()
# # function to check if a number is prime
# def is_prime(n):
#     if n <= 1:
#         return False
#     for i in range(2, int(n**0.5)+1):
#         if n % i == 0:
#             return False
#     return True

# # function to count the number of primes between two numbers
# def count_primes(start, end):
#     count = 0
#     for i in range(start, end+1):
#         if is_prime(i):
#             count += 1
#     return count

# if __name__ == '__main__':
#     # create a thread pool with 4 worker threads
#     with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
#         # divide the range into chunks of size 25000
#         chunks = [(i, i+24999) for i in range(2, 100001, 25000)]
#         # submit a count_primes task for each chunk
#         futures = [executor.submit(count_primes, start, end) for (start, end) in chunks]
#         # wait for all tasks to complete
#         concurrent.futures.wait(futures)
#         # sum the results
#         total_count = sum(f.result() for f in futures)
#         print(f'Total number of primes between 2 and 100,000: {total_count}')
#     print(round((time.time() - start_time), 2), "seconds")








# import time

# # function to check if a number is prime
# def is_prime(n):
#     if n <= 1:
#         return False
#     for i in range(2, int(n**0.5)+1):
#         if n % i == 0:
#             return False
#     return True

# if __name__ == '__main__':
#     start_time = time.time()
#     count = 0
#     for i in range(2, 100001):
#         if is_prime(i):
#             count += 1
#     end_time = time.time()
#     elapsed_time = end_time - start_time
#     print(f'Total number of primes between 2 and 100,000: {count}')
#     print(f'Time taken: {elapsed_time:.2f} seconds')


# import multiprocessing
# import time

# # function to check if a number is prime
# def is_prime(n):
#     if n <= 1:
#         return False
#     for i in range(2, int(n**0.5)+1):
#         if n % i == 0:
#             return False
#     return True

# # function to count the number of primes between two numbers
# def count_primes(start, end):
#     count = 0
#     for i in range(start, end+1):
#         if is_prime(i):
#             count += 1
#     return count

# if __name__ == '__main__':
#     start_time = time.time()
#     with multiprocessing.Pool(processes=4) as pool:
#         # divide the range into chunks of size 25000
#         chunks = [(i, i+24999) for i in range(2, 100001, 25000)]
#         # map the count_primes function to each chunk
#         results = pool.starmap(count_primes, chunks)
#     total_count = sum(results)
#     end_time = time.time()
#     elapsed_time = end_time - start_time
#     print(f'Total number of primes between 2 and 100,000: {total_count}')
#     print(f'Time taken: {elapsed_time:.2f} seconds')






# import os
# import wave
# import concurrent.futures
# import time
# # function to get the duration of a wave file
# def get_duration(file_path):
#     with wave.open(file_path, 'rb') as f:
#         frames = f.getnframes()
#         rate = f.getframerate()
#         duration = frames / float(rate)
#         return duration

# if __name__ == '__main__':
#     start_time = time.time()
#     folder_path = 'D:\\Download\\cv-corpus-13.0-2023-03-09\\vi\\wavs' # replace with the path to your folder
#     wav_files = [f for f in os.listdir(folder_path) if f.endswith('.wav')]

#     with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
#         # submit a get_duration task for each .wav file
#         futures = [executor.submit(get_duration, os.path.join(folder_path, f)) for f in wav_files]
#         # wait for all tasks to complete
#         concurrent.futures.wait(futures)
#         # sum the results
#         total_duration = sum(f.result() for f in futures)
#         print(f'Total duration of all .wav files: {total_duration:.2f} seconds')
#     print(round((time.time() - start_time), 2), "seconds")








# import os
# import wave
# import time
# # function to get the duration of a wave file
# def get_duration(file_path):
#     with wave.open(file_path, 'rb') as f:
#         frames = f.getnframes()
#         rate = f.getframerate()
#         duration = frames / float(rate)
#         return duration

# if __name__ == '__main__':
#     start_time = time.time()
#     folder_path = 'D:\\Download\\cv-corpus-13.0-2023-03-09\\vi\\wavs' # replace with the path to your folder
#     wav_files = [f for f in os.listdir(folder_path) if f.endswith('.wav')]

#     total_duration = 0
#     for f in wav_files:
#         file_path = os.path.join(folder_path, f)
#         duration = get_duration(file_path)
#         total_duration += duration

#     print(f'Total duration of all .wav files: {total_duration:.2f} seconds')
#     print(round((time.time() - start_time), 2), "seconds")




# import os
# import wave
# import concurrent.futures
# import time
# def get_wav_duration(filepath):
#     with wave.open(filepath, 'r') as wav_file:
#         frames = wav_file.getnframes()
#         rate = wav_file.getframerate()
#         duration = frames / float(rate)
#         return duration

# def sum_wav_durations_in_folder(folder_path):
#     with concurrent.futures.ProcessPoolExecutor() as executor:
#         durations = []
#         for filename in os.listdir(folder_path):
#             if filename.endswith('.wav'):
#                 filepath = os.path.join(folder_path, filename)
#                 durations.append(executor.submit(get_wav_duration, filepath))
#         total_duration = sum(d.result() for d in concurrent.futures.as_completed(durations))
#         return total_duration
# if __name__ == '__main__':
#     start_time = time.time()
#     folder_path = 'D:\\Download\\cv-corpus-13.0-2023-03-09\\vi\\wavs' # replace with the path to your folder
#     total_duration=sum_wav_durations_in_folder(folder_path)
#     print(round((time.time() - start_time), 2), "seconds")