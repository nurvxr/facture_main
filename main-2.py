from PyQt5 import QtWidgets, uic, QtPrintSupport, QtGui

t=[]
t1=[]
t2=[]
t3=[]
ch=""
y1=0
i=0
montant_total=0
def ajouter():
    global y,ch,nom,nt,code,montant_total,t,t1,t2,t3,y1,i
    i+=1
    choice=call.choix.currentText()
    price=call.prix.text()
    quantity=call.qtt.text()
    montant=float(price)*int(quantity)
    montant_total+=montant
    call.facture.insertRow(i)
    call.facture.setItem(i,0, QtWidgets.QTableWidgetItem(choice))
    call.facture.setItem(i,1, QtWidgets.QTableWidgetItem(price))
    call.facture.setItem(i,2, QtWidgets.QTableWidgetItem(quantity))
    call.facture.setItem(i,3, QtWidgets.QTableWidgetItem(str(montant)))
    x=f'Produit : {choice}\nPrix : {price}\nQuantité : {quantity}\nMontant : {montant}\n--------------------------------------'
    ch=ch+x+"\n"
    nom=call.np.text()
    nt=call.tel.text()
    code=call.code.text()
    y=f'Nom et prenom : {nom}\nNumero de telephone : {nt}\nCode : {code}'
    t.append(choice)
    t1.append(str(price))
    t2.append(str(quantity))
    t3.append(str(montant))
    y1+=1
def confirm():
    global y,ch,nom,nt,code,montant_total
    fichier=open('fichier.txt','w+')
    fichier.write('--------------------------------------\n               Facture               \n--------------------------------------\n'+y+'\n--------------------------------------\n'+ch)
    fichier.close()
    call1.show()
    nom=call.np.text()
    nt=call.tel.text()
    code=call.code.text()
    call1.np1.setText(nom)
    call1.compte.setText(code)
    call1.tel.setText(nt)
    call1.montant_total.setText(str(montant_total))
    price=call.prix.text()
    quantity=call.qtt.text()
    montant=float(price)*int(quantity)
    montant_total+=montant
    for i in range(y1):
        call1.facture.insertRow(i)
        call1.facture.setItem(i,0, QtWidgets.QTableWidgetItem(t[i]))
        call1.facture.setItem(i,1, QtWidgets.QTableWidgetItem(t1[i]))
        call1.facture.setItem(i,2, QtWidgets.QTableWidgetItem(t2[i]))
        call1.facture.setItem(i,3, QtWidgets.QTableWidgetItem(t3[i]))
    tva1=(montant_total/100)*20
    call1.montant_total_2.setText(str(tva1))
    mont=tva1+montant_total
    call1.montant_total_3.setText(str(mont))

    
def imprimer():

    print_widget(call1)


  #  des.ajouter.setVisible(visible)


def print_widget(win):
    # Create printer
    printer = QtPrintSupport.QPrinter()
    # Create painter
    painter = QtGui.QPainter()
    # Start painter
    painter.begin(printer)
    # Grab a widget you want to print
    screen = win.grab()
    # Draw grabbed pixmap
    painter.drawPixmap(1, 1,600, 900, screen)
    # End painting
    painter.end()

  #  des.ajouter.setVisible(visible)
    

def quitter():
    app.quit()

def quitter_2():
    app.quit()

app=QtWidgets.QApplication([])
call=uic.loadUi('main.ui')
call1=uic.loadUi('valider.ui')
call.Quitter.clicked.connect(quitter)
call.ajouter.clicked.connect(ajouter)
call.confirmer.clicked.connect(confirm)
call1.pushButton.clicked.connect(imprimer)
call.facture.insertRow(0)
call.facture.insertColumn(0)
call.facture.insertColumn(1)
call.facture.insertColumn(2)
call.facture.insertColumn(3)
call.facture.setItem(0,0, QtWidgets.QTableWidgetItem("Produit"))
call.facture.setItem(0,1, QtWidgets.QTableWidgetItem("Prix"))
call.facture.setItem(0,2, QtWidgets.QTableWidgetItem("Quantité"))
call.facture.setItem(0,3, QtWidgets.QTableWidgetItem("Montant"))

call1.facture.insertColumn(0)
call1.facture.insertColumn(1)
call1.facture.insertColumn(2)
call1.facture.insertColumn(3)

call.show()
app.exec()
