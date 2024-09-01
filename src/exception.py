import sys
from src.logger import logging

def error_message_detail(error,error_details:sys):
    _,_,exc_tb = error_details.exc_info()
    filename = exc_tb.tb_frame.f_code.co_filename
    lineno = exc_tb.tb_lineno
    error = str(error)
    error_message = f"Error occured in python script [{filename}] at line number [{lineno}] error maessage [{error}]"

    return error_message
class custom_exception(Exception):
    def __init__(self,error_message,error_details:sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message, error_details = error_details)

    def __str__(self):
        return self.error_message


