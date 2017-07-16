import ai
import clock as cl
import database as d
import generator
from gui import gui
import people as p
import unit as u

class Model(object):

    def __init__(self):
        self.clock          = cl.Clock(self)
        self.week           = cl.Week(self)
        self.calendar       = cl.SecularCalendar()
        self.productionAI   = ai.ProductionAI(self)
        self.jobPoster      = ai.JobPoster(self)
        self.hirer          = ai.Hirer(self)
        self.firer          = ai.Firer(self)
        self.startupAI      = ai.StartupAI()
        self.builder        = ai.Builder(self)
        self.salaryPayer    = ai.SalaryPayer(self)
        ourGen              = generator.generator(self)
        self.ourWorld       = ourGen.generateWorld(10000, 10, 10)
        Jonestown           = d.getLocality()[0]
        #char
        address             = Jonestown.find_property()
        yourHome            = u.House(Jonestown, address)
        Jonestown.claim_node(address, yourHome)
        self.char           = ai.Character(self, "Markemus", "Aristobulus", 0, Jonestown, yourHome, d.getReligions()[0])
        yourHome.addTenant(self.char)
        spouse              = p.People(self, "Susan", "Spinster", 1, Jonestown, yourHome, d.getReligions()[0])
        yourHome.addTenant(spouse)
        self.char.addCapital(10000)
        #makes
        ourGen.makeSpouses()
        ourGen.makeFriends()
        ourGen.makeBosses()
        ourGen.makeChurches(Jonestown)
        ourGen.assignChurches()
        self.gui            = gui.gui(self.char)
        

    def out(self, text):
        self.gui.out(text)

    def getCharBusinesses(self):
        return self.char.getBusinesses()

    def getDayNum(self):
        return self.clock.getDayNum()