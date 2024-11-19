def process_file():

    input_filename = input("Enter the input filename: ")
    output_filename = "modified_" + input_filename
    
    try:
        with open(input_filename, 'r') as input_file:
            content = input_file.read()
        
            modified_content = content.upper()
          
            with open(output_filename, 'w') as output_file:
                output_file.write(modified_content)
                
            print(f"\nSuccess! Modified content written to {output_filename}")
            
          
            print("\nFirst 100 characters of modified content:")
            print(modified_content[:100])
            
    except FileNotFoundError:
        print(f"\nError: The file '{input_filename}' was not found.")
        print("Please check if the file exists and the filename is correct.")
        
    except PermissionError:
        print(f"\nError: Permission denied when trying to access {input_filename}")
        print("Please check file permissions.")
        
    except UnicodeDecodeError:
        print(f"\nError: Unable to read {input_filename}")
        print("The file might be binary or encoded in an unsupported format.")
        
    except Exception as e:
        print(f"\nAn unexpected error occurred: {str(e)}")
        print("Please try again with a different file.")

if __name__ == "__main__":
    print("File Modification Program")
    print("------------------------")
    process_file()