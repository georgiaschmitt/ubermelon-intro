log_file = open("um-server-01.txt")  #This opens a text file and gives it a variable name. Creates a file object from the text file so we can access its contents.


def sales_reports(log_file): # This establishes the sales_reports function and the parameter log_file.
    for line in log_file:  # For every line in the text file, do the following.
        line = line.rstrip()  # This removes extra whitespace to the right.
        day = line[0:3]  # This takes the first 3 characters of that line and assigns it to the variable 'day'.
        if day == "Mon":  # If these 3 characters are "Tue", then print that whole line.
            print(line)


sales_reports(log_file)  # This calls the function and passes the log_file opened at the beginning to the function.


