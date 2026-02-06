#!/usr/bin/env python3
import sys
from datetime import datetime
import os

def display_greeting_message():
    recipient_name = sys.argv[1] if len(sys.argv) > 1 else "World"
    
    current_timestamp = datetime.now().isoformat()
    
    greeting_text = f"Hello {recipient_name}"
    print(greeting_text)
    
    output_var = f"time={current_timestamp}"
    
    github_output_path = os.getenv('GITHUB_OUTPUT')
    if github_output_path:
        with open(github_output_path, 'a') as output_file:
            output_file.write(f"{output_var}\n")
    else:
        print(f"::set-output name=time::{current_timestamp}")

if __name__ == "__main__":
    display_greeting_message()
