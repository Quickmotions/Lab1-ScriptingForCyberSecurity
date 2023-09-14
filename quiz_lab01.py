"""Multiple Choice Quizzes for Lab 5.
   Creates the actual quiz with specific questions and answers.
   Uses variables to match the questions for easy location, eg Q1.1 is q1_1.
   quiz.py defines question types, must be in same dir, parent dir or path.
   Modified: July 2021
"""
# hack to allow import from parent directory
# from https://codeolives.com/2020/01/10/python-reference-module-in-parent-directory/
# next line disables pylint comment about import order, noqa is for pycodestyle
# pylint: disable=C0413
import os
import sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
import quiz  # noqa: E402


def section_one() -> None:
    """calls all questions in section one"""
    # sets the question, options and answers
    q1_1 = quiz.quiz_dropdown(
        "What is the prefix used to indicate a hex number?",
        ["0x", "0b"],
        "0x",
        rand=False,
       
    )
    q1_2 = quiz.quiz_dropdown(
        "What is the prefix used to indicate a binary number",
        ["0x", "0b"],
        "0b",
        rand=False,
      
    )
    q1_3 = quiz.quiz_dropdown(
        "In what notation are the results returned?",
        ["Base 10", "Base 16", "Base 2"],
        "Base 10",
        rand=False,
    )
    quiz.display(q1_1)  # displays the multiple choice
    quiz.display(q1_2)
    quiz.display(q1_3)

    
def section_two() -> None:
    """calls all questions in section two"""
    # sets the question, options and answers
    q2_1 = quiz.quiz_dropdown(
        '_str1 = "hello"',
        ["valid", "valid, but not a good idea", "not valid"],
        "valid",
        rand=False,
       
    )
    q2_2 = quiz.quiz_dropdown(
        'str%23 = "hello"',
        ["valid", "valid, but not a good idea", "not valid"],
        "not valid",
        rand=False,
      
    )
    q2_3 = quiz.quiz_dropdown(
        'for = 29.6',
        ["valid", "valid, but not a good idea", "not valid"],
        "not valid",
        rand=False,
    )
    q2_4 = quiz.quiz_dropdown(
        'my_string = "parrot"',
        ["valid", "valid, but not a good idea", "not valid"],
        "valid",
        rand=False,
    )
    q2_5 = quiz.quiz_dropdown(
        'string = "parrot"',
        ["valid", "valid, but not a good idea", "not valid"],
        "valid, but not a good idea",
        rand=False,
    )
    print("Which of the following are valid variable names?")
    quiz.display(q2_1)  # displays the multiple choice
    quiz.display(q2_2)
    quiz.display(q2_3)
    quiz.display(q2_4)    
    quiz.display(q2_5)    


def section_three() -> None:
    """calls all questions in section 3"""
    q3_1 = quiz.quiz_dropdown(
               "Why is the escape character necessary in str_var2?",
               ["It isn't actually necessary", "Because the string is enclosed in single quotes", "To stop the apostrophe being interpreted as the end of the string"],
               "To stop the apostrophe being interpreted as the end of the string"
                          )
    q3_2 = quiz.quiz_radio("Does the len() function count spaces too, or just visible characters?",
                           ["len() counts all characters, including spaces", "len() only counts visible characters"],
                           "len() counts all characters, including spaces"
                          )
    quiz.display(q3_1)  # displays the multiple choice
    quiz.display(q3_2)
    


def section_four_p1() -> None:
    """calls all questions in section four part 1"""
    q4_1 = quiz.quiz_dropdown(
        "What is the value of str_var1[-7]?",
        ["a", "P", " (a space)", "n", "p"],
        "P",
        rand=False,
    )
    q4_2 = quiz.quiz_dropdown(
        "What negative index returns the last char in the string?",
        ["-0", "-13", "-1"],
        "-1",
        rand=True,
    )
    
    quiz.display(q4_1)
    quiz.display(q4_2)


def section_four_p2() -> None:
    """calls all questions in section four part 2"""
    q4_3 = quiz.quiz_dropdown(
        "Which slice returns the first 3 chars of a string?",
        ["[0:4]",  "[0:3]", "[0:2]", "[4:0]", "[3:0]", "[2:0]"],
        "[0:3]",
        rand=False
    )
    
    q4_4 = quiz.quiz_dropdown(
        'What does str_var1[:-2] extract?',
        ["Don't Panic", "Do", "!!"],
        "Don't Panic",
        rand=False
    )
    
    q4_5 = quiz.quiz_dropdown(
        "What is the result of str_var1[::-1]?",
        ["Don't Panic!", "D", "!!cinaP t'noD"],
        "!!cinaP t'noD",
        rand=False
    )
    
    quiz.display(q4_3)
    print("str_var1 = \"Don't Panic!!\"")
    quiz.display(q4_4)
    quiz.display(q4_5)


def section_ten_p1() -> None:
    """calls all questions in section ten"""
    q10_1 = quiz.quiz_dropdown(
        "How many combinations would a brute force attack need to try for the ‘test’ 4 char password?",
        ["95^4", "4^95", "4*95", "95*4"],
        "95^4",
        rand=False
    )
    q10_2 = quiz.quiz_dropdown(
        "How many combinations would a brute force attack need to try for a 1 char password?",
        ["26", "1", "95", "128"],
        "95",
        rand=False
    )
    q10_3 = quiz.quiz_dropdown(
        "How many combinations would a brute force attack need to try for a 3 char password?",
        ["285", "857375", "31", "28203575"],
        "857375",
        rand=False
    )
    q10_4 = quiz.quiz_dropdown(
        "How many combinations would a brute force attack need to try for an 8 char password?",
        ["6634204312890625", "760", "103", "208827064576"],
        "6634204312890625",
        rand=False
    )
    
    quiz.display(q10_1)
    quiz.display(q10_2)
    quiz.display(q10_3)
    quiz.display(q10_4)

def section_ten_p2() -> None:
    """calls all questions in section ten"""
    q10_5 = quiz.quiz_dropdown(
        "What is the average search space for a 1 character password?",
        ["95", "1", "47.5", "23.75"],
        "47.5",
        rand=False
    )
    q10_6 = quiz.quiz_dropdown(
        "What is the average search space for a 5 character password?",
        ["475", "5", "241806542.9", "3868904687.5"],
        "3868904687.5",
        rand=False
    )
      
    quiz.display(q10_5)
    quiz.display(q10_6)
    
def section_ten_p3() -> None:
    """calls all questions in section ten"""
    q10_7 = quiz.quiz_dropdown(
        "How many hours to find a 1 character password?",
        ["2.375e-07", "1e-07", "4.75e-06", "2.475e-06"],
        "2.375e-07",
        rand=False
    )
    q10_8 = quiz.quiz_dropdown(
        "How many hours to find a 3 character password?",
        ["0.0475", "0.0021434375", "2.14", "0.003868904687"],
        "0.0021434375",
        rand=False
    )
    q10_9 = quiz.quiz_dropdown(
        "How many hours to find the password ‘napier123’?",
        ["1575623524.3115234", "0.475", "2418.065429", "663.42043128"],
        "1575623524.3115234",
        rand=False
    )
    
    quiz.display(q10_7)
    quiz.display(q10_8)
    quiz.display(q10_9)

def main() -> None:
    """Calls all sections, could be used for a recap quiz at end"""
    section_one()
    section_three()
    section_four_p1()
    section_four_p2()
    section_ten_p1()
    section_ten_p2()
    section_ten_p3()
    # add other section functions here as you make them


# Standard boilerplate code to call the main() function
if __name__ == "__main__":
    main()
