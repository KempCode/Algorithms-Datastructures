# O(N) time O(N) space best complexity
def runLengthEncoding(string):
    output = ""
    run_counter = 1

    for i in range(len(string)):
        if(run_counter == 9):
            output += str(run_counter)
            output += string[i]
            run_counter = 1  # reset run counter for the next run
            
        elif i == len(string) - 1 or string[i] != string[i + 1]:
            # If current character is the last one or different from the next one,
            # we need to end the current run
            output += str(run_counter)
            output += string[i]
            run_counter = 1  # reset run counter for the next run
        else:
            # If current character is same as the next one increment the run counter
            run_counter += 1

    return output