from page1 import Ui_DATAMINING
from page2 import UI_page2
from page3 import Ui_page3
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog, QFileDialog,QVBoxLayout, QTableWidget, QTableWidgetItem
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCan   

from sklearn.preprocessing import label_binarize
from sklearn.metrics import roc_curve,auc
from sklearn.metrics import DetCurveDisplay, RocCurveDisplay
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.metrics import ConfusionMatrixDisplay
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.svm import SVC
from sklearn.inspection import DecisionBoundaryDisplay

from sklearn.cluster import AgglomerativeClustering, KMeans, DBSCAN
from sklearn_extra.cluster import KMedoids
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.neighbors import NearestNeighbors
from sklearn import metrics
from scipy.spatial.distance import pdist, squareform

from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pandas import read_csv
import warnings
warnings.filterwarnings("ignore")
#plt.style.use('seaborn')
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import plot_tree
import os


dat=0
x=0
y=0
interg = []
intrag = []

def importdata():
       global dat ,x,y

       fname = QFileDialog.getOpenFileName(ui, 'Open file', 'D:\codefirst.io\PyQt5 tutorials\Browse Files', )
       data = read_csv(fname[0])
       dat= data
       ui.textEdit.setText(fname[0])
       x = dat.drop(dat.columns[-1], axis=1)
       y=dat.iloc[:,-1]
       tabl()
       tabl2()
       return (dat,x,y)

def tabl():
       global dat
       p2.tableWidget.clearContents()
       p2.tableWidget.setRowCount(0)
       p2.tableWidget.setColumnCount(0)

    # Set the new data in the table
       p2.tableWidget.setColumnCount(len(dat.columns))
       p2.tableWidget.setRowCount(len(dat))

       for i, column_name in enumerate(dat.columns):
            p2.tableWidget.setHorizontalHeaderItem(i, QTableWidgetItem(column_name))

       for i, row_data in enumerate(dat.values):
            for j, cell_data in enumerate(row_data):
                item = QTableWidgetItem(str(cell_data))
                p2.tableWidget.setItem(i, j, item) 
       global x
       p3.tableWidget.clearContents()
       p3.tableWidget.setRowCount(0)
       p3.tableWidget.setColumnCount(0)

    # Set the new data in the table
       p3.tableWidget.setColumnCount(len(x.columns))
       p3.tableWidget.setRowCount(len(x))
       for i, column_name in enumerate(x.columns):
            p3.tableWidget.setHorizontalHeaderItem(i, QTableWidgetItem(column_name))
       for i, row_data in enumerate(x.values):
            for j, cell_data in enumerate(row_data):
                item = QTableWidgetItem(str(cell_data))
                p3.tableWidget.setItem(i, j, item)

def tabl2():
       global x
       p3.tableWidget.clearContents()
       p3.tableWidget.setRowCount(0)
       p3.tableWidget.setColumnCount(0)

    # Set the new data in the table
       p3.tableWidget.setColumnCount(len(x.columns))
       p3.tableWidget.setRowCount(len(x))
       for i, column_name in enumerate(x.columns):
            p3.tableWidget.setHorizontalHeaderItem(i, QTableWidgetItem(column_name))
       for i, row_data in enumerate(x.values):
            for j, cell_data in enumerate(row_data):
                item = QTableWidgetItem(str(cell_data))
                p3.tableWidget.setItem(i, j, item)

def pag():
      if (ui.radioButton.isChecked() == True):
            page2.show()
      if (ui.radioButton_2.isChecked() == True):
            page3.show()

def Norormalisation():
       global x
       Newdata2 = x.copy()
       for column in x.columns:
              if Newdata2[column].dtype == 'float64' or Newdata2[column].dtype =='int64':
                     Newdata2[column] = (x[column] - x[column].mean()) / x[column].std()
       M=[]
       l=Newdata2.shape[0]
       for i in range(l):
              c=0
              for column in Newdata2.columns:
                     if Newdata2[column].dtype == 'float64':
                            c=c+1
                            M.append(Newdata2[column].iloc[i])
       newar=np.asarray(M)
       newdat=newar.reshape(l,c)
       x = pd.DataFrame(newdat,columns = [column for column in Newdata2.columns if Newdata2[column].dtype == 'float64'])

       p2.tableWidget.clearContents()
       p2.tableWidget.setRowCount(0)
       p2.tableWidget.setColumnCount(0)
# Set the new data in the table
       p2.tableWidget.setColumnCount(len(x.columns))
       p2.tableWidget.setRowCount(len(x))

       for i, column_name in enumerate(x.columns):
             p2.tableWidget.setHorizontalHeaderItem(i, QTableWidgetItem(column_name))

       for i, row_data in enumerate(x.values):
             for j, cell_data in enumerate(row_data):
                item = QTableWidgetItem(str(cell_data))
                p2.tableWidget.setItem(i, j, item)
       p3.tableWidget.clearContents()
       p3.tableWidget.setRowCount(0)
       p3.tableWidget.setColumnCount(0)
# Set the new data in the table
       p3.tableWidget.setColumnCount(len(x.columns))
       p3.tableWidget.setRowCount(len(x))

       for i, column_name in enumerate(x.columns):
             p3.tableWidget.setHorizontalHeaderItem(i, QTableWidgetItem(column_name))

       for i, row_data in enumerate(x.values):
             for j, cell_data in enumerate(row_data):
                item = QTableWidgetItem(str(cell_data))
                p3.tableWidget.setItem(i, j, item)
       return(x)

def grafe1():
      global dat
      p2.figure.clear()  # Clear the existing plot in p2.figure
      ax = p2.figure.add_subplot(111) 
      ax.set_facecolor("#E5E8E8")
      # Use Seaborn to plot the jointplot directly on p2.figure
      sns.scatterplot(data=dat, x=dat.columns[1], y=dat.columns[2], hue=dat.columns[-1], palette="magma",ax=ax)
      ax.set_title("scatterplot")
      p2.canvas2.draw()

def grafe2():
      global dat
      p3.figure.clear()  # Clear the existing plot in p2.figure
      ax = p3.figure.add_subplot(111) 
      ax.set_facecolor("#E5E8E8")
      # Use Seaborn to plot the jointplot directly on p2.figure
      sns.scatterplot(data=dat, x=dat.columns[1], y=dat.columns[2] ,ax=ax)
      ax.set_title("scatterplot")
      p3.canvas2.draw()

def boxplot():
      global x
      p2.figure.clear()  # Clear the existing plot in p2.figure
      ax = p2.figure.add_subplot(111)  # Create an axes on p2.figure
      ax.set_facecolor("#E5E8E8")
      # Use Seaborn to plot the boxplot on the specified axes (ax)
      sns.boxplot(data=x, palette="magma", ax=ax)
      ax.set_title("BOX-PLOT")
      p2.canvas3.draw()  # Redraw the canvas

def boxplot2():
      global x
      p3.figure.clear()  # Clear the existing plot in p2.figure
      ax = p3.figure.add_subplot(111)  # Create an axes on p2.figure
      ax.set_facecolor("#E5E8E8")
      # Use Seaborn to plot the boxplot on the specified axes (ax)
      sns.boxplot(data=x, palette="magma", ax=ax)
      ax.set_title("BOX-PLOT")
      p3.canvas3.draw()  # Redraw the canvas

def datNum():
       global dat,x
       Colome=[]
       for i in range (len(dat.columns)-1):
              Colome.append(dat.columns[i])
       one_hot = OneHotEncoder()
       transformer = ColumnTransformer([("one_hot",one_hot,Colome)],remainder = "passthrough")
       transformed = transformer.fit_transform(dat)
       dat = pd.DataFrame(transformed)
       x = dat.drop(dat.columns[-1], axis=1)
       tabl()
       tabl2()
       return(dat,x)

def KNN():
      global x,y

      X=x
      Y=y
      x_train, x_test, y_train ,y_test = train_test_split(X,Y,test_size=float(p2.lineEdit_5.text()))
      KNN=KNeighborsClassifier(n_neighbors=int(p2.lineEdit.text()))
      KNN.fit(x_train,y_train)
      sco=round(KNN.score(x_test,y_test),2)
      d=str(sco * 100)+'%'
      
      m=ConfusionMatrixDisplay.from_estimator(KNN, x_test, y_test)
      p2.figure.clear()
      ax = p2.figure.add_subplot(111)
      ax.set_facecolor("#E5E8E8")
      m.plot(ax=ax)
      ax.set_title("ConfusionMatrix")
      p2.canvas4.draw()
      
      nb=int(p2.lineEdit_2.text())
      val_scortrain=[]
      val_scortest=[]
      for k in range(1,nb):
            score1=cross_val_score(KNeighborsClassifier(k),x_train,y_train,cv=int(p2.lineEdit_4.text()), scoring='accuracy').mean()
            val_scortrain.append(score1)
            score2=cross_val_score(KNeighborsClassifier(k),x_test,y_test,cv=5, scoring='accuracy').mean()
            val_scortest.append(score2)
       # and the first axes using subplot populated with data 
      xi=np.arange(1,nb)
      p2.figure.clear()
      ax = p2.figure.add_subplot(111)
      ax.set_facecolor("#E5E8E8")
      ax.plot(xi, val_scortrain, label="Train",c="#4B2991")
      ax.plot(xi, val_scortest, label="Test",c="#F6A97A")
      ax.set_xlabel("Nombre d'execution")
      ax.set_ylabel("Score")
      ax.set_title("cross_val")
      ax.legend()
      p2.canvas5.draw()
      #courb roc-----------------------------------------------------
      p2.figure.clear()
      y_test_binarized = label_binarize(y_test, classes=np.unique(y_test))
      if len(y_test_binarized[0])<=1:
            ax_roc = p2.figure.add_subplot(111)
            ax_roc.set_facecolor("#E5E8E8")
            RocCurveDisplay.from_estimator(KNN, x_test, y_test, ax=ax_roc ,c='#A50062')
            ax_roc.plot([0,1],[0,1],'--',c='black')
            ax_roc.set_title("Receiver Operating Characteristic (ROC) curves")
            ax_roc.legend()
            p2.canvas6.draw()
      else :
            ax2= p2.figure.add_subplot(111)
            ax2.set_facecolor("#E5E8E8")
            C=["#4B2991","#952EA0","#D44292","#F66D7A","#F6A97A"]
            Classses=np.unique(y_test)
            pred_prob=KNN.predict_proba(x_test)
            fpr = {}
            tpr = {}
            thresh ={}
            roc_auc = dict()
            n_classe = len(Classses)
            for i in range (n_classe):
                  fpr[i], tpr[i], thresh[i] = roc_curve(y_test_binarized[:,i], pred_prob[:,i])
                  roc_auc[i] = auc (fpr[i], tpr[i])
                  # traçage 
                  ax2.plot(fpr[i], tpr[i],label='%s vs Rest (AUC=%0.2f)'%(Classses[i], roc_auc[i]),c=C[i]) 
            ax2.plot([0,1], [0,1],linestyle='--', c='black')
            ax2.set_xlim([0,1])
            ax2.set_ylim([0,1.05])
            ax2.set_title('Receiver Operting Characteristic(ROC) courves')
            ax2.set_xlabel('False Rate')
            ax2.set_ylabel('True Rate')
            ax2.legend()
            p2.canvas6.draw()
      p2.textBrowser.setText(str(d))

def NaveBais():
      global x,y

      X=x
      Y=y
      x_train, x_test, y_train ,y_test = train_test_split(X,Y,test_size=float(p2.lineEdit_5.text()))
      NB=GaussianNB()
      NB.fit(x_train,y_train)
      sco=round(NB.score(x_test,y_test),2)
      d=str(sco * 100)+'%'
      
      m=ConfusionMatrixDisplay.from_estimator(NB, x_test, y_test,cmap="magma")
      p2.figure.clear()
      ax = p2.figure.add_subplot(111)
      ax.set_facecolor("#E5E8E8")
      m.plot(ax=ax)
      ax.set_title("ConfusionMatrix")
      p2.canvas4.draw()
      
      nb=int(p2.lineEdit_2.text())
      val_scortrain=[]
      val_scortest=[]
      for k in range(1,nb):
            score1=cross_val_score(GaussianNB(var_smoothing=k),x_train,y_train,cv=int(p2.lineEdit_4.text()), scoring='accuracy').mean()
            val_scortrain.append(score1)
            score2=cross_val_score(GaussianNB(var_smoothing=k),x_test,y_test,cv=int(p2.lineEdit_4.text()), scoring='accuracy').mean()
            val_scortest.append(score2)
       # and the first axes using subplot populated with data 
      xi=np.arange(1,nb)
      p2.figure.clear()
      ax = p2.figure.add_subplot(111)
      ax.set_facecolor("#E5E8E8")
      ax.plot(xi, val_scortrain, label="Train",c="#4B2991")
      ax.plot(xi, val_scortest, label="Test",c="#F6A97A")
      ax.set_xlabel("Nombre d'execution")
      ax.set_ylabel("Score")
      ax.set_title("cross_val")
      ax.legend()
      p2.canvas5.draw()
      #courb roc-----------------------------------------------------
      p2.figure.clear()
      y_test_binarized = label_binarize(y_test, classes=np.unique(y_test))
      if len(y_test_binarized[0])<=1:
            ax_roc = p2.figure.add_subplot(111)
            ax_roc.set_facecolor("#E5E8E8")
            RocCurveDisplay.from_estimator(NB, x_test, y_test, ax=ax_roc ,c='#A50062')
            ax_roc.plot([0,1],[0,1],'--',c='black')
            ax_roc.set_title("Receiver Operating Characteristic (ROC) curves")
            ax_roc.legend()
            p2.canvas6.draw()
      else :
            ax2= p2.figure.add_subplot(111)
            ax2.set_facecolor("#E5E8E8")
            C=["#4B2991","#952EA0","#D44292","#F66D7A","#F6A97A"]
            Classses=np.unique(y_test)
            pred_prob=NB.predict_proba(x_test)
            fpr = {}
            tpr = {}
            thresh ={}
            roc_auc = dict()
            n_classe = len(Classses)
            for i in range (n_classe):
                  fpr[i], tpr[i], thresh[i] = roc_curve(y_test_binarized[:,i], pred_prob[:,i])
                  roc_auc[i] = auc (fpr[i], tpr[i])
                  # traçage 
                  ax2.plot(fpr[i], tpr[i],label='%s vs Rest (AUC=%0.2f)'%(Classses[i], roc_auc[i]),c=C[i]) 
            ax2.plot([0,1], [0,1],linestyle='--', c='black')
            ax2.set_xlim([0,1])
            ax2.set_ylim([0,1.05])
            ax2.set_title('Receiver Operting Characteristic(ROC) courves')
            ax2.set_xlabel('False Rate')
            ax2.set_ylabel('True Rate')
            ax2.legend()
            p2.canvas6.draw()
      p2.textBrowser.setText(str(d))
      
def ArbeDis():
      global x,y

      X=x
      Y=y
      x_train, x_test, y_train ,y_test = train_test_split(X,Y,test_size=float(p2.lineEdit_5.text()))
      AD=DecisionTreeClassifier(criterion = 'gini',max_depth=int(p2.lineEdit.text()),random_state =0)
      AD.fit(x_train,y_train)
      sco=round(AD.score(x_test,y_test),2)
      d=str(sco * 100)+'%'
      p2.figure.clear()
      ax = p2.figure.add_subplot(111)
      ax.set_facecolor("#E5E8E8")
      tree.plot_tree(AD,filled=True,ax=ax)
      ax.set_xlabel("n_neighbors")
      ax.set_ylabel("Score")
      ax.set_title("cross_val")
      ax.legend()
      plt.savefig("arber.png")
      p2.canvas4.draw()
      
      nb=int(p2.lineEdit_2.text())
      val_scortrain=[]
      val_scortest=[]
      for k in range(1,nb):
            score1=cross_val_score(DecisionTreeClassifier(criterion = 'gini',max_depth=k,random_state =0),x_train,y_train,cv=int(p2.lineEdit_4.text()), scoring='accuracy').mean()
            val_scortrain.append(score1)
            score2=cross_val_score(DecisionTreeClassifier(criterion = 'gini',max_depth=k,random_state =0),x_test,y_test,cv=int(p2.lineEdit_4.text()), scoring='accuracy').mean()
            val_scortest.append(score2)
       # and the first axes using subplot populated with data 
      xi=np.arange(1,nb)
      p2.figure.clear()
      ax = p2.figure.add_subplot(111)
      ax.set_facecolor("#E5E8E8")
      ax.plot(xi, val_scortrain, label="Train",c="#4B2991")
      ax.plot(xi, val_scortest, label="Test",c="#F6A97A")
      ax.set_xlabel("Nombre d'execution")
      ax.set_ylabel("Score")
      ax.set_title("cross_val")
      ax.legend()
      p2.canvas5.draw()
      #courb roc-----------------------------------------------------
      p2.figure.clear()
      y_test_binarized = label_binarize(y_test, classes=np.unique(y_test))
      if len(y_test_binarized[0])<=1:
            ax_roc = p2.figure.add_subplot(111)
            ax_roc.set_facecolor("#E5E8E8")
            RocCurveDisplay.from_estimator(AD, x_test, y_test, ax=ax_roc ,c='#A50062')
            ax_roc.plot([0,1],[0,1],'--',c='black')
            ax_roc.set_title("Receiver Operating Characteristic (ROC) curves")
            ax_roc.legend()
            p2.canvas6.draw()
      else :
            ax2= p2.figure.add_subplot(111)
            ax2.set_facecolor("#E5E8E8")
            C=["#4B2991","#952EA0","#D44292","#F66D7A","#F6A97A"]
            Classses=np.unique(y_test)
            pred_prob=AD.predict_proba(x_test)
            fpr = {}
            tpr = {}
            thresh ={}
            roc_auc = dict()
            n_classe = len(Classses)
            for i in range (n_classe):
                  fpr[i], tpr[i], thresh[i] = roc_curve(y_test_binarized[:,i], pred_prob[:,i])
                  roc_auc[i] = auc (fpr[i], tpr[i])
                  # traçage 
                  ax2.plot(fpr[i], tpr[i],label='%s vs Rest (AUC=%0.2f)'%(Classses[i], roc_auc[i]),c=C[i]) 
            ax2.plot([0,1], [0,1],linestyle='--', c='black')
            ax2.set_xlim([0,1])
            ax2.set_ylim([0,1.05])
            ax2.set_title('Receiver Operting Characteristic(ROC) courves')
            ax2.set_xlabel('False Rate')
            ax2.set_ylabel('True Rate')
            ax2.legend()
            p2.canvas6.draw()
      
      p2.textBrowser.setText(str(d))

def reseau():
      global x,y

      X=x
      Y=y
      x_train, x_test, y_train ,y_test = train_test_split(X,Y,test_size=float(p2.lineEdit_5.text()))
      ML=MLPClassifier(max_iter=int(p2.lineEdit.text()))
      ML.fit(x_train,y_train)
      sco=round(ML.score(x_test,y_test),2)
      d=str(sco * 100)+'%'
      
      m=ConfusionMatrixDisplay.from_estimator(ML, x_test, y_test)
      p2.figure.clear()
      ax = p2.figure.add_subplot(111)
      ax.set_facecolor("#E5E8E8")
      m.plot(ax=ax)
      ax.set_title("ConfusionMatrix")
      p2.canvas4.draw()
     
      
      nb=int(p2.lineEdit_2.text())
      val_scortrain=[]
      val_scortest=[]
      for k in range(1,nb):
            score1=cross_val_score(MLPClassifier(max_iter=k*10),x_train,y_train,cv=int(p2.lineEdit_4.text()), scoring='accuracy').mean()
            val_scortrain.append(score1)
            score2=cross_val_score(MLPClassifier(max_iter=k*10),x_test,y_test,cv=int(p2.lineEdit_4.text()), scoring='accuracy').mean()
            val_scortest.append(score2)
       # and the first axes using subplot populated with data 
      xi=np.arange(1,nb)
      p2.figure.clear()
      ax = p2.figure.add_subplot(111)
      ax.set_facecolor("#E5E8E8")
      ax.plot(xi, val_scortrain, label="Train",c="#4B2991")
      ax.plot(xi, val_scortest, label="Test",c="#F6A97A")
      ax.set_xlabel("Nombre d'execution")
      ax.set_ylabel("Score")
      ax.set_title("cross_val")
      ax.legend()
      p2.canvas5.draw()
      #courb roc-----------------------------------------------------
      p2.figure.clear()
      y_test_binarized = label_binarize(y_test, classes=np.unique(y_test))
      if len(y_test_binarized[0])<=1:
            ax_roc = p2.figure.add_subplot(111)
            ax_roc.set_facecolor("#E5E8E8")
            RocCurveDisplay.from_estimator(ML, x_test, y_test, ax=ax_roc ,c='#A50062')
            ax_roc.plot([0,1],[0,1],'--',c='black')
            ax_roc.set_title("Receiver Operating Characteristic (ROC) curves")
            ax_roc.legend()
            p2.canvas6.draw()
      else :
            ax2= p2.figure.add_subplot(111)
            ax2.set_facecolor("#E5E8E8")
            C=["#4B2991","#952EA0","#D44292","#F66D7A","#F6A97A"]
            Classses=np.unique(y_test)
            pred_prob=ML.predict_proba(x_test)
            fpr = {}
            tpr = {}
            thresh ={}
            roc_auc = dict()
            n_classe = len(Classses)
            for i in range (n_classe):
                  fpr[i], tpr[i], thresh[i] = roc_curve(y_test_binarized[:,i], pred_prob[:,i])
                  roc_auc[i] = auc (fpr[i], tpr[i])
                  # traçage 
                  ax2.plot(fpr[i], tpr[i],label='%s vs Rest (AUC=%0.2f)'%(Classses[i], roc_auc[i]),c=C[i]) 
            ax2.plot([0,1], [0,1],linestyle='--', c='black')
            ax2.set_xlim([0,1])
            ax2.set_ylim([0,1.05])
            ax2.set_title('Receiver Operting Characteristic(ROC) courves')
            ax2.set_xlabel('False Rate')
            ax2.set_ylabel('True Rate')
            ax2.legend()
            p2.canvas6.draw()
      p2.textBrowser.setText(str(d))

def SVM():
      global x,y

      X=x
      Y=y
      x_train, x_test, y_train ,y_test = train_test_split(X,Y,test_size=float(p2.lineEdit_5.text()))
      svm=SVC(C=int(p2.lineEdit.text()))
      svm.fit(x_train,y_train)
      sco=round(svm.score(x_test,y_test),2)
      d=str(sco * 100)+'%'
      XX = X.iloc[:, 1:3]
      clf = SVC(kernel="linear", C=1)
      clf.fit(XX, Y) 
      p2.figure.clear()
      ax = p2.figure.add_subplot(111)
      ax.set_facecolor("#E5E8E8")
      X0, X1 = XX.iloc[:, 0], XX.iloc[:, 1]
      disp = DecisionBoundaryDisplay.from_estimator(
            clf,
            XX,
            response_method="predict",
            alpha=0.7,)
      disp.plot(ax=ax,cmap=plt.cm.coolwarm)
      m=round(clf.score(XX,Y),2)
      ax.scatter(X0, X1, c=y, s=20, edgecolors="k")
      ax.set_xticks(())
      ax.set_yticks(())
      ax.set_title(f"SVM with linear kernel,accuracy={m}")
      p2.canvas4.draw()
      XX = X.iloc[:, 1:3]
      clf = SVC(kernel="rbf", C=1)
      clf.fit(XX, Y) 
      p2.figure.clear()
      ax = p2.figure.add_subplot(111)
      ax.set_facecolor("#E5E8E8")
      X0, X1 = XX.iloc[:, 0], XX.iloc[:, 1]
      disp = DecisionBoundaryDisplay.from_estimator(
            clf,
            XX,
            response_method="predict",
            alpha=0.7,)
      disp.plot(ax=ax,cmap=plt.cm.coolwarm)
      m=round(clf.score(XX,Y),2)
      ax.scatter(X0, X1, c=y, s=20, edgecolors="k")
      ax.set_xticks(())
      ax.set_yticks(())
      ax.set_title(f"SVM with rbf kernel,accuracy={m}")
      p2.canvas5.draw()
      XX = X.iloc[:, 1:3]
      clf = SVC(kernel="poly", C=1)
      clf.fit(XX, Y) 
      p2.figure.clear()
      ax = p2.figure.add_subplot(111)
      ax.set_facecolor("#E5E8E8")
      X0, X1 = XX.iloc[:, 0], XX.iloc[:, 1]
      disp = DecisionBoundaryDisplay.from_estimator(
            clf,
            XX,
            response_method="predict",
            alpha=0.7,)
      disp.plot(ax=ax,cmap=plt.cm.coolwarm)
      m=round(clf.score(XX,Y),2)
      ax.scatter(X0, X1, c=y, s=20, edgecolors="k")
      ax.set_xticks(())
      ax.set_yticks(())
      ax.set_title(f"SVM with poly kernel,accuracy={m}")
      p2.canvas6.draw()

      p2.textBrowser.setText(str(d))

def compar():
      global x,y
      X=x
      X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=float(p2.lineEdit_5.text()))
      models = (
            KNeighborsClassifier(),
            GaussianNB(),
            DecisionTreeClassifier(),
            MLPClassifier(),
            SVC(probability=True),
            )
      titre = ("KNeighbors","NaveBais","ArberDecision","reseau N","SVM")
      Co=["#4B2991","#952EA0","#D44292","#F66D7A","#F6A97A"] 
      nm=[]
      C=[]
      typr=[]
      p2.figure.clear()
      ax = p2.figure.add_subplot(111)
      ax.set_facecolor("#E5E8E8")
      for clf,k,ti in zip(models,Co,titre):
            algo = clf
            algo.fit(X_train, y_train)
            ssco=algo.score(X_test,y_test)
            nm.append(ti)
            C.append(int(ssco*100))
            typr.append("auc")
            nm.append(ti)
            C.append(int((1-ssco)*100))
            typr.append("Err")
            RocCurveDisplay.from_estimator(algo, X_test, y_test, ax=ax,c=k )
            ax.plot([0,1],[0,1],'--',c='black')
            ax.set_title("Receiver Operating Characteristic (ROC) curves")
            ax.legend()
      p2.canvas5.draw()
      MM = pd.DataFrame({'algorithme': nm, 'resulta': C, 'type': typr})
      
      p2.figure.clear()
      ax = p2.figure.add_subplot(111)
      ax.set_facecolor("#E5E8E8")
      sns.barplot(x="algorithme", y="resulta", hue="type",palette="magma", data=MM,ax=ax)
      ax.set_title("histograme de model")
      p2.canvas6.draw()

def choiAlgo():
      if (p2.radioButton.isChecked()== True):
            KNN()
      if (p2.radioButton_2.isChecked() == True):
            NaveBais()
      if (p2.radioButton_3.isChecked() == True):
            ArbeDis()
      if (p2.radioButton_4.isChecked() == True):
            reseau()
      if (p2.radioButton_5.isChecked() == True):
            SVM()

def choiAlgo3():
      if (p3.radioButton.isChecked()== True):
            Kmeans()
      if (p3.radioButton_2.isChecked() == True):
            kmedoid()
      if (p3.radioButton_3.isChecked() == True):
            agnes()
      if (p3.radioButton_4.isChecked() == True):
            diana()
      if (p3.radioButton_5.isChecked() == True):
            dbiscann()

def elbou():
      
      global x
      p3.figure.clear()
      X = x
      inertia = []
      k = range(1, 20)
      for j in k:
            K_Model = KMeans(n_clusters=j).fit(X)
            inertia.append(K_Model.inertia_)
      ax = p3.figure.add_subplot(111)
      ax.set_facecolor("#E5E8E8")
      ax.plot(k, inertia)
      ax.set_xlabel('Nomber de clusters')
      ax.set_ylabel('Cout du modele')
      ax.set_title("La courbe de elbow")
      p3.canvas4.draw()

def Kmeans():
      global x
      global dat
      p3.figure.clear()
      X = x
      K_Model = KMeans(n_clusters=int(p3.lineEdit.text()))
      K_Model.fit(X)
      MR = K_Model.labels_
      ax = p3.figure.add_subplot(111) 
      ax.set_facecolor("#E5E8E8")
      sns.scatterplot(data=X, x=X.columns[1], y=X.columns[2] ,hue=MR, palette="magma",ax=ax)
      ax.scatter(K_Model.cluster_centers_[:, 1], K_Model.cluster_centers_[:, 2], c='g')

      ax.set_title("KMeans")
      p3.canvas5.draw()
      s=metrics.silhouette_score(X, K_Model.labels_, metric='sqeuclidean')
      if s<0:
            s=s*(-1)
      p3.textBrowser_5.setText(str(round(s,2)))
      distances = squareform(pdist(X))
      for cluster_label in set(K_Model.labels_):
            cluster_indices = (K_Model.labels_ == cluster_label)
            row_numbers = dat[cluster_indices].index.tolist()
            intra_distances = distances[np.ix_(cluster_indices, cluster_indices)]
            center_of_gravity = X[cluster_indices].mean(axis=0)
      k = 0
      m = 0
      for cluster_label in set(K_Model.labels_):
            intra_distances = distances[np.ix_(cluster_indices, cluster_indices)]
            center_of_gravity = X[cluster_indices].mean(axis=0)
            m = m + intra_distances.mean(axis=0)
            m = m.mean(axis=0)
            k = k + center_of_gravity.mean(axis=0)
      if k<0:
            k=k*(-1)
      p3.textBrowser.setText(str(round(k,2)))
      p3.textBrowser_3.setText(str(round(m,2)))
      intrag.append(k)
      interg.append(m)
      p3.textBrowser_4.setText(str(round((m+k),2)))

def kmedoid():
      global x
      X = x
      kmedoids = KMedoids(n_clusters=int(p3.lineEdit.text())).fit(X)
      km = kmedoids.labels_
      p3.figure.clear()
      ax = p3.figure.add_subplot(111) 
      ax.set_facecolor("#E5E8E8")
      sns.scatterplot(data=X, x=X.columns[1], y=X.columns[2] ,hue=km, palette="magma",ax=ax)
      ax.scatter(kmedoids.cluster_centers_[:, 1], kmedoids.cluster_centers_[:, 2], c='r')
      ax.set_title("KMedoids")
      p3.canvas5.draw()
      s=metrics.silhouette_score(X, kmedoids.labels_,metric='sqeuclidean')
      if s<0:
            s=s*(-1)
      p3.textBrowser_5.setText(str(round(s,2)))
      distances = squareform(pdist(X))
      for cluster_label in set(kmedoids.labels_):
            cluster_indices = (kmedoids.labels_ == cluster_label)
            row_numbers = dat[cluster_indices].index.tolist()
            intra_distances = distances[np.ix_(cluster_indices, cluster_indices)]
            center_of_gravity = X[cluster_indices].mean(axis=0)
      k = 0
      m = 0
      for cluster_label in set(kmedoids.labels_):
            intra_distances = distances[np.ix_(cluster_indices, cluster_indices)]
            center_of_gravity = X[cluster_indices].mean(axis=0)
            m = m + intra_distances.mean(axis=0)
            m = m.mean(axis=0)
            k = k + center_of_gravity.mean(axis=0)
      if k<0:
            k=k*(-1)
      p3.textBrowser.setText(str(round(k,2)))
      p3.textBrowser_3.setText(str(round(m,2)))
      intrag.append(k)
      interg.append(m)
      p3.textBrowser_4.setText(str(round((m+k),2)))

def graphAn():
      global x
      X=x
      if p3.radioButton_3.isChecked():
            p3.figure.clear()
            ax = p3.figure.add_subplot(111) 
            ax.set_facecolor("#E5E8E8")
            Z = linkage(X, 'ward')
            dn = dendrogram(Z)
            ax.axhline(y=20, color='r', linestyle='--')
            ax.set_title("Dendrogramme")
            p3.canvas6.draw()

def agnes():
      global x
      X = x
      AHA = AgglomerativeClustering(n_clusters=int(p3.lineEdit.text()), linkage='ward').fit(X)
      aha = AHA.labels_
      p3.figure.clear()
      ax = p3.figure.add_subplot(111) 
      ax.set_facecolor("#E5E8E8")
      sns.scatterplot(data=X, x=X.columns[1], y=X.columns[2] ,hue=aha, palette="magma",ax=ax)
      ax.set_title("AGNES")
      p3.canvas5.draw()
      s = metrics.silhouette_score(X, AHA.labels_, metric='sqeuclidean')
      if s<0:
            s=s*(-1)
      p3.textBrowser_5.setText(str(round(s,2)))
      AHA.fit(X)
      distances = squareform(pdist(X))
      for cluster_label in set(AHA.labels_):
            cluster_indices = (AHA.labels_ == cluster_label)
            row_numbers = dat[cluster_indices].index.tolist()
            intra_distances = distances[np.ix_(cluster_indices, cluster_indices)]
            center_of_gravity = X[cluster_indices].mean(axis=0)
      k = 0
      m = 0
      for cluster_label in set(AHA.labels_):
            intra_distances = distances[np.ix_(cluster_indices, cluster_indices)]
            center_of_gravity = X[cluster_indices].mean(axis=0)
            m = m + intra_distances.mean(axis=0)
            m = m.mean(axis=0)
            k = k + center_of_gravity.mean(axis=0)
      if k<0:
            k=k*(-1)
      p3.textBrowser.setText(str(round(k,2)))
      p3.textBrowser_3.setText(str(round(m,2)))
      intrag.append(k)
      interg.append(m)
      p3.textBrowser_4.setText(str(round((m+k),2)))

def graphdi():
      global x
      X=x
      if p3.radioButton_4.isChecked():
            p3.figure.clear()
            ax = p3.figure.add_subplot(111) 
            ax.set_facecolor("#E5E8E8")
            Z = linkage(X, 'complete')
            dn = dendrogram(Z)
            ax.axhline(y=20, color='r', linestyle='--')
            ax.set_title("Dendrogramme")
            p3.canvas6.draw()

def diana():
      global x
      X = x
      dian = AgglomerativeClustering(n_clusters=int(p3.lineEdit.text()), linkage='complete').fit(X)
      dian1 = dian.labels_
      p3.figure.clear()
      ax = p3.figure.add_subplot(111) 
      ax.set_facecolor("#E5E8E8")
      sns.scatterplot(data=X, x=X.columns[1], y=X.columns[2] ,hue=dian1, palette="magma",ax=ax)
      ax.set_title("DIANA")
      p3.canvas5.draw()
      s = metrics.silhouette_score(X, dian.labels_, metric='sqeuclidean')
      if s<0:
            s=s*(-1)
      p3.textBrowser_5.setText(str(round(s,2)))
      dian.fit(X)
      distances = squareform(pdist(X))
      for cluster_label in set(dian.labels_):
            cluster_indices = (dian.labels_ == cluster_label)
            row_numbers = dat[cluster_indices].index.tolist()
            intra_distances = distances[np.ix_(cluster_indices, cluster_indices)]
            center_of_gravity = X[cluster_indices].mean(axis=0)
      k = 0
      m = 0
      for cluster_label in set(dian.labels_):
            intra_distances = distances[np.ix_(cluster_indices, cluster_indices)]
            center_of_gravity = X[cluster_indices].mean(axis=0)
            m = m + intra_distances.mean(axis=0)
            m = m.mean(axis=0)
            k = k + center_of_gravity.mean(axis=0)
      if k<0:
            k=k*(-1)
      p3.textBrowser.setText(str(round(k,2)))
      p3.textBrowser_3.setText(str(round(m,2)))
      intrag.append(k)
      interg.append(m)
      p3.textBrowser_4.setText(str(round((m+k),2)))

def graphpi():
      global x
      X=x
      if p3.radioButton_5.isChecked():
            neigh = NearestNeighbors(n_neighbors=4)
            nbrs = neigh.fit(X)
            distances, indices = nbrs.kneighbors(X)
            distances = np.sort(distances, axis=0)
            distances = distances[:, 1]
            p3.figure.clear()
            ax = p3.figure.add_subplot(111) 
            ax.set_facecolor("#E5E8E8")
            ax.plot(distances)
            ax.set_xlabel('Nomber de point')
            ax.set_ylabel('rayon')
            ax.set_title("Paremeter  DBSCAN")
            p3.canvas6.draw()

def dbiscann():
      global x
      X = x
      db = DBSCAN(eps=float(p3.lineEdit_2.text()), min_samples=int(p3.lineEdit.text())).fit(X)
      labels = db.labels_
      p3.figure.clear()
      ax = p3.figure.add_subplot(111) 
      ax.set_facecolor("#E5E8E8")
      sns.scatterplot(data=X, x=X.columns[1], y=X.columns[2] ,hue=labels, palette="magma",ax=ax)
      ax.set_title("DBScan")
      p3.canvas5.draw()
      s = metrics.silhouette_score(X, db.labels_, metric='sqeuclidean')
      if s<0:
            s=s*(-1)
      p3.textBrowser_5.setText(str(round(s,2)))
      db.fit(X)
      distances = squareform(pdist(X))
      for cluster_label in set(db.labels_):
            cluster_indices = (db.labels_ == cluster_label)
            row_numbers = dat[cluster_indices].index.tolist()
            intra_distances = distances[np.ix_(cluster_indices, cluster_indices)]
            center_of_gravity = X[cluster_indices].mean(axis=0)
      k = 0
      m = 0
      for cluster_label in set(db.labels_):
            intra_distances = distances[np.ix_(cluster_indices, cluster_indices)]
            center_of_gravity = X[cluster_indices].mean(axis=0)
            m = m + intra_distances.mean(axis=0)
            m = m.mean(axis=0)
            k = k + center_of_gravity.mean(axis=0)
      if k<0:
            k=k*(-1)
      p3.textBrowser.setText(str(round(k,2)))
      p3.textBrowser_3.setText(str(round(m,2)))
      intrag.append(k)
      interg.append(m)
      p3.textBrowser_4.setText(str(round((m+k),2)))

def comparier():
      p3.figure.clear()
      ax = p3.figure.add_subplot(111) 
      ax.set_facecolor("#E5E8E8")
      ind = np.arange(len(interg))  # the x locations for the groups
      width = 0.35
      ax.bar(ind, intrag, width, color='#4B2991')
      ax.bar(ind, interg, width, bottom=intrag, color='#F6A97A')
      ax.set_ylabel('Scores')
      ax.set_title('Scores by group and gender')
      ax.set_xticks(ind, ('K_menas', 'K_Medoids', 'AGNES', 'DIANA', 'DBScan'))
      ax.legend(labels=['intra', 'inter'])
      p3.canvas6.draw()

import sys
app = QtWidgets.QApplication(sys.argv)
DATAMINING = QtWidgets.QMainWindow()
ui = Ui_DATAMINING()
ui.setupUi(DATAMINING)
DATAMINING.show()
ui.browse.clicked.connect(importdata)
ui.pushButton.clicked.connect(pag)


page2 = QtWidgets.QMainWindow()
p2 = UI_page2()
p2.setupUi(page2)

page3 = QtWidgets.QMainWindow()
p3 = Ui_page3()
p3.setupUi(page3)

p2.pushButton_3.clicked.connect(grafe1)
p2.pushButton.clicked.connect(boxplot)
p2.pushButton_2.clicked.connect(datNum)
p2.pushButton_5.clicked.connect(Norormalisation)
p2.pushButton_4.clicked.connect(choiAlgo)
p2.pushButton_6.clicked.connect(compar)

p3.pushButton_5.clicked.connect(Norormalisation)
p3.pushButton_3.clicked.connect(grafe2)
p3.pushButton.clicked.connect(boxplot2)
p3.pushButton_2.clicked.connect(datNum)
p3.pushButton_6.clicked.connect(elbou)
p3.pushButton_4.clicked.connect(choiAlgo3)
p3.radioButton_3.toggled.connect(graphAn)
p3.radioButton_4.toggled.connect(graphdi)
p3.radioButton_5.toggled.connect(graphpi)
p3.pushButton_7.clicked.connect(comparier)


sys.exit(app.exec_())
