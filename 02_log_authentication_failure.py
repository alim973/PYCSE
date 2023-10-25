import re
from collections import Counter


with open("Linux_2k.log", 'r') as log_file:
       
        content = log_file
        
        
        
        with open("04_Output_auth.txt", 'w') as output_file:
                for line in log_file:
                        if "authentication failure" in line:
                                output_file.write(line)
                                
                print (content)
                
log_file.close()
output_file.close()