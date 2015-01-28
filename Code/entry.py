"""Deals with Entries"""

import datetime

from utilities import requiredFieldIsGood, optionalFieldIsGood, convertStringToTimedelta

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
        return '"Participant","Teacher","Discipline","Level","Years of Instruction","Instrument","Time","Title","Composer/Arranger/Author","Title of Musical","Scheduling Requirements"'
        
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
            
        s = '{indent}"{participantName}","{teacherName}","{discipline}","{level}","{yearsOfInstruction}","{instrument}","{requirements}'.format(
            indent=leadingCommas,
            participantName=participant,
            teacherName=teacher,
            discipline=self.discipline,
            level=self.level,
            yearsOfInstruction=self.yearsOfInstruction,
            instrument=self.instrument,
            requirements=self.schedulingRequirements
        )
        
        # instead of duplicating all the entry data just have an indented list of all selections
        for i in range(len(self.selections)):
            if i != 0:
                s += '{indent},,,,,,'.format(indent=leadingCommas)
                
            s += '{time}","{title}","{composer}","{musical}"\n'.format(
                time=self.selections[i]['performanceTime'],
                title=self.selections[i]['title'],
                composer=self.selections[i]['composerArranger'],
                musical=self.selections[i]['titleOfMusical']
            )
        
        csvFile.write(s)

    def toWordFile(self, document, p):
        """Creates a docx for the printer, document is from docx module"""
        # super hack
        from databaseInteraction import dbInteractionInstance
        
        participant = dbInteractionInstance.getParticipantFromId(self.participantID)

        pString = ""
        try:
            pString = "{0} {1}, {2}".format(participant.first, participant.last, participant.town)
        except Exception:
            if len(participant.participants) > 0:
                actualParticipants = []
                for pId in participant.participants:
                    actualParticipants.append(dbInteractionInstance.getParticipantFromId(pId))
                pString = ", ".join(actualParticipants)
                index = pString.rfind(", ")
                pString = pString[:index-1] + " & " + pString[index+1:]
            pString += ", {0}".format(participant.groupName)
            if participant.schoolGrade != "":
                pString += ", gr. " + participant.schoolGrade

        p.add_run(pString)

        for i in range(len(self.pieces)):
            letter = chr(i + ord('a'))
            p.add_run("\n\t{0}) {1}".format(letter, self.pieces[i]['title']))
