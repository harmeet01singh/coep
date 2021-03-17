import csv

def database_fn(
    Question_Type='text',
    Answer_Type=None,
    Topic_Number=None,
    Variation=None,
    Question=None,
    Correct_Answer_1=None,
    Correct_Answer_2='',
    Correct_Answer_3='',
    Correct_Answer_4='',
    Wrong_Answer_1=None,
    Wrong_Answer_2=None,
    Wrong_Answer_3=None,
    Time_in_seconds=60,
    Difficulty_Level=3,
    Question_IAV='',
    ContributorMail=None,
    Solution_text=None,
    Solution_IAV=''
):

    dataset_dict={
        'Question_Type':Question_Type,
        'Answer_Type':Answer_Type,
        'Topic_Number':Topic_Number,
        'Variation':Variation,
        'Question':Question,
        'Correct_Answer_1':Correct_Answer_1,
        'Correct_Answer_2':Correct_Answer_2,
        'Correct_Answer_3':Correct_Answer_3,
        'Correct_Answer_4':Correct_Answer_4,
        'Wrong_Answer_1':Wrong_Answer_1,
        'Wrong_Answer_2':Wrong_Answer_2,
        'Wrong_Answer_3':Wrong_Answer_3,
        'Time_in_seconds':Time_in_seconds,
        'Difficulty_Level':Difficulty_Level,
        'Question_IAV':Question_IAV,
        'ContributorMail':ContributorMail,
        'Solution_text':Solution_text,
        'Solution_IAV':Solution_IAV
    }
    return dataset_dict



#open csv file
def putInCsv(Topic_Number,Number_Of_Iterations,Main_Function,Filename):
    csv_filename= Topic_Number + '_' + Filename.split('.')[0] + '.csv'
    with open(csv_filename,'w',newline='') as f:
        fieldnames = [
            'Question_Type',
            'Answer_Type',
            'Topic_Number',
            'Variation',
            'Question',
            'Correct_Answer_1',
            'Correct_Answer_2',
            'Correct_Answer_3',
            'Correct_Answer_4',
            'Wrong_Answer_1',
            'Wrong_Answer_2',
            'Wrong_Answer_3',
            'Time_in_seconds',
            'Difficulty_Level',
            'Question_IAV',
            'ContributorMail',
            'Solution_text',
            'Solution_IAV'
        ]
        thewriter = csv.DictWriter(f, fieldnames=fieldnames)
        thewriter.writeheader()

        for i in range(Number_Of_Iterations):
            field_dict = Main_Function()
            thewriter.writerow(field_dict)
