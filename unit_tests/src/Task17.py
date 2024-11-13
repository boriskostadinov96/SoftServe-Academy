# To train for an upcoming marathon, Johnny goes on one long-distance run each Saturday. He wants to track how often the number of miles he runs exceeds the previous Saturday. This is called a progress day.
# Create a function that takes in a list of miles run every Saturday and returns Johnny's total number of progress days.

def progress_day(days):
    result = 0
    for i in range(1, len(days)):
        if days[i] > days[i - 1]:
            result += 1
    return result


print(progress_day([10, 11, 12, 9, 10]))
