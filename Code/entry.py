"""Deals with Entries"""

import datetime

from utilities import requiredFieldIsGood, optionalFieldIsGood, convertStringToTimedelta
from participant import SoloParticipant

class Entry(object):
    """holds Entry data as strings"""
    def __init__(self, participantID="", teacherID="", discipline="", level="", yearsOfInstruction="", classNumber="", className="", instrument="", selections=None, schedulingRequirements=""):
        self.participantID = participantID
        self.teacherID = teacherID
        self.discipline = discipline
        self.level = level
        self.yearsOfInstruction = yearsOfInstruction
        self.classNumber = classNumber
        self.className = className
        self.instrument = instrument
        self.selections = selections if selections is not None else []
        self.schedulingRequirements = schedulingRequirements

    def isEqualTo(self, obj):
        """check if obj is equal to this Entry (test purposes only?)"""
        if isinstance(obj, Entry):
            if (requiredFieldIsGood(self.participantID, obj.participantID) and 
                    requiredFieldIsGood(self.teacherID, obj.teacherID) and
                    requiredFieldIsGood(self.discipline, obj.discipline) and
                    optionalFieldIsGood(self.level, obj.level) and
                    optionalFieldIsGood(self.yearsOfInstruction, obj.yearsOfInstruction) and
                    requiredFieldIsGood(self.classNumber, obj.classNumber) and
                    requiredFieldIsGood(self.className, obj.className) and
                    optionalFieldIsGood(self.instrument, obj.instrument)):
                return True
            else:
                return False
        else:
            return False

    def totalTime(self):
        totalTime = datetime.timedelta()
        for selection in self.selections:
            totalTime += convertStringToTimedelta(selection['performanceTime'])
        return totalTime

    def __str__(self):
        print "Entry has selections {0}".format(self.selections)        
        return self.participantID + self.teacherID + self.discipline + self.level + self.yearsOfInstruction + self.classNumber + self.className + self.instrument
        
    @staticmethod
    def getCsvHeader():
        """Returns a comma-separated string of column headers for use in a CSV file"""
        return '"Participant","Teacher","Discipline","Level","Years of Instruction","Instrument","Scheduling Requirements","Earliest Performance Time","Latest Performance Time","Time","Title","Composer/Arranger/Author","Title of Musical"'
        
    def export(self, csvFile, depth=2):
        """Write this entry to a csv file, padded with <depth> empty columns as indentation. \
        csvFile must be an open file with write permissions."""
        # super hack
        from databaseInteraction import dbInteractionInstance
        
        participant = dbInteractionInstance.getParticipantFromId(self.participantID)
        teacher = dbInteractionInstance.getTeacherFromId(self.teacherID)
        
        leadingCommas = ''
        for _ in range(depth):
            leadingCommas = leadingCommas+','
            
        s = '{indent}"{participantName}","{teacherName}","{discipline}","{level}","{yearsOfInstruction}","{instrument}","{requirements}",'.format(
            indent=leadingCommas,
            participantName=participant,
            teacherName=teacher,
            discipline=self.discipline,
            level=self.level,
            yearsOfInstruction=self.yearsOfInstruction,
            instrument=self.instrument,
            requirements=self.schedulingRequirements
        )

        try:
            s += '"{early}","{late}",'.format(
                early=participant.earliestPerformanceTime,
                late=participant.latestPerformanceTime
            )
        except Exception:
            s += ",,"
        
        # instead of duplicating all the entry data just have an indented list of all selections
        for i in range(len(self.selections)):
            if i != 0:
                s += '{indent},,,,,,,,,'.format(indent=leadingCommas)
                
            s += '"{time}","{title}","{composer}","{musical}"\n'.format(
                time=self.selections[i]['performanceTime'],
                title=self.selections[i]['title'],
                composer=self.selections[i]['composerArranger'],
                musical=self.selections[i]['titleOfMusical']
            )
        
        csvFile.write(s)

    @staticmethod
    def reportByDisciplineHeader():
        """Returns a comma-separated string of column headers for use in a CSV file"""
        return '"Discipline","Class Number","Class Name","Participant","Teacher","Level","Years of Instruction","Instrument","Scheduling Requirements","Time","Title","Composer/Arranger/Author","Title of Musical"\n'

    def reportByDiscipline(self, csvFile, depth=0):
        """Write this entry to a csv file, padded with <depth> empty columns as indentation. \
        csvFile must be an open file with write permissions."""
        
        leadingCommas = ''
        for _ in range(depth):
            leadingCommas = leadingCommas+','
            
        s = '{indent}"{discipline}","{classNumber}","{className}","{participantName}","{teacherName}","{level}","{yearsOfInstruction}","{instrument}","{requirements}",'.format(
            indent=leadingCommas,
            discipline=self.discipline,
            classNumber=self.classNumber,
            className=self.className,
            participantName=self.participantID,
            teacherName=self.teacherID,
            level=self.level,
            yearsOfInstruction=self.yearsOfInstruction,
            instrument=self.instrument,
            requirements=self.schedulingRequirements
        )
        
        # instead of duplicating all the entry data just have an indented list of all selections
        for i in range(len(self.selections)):
            if i != 0:
                s += '{indent},,,,,,,,,'.format(indent=leadingCommas)
                
            s += '"{time}","{title}","{composer}","{musical}"\n'.format(
                time=self.selections[i]['performanceTime'],
                title=self.selections[i]['title'],
                composer=self.selections[i]['composerArranger'],
                musical=self.selections[i]['titleOfMusical']
            )
        
        csvFile.write(s)

    @staticmethod
    def reportByTeacherHeader():
        """Returns a comma-separated string of column headers for use in a CSV file"""
        return '"Teacher","Participant","Discipline","Class Number","Class Name","Level","Years of Instruction","Instrument","Scheduling Requirements","Time","Title","Composer/Arranger/Author","Title of Musical"\n'

    def reportByTeacher(self, csvFile, depth=0):
        """Write this entry to a csv file, padded with <depth> empty columns as indentation. \
        csvFile must be an open file with write permissions."""
        
        leadingCommas = ''
        for _ in range(depth):
            leadingCommas = leadingCommas+','
            
        s = '{indent}"{teacherName}","{participantName}","{discipline}","{classNumber}","{className}","{level}","{yearsOfInstruction}","{instrument}","{requirements}",'.format(
            indent=leadingCommas,
            teacherName=self.teacherID,
            participantName=self.participantID,
            discipline=self.discipline,
            classNumber=self.classNumber,
            className=self.className,
            level=self.level,
            yearsOfInstruction=self.yearsOfInstruction,
            instrument=self.instrument,
            requirements=self.schedulingRequirements
        )
        
        # instead of duplicating all the entry data just have an indented list of all selections
        for i in range(len(self.selections)):
            if i != 0:
                s += '{indent},,,,,,,,,'.format(indent=leadingCommas)
                
            s += '"{time}","{title}","{composer}","{musical}"\n'.format(
                time=self.selections[i]['performanceTime'],
                title=self.selections[i]['title'],
                composer=self.selections[i]['composerArranger'],
                musical=self.selections[i]['titleOfMusical']
            )
        
        csvFile.write(s)

    @staticmethod
    def dumpHeader():
        """Returns a comma-separated string of column headers for use in a CSV file"""
        return '"Class Number","Class Name","Discipline","Level","Years of Instruction","Instrument","Scheduling Requirements",\
        "Time","Title","Composer/Arranger/Author","Title of Musical",\
        "Participant First Name","Participant Last Name","Participant Address","Participant Town","Participant Postal Code","Participant Home Phone","Participant Cell Phone","Participant Email","Participant Date of Birth","Participant School","Participant Parent","Participant Age","Participant Grade",\
        "Group Name","Group Size","Group Grade","Group Age","Group Participants","Earliest Performance Time","Latest Performance Time",\
        "Teacher/Contact First Name","Teacher/Contact Last Name","Teacher/Contact Address","Teacher/Contact City","Teacher/Contact Postal Code","Teacher/Contact Daytime Phone","Teacher/Contact Evening Phone","Teacher/Contact Email",\
        \n'

    def dump(self, csvFile):
        """Write this entry to a csv file, csvFile must be an open file with write permissions."""
            
        # super hack
        from databaseInteraction import dbInteractionInstance
        
        participant = dbInteractionInstance.getParticipantFromId(self.participantID)

        # Entry data
        s = '"{classNumber}","{className}","{discipline}","{level}","{yearsOfInstruction}","{instrument}","{requirements}",'.format(
            classNumber=self.classNumber,
            className=self.className,
            discipline=self.discipline,
            level=self.level,
            yearsOfInstruction=self.yearsOfInstruction,
            instrument=self.instrument,
            requirements=self.schedulingRequirements
        )

        # selection data
        # separated with slashes in each field
        time = ""
        title = ""
        composer = ""
        musical = ""
        for i in range(len(self.selections)):
            time += self.selections[i]['performanceTime']
            title += self.selections[i]['title']
            composer += self.selections[i]['composerArranger']
            musical += self.selections[i]['titleOfMusical']

            if i < len(self.selections)-1:
                time += '/'
                title += '/'
                composer += '/'
                musical += '/'
                
        s += '"{time}","{title}","{composer}","{musical}",'.format(
            time=time,
            title=title,
            composer=composer,
            musical=musical
        )

        # Participant data, solo then group
        if type(participant) is SoloParticipant:
            s += '"{first}","{last}","{address}","{town}","{postal}","{home}","{cell}","{email}","{dob}","{school}","{parent}","{age}","{grade}",'.format(
                first=participant.first,
                last=participant.last,
                address=participant.address,
                town=participant.town,
                postal=participant.postal,
                home=participant.home,
                cell=participant.cell,
                email=participant.email,
                dob=participant.dob,
                school=participant.schoolAttending,
                parent=participant.parent,
                age=participant.age,
                grade=participant.schoolGrade
            )
            s += ',,,,,,,'
        else:
            pString = ""
            tokens = participant.participants.split(',')
            if tokens[0] != "":
                for index in tokens:
                    sp = dbInteractionInstance.getParticipantFromId(index)
                    pString += "{first} {last}".format(first=sp.first, last=sp.last)
                    if sp.age != "":
                        pString += "{age}".format(age=sp.age)
                    pString += ", "
                if pString != "":
                    # remove final comma space
                    pString = pString[:-2]

            s += ',,,,,,,,,,,,,'

            s += '"{name}","{size}","{grade}","{age}","{participants}","{early}","{late}",'.format(
                name=participant.groupName,
                size=participant.groupSize,
                grade=participant.schoolGrade,
                age=participant.averageAge,
                participants=pString,
                early=participant.earliestPerformanceTime,
                late=participant.latestPerformanceTime
            )

        # contact/teacher info
        try:
            person = dbInteractionInstance.getTeacherFromId(participant.contact)
        except Exception:
            person = dbInteractionInstance.getTeacherFromId(self.teacherID)
        s += '"{first}","{last}","{address}","{city}","{postal}","{daytimePhone}","{eveningPhone}","{email}"\n'.format(
                first=person.first,
                last=person.last,
                address=person.address,
                city=person.city,
                postal=person.postal,
                daytimePhone=person.daytimePhone,
                eveningPhone=person.eveningPhone,
                email=person.email
            )
        
        csvFile.write(s)

    def toWordFile(self, p):
        """Creates a docx for the printer, document is from docx module"""
        # super hack
        from databaseInteraction import dbInteractionInstance
        
        participant = dbInteractionInstance.getParticipantFromId(self.participantID)
        pString = ""
        try:
            # Print soloist name
            pString = "{0} {1}, ".format(participant.first, participant.last)
            if participant.schoolAttending != "":
                pString += participant.schoolAttending
            else:
                pString += participant.town
        except Exception:
            # Print list of participants in group
            if len(participant.participants) > 0:
                actualParticipants = []
                tokens = participant.participants.split(',')
                if tokens[0] != "":
                    for index in tokens:
                        sp = dbInteractionInstance.getParticipantFromId(index)
                        if sp.first != "":
                            actualParticipants.append("{0} {1}".format(sp.first, sp.last))

                # Correctly "comma-ify" the list of names
                pString = ", ".join(actualParticipants)
                index = pString.rfind(", ")
                if index > -1:
                    pString = pString[:index-1] + " &" + pString[index+1:]

            # Print the group name
            if self.discipline in ["Choral", "Band", "Dance"]:
                if len(participant.participants) > 0:
                    pString += ", "
                pString += "{0}".format(participant.groupName)
            elif self.discipline == "Speech" and len(participant.participants) == 0:
                pString += "{0}".format(participant.groupName)
            
            # Print the grade
            if participant.schoolGrade != "":
                pString += ", gr. " + participant.schoolGrade

        p.add_run(pString)

        # Don't number if only one selection
        if len(self.selections) == 1:
            pString = "\n\t\t{0}".format(self.selections[0]['title'])

            if self.selections[0]['titleOfMusical'] != "":
                pString += " ({0})".format(self.selections[0]['titleOfMusical'])

            if self.selections[0]['composerArranger'] != "":
                pString += " - {0}".format(self.selections[0]['composerArranger'])

            p.add_run(pString)

        else:
            # Number selections like a)
            for i in range(len(self.selections)):
                letter = chr(i + ord('a')) # get the choresponding letter from the index
                pString = ("\n\t\t{0}) {1}".format(letter, self.selections[i]['title']))

                if self.selections[0]['titleOfMusical'] != "":
                    pString += " ({0})".format(self.selections[0]['titleOfMusical'])

                if self.selections[0]['composerArranger'] != "":
                    pString += " - {0}".format(self.selections[0]['composerArranger'])

                p.add_run(pString)
