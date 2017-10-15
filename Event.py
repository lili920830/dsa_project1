# mn":27},"end":{"row":22,"column":28},"action":"insert","lines":["f"],"id":709}],[{"start":{"row":22,"column":28},"end":{"row":22,"column":29},"action":"insert","lines":[" "],"id":710}],[{"start":{"row":22,"column":29},"end":{"row":22,"column":30},"action":"insert","lines":["e"],"id":711}],[{"start":{"row":22,"column":30},"end":{"row":22,"column":31},"action":"insert","lin


# blockEvent = Event.Event('block', clock, NODE_ID, str(userId))
import datetime

class Event:
    """
    Base class for Event instance
    """
    def __init__(self, op, time, node, content):
        self.op = op 
        self.time = time
        self.node = node 
        self.content = content
        self.utc = datetime.datetime.utcnow()