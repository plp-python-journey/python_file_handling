def modify_file(input_file, output_file):
    try:
        with open(input_file, "r") as infile:
            content = infile.read()
        #modifying the content to all text uppercase after reading operation is performed
        modified_content = content.upper()
        #performing writing operation
        with open(output_file, "w") as outfile:
            outfile.write(modified_content)

        print(f"Modified content written to '{output_file}' successfully.")
#handling specific errors instead of generalizing
    except FileNotFoundError:
        print(f"Error: '{input_file}' does not exist.")
    except PermissionError:
        print(f"Error: You don't have permission to read/write this file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Example usage
if __name__ == "__main__":
    modify_file("input.txt", "output.txt")
