'''
    [ receive user selection
      match columns
      compute metrics

    .... handle languages
    ]



    create 'help' command option
''' 

import csv

"""
    handles analysis of a csv document, providing metrics of scored data against labeled data, across
    languages
"""
class Cli:
    """
        Starting method for program.
        Obtains for user the filenmae to analyze
    """
    def welcome(self):
        print("Welcome to the Metrics CLI.")
        print("Type '-help' to see documentation. Type '-exit' to exit")
        user_input = input("Enter file name: ")
        if (user_input == '-help'):
            self.__help_doc()
            cont = input("Do you wish to continue? y/n \n\n")
            if (cont == 'y'):
                self.welcome()
            else:
                print("\n\nDo come again\n")
                exit()
        
        self.__exit_check(user_input)
        
        self.__read_file(user_input)
 
    """
        input: filename
        output: 
    """
    def __read_file(self, filename):
        print(filename)
        try: 
            with open(filename) as f:
                csvreader = csv.reader(f)
                headers = next(csvreader)
                run_analyze = 'y'

                while (run_analyze =='y'):
                    [labeled, scored] = self.__get_columns(headers)
                    print("Columns are: ", labeled, scored)


                    run_analyze = input("Do you wish to analyze another pair of columns? y/n ")    
            
                print("\n\nDo come again\n")
                exit()

        except Exception as e:
            print("Error occured: ", e)
            self.welcome()


    """
        @params: headers <list> 
        @return: tuple [labeled_column_number, scored_column_number] to be analyzed

    """
    def __get_columns(self, headers):
        print("\n*******  Column headers  ******* ")
        [print(f"{x}. {headers[x]}") for x in range(len(headers))]
        
        labeled = input("\nSelect the 'labeled' column: ")
        self.__exit_check(labeled)
        
        while (int(labeled) not in range(0, len(headers))):
            labeled = input("Your selection is not valid. Please try again.\n Select the 'labeled' column: ")
            self.__exit_check(labeled)
        
        scored = input("Select the matching 'scored' column: ")
        self.__exit_check(scored)
        while (int(scored) not in  range(0, len(headers))):
            scored = input("Your selection is not valid. Please try again.\nSelect the 'scored' column: ")
            self.__exit_check(scored)

        if (scored == labeled):
            print("\n\nYour column selections must be different.")
            print("Please try again.\n")
            self.__get_columns(headers)

        confirmed = input(
            f'''
            Please confirm:
            \tlabeled column: {headers[int(labeled)]}
            \tscored column: {headers[int(scored)]}

            Is this correct? y/n
            >  '''
        )

        self.__exit_check(confirmed)

        if (confirmed == 'n'):
            self.__get_columns(headers)

        return [labeled, scored]

    """
        @params: user_input<string>
        exits program if user_input is '-exit'
    """
    def __exit_check(self, user_input):
        if (user_input == '-exit'):
            print("\n\nDo come again\n")
            exit()



    '''
        Provides help documentation with instruction for how to use tool
    '''
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
        user_input = input(
            '''
                
            '''
        )




prog = Cli()
prog.welcome()







