import random

def find_together(list_people,expected_people):
    random.shuffle(list_people)
    oneOfExpectedPeopleFound = False

    for person in list_people:
        if oneOfExpectedPeopleFound:
            if person in expected_people:
                break

        if person in expected_people:
            oneOfExpectedPeopleFound = True

        else:
            oneOfExpectedPeopleFound = False

    return oneOfExpectedPeopleFound

print(find_together(list_people = ["Ahmet", "Vural", "Fatih", "Mehmet"], expected_people = ["Vural", "Fatih"]
))






# list_people = ["Ahmet", "Vural", "Fatih", "Mehmet"]
# random.shuffle(list_people)
# print(list_people)
#
# expected_people = ["Vural", "Fatih"]
# oneOfExpectedPeopleFound = False
#
# for person in list_people:
#     if oneOfExpectedPeopleFound:
#         if person in expected_people:
#             break
#
#     if person in expected_people:
#         oneOfExpectedPeopleFound = True
#
#     else:
#         oneOfExpectedPeopleFound = False
#
# print(oneOfExpectedPeopleFound)

