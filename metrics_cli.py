'''
    supply user message

    import file
    read from file
    print out each header column along with an index number
    
    
    [ receive user selection
      match columns
      compute metrics

    .... handle languages
    ]



    create 'help' command option
''' 


class Cli:
    def welcome(self):
        print("Welcome to the Metrics CLI.")
        print("Type '-help' at any time to see documentation. Type '-exit' to exit")
        user_input = input("Enter file name: ")
        if (user_input == '-help'):
            self.__help_doc()
            cont = input("Do you wish to continue? y/n \n\n")
            if (cont == 'y'):
                self.welcome()
            else:
                print("Adios\n")
                exit()
        if (user_input == '-exit'):
            print("Do come again\n")
            exit()
        

    def __help_doc(self):
        print("*******   Documentation   *********\n\n")
        print("This CLI program is designed to provide metrics on a CSV file.  When prompted, enter the filename to be analyzed. File must be in the same directory.\n")
        print("You will then be prompted with each column of the file and be asked to indicate the labeled column and the scored column.\n")
        print(
            '''The file requirements are the following: \n
                * must be a .csv 
                * must have at least one column of labeled data
                * must have at least one column of scored data
            '''
            )




prog = Cli()
prog.welcome()







