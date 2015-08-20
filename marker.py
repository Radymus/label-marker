# -*- coding: cp1250 -*-
__author__ = "Radim Spigel"
__version__ = "0.1"
import sys
from PySide.QtGui import QMainWindow, QApplication, QTableWidgetItem
from PySide.QtCore import SIGNAL
from PySide import QtGui
import gui
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, SubElement, Comment, tostring
DBXML = 'db.xml'
LEN_LINE = 40
MAX_LEN = 60


class Marker(QMainWindow, gui.Ui_MainWindow):

    def __init__(self, parent=None):
        super(Marker, self).__init__()
        self.setupUi(self)
        self.connect(self.SaveBtn, SIGNAL("clicked()"), self.saveToXml)
        self.connect(self.AddRecordBtn, SIGNAL("clicked()"), self.addRecordIntoTable)
        self.connect(self.SaveChangeBtn, SIGNAL("clicked()"), self.saveChangeToTable)
        self.connect(self.DeleteRecordBtn, SIGNAL("clicked()"), self.deleteRowFromTable)
        self.connect(self.PrintToFileBtn, SIGNAL("clicked()"), self.saveTableToTxt)
        self.connect(self.PrintSelectedToFileBtn, SIGNAL("clicked()"), self.saveSelectedTableToTxt)
        self.tableView.cellClicked.connect(self.cell_was_clicked)
             
        self.tree = ET.parse(DBXML)
        self.root = self.tree.getroot()
        for child in self.root:
            print child.tag, child.attrib
        self.showData()
        

        
    def cell_was_clicked(self):
        row = self.tableView.currentItem().row()
        print "row=",row
        col = self.tableView.currentItem().column()
        print "col=",col
        item = self.tableView.horizontalHeaderItem(col).text()
        print "item=",item,self.tableView.item(row, col).text()
        print self.root[row-1].attrib["id"]
        for child in self.root:
            if int(child.attrib["id"]) == row+1:
                self.PriceForUnitTF.setText(child.attrib["priceForUnit"])
                self.DescriptionTE.setPlainText(child.attrib["description"])
                self.ArtikelTF.setText(child.attrib["artikel"])
                self.WeightTF.setText(child.attrib["weight"])
                if child.attrib["unitDescription"] == "g":
                    self.UnitCB.setCurrentIndex(0)
                else:
                    self.UnitCB.setCurrentIndex(1)
                break
    def showData(self):
        self.tableView.setRowCount(len(self.root))        
        for ix, child in enumerate(self.root):
            s = u""+child.attrib["priceForFull"]+u"Kč/"+child.attrib["mainUnitDescription"]
            self.tableView.setItem(ix, 0, QTableWidgetItem(s))
            s = u""+child.attrib["priceForUnit"]+u"Kč"
            self.tableView.setItem(ix, 1, QTableWidgetItem(s))
            self.tableView.setItem(ix, 2, QTableWidgetItem(child.attrib["weight"]+child.attrib["unitDescription"]))
            self.tableView.setItem(ix, 3, QTableWidgetItem(unicode(u""+child.attrib["description"])))   

    def get_data(self):
        recs = []
        for ix, it in enumerate(self.tableView):
            pass
        return []
    
    def getMainUnit(self):
        if self.UnitCB.currentText() == "g":
            return "Kg"
        elif self.UnitCB.currentText() == "ml":
            return "l"
        
    def getFullPrice(self):
        print self.PriceForUnitTF.text(), self.WeightTF.text()
        try:
            one = float(self.PriceForUnitTF.text())/float(self.WeightTF.text())
            return "%.2f" % (one * 1000.0)
        except ValueError:
            return "0"
        
    def saveToXml(self):
        with open("db.xml","w") as file:
            file.write("<DB>\n")
            for rec in self.get_data():
                #s = '<record  id="{0}" artikel="{1}" description="{2}" unitDescriotion="{3}" mainUnitDescriotion="{4}" weight="{5}" priceForUnit="{6}" priceForFull="{7}"></record>'
                s = '<record  id={0} artikel={1} description={2} unitDescription={3} mainUnitDescription={4} weight={5} priceForUnit={6} priceForFull={7}></record>'.\
                format(rec["id"],rec["artikel"],rec["description"],rec["unitDescription"],rec["mainUnitDescription"],rec["weight"],rec["priceForUnit"],rec["priceForFull"])
                file.write(s)
            file.write("<\DB>\n")

    def __saveDescription(self):
        print "len ",len(self.DescriptionTE.toPlainText())
        if len(self.DescriptionTE.toPlainText()) > MAX_LEN:
            print "MOOOC",len(self.DescriptionTE.toPlainText()), ">", MAX_LEN
            return unicode(self.DescriptionTE.toPlainText()[:MAX_LEN])
        else:    
            return unicode(self.DescriptionTE.toPlainText())
        

    def addRecordIntoTable(self):
        rec = Element("record",id=str(len(self.root)+1), artikel=self.ArtikelTF.text(), description=self.__saveDescription(),
                         unitDescription=self.UnitCB.currentText(),mainUnitDescription=self.getMainUnit(), weight=self.WeightTF.text(),
                         priceForUnit=self.PriceForUnitTF.text().encode('cp1250'),priceForFull=self.getFullPrice().encode('cp1250'))
        self.root.append(rec)
        self.showData()
        
    def saveChangeToTable(self):
        for child in self.root:
            if int(child.attrib["id"]) == self.tableView.currentItem().row()+1:
                child.set('artikel', self.ArtikelTF.text())
                child.set('description', self.__saveDescription())
                child.set('unitDescription', self.UnitCB.currentText())
                child.set('mainUnitDescription', self.getMainUnit())
                child.set('weight', self.WeightTF.text())
                child.set('priceForUnit', self.PriceForUnitTF.text())
                child.set('priceForFull', str(self.getFullPrice()))
                print child.attrib
        self.showData()
    
    def deleteRowFromTable(self):
        rows = self.tableView.selectionModel().selectedRows()
        print rows   
        if len(rows) <= 0:
            node = self.root[self.tableView.currentItem().row()]          
            self.root.remove(node)
        else:
            remnode = []                 
            for i in rows: remnode.append(i.row())
            childrem = []
            for ix, child in enumerate(self.root):
                print int(child.attrib["id"]), remnode
                if int(child.attrib["id"]) in remnode:
                    childrem.append(child)
            for i in childrem: self.root.remove(i)
        for ix,child in enumerate(self.root):
            child.attrib["id"] = str(ix+1)
        self.showData()
        
    def saveToXml(self):
        self.tree.write(DBXML, encoding="utf-8")
        
    def add_descr(self, string, minus=4,sec=False):
        start = 0
        end = len(string)
        s = ""
        diff = (LEN_LINE - minus)
        if len(string) > diff and sec:
            end = len(string) #- diff #4 for "| "*2
            start = len(string)-(len(string) - diff)
            return string[start:end]+" "*(diff-len(string[start:end]))
        else:
            end = diff-len(string)
        if len(string) < diff:
            s += string[start:end]+" "*(diff-len(string))
            return s
        return string[start:end]
    
    def secLine(self, string, startS=""):
            emptyLine = " "*(LEN_LINE-2)    
            if len(string) > LEN_LINE-4:
                return startS+" "+self.add_descr(string,sec=True)+" |"
            else:
                return startS+emptyLine+"|"
            
    def joinDescr(self, rec, start="|"):
        print rec["description"]
        s = unicode(rec["description"])
        st = u"{0} {1}{2} ".format(s, rec["weight"],unicode(rec["unitDescription"]))
        return st, start+" "+self.add_descr(st)+" |"
    
    def tdToHTML(self,rec):
        s = u'<td height="38mm" width="297px">'#height="143px" width="297px"
        s+= u'<div id="desc">{0} {1}{2} </div>'.format(unicode(rec["description"]),rec["weight"],rec["unitDescription"])
        s+= u'<b><div id="priceUnit">{0} Kč</div><br></b>'.format(rec["priceForUnit"])
        s+= u'<div id="artikel"></div><div id="priceAll">{0} Kč/{1}</div><br>'.format(rec["priceForFull"],rec["mainUnitDescription"])
        s+= '</td>'
        return s
    
    def headToHTML(self):
        s = "<html>  <head>"
        s += "<title></title>"
        s += '<style type"text/css">'
        #s += "#desc{text-align: center;}:"
        s += "#priceUnit{text-align: right;font-size: 20px;}"
        s += "#priceAll{text-align: right;font-size: 10px;}"
        s += "#artikel{text-align:left;}"
        s += "</style></head><body>"
        s += '<table border="1">'
        return s
    
    def endToHTML(self,string):
        string += '</table></body></html>'            
        with open("out.html", "w") as file:
            file.write(string.encode("cp1250"))
            
    def saveTableToHtml(self):
        s = self.headToHTML()
        for idx in range(0,len(self.root),2):
            s+= '<tr>'
            s+= self.tdToHTML(self.root[idx].attrib)
            if idx+1 < len(self.root):
                s+= self.tdToHTML(self.root[idx].attrib)
            s+= '</tr>'
        self.endToHTML(s)
        
    def saveSelectedTableToTxt(self):
        s = self.headToHTML()
        rows = self.tableView.selectionModel().selectedRows()
        print rows   
      # print self.tableView.currentItem().row(), rows[0].row()
        if len(rows) <= 0:
            node = self.root[self.tableView.currentItem().row()]          
            s+=self.tdToHTML(node.attrib)
            s+= '</tr>'
        else:
            idx = 0
            tmp = [i.row()+1 for i in rows]
            for el in self.root:
                print int(el.attrib["id"]), tmp
                if int(el.attrib["id"]) in tmp:
                    if idx%2 ==0:
                        s+= '<tr>'                    
                    print int(el.attrib["id"])
                    s+= self.tdToHTML(el.attrib)
                    if idx%2:
                        s+= '</tr>'
                    idx+=1                        
                        #s+= self.tdToHTML(el.attrib)5
        self.endToHTML(s)
        
    def saveTableToTxt(self):
        self.saveTableToHtml()
        s = ""
        li = "--------------------------------------"
        for idx in range(0,len(self.root),2):
            rec = self.root[idx].attrib
            st = self.joinDescr(rec)[0]
            s += self.joinDescr(rec)[1]
            if idx+1 < len(self.root):
                secCh = self.root[idx+1].attrib
                stt = self.joinDescr(secCh,start="")[0]
                s += self.joinDescr(secCh,start="")[1]+"\n"           
            else:
                s+="\n"
            s+=self.secLine(st,startS="|")
            if idx+1 < len(self.root):
                s+=self.secLine(stt)
            kc = rec["priceForUnit"]+u" Kč"
            if idx+1 < len(self.root):
                kc2 = secCh["priceForUnit"]+u" Kč"
                s += "\n| "+" "*(LEN_LINE-len(kc)-4)+kc+" |"+" "*(LEN_LINE-len(kc)-3)+kc2+" "
            else:
                s += "\n| "+" "*(LEN_LINE-len(kc)-4)+kc+" "
            s += "|\n|"+" "*(LEN_LINE -7-len(rec["priceForFull"])-len(rec["mainUnitDescription"]))
            s += str(rec["priceForFull"])+u" Kč/{0} |".format(rec["mainUnitDescription"])
            if idx+1 < len(self.root):
                s += " "*(LEN_LINE -7-len(secCh["priceForFull"])-len(secCh["mainUnitDescription"]))
                s += str(secCh["priceForFull"])+u" Kč/{0} |\n".format(secCh["mainUnitDescription"])
            else:
                s += "\n "+li+" "
                continue
                #s += (" "*(LEN_LINE-2))*2+"|\n"  
            s += " "+li+" "
            if idx+1 < len(self.root):
                s+=li+"\n"
            else:
                s+="\n"
        print s
        with open("out.txt","w") as file:
            file.write(s.encode("cp1250"))
    
    def closeEvent(self, event):
        sys.exit(0)

if __name__ == "__main__":
  try:
      app = QApplication(sys.argv)
      beta = Marker()
      beta.show()
      app.exec_()
      sys.exit(app.exec_())
  except KeyboardInterrupt:
      pass
  except SystemExit:
      sys.exit(0)
  
