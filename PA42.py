def isValidIndex(index, lst):
    if (index - 1) >= 0 and (index - 1) < len(lst):
        return True
    return False

def printMenu():
    print()
    print("1. Print Integer Sequences")
    print("2. Print an Integer Sequence")
    print("3. Add a value to an Integer Sequence")
    print("4. Delete a value from an Integer Sequence")
    print("5. Modify a value from an Integer Sequence")
    print("6. Delete an Integer Sequence")
    print("7. Exit")
    print()

# Write the definition and implementation of the readFromFile function


# Write the definition and implementation of the printIntegerSequences function


# Write the definition and implementation of the printIntegerSequenceInformation function


# Write the definition and implementation of the addValueToSequence function


# Write the definition and implementation of the removeValueFromSequence function


# Write the definition and implementation of the modifyValueFromSequence function


# Write the definition and implementation of the removeSequence function


# Main program (DO NOT MODIFY)

filename = input("Enter the file name: ")
integerSequences = readFromFile(filename)
menuOption = 0
while menuOption != 7:
    printMenu()
    menuOption = int(input("Enter your option: "))
    if menuOption == 1:
        printIntegerSequences(integerSequences)
    elif menuOption >= 2 and menuOption <= 6:   # Reading the sequence number for options 2,3,4,5,6. Only a value between 1 and the number of sequences is a valid sequence number
        sequenceNo = int(input("Enter the sequence number: "))
        if isValidIndex(sequenceNo,integerSequences) == False:
            print("Invalid sequence number")
        else:
            if menuOption == 2: # Printing the information of the selected sequence
                printIntegerSequenceInformation(integerSequences[sequenceNo-1])
            elif menuOption != 6:   # Reading the position for options 3,4,5. 
                pos = int(input("Enter the position: "))
                if menuOption == 3: # When adding a value to a sequence, -1 is a valid position (adds the element at the end of the sequence)
                    validPosition = isValidIndex(pos,integerSequences[sequenceNo-1]) or (pos == -1)
                else: # For the other functions (remove and modify), only a value between 1 and the number of elements is a valid position
                    validPosition = isValidIndex(pos,integerSequences[sequenceNo-1])
                if validPosition == False:
                    print("Invalid position")
                else:
                    if menuOption == 3: # Adding a new value to the selected sequence
                        value = int(input("Enter the value: "))
                        addValueToSequence(value,pos,integerSequences[sequenceNo-1])
                    elif menuOption == 4: # Removing the selected value from the selected sequence
                        removeValueFromSequence(pos,integerSequences[sequenceNo-1])
                    else: # Modifying the selected value from the selected sequence
                        value = int(input("Enter the value: "))
                        modifyValueFromSequence(value,pos,integerSequences[sequenceNo-1])
            else:   # Option 6. Removing a sequence from the list of sequences.
                removeSequence(sequenceNo,integerSequences)
    elif menuOption != 7:
        print("Invalid option")