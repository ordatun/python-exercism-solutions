"""Functions for organizing and calculating student exam scores."""

import math
def round_scores(student_scores):
    """Round all provided student scores.

    :param student_scores: list - float or int of student exam scores.
    :return: list - student scores *rounded* to nearest integer value.
    """
    score=[]
    for i in student_scores:
        new=round(i)
        score.append(new)
        score.reverse()
    return score
        


def count_failed_students(student_scores):
    """Count the number of failing students out of the group provided.

    :param student_scores: list - containing int student scores.
    :return: int - count of student scores at or below 40.
    """
    total=0
    for scores in student_scores:
        if scores<=40:
             total+=1
    return total
    


def above_threshold(student_scores, threshold):
    """Determine how many of the provided student scores were 'the best' based on the provided threshold.

    :param student_scores: list - of integer scores.
    :param threshold: int - threshold to cross to be the "best" score.
    :return: list - of integer scores that are at or above the "best" threshold.
    """

    above_score=[]
    for number in student_scores:
        if number>=threshold:
            above_score.append(number)
    return above_score
        


def letter_grades(highest):
    """Create a list of grade thresholds based on the provided highest grade.

    :param highest: int - value of highest exam score.
    :return: list - of lower threshold scores for each D-A letter grade interval.
            For example, where the highest score is 100, and failing is <= 40,
            The result would be [41, 56, 71, 86]:

            41 <= "D" <= 55
            56 <= "C" <= 70
            71 <= "B" <= 85
            86 <= "A" <= 100
    """
    high_score=[]
    subs=highest-40
    div=round(subs/4)
    for i in range(0,4):
        again=41+(div*i)
        high_score.append(again)
    return high_score
    


def student_ranking(student_scores, student_names):
    """Organize the student's rank, name, and grade information in descending order.

    :param student_scores: list - of scores in descending order.
    :param student_names: list - of string names by exam score in descending order.
    :return: list - of strings in format ["<rank>. <student name>: <score>"].
    """
    new_list_rank=[]

    for i in range(len(student_scores)):
        result = f"{i+1}. {student_names[i]}: {student_scores[i]}"
        new_list_rank.append(result)
    return new_list_rank


def perfect_score(student_info):
    """Create a list that contains the name and grade of the first student to make a perfect score on the exam.

    :param student_info: list - of [<student name>, <score>] lists.
    :return: list - first `[<student name>, 100]` or `[]` if no student score of 100 is found.
    """
    for info in student_info:   
        if info[1]==100:
            return info
    return []   
    
        
     
        
        
        
