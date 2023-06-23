################################################################
# HISTORY:

# this is a re-write of s.t. used to drive question logic based on Cyc KB.

# now instead of Cyc KB, we are using Michaels AskMD enpoint.

# some of the fn names and comments might be legacy, i.e. not relevant
  to Michaels AskMD enpoint.

################################################################
# PURPOSE:

# to serve as a: dialog engine experimentation platform
# a way to prove we can replicate AskMD functionality
# etc

# Closest match in AskMD is EngDocService

# Legend:

# QPE - question panel element
# AQ - AskMD Question

# AQR - #$QuestionPanelResponse " If the user selects one of these
# during a AskMDConsultEvent then they are performing an instance of
# ReplyingToAQuestion."

################################################################

#import cyc_telnet as ct
#import interact as ci

# gave up on the follwoing:
# from .. import util
# see https://stackoverflow.com/questions/1054271/how-to-import-a-python-class-that-is-in-a-directory-above
# and https://www.python.org/dev/peps/pep-0328/
# and https://stackoverflow.com/questions/16981921/relative-imports-in-python-3

import pdb

NUM_PADDING_CHARS = 5

LEFT_MARGIN = 75
# how many characters wide things should be.
# LEFT_MARGINs specifies the right most allowable text for a pretty
#  display
# 
# Note that @func left_justify_col2 is not guarantted to be that if
# the columns are too big to fit!!

def diagnose(consult, cyc, print_cyc_objects_p = False):
    #pdb.set_trace()
    first_questions = ci.predicate_values(consult, "#$consultFirstQuestionsAre", cyc)
    if len(first_questions) > 1:
       print("Hrm, there is more than one first_question.  I am not yet programmed to handle this so I will arbitrarily handle just 1")
       print("The list of first questions is: ", first_questions)
       first_questions = first_questions[0]
       print("Okay, I have chosen to start with {first_questions}")
    else:
        first_questions = first_questions[0]
        
    last_questions = ci.predicate_values(consult, "#$consultLastQuestionIs", cyc)

    print("################")
    print("Ready to Start Dialog")
    print("First Question(s):", first_questions)
    print("Last Question(s):", last_questions)
    print("################")
    print()
    
    current_question = first_questions

    while (current_question not in last_questions):
          #if print_cyc_objects_p:     
          #   print(current_question)
          handle_one_question(current_question, cyc, print_cyc_objects_p)
          next_question = earo(ci.predicate_values(current_question, "#$nextQuestionIs", cyc))
          current_question = next_question
    if current_question in last_questions:
        print("Okay, on last question!!:")
        handle_one_question(current_question, cyc, print_cyc_objects_p)
        next_question = earo(ci.predicate_values(current_question, "#$nextQuestionIs", cyc))
        print("And now that we have asked the last question, what is value of next question?  Should be nil or something, eh?")
        print("The value of @param next_question is:", next_question)
    else:
        print("Huh?  How did you get here.  There's a bug in program logic or in data or in assumptions")
        pdb.set_trace()
    
def handle_one_question(question, cyc, print_cyc_objects_p):
    text = ci.predicate_values(question, "#$preferredNameString", cyc)
    #print("Text of Question:", text)
    if print_cyc_objects_p:
       #print(f"FLAG: Text is: {text}XXXXX")
       display_text = left_justify_col2(text, f"({question})", LEFT_MARGIN)
    else:
       display_text = text
            
    #print("Question Text:", display_text)
    print(display_text)
    #pdb.set_trace()
    panels = ci.predicate_values(question, "#$questionPanelElementsAre", cyc)
    panels.sort()
    #print("panels are:", panels)
    padding = " "*NUM_PADDING_CHARS
    for panel in panels:
        handle_one_question_panel_element(panel, cyc, print_cyc_objects_p, padding)
    input("Press any key to go to the next question")

def handle_one_question_panel_element(qpe, cyc, print_cyc_objects_p, padding):
    #if print_cyc_objects_p: 
    #    print("panel", qpe)
    text = ci.predicate_values(qpe, "#$preferredNameString", cyc)
    #print(f"{padding}Text of Question Panel Element: {text}")
    display_text = left_justify_col2(f"{padding}QPE:: {text}", qpe, LEFT_MARGIN)
    print(display_text)

    responses = ci.predicate_values(qpe, "#$questionPanelResponsesAre", cyc)
    responses.sort()
    for (nth, response) in enumerate(responses):
        handle_one_response(response, nth + 1 , cyc, print_cyc_objects_p, padding + padding)
    input("Type in your choice (currently ignored):")
    
def handle_one_response(response, nth, cyc, print_cyc_objects_p, padding):
    #if print_cyc_objects_p:
    #   print("response option:", response)
    text = ci.predicate_values(response, "#$pcwText", cyc)
    #print("Response Text:", text)
    #print(f"{padding} {nth}: {text}")
    if print_cyc_objects_p:
        display_text = left_justify_col2(f"{padding} {nth}: {text}", response, LEFT_MARGIN)
    else:
        display_text = f"{padding} {nth}: {text}"
    print(display_text)

def earo(list_of_values):
    """ earo stands for expect and return one"""
    if len(list_of_values) != 1:
       print("WARNING: expecting exactly one value but we have this:", list_of_values)
    else:
       return(list_of_values[0])

def left_justify_col2(str1, str2, left_edge_col2, min_pad_if_overflow = 2):
    """
    >>> left_justify_col2("0", "7890123456790", 7)
    '0      7890123456790'

    >>> left_justify_col2("0", "7890123456790", 14)
    '0             7890123456790'

    >>> left_justify_col2(['History'], "7890123456790", 14)
    "['History']   7890123456790"

    >>> left_justify_col2("0123", "7890123456790", 7)
    '0123   7890123456790'

    >>> left_justify_col2("01234", "7890123456790", 7)
    '01234  7890123456790'

    Below here we show that when the right column is too long to make
    the left edge work, it keeps two spaces bc of @param
    min_pad_if_overflow

    >>> left_justify_col2("012345", "7890123456790", 7)
    '012345  7890123456790'

    >>> left_justify_col2("0123456", "7890123456790", 7)
    '0123456  7890123456790'

    >>> left_justify_col2("0123456789", "7890123456790", 7)
    '0123456789  7890123456790'

    """
    str1 = str(str1) # we need this if e.g. str1 is ['History'] bc that things length is 1 not 7 (see ['History'] DocTest above)
    len1 = len(str1)
    num_spaces_padding = left_edge_col2 - len1
    if num_spaces_padding < min_pad_if_overflow:
       num_spaces_padding = min_pad_if_overflow
    pad_btwn_str1_end_and_str2_start = " "* num_spaces_padding
    #print(f"FLAG: left_justify_col2 len arg1: {len1}, left: {left_edge_col2}, num padding spcs: {num_spaces_padding}")

    return(str(str1) + pad_btwn_str1_end_and_str2_start + str(str2))




def right_justify_str2(str1, str2, right_edge, min_pad_if_overflow = 2):
    """
    If you have two columns of text and you want the 2nd column
    to end at nth char of any given line then use this function.

    >>> right_justify_str2("0Now is th0e time  0", "for0", 30)
    '0Now is th0e time  0      for0'

    >>> right_justify_str2("0123", "WXYZ", 30)
    '0123                      WXYZ'

    >>> right_justify_str2("0123", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", 10)
    '0123  ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    """
    len1 = len(str1)
    len2 = len(str2)
    num_spaces_padding = right_edge - len1 - len2
    if num_spaces_padding < min_pad_if_overflow:
       num_spaces_padding = min_pad_if_overflow
    pad_btwn_str1_end_and_str2_start = " "* num_spaces_padding
    #print(f"FLAG: right_justify_str2 len arg1: {len1}, len arg2: {len2}, right edge: {right_edge}, num padding spcs: {num_spaces_padding}")

    return(str(str1) + pad_btwn_str1_end_and_str2_start + str(str2))

def doit(print_cyc_objects_p = False):
    CycObj = ct.CycTelnetClient(raise_for_status=True)
    #diagnose("#$Consult-Inflammatory-Bowel-Disease-Management-182", CycObj, print_cyc_objects_p = print_cyc_objects_p)
    #diagnose("#$Consult-Headache-Diagnosis-4", CycObj, print_cyc_objects_p = print_cyc_objects_p)
    diagnose("#$Consult-Abdominal-Pain-and-Discomfort-Diagnosis-98", CycObj, print_cyc_objects_p = print_cyc_objects_p)    
    CycObj.close()

doit(print_cyc_objects_p = True)
