from utilities import requiredFieldIsGood, optionalFieldIsGood

class Entry:
    """holds Entry data as strings"""
    def __init__(self, participantID=None, teacherID=None, level=None, classNumber=None, className=None, title=None, performanceTime=None):
        # Deal with getting QStrings from UI
        self.participantID = participantID if participantID is not None else None
        self.teacherID = teacherID if teacherID is not None else None
        self.level = str(level) if level is not None else None
        self.classNumber = str(classNumber) if classNumber is not None else None
        self.className = str(className) if className is not None else None
        self.title = str(title) if title is not None else None
        self.performanceTime = str(performanceTime) if performanceTime is not None else None

    def isEqualTo(self, obj):
        """check if obj is equal to this Entry (test purposes only?)"""
        if isinstance(obj, Entry):
            if (requiredFieldIsGood(self.participantID, obj.participantID) and 
                    requiredFieldIsGood(self.teacherID, obj.teacherID) and
                    optionalFieldIsGood(self.level, obj.level) and
                    requiredFieldIsGood(self.classNumber, obj.classNumber) and
                    requiredFieldIsGood(self.className, obj.className) and
                    requiredFieldIsGood(self.title, obj.title) and
                    optionalFieldIsGood(self.performanceTime, obj.performanceTime)):
                return True
            else:
                return False
        else:
            return False

    def addToDB(self, conn):
        """add this Entry to the database using connection conn"""
        conn.execute("INSERT INTO entries (participant_id, teacher_id, level, class_number, class_name, title, performance_time) VALUES (?, ?, ?, ?, ?, ?, ?)", (self.participantID, self.teacherID, self.level, self.classNumber, self.className, self.title, self.performanceTime));
        conn.commit()
        return True

class DanceEntry(Entry):
    def __init__(self, style=None):
        super(DanceEntry, self).__init__()
        self.style = str(style) if style is None else None
         
class PianoEntry(Entry):
    def __init__(self, composer=None, opus=None, no=None, movement=None):
        super(PianoEntry, self).__init__()
        self.composer = str(composer) if composer is not None else None
        self.opus = str(opus) if opus is not None else None
        self.no = str(no) if no is not None else None
        self.movement = str(movement) if movement is not None else None

class ChoralEntry(Entry):
    def __init__(self, style=None, composer=None, arranger=None, artist=None):
        super(ChoralEntry, self).__init__()
        self.style = str(style) if style is not None else None
        self.composer = str(composer) if composer is not None else None
        self.arranger = str(arranger) if arranger is not None else None
        self.artist = str(artist) if artist is not None else None

class VocalEntry(Entry):
    def __init__(self, style=None, composer=None, arranger=None, artist=None):
        super(VocalEntry, self).__init__()
        self.style = str(style) if style is not None else None
        self.composer = str(composer) if composer is not None else None
        self.arranger = str(arranger) if arranger is not None else None
        self.artist = str(artist) if artist is not None else None

class InstrumentalEntry(Entry):
    def __init__(self, instrument=None, composer=None, arranger=None):
        super(InstrumentalEntry, self).__init__()
        self.instrument = str(instrument) if instrument is not None else None
        self.composer = str(composer) if composer is not None else None
        self.arranger = str(arranger) if arranger is not None else None

class BandEntry(Entry):
    def __init__(self, style=None, composer=None, arranger=None):
        super(BandEntry, self).__init__()
        self.style = str(style) if style is not None else None
        self.composer = str(composer) if composer is not None else None
        self.arranger = str(arranger) if arranger is not None else None
                        
class SpeechEntry(Entry):
    def __init__(self, author=None):
        super(SpeechEntry, self).__init__()
        self.author = str(author) if author is not None else None 
        