def file_automation():
    try:
        # Write to file
        with open("example.txt", "w") as file:
            file.write("Hello, File!")

        # Read from file
        with open("example.txt", "r") as file:
            line = file.readline()
            print(f"File Content: {line.strip()}")

    except IOError as e:
        print(f"An IOError occurred: {e}")


# Run the file automation function
file_automation()
