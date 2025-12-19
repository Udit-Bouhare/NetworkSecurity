import sys 

def error_message_detail(error): 
    _,_,exc_tb = sys.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    file_no = exc_tb.tb_lineno
    error_message = f"Error occurred in file [{file_name}] line [{file_no}] message [{error}]"
    return error_message 

class NetworkSecurityException(Exception): 
    def __init__(self, error_message):
        super().__init__(error_message)

        self.error_message = error_message_detail(error_message)

    def __str__(self): 
        return self.error_message
    

                
