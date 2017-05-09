# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dim_cabos.ui'
#
# Created by: PyQt5 UI code generator 5.8.1
#
# WARNING! All changes made in this file will be lost!
import os
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidget,QTableWidgetItem,QFileDialog

import listas_dim_cabos
import funcoes

class Ui_Form(object):
    def __init__(self):
        self.sistema = listas_dim_cabos.lista_sistema
        self.linha = listas_dim_cabos.lista_tipo_linha
        self.tipoCondutor = listas_dim_cabos.lista_tipo_condutor
        self.condutoresCarregados = listas_dim_cabos.lista_condutores_carregados
        self.isolamento = listas_dim_cabos.lista_tipo_isolamento
        self.temperaturaCondutor = listas_dim_cabos.lista_temperatura_condutor
        self.temperaturaAmbiente = listas_dim_cabos.lista_temperatura
        self.resistividade = listas_dim_cabos.lista_resistividade_termica_solo
        self.formaAgrupamento = listas_dim_cabos.lista_forma_agrupamento
        self.circuitosAgrupados = listas_dim_cabos.lista_cicuitos_agrupados
        self.distanciaCondutores = listas_dim_cabos.lista_distancia_cond_dutos
        self.harmonica = listas_dim_cabos.lista_taxa_3_harmonica
        self.tipoCircuito = listas_dim_cabos.lista_tipo_circuito

        self.resultado = []
        self.circuitos = []
        
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(668, 350)

        font = QtGui.QFont()
        font.setPointSize(9)
        
        self.verticalLayout_20 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout = QtWidgets.QGridLayout(self.tab)
        self.gridLayout.setObjectName("gridLayout")

        self.verticalLayoutNomeCircuito = QtWidgets.QVBoxLayout()
        self.verticalLayoutNomeCircuito.setObjectName("verticalLayoutNomeCircuito")

        self.labelNomeCircuito = QtWidgets.QLabel(self.tab)
        self.labelNomeCircuito.setFont(font)
        self.labelNomeCircuito.setObjectName("labelNomeCircuito")
        self.verticalLayoutNomeCircuito.addWidget(self.labelNomeCircuito)
        
        self.lineEditNomeCircuito = QtWidgets.QLineEdit(self.tab)
        self.lineEditNomeCircuito.setFont(font)
        self.lineEditNomeCircuito.setObjectName("lineEditNomeCircuito")
        self.lineEditNomeCircuito.setToolTip("<html><head/><body><p>Insira o nome do circuito.</p></body></html>")
        self.verticalLayoutNomeCircuito.addWidget(self.lineEditNomeCircuito)
        
        self.gridLayout.addLayout(self.verticalLayoutNomeCircuito, 0, 0, 1, 1)

        self.verticalLayoutTipoCircuito = QtWidgets.QVBoxLayout()
        self.verticalLayoutTipoCircuito.setObjectName("verticalLayoutTipoCircuito")
        
        self.labelTipoCircuito = QtWidgets.QLabel(self.tab)
        self.labelTipoCircuito.setFont(font)
        self.labelTipoCircuito.setObjectName("labelTipoCircuito")
        self.verticalLayoutTipoCircuito.addWidget(self.labelTipoCircuito)
        
        self.comboBoxTipoCircuito = QtWidgets.QComboBox(self.tab)
        self.comboBoxTipoCircuito.setFont(font)
        self.comboBoxTipoCircuito.setObjectName("comboBoxTipoCircuito")
        self.comboBoxTipoCircuito.setToolTip("<html><head/><body><p>Escolha o tipo de circuito.</p></body></html>")
        for item in self.tipoCircuito:
            self.comboBoxTipoCircuito.addItem(item)
        self.verticalLayoutTipoCircuito.addWidget(self.comboBoxTipoCircuito)
        
        self.gridLayout.addLayout(self.verticalLayoutTipoCircuito, 0, 1, 1, 1)
        
        self.verticalLayoutPotencia = QtWidgets.QVBoxLayout()
        self.verticalLayoutPotencia.setObjectName("verticalLayoutPotencia")
        
        self.labelPotencia = QtWidgets.QLabel(self.tab)
        self.labelPotencia.setFont(font)
        self.labelPotencia.setObjectName("labelPotencia")
        self.verticalLayoutPotencia.addWidget(self.labelPotencia)
        
        self.doubleSpinBoxPotencia = QtWidgets.QDoubleSpinBox(self.tab)
        self.doubleSpinBoxPotencia.setFont(font)
        self.doubleSpinBoxPotencia.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.doubleSpinBoxPotencia.setMaximum(999999.99)
        self.doubleSpinBoxPotencia.setObjectName("doubleSpinBoxPotencia")
        self.doubleSpinBoxPotencia.setToolTip("<html><head/><body><p>Insira a potência do circuito. Caso tenha que descontar o rendimento do equipamento, insira a potência já dividida pelo seu rendimento.</p></body></html>")
        self.verticalLayoutPotencia.addWidget(self.doubleSpinBoxPotencia)
        
        self.gridLayout.addLayout(self.verticalLayoutPotencia, 0, 2, 1, 1)

        self.verticalLayoutTipoSistema = QtWidgets.QVBoxLayout()
        self.verticalLayoutTipoSistema.setObjectName("verticalLayoutTipoSistema")
        
        self.labelTipoSistema = QtWidgets.QLabel(self.tab)
        self.labelTipoSistema.setFont(font)
        self.labelTipoSistema.setObjectName("labelTipoSistema")
        self.verticalLayoutTipoSistema.addWidget(self.labelTipoSistema)
        
        self.comboBoxTipoSistema = QtWidgets.QComboBox(self.tab)
        self.comboBoxTipoSistema.setFont(font)
        self.comboBoxTipoSistema.setObjectName("comboBoxTipoSistema")
        self.comboBoxTipoSistema.setToolTip("<html><head/><body><p>Escolha o tipo do sistema.</p></body></html>")
        for item in self.sistema:
            self.comboBoxTipoSistema.addItem(item)
        self.verticalLayoutTipoSistema.addWidget(self.comboBoxTipoSistema)
        
        self.gridLayout.addLayout(self.verticalLayoutTipoSistema, 0, 3, 1, 1)

        self.verticalLayoutTensao = QtWidgets.QVBoxLayout()
        self.verticalLayoutTensao.setObjectName("verticalLayoutTensao")
        
        self.labelTensao = QtWidgets.QLabel(self.tab)
        self.labelTensao.setFont(font)
        self.labelTensao.setObjectName("labelTensao")
        self.verticalLayoutTensao.addWidget(self.labelTensao)
        
        self.doubleSpinBoxTensao = QtWidgets.QDoubleSpinBox(self.tab)
        self.doubleSpinBoxTensao.setFont(font)
        self.doubleSpinBoxTensao.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.doubleSpinBoxTensao.setMaximum(999999.99)
        self.doubleSpinBoxTensao.setObjectName("doubleSpinBoxTensao")
        self.doubleSpinBoxTensao.setToolTip("<html><head/><body><p>Insira a tensão nominal do circuito. Fique atento para fornecer a tensão adequada - Linha ou Fase.</p></body></html>")
        
        self.verticalLayoutTensao.addWidget(self.doubleSpinBoxTensao)
        
        self.gridLayout.addLayout(self.verticalLayoutTensao, 1, 0, 1, 1)

        self.verticalLayoutFatorPotencia = QtWidgets.QVBoxLayout()
        self.verticalLayoutFatorPotencia.setObjectName("verticalLayoutFatorPotencia")
        
        self.labelFatorPotencia = QtWidgets.QLabel(self.tab)
        self.labelFatorPotencia.setFont(font)
        self.labelFatorPotencia.setObjectName("labelFatorPotencia")
        self.verticalLayoutFatorPotencia.addWidget(self.labelFatorPotencia)
        
        self.doubleSpinBoxFatorPotencia = QtWidgets.QDoubleSpinBox(self.tab)
        self.doubleSpinBoxFatorPotencia.setFont(font)
        self.doubleSpinBoxFatorPotencia.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
##        self.doubleSpinBoxFatorPotencia.setMinimum(-1.00)
        self.doubleSpinBoxFatorPotencia.setMaximum(1.00)
        self.doubleSpinBoxFatorPotencia.setObjectName("doubleSpinBoxFatorPotencia")
        self.doubleSpinBoxFatorPotencia.setToolTip("<html><head/><body><p>Insira o fator de potência do circuito.</p></body></html>")
        self.verticalLayoutFatorPotencia.addWidget(self.doubleSpinBoxFatorPotencia)
        
        self.gridLayout.addLayout(self.verticalLayoutFatorPotencia, 1, 1, 1, 1)
                        
        self.verticalLayoutTipoLinha = QtWidgets.QVBoxLayout()
        self.verticalLayoutTipoLinha.setObjectName("verticalLayoutTipoLinha")
        
        self.labelTipoLinha = QtWidgets.QLabel(self.tab)
        self.labelTipoLinha.setFont(font)
        self.labelTipoLinha.setObjectName("labelTipoLinha")
        self.verticalLayoutTipoLinha.addWidget(self.labelTipoLinha)
        
        self.comboBoxTipoLinha = QtWidgets.QComboBox(self.tab)
        self.comboBoxTipoLinha.setFont(font)
        self.comboBoxTipoLinha.setObjectName("comboBoxTipoLinha")
        self.comboBoxTipoLinha.setToolTip("<html><head/><body><p>Escolha o tipo de linha do circuito.</p></body></html>")
        for item in self.linha:
            self.comboBoxTipoLinha.addItem(item)
        self.verticalLayoutTipoLinha.addWidget(self.comboBoxTipoLinha)
        
        self.gridLayout.addLayout(self.verticalLayoutTipoLinha, 1, 2, 1, 2)

        self.verticalLayoutTipoCondutor = QtWidgets.QVBoxLayout()
        self.verticalLayoutTipoCondutor.setObjectName("verticalLayoutTipoCondutor")
        
        self.labelTipoCondutor = QtWidgets.QLabel(self.tab)
        self.labelTipoCondutor.setFont(font)
        self.labelTipoCondutor.setObjectName("labelTipoCondutor")
        self.verticalLayoutTipoCondutor.addWidget(self.labelTipoCondutor)
        
        self.comboBoxTipoCondutor = QtWidgets.QComboBox(self.tab)
        self.comboBoxTipoCondutor.setFont(font)
        self.comboBoxTipoCondutor.setObjectName("comboBoxTipoCondutor")
        self.comboBoxTipoCondutor.setToolTip("<html><head/><body><p>Escolha o tipo de condutor do circuito.</p></body></html>")
        for item in self.tipoCondutor:
            self.comboBoxTipoCondutor.addItem(item)
        self.verticalLayoutTipoCondutor.addWidget(self.comboBoxTipoCondutor)
        
        self.gridLayout.addLayout(self.verticalLayoutTipoCondutor, 2, 0, 1, 1)

        self.verticalLayoutCondutoresCarregados = QtWidgets.QVBoxLayout()
        self.verticalLayoutCondutoresCarregados.setObjectName("verticalLayoutCondutoresCarregados")
        
        self.labelCondutoresCarregados = QtWidgets.QLabel(self.tab)
        self.labelCondutoresCarregados.setFont(font)
        self.labelCondutoresCarregados.setObjectName("labelCondutoresCarregados")
        self.verticalLayoutCondutoresCarregados.addWidget(self.labelCondutoresCarregados)
        
        self.comboBoxCondutoresCarregados = QtWidgets.QComboBox(self.tab)
        self.comboBoxCondutoresCarregados.setFont(font)
        self.comboBoxCondutoresCarregados.setObjectName("comboBoxCondutoresCarregados")
        self.comboBoxCondutoresCarregados.setToolTip("<html><head/><body><p>Escolha a quantidade de condutores carregados do circuito.</p></body></html>")
        for item in self.condutoresCarregados:
            self.comboBoxCondutoresCarregados.addItem(item)
        self.verticalLayoutCondutoresCarregados.addWidget(self.comboBoxCondutoresCarregados)
        
        self.gridLayout.addLayout(self.verticalLayoutCondutoresCarregados, 2, 1, 1, 2)

        self.verticalLayoutTempCondutor = QtWidgets.QVBoxLayout()
        self.verticalLayoutTempCondutor.setObjectName("verticalLayoutTempCondutor")
        
        self.labelTempCondutor = QtWidgets.QLabel(self.tab)
        self.labelTempCondutor.setFont(font)
        self.labelTempCondutor.setObjectName("labelTempCondutor")
        self.verticalLayoutTempCondutor.addWidget(self.labelTempCondutor)
        
        self.comboBoxTempCondutor = QtWidgets.QComboBox(self.tab)
        self.comboBoxTempCondutor.setFont(font)
        self.comboBoxTempCondutor.setObjectName("comboBoxTempCondutor")
        self.comboBoxTempCondutor.setToolTip("<html><head/><body><p>Escolha a temperatura de trabalho dos condutores do circuito.</p></body></html>")
        for item in self.temperaturaCondutor:
            self.comboBoxTempCondutor.addItem(item)
        self.verticalLayoutTempCondutor.addWidget(self.comboBoxTempCondutor)
        
        self.gridLayout.addLayout(self.verticalLayoutTempCondutor, 2, 3, 1, 1)

        self.verticalLayoutTempAmbiente = QtWidgets.QVBoxLayout()
        self.verticalLayoutTempAmbiente.setObjectName("verticalLayoutTempAmbiente")
        
        self.labelTempAmbiente = QtWidgets.QLabel(self.tab)
        self.labelTempAmbiente.setFont(font)
        self.labelTempAmbiente.setObjectName("labelTempAmbiente")
        self.verticalLayoutTempAmbiente.addWidget(self.labelTempAmbiente)
        
        self.comboBoxTempAmbiente = QtWidgets.QComboBox(self.tab)
        self.comboBoxTempAmbiente.setFont(font)
        self.comboBoxTempAmbiente.setObjectName("comboBoxTempAmbiente")
        self.comboBoxTempAmbiente.setToolTip("<html><head/><body><p>Escolha a temperatura ambiente de trabalho dos condutores do circuito.</p></body></html>")
        for item in self.temperaturaAmbiente:
            self.comboBoxTempAmbiente.addItem(item)
        self.verticalLayoutTempAmbiente.addWidget(self.comboBoxTempAmbiente)
        
        self.gridLayout.addLayout(self.verticalLayoutTempAmbiente, 3, 0, 1, 1)

        self.verticalLayoutTipoIsolamento = QtWidgets.QVBoxLayout()
        self.verticalLayoutTipoIsolamento.setObjectName("verticalLayoutTipoIsolamento")
        
        self.labelTipoIsolamento = QtWidgets.QLabel(self.tab)
        self.labelTipoIsolamento.setFont(font)
        self.labelTipoIsolamento.setObjectName("labelTipoIsolamento")
        self.verticalLayoutTipoIsolamento.addWidget(self.labelTipoIsolamento)
        
        self.comboBoxTipoIsolamento = QtWidgets.QComboBox(self.tab)
        self.comboBoxTipoIsolamento.setFont(font)
        self.comboBoxTipoIsolamento.setObjectName("comboBoxTipoIsolamento")
        self.comboBoxTipoIsolamento.setToolTip("<html><head/><body><p>Escolha o tipo de isolamento dos condutores do circuito.</p></body></html>")
        for item in self.isolamento:
            self.comboBoxTipoIsolamento.addItem(item)
        self.verticalLayoutTipoIsolamento.addWidget(self.comboBoxTipoIsolamento)
        
        self.gridLayout.addLayout(self.verticalLayoutTipoIsolamento, 3, 1, 1, 1)

        self.verticalLayoutComprimento = QtWidgets.QVBoxLayout()
        self.verticalLayoutComprimento.setObjectName("verticalLayoutComprimento")
        
        self.labelComprimento = QtWidgets.QLabel(self.tab)
        self.labelComprimento.setFont(font)
        self.labelComprimento.setObjectName("labelComprimento")
        self.verticalLayoutComprimento.addWidget(self.labelComprimento)
        
        self.doubleSpinBoxComprimento = QtWidgets.QDoubleSpinBox(self.tab)
        self.doubleSpinBoxComprimento.setFont(font)
        self.doubleSpinBoxComprimento.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.doubleSpinBoxComprimento.setMaximum(999999.99)
        self.doubleSpinBoxComprimento.setObjectName("doubleSpinBoxComprimento")
        self.doubleSpinBoxComprimento.setToolTip("<html><head/><body><p>insira o comprimento do circuito.</p></body></html>")
        self.verticalLayoutComprimento.addWidget(self.doubleSpinBoxComprimento)
        
        self.gridLayout.addLayout(self.verticalLayoutComprimento, 3, 2, 1, 1)

        self.verticalLayoutResistividadeSolo = QtWidgets.QVBoxLayout()
        self.verticalLayoutResistividadeSolo.setObjectName("verticalLayoutResistividadeSolo")
        
        self.labelResistividadeSolo = QtWidgets.QLabel(self.tab)
        self.labelResistividadeSolo.setFont(font)
        self.labelResistividadeSolo.setObjectName("labelResistividadeSolo")
        self.verticalLayoutResistividadeSolo.addWidget(self.labelResistividadeSolo)
        
        self.comboBoxResistividadeSolo = QtWidgets.QComboBox(self.tab)
        self.comboBoxResistividadeSolo.setFont(font)
        self.comboBoxResistividadeSolo.setObjectName("comboBoxResistividadeSolo")
        self.comboBoxResistividadeSolo.setToolTip("<html><head/><body><p>Escolha a resisitividade térmica do solo em estará o circuito.</p></body></html>")
        for item in self.resistividade:
            self.comboBoxResistividadeSolo.addItem(item)
        self.verticalLayoutResistividadeSolo.addWidget(self.comboBoxResistividadeSolo)
        
        self.gridLayout.addLayout(self.verticalLayoutResistividadeSolo, 3, 3, 1, 1)
        
        self.verticalLayoutFormaAgrupamento = QtWidgets.QVBoxLayout()
        self.verticalLayoutFormaAgrupamento.setObjectName("verticalLayoutFormaAgrupamento")
        
        self.labelFormaAgrupamento = QtWidgets.QLabel(self.tab)
        self.labelFormaAgrupamento.setFont(font)
        self.labelFormaAgrupamento.setObjectName("labelFormaAgrupamento")
        self.verticalLayoutFormaAgrupamento.addWidget(self.labelFormaAgrupamento)
        
        self.comboBoxFormaAgrupamento = QtWidgets.QComboBox(self.tab)
        self.comboBoxFormaAgrupamento.setFont(font)
        self.comboBoxFormaAgrupamento.setObjectName("comboBoxFormaAgrupamento")
        self.comboBoxFormaAgrupamento.setToolTip("<html><head/><body><p>Escolha a forma de agrupamento do circuito.</p></body></html>")
        for item in self.formaAgrupamento:
            self.comboBoxFormaAgrupamento.addItem(item)
        self.verticalLayoutFormaAgrupamento.addWidget(self.comboBoxFormaAgrupamento)
        self.gridLayout.addLayout(self.verticalLayoutFormaAgrupamento, 4, 0, 1, 2)                

        self.verticalLayoutCircuitosAgrupados = QtWidgets.QVBoxLayout()
        self.verticalLayoutCircuitosAgrupados.setObjectName("verticalLayoutCircuitosAgrupados")
        
        self.labelCircuitosAgrupados = QtWidgets.QLabel(self.tab)
        self.labelCircuitosAgrupados.setFont(font)
        self.labelCircuitosAgrupados.setObjectName("labelCircuitosAgrupados")
        self.verticalLayoutCircuitosAgrupados.addWidget(self.labelCircuitosAgrupados)
        
        self.comboBoxCircuitosAgrupados = QtWidgets.QComboBox(self.tab)
        self.comboBoxCircuitosAgrupados.setFont(font)
        self.comboBoxCircuitosAgrupados.setObjectName("comboBoxCircuitosAgrupados")
        self.comboBoxCircuitosAgrupados.setToolTip("<html><head/><body><p>Escolha a quantidade de circuitos agrupados ao circuito em questão.</p></body></html>")
        for item in self.circuitosAgrupados:
            self.comboBoxCircuitosAgrupados.addItem(item)
        self.verticalLayoutCircuitosAgrupados.addWidget(self.comboBoxCircuitosAgrupados)
        
        self.gridLayout.addLayout(self.verticalLayoutCircuitosAgrupados, 4, 2, 1, 1)

        self.verticalLayoutDistancia = QtWidgets.QVBoxLayout()
        self.verticalLayoutDistancia.setObjectName("verticalLayoutDistancia")
        
        self.labelDistancia = QtWidgets.QLabel(self.tab)
        self.labelDistancia.setFont(font)
        self.labelDistancia.setObjectName("labelDistancia")
        self.verticalLayoutDistancia.addWidget(self.labelDistancia)
        
        self.comboBoxDistancia = QtWidgets.QComboBox(self.tab)
        self.comboBoxDistancia.setFont(font)
        self.comboBoxDistancia.setObjectName("comboBoxDistancia")
        self.comboBoxDistancia.setToolTip("<html><head/><body><p>Escolha a distância entre os cabos agrupados.</p></body></html>")
        for item in self.distanciaCondutores:
            self.comboBoxDistancia.addItem(item)
        self.verticalLayoutDistancia.addWidget(self.comboBoxDistancia)
        
        self.gridLayout.addLayout(self.verticalLayoutDistancia, 4, 3, 1, 1)

        self.verticalLayoutHarmonica = QtWidgets.QVBoxLayout()
        self.verticalLayoutHarmonica.setObjectName("verticalLayoutHarmonica")
        
        self.labelHarmonica = QtWidgets.QLabel(self.tab)
        self.labelHarmonica.setFont(font)
        self.labelHarmonica.setObjectName("labelHarmonica")
        self.verticalLayoutHarmonica.addWidget(self.labelHarmonica)
        
        self.comboBoxHarmonica = QtWidgets.QComboBox(self.tab)
        self.comboBoxHarmonica.setFont(font)
        self.comboBoxHarmonica.setObjectName("comboBoxHarmonica")
        self.comboBoxHarmonica.setToolTip("<html><head/><body><p>Escolha a taxa de 3ª harmônica.</p></body></html>")
        for item in self.harmonica:
            self.comboBoxHarmonica.addItem(item)
        self.verticalLayoutHarmonica.addWidget(self.comboBoxHarmonica)
        
        self.gridLayout.addLayout(self.verticalLayoutHarmonica, 5, 0, 1, 1)

        self.verticalLayoutCorrenteIB = QtWidgets.QVBoxLayout()
        self.verticalLayoutCorrenteIB.setObjectName("verticalLayoutCorrenteIB")
        
        self.labelCorrenteIB = QtWidgets.QLabel(self.tab)
        self.labelCorrenteIB.setFont(font)
        self.labelCorrenteIB.setObjectName("labelCorrenteIB")
        self.verticalLayoutCorrenteIB.addWidget(self.labelCorrenteIB)
        
        self.doubleSpinBoxCorrenteIB = QtWidgets.QDoubleSpinBox(self.tab)
        self.doubleSpinBoxCorrenteIB.setFont(font)
        self.doubleSpinBoxCorrenteIB.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.doubleSpinBoxCorrenteIB.setMaximum(999999.99)
        self.doubleSpinBoxCorrenteIB.setObjectName("doubleSpinBoxCorrenteIB")
        self.doubleSpinBoxCorrenteIB.setToolTip("<html><head/><body><p>Insira a corrente IB.<br> IB = &radic;&nbsp;(I<sub>1</sub><sup>2</sup> + I<sub>i</sub><sup>2</sup> + I<sub>j</sub><sup>2</sup> +...+ I<sub>n</sub><sup>2</sup>).<br> Em que: <br> I<sub>1</sub> = valor eficaz da componente fundamental ou componente 60 Hz. <br> I<sub>i</sub> , I<sub>j</sub> ,...,I<sub>n</sub> = valores eficazes das componentes harmônicas de ordem i, j ... n presentes na corrente de fase.</p></body></html>")
        self.verticalLayoutCorrenteIB.addWidget(self.doubleSpinBoxCorrenteIB)
        
        self.gridLayout.addLayout(self.verticalLayoutCorrenteIB, 5, 1, 1, 1)

        self.lineSetupsGeraRelatorio = QtWidgets.QFrame(self.tab)
        self.lineSetupsGeraRelatorio.setFrameShape(QtWidgets.QFrame.HLine)
        self.lineSetupsGeraRelatorio.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lineSetupsGeraRelatorio.setObjectName("lineSetupsGeraRelatorio")                
        self.gridLayout.addWidget(self.lineSetupsGeraRelatorio, 6, 0, 1, 5)
        
        self.pushButtonAddCircuito = QtWidgets.QPushButton(self.tab)
        self.pushButtonAddCircuito.setStyleSheet("background-color: MidnightBlue; color: White")
        self.pushButtonAddCircuito.setObjectName("pushButtonAddCircuito")
        self.gridLayout.addWidget(self.pushButtonAddCircuito, 7, 0, 1, 5)
        
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        
        self.tableWidget = QtWidgets.QTableWidget(self.tab_2)
        self.tableWidget.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setFont(font)
        
        cabecalhoH = ['Circuito','Corrente Corrigida (A)','Seção Nominal do Condutor Fase (mm²)','Seção Nominal do Condutor Neutro (mm²)',
                      'Seção Nominal do Condutor de Proteção (mm²)','Corrente Máxima do Condutor Fase (A)','Corrente Máxima do Condutor Neutro (A)',
                      'Corrente Máxima do Condutor Proteção (A)','Potência(W)','Tensão (V)','Fator de Potência',
                      'Corrente Não Corrigida','FC Temperatura','FC Resistividade Térmica do Solo',
                      'FC Agrupamento','F Harmônica','Fases','Condutores Carregados','Linha Elétrica',
                      'Condutor','Método de Instalação','Temp. Condutor (ºC)','Linha Subterrânea',
                      'Temp. Ambiente (ºC)','Isolamento','Resistividade Térmica do Solo','Agrupamento',
                      'Circuitos Agrupados','Distância','Taxa 3ª Harmônica','Corrente IB']
        
        self.tableWidget.setColumnCount(len(cabecalhoH))
        i = 0
        for col in cabecalhoH:
            self.tableWidget.setHorizontalHeaderItem(i, QTableWidgetItem(col))            
            i+=1
        self.tableWidget.resizeColumnsToContents()
        
        self.gridLayout_2.addWidget(self.tableWidget, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")

        self.line = QtWidgets.QFrame(self.tab_2)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_2.addWidget(self.line, 1, 0, 1, 1)

        self.gridLayoutGerenciamentoCircuitos = QtWidgets.QGridLayout()
        self.gridLayoutGerenciamentoCircuitos.setObjectName("gridLayoutGerenciamentoCircuitos")
        
        self.pushButtonGerarArquivos = QtWidgets.QPushButton(self.tab_2)
        self.pushButtonGerarArquivos.setFont(font)
        self.pushButtonGerarArquivos.setObjectName("pushButtonGerarArquivos")
        self.gridLayoutGerenciamentoCircuitos.addWidget(self.pushButtonGerarArquivos, 1, 1, 1, 1)
        
        self.pushButtonExcluirCircuito = QtWidgets.QPushButton(self.tab_2)
        self.pushButtonExcluirCircuito.setFont(font)
        self.pushButtonExcluirCircuito.setObjectName("pushButtonExcluirCircuito")
        self.gridLayoutGerenciamentoCircuitos.addWidget(self.pushButtonExcluirCircuito, 1, 0, 1, 1)
        
        self.gridLayout_2.addLayout(self.gridLayoutGerenciamentoCircuitos, 3, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.tab_3)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.textBrowser = QtWidgets.QTextBrowser(self.tab_3)
        self.textBrowser.setObjectName("textBrowser")
        self.horizontalLayout.addWidget(self.textBrowser)
        self.tabWidget.addTab(self.tab_3, "")
                
        self.verticalLayout_20.addWidget(self.tabWidget)

        self.comboBoxTipoSistema.currentIndexChanged.connect(self.determina_condCarregados)
        self.comboBoxTipoLinha.currentIndexChanged.connect(self.change_linhaEletrica)
        self.comboBoxTempAmbiente.currentIndexChanged.connect(self.change_temperaturaAmbiente)

        self.pushButtonAddCircuito.clicked.connect(self.clicked_pushButtonAddCircuito)
        self.pushButtonExcluirCircuito.clicked.connect(self.clicked_excluir_circuitos)
        self.pushButtonGerarArquivos.clicked.connect(self.clicked_salva_csv)

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "DimCabos - Dimensionamento de Cabos Elétricos pela Capacidade de Condução de Corrente"))
        self.labelTensao.setText(_translate("Form", "Tensão (V)"))
        self.labelCondutoresCarregados.setText(_translate("Form", "Condutores carregados"))
        self.labelTipoCondutor.setText(_translate("Form", "Tipo de condutor"))
        self.labelTempAmbiente.setText(_translate("Form", "Temperatura ambiente (ºC)"))
        self.labelPotencia.setText(_translate("Form", "Potência calculada (W)"))
        self.labelTipoCircuito.setText(_translate("Form", "Tipo de circuito"))
        self.labelTipoLinha.setText(_translate("Form", "Tipo de linha elétrica"))
        self.labelFormaAgrupamento.setText(_translate("Form", "Forma de agrupamento"))
        self.labelNomeCircuito.setText(_translate("Form", "Nome do circuito"))
        self.labelTempCondutor.setText(_translate("Form", "Temperatura no condutor (ºC)"))
        self.labelCorrenteIB.setText(_translate("Form", "Corrente IB"))
        self.labelTipoIsolamento.setText(_translate("Form", "Tipo de isolamento"))
        self.labelHarmonica.setText(_translate("Form", "Taxa de 3ª harmônica"))
        self.labelCircuitosAgrupados.setText(_translate("Form", "Circuitos agrupados"))
        self.labelTipoSistema.setText(_translate("Form", "Tipo de sistema"))
        self.labelDistancia.setText(_translate("Form", "Distância"))
        self.labelResistividadeSolo.setText(_translate("Form", "Resistividade térmica do solo"))
        self.labelFatorPotencia.setText(_translate("Form", "Fator de potência"))
        self.labelComprimento.setText(_translate("Form", "Comprimento (m)"))
        self.pushButtonAddCircuito.setText(_translate("Form", "Adicionar Circuito ao Projeto"))
        self.pushButtonGerarArquivos.setText(_translate("Form", "Gerar Arquivo \".csv\""))
        self.pushButtonExcluirCircuito.setText(_translate("Form", "Excluir Circuito"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "Dados do Circuito"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "Tabela de Cálculos"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Form", "Sobre"))
        self.textBrowser.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li align=\"justify\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; font-weight:600; font-style:italic; text-decoration: underline; color:#000000;\">Orietação Geral</span><span style=\" font-size:9pt; font-weight:600; font-style:italic; color:#000000;\">:</span><span style=\" font-size:9pt; font-weight:600; font-style:italic; text-decoration: underline; color:#000000;\"><br /></span><span style=\" font-size:9pt; color:#000000;\"><br />Este software, projetado em Python 3.5, foi elaborado para auxiliar nos estudos de cálculos de dimensionamento de cabos elétricos de baixa tensão pelo critério da capacidade de corrente seguindo a norma NBR 5410/2011.<br />Atenção: Este programa ainda está em sua versão BETA de testes, portanto, não deve ser usado como fonte única de projetos elétricos reais, uma vez que ainda está em fase de desenvolvimento e pode conter erros.</span></li>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" font-size:9pt; color:#000000;\" align=\"justify\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic; text-decoration: underline;\">Versão </span><span style=\" font-weight:600; font-style:italic;\">: </span>DimCabos - BETA1.0</li></ul>\n"
"<li style=\" font-size:9pt; color:#000000;\" align=\"justify\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; font-style:italic; text-decoration: underline;\">Link para Exemplos</span><span style=\" font-weight:600; font-style:italic;\">: </span>www.sclab.com.br/dimcabos</li>\n"
"<li style=\" text-decoration: underline; color:#0000ff;\" align=\"justify\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; font-weight:600; font-style:italic; color:#000000;\">Pacotes utilizados</span><span style=\" font-size:9pt; font-weight:600; font-style:italic; text-decoration:none; color:#000000;\">:<br /></span></li></ul>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 2;\"><li style=\" font-size:9pt; color:#000000;\" align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Pyqt5 5.8.1</li>\n"
"<li style=\" font-size:9pt; color:#000000;\" align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">PyInstaller 3.2.1</li></ul>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" text-decoration: underline; color:#0000ff;\" align=\"justify\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; font-weight:600; font-style:italic; color:#000000;\">Licença</span><span style=\" font-size:9pt; font-weight:600; font-style:italic; text-decoration:none; color:#000000;\">: </span><span style=\" font-size:9pt; text-decoration:none; color:#000000;\">LGPL v3</span></li></ul>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:0px;\"><span style=\" font-size:9pt; color:#000000;\">Este programa é um software livre: você pode redistribuí-lo e/ou  modificá-lo sob os termos da GNU Lesser General Public License (LGPL) publicada pela Free Software Foundation (FSF),  na versão 3 da licença.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:0px;\"><span style=\" font-size:9pt; color:#000000;\">Este programa é distribuído na esperança de que possa ser útil, mas SEM NENHUMA GARANTIA; sem garantia implícita de ADEQUAÇÃO a qualquer MERCADO ou APLICAÇÃO EM PARTICULAR. Veja a GNU LGPL (Lesser General Public License) para mais detalhes.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:0px;\"><span style=\" font-size:9pt; color:#000000;\">Veja a cópia dessa licença em sua língua original em:  www.gnu.org/licenses/</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:1; text-indent:0px;\"><span style=\" font-size:9pt; color:#000000;\">Todo o código pode ser encontrado em: github.com/guilhermetabordaribas/sclab-dimcabos</span></p>\n"
"<ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" text-decoration: underline; color:#0000ff;\" align=\"justify\" style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:9pt; font-weight:600; font-style:italic; color:#000000;\">Doações</span><span style=\" font-size:9pt; font-weight:600; font-style:italic; text-decoration:none; color:#000000;\">: </span><span style=\" font-size:9pt; text-decoration:none; color:#000000;\">www.sclab.com.br/doacoes</span></li></ul>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; color:#000000;\"><br /></p></body></html>"))

    def determina_condCarregados(self):
        self.comboBoxTipoLinha.setCurrentIndex(0)
        
        if self.comboBoxTipoSistema.currentText() in ['Bifásico (2F + N)', 'Bifásico com Terra (2F + N + T)',
                                                      'Trifásico (3F + N)', 'Trifásico com Terra (3F + N + T)']:

            self.comboBoxHarmonica.setEnabled(True)
            self.doubleSpinBoxCorrenteIB.setEnabled(True)
        else:
            self.comboBoxHarmonica.setEnabled(False)
            self.doubleSpinBoxCorrenteIB.setEnabled(False)

    def change_linhaEletrica(self):
        self.comboBoxTipoCondutor.setCurrentIndex(0)
        self.comboBoxCondutoresCarregados.setCurrentIndex(0)
        self.comboBoxDistancia.setCurrentIndex(0)
        
        exclui_isolado = ['Afastado da parede ou suspenso por cabo de suporte (unipolar)',
                          'Afastado da parede ou suspenso por cabo de suporte (multipolar)',
                          'Bandejas não perfuradas ou prateleiras','Bandejas perfuradas (horizontal ou vertical)(unipolar)',
                          'Bandejas perfuradas (horizontal ou vertical)(multipolar)','Canaleta ventilada no piso ou solo',
                          'Diretamente em espaço de construção - 1,5De ≤ V < 5De','Diretamente em espaço de construção - 5De ≤ V ≤ 50De',
                          'Eletroduto de seção não circular embutido em alvenaria','Diretamente enterrado','Eletroduto em espaço de construção',
                          'Eletroduto enterrado no solo ou canaleta não ventilada no solo','Embutimento direto em alvenaria',
                          'Embutimento direto em caixilho de porta ou janela','Embutimento direto em parede isolante',
                          'Fixação direta à parede ou teto','Forro falso ou piso elevado - 1,5De ≤ V < 5De',
                          'Forro falso ou piso elevado - 5De ≤ V ≤ 50De','Leitos, suportes horizontais ou telas (unipolar)',
                          'Leitos, suportes horizontais ou telas (multipolar)']

        exclui_unipolar = ['Afastado da parede ou suspenso por cabo de suporte (multipolar)',
                           'Bandejas perfuradas (horizontal ou vertical)(multipolar)',
                           'Eletroduto de seção não circular embutido em alvenaria - 1,5De ≤ V < 5De',
                           'Eletroduto de seção não circular embutido em alvenaria - 5De ≤ V < 50De',
                           'Eletroduto em canaleta ventilada no piso ou solo',
                           'Eletroduto em espaço de construção - 1,5De ≤ V < 20De','Eletroduto em espaço de construção - V ≥ 20De',
                           'Eletroduto embutido em caixilho de porta ou janela','Embutimento direto em parede isolante',
                           'Leitos, suportes horizontais ou telas (multipolar)','Sobre isoladores']

        exclui_multipolar =['Afastado da parede ou suspenso por cabo de suporte (unipolar)',
                            'Bandejas perfuradas (horizontal ou vertical)(unipolar)',
                            'Eletroduto de seção não circular embutido em alvenaria - 1,5De ≤ V < 5De',
                            'Eletroduto de seção não circular embutido em alvenaria - 5De ≤ V < 50De',
                            'Eletroduto em canaleta fechada - 1,5De ≤ V < 20De','Eletroduto em canaleta fechada - V ≥ 20De',
                            'Eletroduto em canaleta ventilada no piso ou solo','Eletroduto em espaço de construção - 1,5De ≤ V < 20De',
                            'Eletroduto em espaço de construção - V ≥ 20De','Eletroduto embutido em caixilho de porta ou janela',
                            'Moldura','Leitos, suportes horizontais ou telas (unipolar)','Sobre isoladores']

        dois_condutores = ['Monofásico (F + N)', 'Monofásico com Terra (F + N + T)',
                           'Bifásico (2F)','Bifásico com Terra (2F + T)'
                           ]
        
        tres_condutores = ['Bifásico (2F + N)','Bifásico com Terra (2F + N + T)','Trifásico (3F)',
                           'Trifásico (3F + N)','Trifásico com Terra (3F + T)', 'Trifásico com Terra (3F + N + T)'
                           ]

        
        if self.comboBoxTipoLinha.currentText() in exclui_isolado:
            self.comboBoxTipoCondutor.model().item(self.comboBoxTipoCondutor.findText('Isolado', QtCore.Qt.MatchFixedString)).setEnabled(False)
            self.comboBoxCondutoresCarregados.model().item(self.comboBoxCondutoresCarregados.findText('3 condutores carragados no mesmo plano espaçados (Horizontal)', QtCore.Qt.MatchFixedString)).setEnabled(False)
            self.comboBoxCondutoresCarregados.model().item(self.comboBoxCondutoresCarregados.findText('3 condutores carragados no mesmo plano espaçados (Vertical)', QtCore.Qt.MatchFixedString)).setEnabled(False)

            if self.comboBoxTipoLinha.currentText() == 'Diretamente enterrado':
                self.comboBoxDistancia.setEnabled(True)
                self.comboBoxDistancia.model().item(self.comboBoxDistancia.findText('Um diâmetro de de cabo', QtCore.Qt.MatchFixedString)).setEnabled(True)
                self.comboBoxDistancia.model().item(self.comboBoxDistancia.findText('0.125m', QtCore.Qt.MatchFixedString)).setEnabled(True)
                self.comboBoxDistancia.model().item(self.comboBoxDistancia.findText('1.0m', QtCore.Qt.MatchFixedString)).setEnabled(False)
                self.labelDistancia.setText('Distância entre Cabos')
                
            elif self.comboBoxTipoLinha.currentText() == 'Eletroduto enterrado no solo ou canaleta não ventilada no solo':
                self.comboBoxDistancia.setEnabled(True)
                self.comboBoxDistancia.model().item(self.comboBoxDistancia.findText('Um diâmetro de de cabo', QtCore.Qt.MatchFixedString)).setEnabled(False)
                self.comboBoxDistancia.model().item(self.comboBoxDistancia.findText('0.125m', QtCore.Qt.MatchFixedString)).setEnabled(False)
                self.comboBoxDistancia.model().item(self.comboBoxDistancia.findText('1.0m', QtCore.Qt.MatchFixedString)).setEnabled(True)
                self.labelDistancia.setText('Distância entre Eletrodutos')
            else:
                self.comboBoxDistancia.setEnabled(False)
                
        else:
            self.comboBoxTipoCondutor.model().item(self.comboBoxTipoCondutor.findText('Isolado', QtCore.Qt.MatchFixedString)).setEnabled(True)
            self.comboBoxCondutoresCarregados.model().item(self.comboBoxCondutoresCarregados.findText('3 condutores carragados no mesmo plano espaçados (Horizontal)', QtCore.Qt.MatchFixedString)).setEnabled(True)
            self.comboBoxCondutoresCarregados.model().item(self.comboBoxCondutoresCarregados.findText('3 condutores carragados no mesmo plano espaçados (Vertical)', QtCore.Qt.MatchFixedString)).setEnabled(True)

        if self.comboBoxTipoLinha.currentText() in exclui_unipolar:
            self.comboBoxTipoCondutor.model().item(self.comboBoxTipoCondutor.findText('Unipolar', QtCore.Qt.MatchFixedString)).setEnabled(False)
            self.comboBoxCondutoresCarregados.model().item(self.comboBoxCondutoresCarregados.findText('2 condutores carregados justapostos', QtCore.Qt.MatchFixedString)).setEnabled(False)
            self.comboBoxCondutoresCarregados.model().item(self.comboBoxCondutoresCarregados.findText('3 condutores carregados em triófilo', QtCore.Qt.MatchFixedString)).setEnabled(False)
            self.comboBoxCondutoresCarregados.model().item(self.comboBoxCondutoresCarregados.findText('3 condutores carregados no mesmo plano justapostos', QtCore.Qt.MatchFixedString)).setEnabled(False)

            if self.comboBoxTipoLinha.currentText() == 'Diretamente enterrado':
                self.comboBoxDistancia.setEnabled(True)
                self.comboBoxDistancia.model().item(self.comboBoxDistancia.findText('Um diâmetro de de cabo', QtCore.Qt.MatchFixedString)).setEnabled(True)
                self.comboBoxDistancia.model().item(self.comboBoxDistancia.findText('0.125m', QtCore.Qt.MatchFixedString)).setEnabled(True)
                self.comboBoxDistancia.model().item(self.comboBoxDistancia.findText('1.0m', QtCore.Qt.MatchFixedString)).setEnabled(False)
                self.labelDistancia.setText('Distância entre Cabos')

            elif self.comboBoxTipoLinha.currentText() == 'Eletroduto enterrado no solo ou canaleta não ventilada no solo':
                self.comboBoxDistancia.setEnabled(True)
                self.comboBoxDistancia.model().item(self.comboBoxDistancia.findText('Um diâmetro de de cabo', QtCore.Qt.MatchFixedString)).setEnabled(False)
                self.comboBoxDistancia.model().item(self.comboBoxDistancia.findText('0.125m', QtCore.Qt.MatchFixedString)).setEnabled(False)
                self.comboBoxDistancia.model().item(self.comboBoxDistancia.findText('1.0m', QtCore.Qt.MatchFixedString)).setEnabled(True)
                self.labelDistancia.setText('Distância entre Cabos')

            else:
                self.comboBoxCondutoresCarregados.model().item(self.comboBoxCondutoresCarregados.findText('2 condutores carregados justapostos', QtCore.Qt.MatchFixedString)).setEnabled(True)
                self.comboBoxCondutoresCarregados.model().item(self.comboBoxCondutoresCarregados.findText('3 condutores carregados em triófilo', QtCore.Qt.MatchFixedString)).setEnabled(True)
                self.comboBoxCondutoresCarregados.model().item(self.comboBoxCondutoresCarregados.findText('3 condutores carregados no mesmo plano justapostos', QtCore.Qt.MatchFixedString)).setEnabled(True)
        else:
            self.comboBoxTipoCondutor.model().item(self.comboBoxTipoCondutor.findText('Unipolar', QtCore.Qt.MatchFixedString)).setEnabled(True)    

        if self.comboBoxTipoLinha.currentText() in exclui_multipolar:
            self.comboBoxTipoCondutor.model().item(self.comboBoxTipoCondutor.findText('Multipolar', QtCore.Qt.MatchFixedString)).setEnabled(False)

            if self.comboBoxTipoLinha.currentText() == 'Diretamente enterrado':
                self.comboBoxDistancia.setEnabled(True)
                self.comboBoxDistancia.model().item(self.comboBoxDistancia.findText('Um diâmetro de de cabo', QtCore.Qt.MatchFixedString)).setEnabled(True)
                self.comboBoxDistancia.model().item(self.comboBoxDistancia.findText('0.125m', QtCore.Qt.MatchFixedString)).setEnabled(True)
                self.comboBoxDistancia.model().item(self.comboBoxDistancia.findText('1.0m', QtCore.Qt.MatchFixedString)).setEnabled(False)
                self.labelDistancia.setText('Distância entre Cabos')

            elif self.comboBoxTipoLinha.currentText() == 'Eletroduto enterrado no solo ou canaleta não ventilada no solo':
                self.comboBoxDistancia.setEnabled(True)
                self.comboBoxDistancia.model().item(self.comboBoxDistancia.findText('Um diâmetro de de cabo', QtCore.Qt.MatchFixedString)).setEnabled(False)
                self.comboBoxDistancia.model().item(self.comboBoxDistancia.findText('0.125m', QtCore.Qt.MatchFixedString)).setEnabled(False)
                self.comboBoxDistancia.model().item(self.comboBoxDistancia.findText('1.0m', QtCore.Qt.MatchFixedString)).setEnabled(True)
                self.labelDistancia.setText('Distância entre Eletrodutos')

            else:
                self.comboBoxDistancia.setEnabled(False)

        else:
            self.comboBoxTipoCondutor.model().item(self.comboBoxTipoCondutor.findText('Multipolar', QtCore.Qt.MatchFixedString)).setEnabled(True)

        if self.comboBoxTipoLinha.currentText() == 'Afastado da parede ou suspenso por cabo de suporte (unipolar)':
            self.comboBoxCondutoresCarregados.model().item(self.comboBoxCondutoresCarregados.findText('2 condutores carregados', QtCore.Qt.MatchFixedString)).setEnabled(False)
            self.comboBoxCondutoresCarregados.model().item(self.comboBoxCondutoresCarregados.findText('3 condutores carregados', QtCore.Qt.MatchFixedString)).setEnabled(False)
            self.comboBoxCondutoresCarregados.model().item(self.comboBoxCondutoresCarregados.findText('2 condutores carregados justapostos', QtCore.Qt.MatchFixedString)).setEnabled(True)
            self.comboBoxCondutoresCarregados.model().item(self.comboBoxCondutoresCarregados.findText('3 condutores carregados em triófilo', QtCore.Qt.MatchFixedString)).setEnabled(True)
            self.comboBoxCondutoresCarregados.model().item(self.comboBoxCondutoresCarregados.findText('3 condutores carregados no mesmo plano justapostos', QtCore.Qt.MatchFixedString)).setEnabled(True)
            
        elif self.comboBoxTipoLinha.currentText() == 'Bandejas perfuradas (horizontal ou vertical)(unipolar)':
            self.comboBoxCondutoresCarregados.model().item(self.comboBoxCondutoresCarregados.findText('2 condutores carregados', QtCore.Qt.MatchFixedString)).setEnabled(False)
            self.comboBoxCondutoresCarregados.model().item(self.comboBoxCondutoresCarregados.findText('3 condutores carregados', QtCore.Qt.MatchFixedString)).setEnabled(False)
            self.comboBoxCondutoresCarregados.model().item(self.comboBoxCondutoresCarregados.findText('2 condutores carregados justapostos', QtCore.Qt.MatchFixedString)).setEnabled(True)
            self.comboBoxCondutoresCarregados.model().item(self.comboBoxCondutoresCarregados.findText('3 condutores carregados em triófilo', QtCore.Qt.MatchFixedString)).setEnabled(True)
            self.comboBoxCondutoresCarregados.model().item(self.comboBoxCondutoresCarregados.findText('3 condutores carregados no mesmo plano justapostos', QtCore.Qt.MatchFixedString)).setEnabled(True)

        elif self.comboBoxTipoLinha.currentText() == 'Leitos, suportes horizontais ou telas (unipolar)':
            self.comboBoxCondutoresCarregados.model().item(self.comboBoxCondutoresCarregados.findText('2 condutores carregados', QtCore.Qt.MatchFixedString)).setEnabled(False)
            self.comboBoxCondutoresCarregados.model().item(self.comboBoxCondutoresCarregados.findText('3 condutores carregados', QtCore.Qt.MatchFixedString)).setEnabled(False)
            self.comboBoxCondutoresCarregados.model().item(self.comboBoxCondutoresCarregados.findText('2 condutores carregados justapostos', QtCore.Qt.MatchFixedString)).setEnabled(True)
            self.comboBoxCondutoresCarregados.model().item(self.comboBoxCondutoresCarregados.findText('3 condutores carregados em triófilo', QtCore.Qt.MatchFixedString)).setEnabled(True)
            self.comboBoxCondutoresCarregados.model().item(self.comboBoxCondutoresCarregados.findText('3 condutores carregados no mesmo plano justapostos', QtCore.Qt.MatchFixedString)).setEnabled(True)

        elif self.comboBoxTipoLinha.currentText() == 'Sobre isoladores':
            self.comboBoxCondutoresCarregados.model().item(self.comboBoxCondutoresCarregados.findText('2 condutores carregados', QtCore.Qt.MatchFixedString)).setEnabled(False)
            self.comboBoxCondutoresCarregados.model().item(self.comboBoxCondutoresCarregados.findText('3 condutores carregados', QtCore.Qt.MatchFixedString)).setEnabled(False)
            self.comboBoxCondutoresCarregados.model().item(self.comboBoxCondutoresCarregados.findText('3 condutores carragados no mesmo plano espaçados (Horizontal)', QtCore.Qt.MatchFixedString)).setEnabled(True)
            self.comboBoxCondutoresCarregados.model().item(self.comboBoxCondutoresCarregados.findText('3 condutores carragados no mesmo plano espaçados (Vertical)', QtCore.Qt.MatchFixedString)).setEnabled(True)

        elif self.comboBoxTipoLinha.currentText() == 'Canaleta fechada no piso, solo ou parede':
            self.comboBoxDistancia.setEnabled(False)

        elif self.comboBoxTipoLinha.currentText() == 'Eletrocalha':
            self.comboBoxDistancia.setEnabled(False)

        elif self.comboBoxTipoLinha.currentText() == 'Eletroduto aparente':
            self.comboBoxDistancia.setEnabled(False)

        elif self.comboBoxTipoLinha.currentText() == 'Eletroduto embutido em alvenaria':
            self.comboBoxDistancia.setEnabled(False)
            self.comboBoxCondutoresCarregados.model().item(self.comboBoxCondutoresCarregados.findText('2 condutores carregados justapostos', QtCore.Qt.MatchFixedString)).setEnabled(False)

        elif self.comboBoxTipoLinha.currentText() == 'Eletroduto embutido em parede isolante':
            self.comboBoxDistancia.setEnabled(False)

        else:
            self.comboBoxCondutoresCarregados.model().item(self.comboBoxCondutoresCarregados.findText('2 condutores carregados', QtCore.Qt.MatchFixedString)).setEnabled(True)
            self.comboBoxCondutoresCarregados.model().item(self.comboBoxCondutoresCarregados.findText('3 condutores carregados', QtCore.Qt.MatchFixedString)).setEnabled(True)
            self.comboBoxCondutoresCarregados.model().item(self.comboBoxCondutoresCarregados.findText('2 condutores carregados justapostos', QtCore.Qt.MatchFixedString)).setEnabled(False)
            self.comboBoxCondutoresCarregados.model().item(self.comboBoxCondutoresCarregados.findText('3 condutores carregados em triófilo', QtCore.Qt.MatchFixedString)).setEnabled(False)
            self.comboBoxCondutoresCarregados.model().item(self.comboBoxCondutoresCarregados.findText('3 condutores carregados no mesmo plano justapostos', QtCore.Qt.MatchFixedString)).setEnabled(False)
            self.comboBoxCondutoresCarregados.model().item(self.comboBoxCondutoresCarregados.findText('3 condutores carragados no mesmo plano espaçados (Horizontal)', QtCore.Qt.MatchFixedString)).setEnabled(False)
            self.comboBoxCondutoresCarregados.model().item(self.comboBoxCondutoresCarregados.findText('3 condutores carragados no mesmo plano espaçados (Vertical)', QtCore.Qt.MatchFixedString)).setEnabled(False)

        if self.comboBoxTipoSistema.currentText() in dois_condutores:
            self.comboBoxCondutoresCarregados.model().item(self.comboBoxCondutoresCarregados.findText('3 condutores carregados', QtCore.Qt.MatchFixedString)).setEnabled(False)
            self.comboBoxCondutoresCarregados.model().item(self.comboBoxCondutoresCarregados.findText('3 condutores carregados em triófilo', QtCore.Qt.MatchFixedString)).setEnabled(False)
            self.comboBoxCondutoresCarregados.model().item(self.comboBoxCondutoresCarregados.findText('3 condutores carregados no mesmo plano justapostos', QtCore.Qt.MatchFixedString)).setEnabled(False)
            self.comboBoxCondutoresCarregados.model().item(self.comboBoxCondutoresCarregados.findText('3 condutores carragados no mesmo plano espaçados (Horizontal)', QtCore.Qt.MatchFixedString)).setEnabled(False)
            self.comboBoxCondutoresCarregados.model().item(self.comboBoxCondutoresCarregados.findText('3 condutores carragados no mesmo plano espaçados (Vertical)', QtCore.Qt.MatchFixedString)).setEnabled(False)

        if self.comboBoxTipoSistema.currentText() in tres_condutores:
            self.comboBoxCondutoresCarregados.model().item(self.comboBoxCondutoresCarregados.findText('2 condutores carregados', QtCore.Qt.MatchFixedString)).setEnabled(False)
            self.comboBoxCondutoresCarregados.model().item(self.comboBoxCondutoresCarregados.findText('2 condutores carregados justapostos', QtCore.Qt.MatchFixedString)).setEnabled(False)

            
    def change_temperaturaAmbiente(self):
        self.comboBoxTipoIsolamento.setCurrentIndex(0)
        exclui_pvc = ['65', '70', '75', '80']
        
        if self.comboBoxTempAmbiente.currentText() in exclui_pvc:
            self.comboBoxTipoIsolamento.model().item(self.comboBoxTipoIsolamento.findText('PVC', QtCore.Qt.MatchFixedString)).setEnabled(False)
        else:
            self.comboBoxTipoIsolamento.model().item(self.comboBoxTipoIsolamento.findText('PVC', QtCore.Qt.MatchFixedString)).setEnabled(True)

    def clicked_pushButtonAddCircuito(self):
        if self.lineEditNomeCircuito.text() == '':
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText('Insira um nome para o circuito.')
            msg.setWindowTitle("Atenção - Inserir Nome do Circuito")
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msg.exec_()
        elif self.comboBoxTipoCircuito.currentText() == '':
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText('Escolha o tipo do circuito, sua finalidade.')
            msg.setWindowTitle("Atenção - Escolher Tipo do Circuito")
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msg.exec_()
        elif self.doubleSpinBoxPotencia.value() == 0.0:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText('Insira o valor da potência (W).')
            msg.setWindowTitle("Atenção - Inserir Potência do Circuito")
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msg.exec_()
        elif self.comboBoxTipoSistema.currentText() == '':
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText('Escolha o tipo de Sistema.')
            msg.setWindowTitle("Atenção - Escolher Tipo de Sistema")
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msg.exec_()
        elif self.doubleSpinBoxTensao.value() == 0.0:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText('Insira a '+self.labelTensao.text()+' do circuito.')
            msg.setWindowTitle("Atenção - Inserir Tensão")
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msg.exec_()
        elif self.doubleSpinBoxFatorPotencia.value() == 0.0:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText('Insira um fator de potência do circuito. Valor deve ser diferente de zero.')
            msg.setWindowTitle("Atenção - Inserir Fator de Potência")
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msg.exec_()
        elif self.comboBoxTipoLinha.currentText() == '':
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText('Escolha um tipo de linha elétrica.')
            msg.setWindowTitle("Atenção - Escolher Linha Elétrica")
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msg.exec_()
        elif self.comboBoxTipoCondutor.currentText() == '':
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText('Escolha um tipo de condutor.')
            msg.setWindowTitle("Atenção - Escolher Condutor")
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msg.exec_()
        elif self.comboBoxCondutoresCarregados.currentText() == '':
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText('Escolha a quantidade de condutores carregados.')
            msg.setWindowTitle("Atenção - Escolher Quantidadde de Condutores Carregados")
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msg.exec_()
        elif self.comboBoxTempCondutor.currentText() == '':
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText('Escolha a temperatura de operação do condutor.')
            msg.setWindowTitle("Atenção - Escolher Temperatura do Condutor")
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msg.exec_()
        elif self.comboBoxTempAmbiente.currentText() == '':
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText('Escolha a temperatura ambiente de operação.')
            msg.setWindowTitle("Atenção - Escolher Temperatura Ambiente")
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msg.exec_()
        elif self.comboBoxTipoIsolamento.currentText() == '':
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText('Escolha o tipo de isolamento do condutor.')
            msg.setWindowTitle("Atenção - Escolher Isolamento")
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msg.exec_()
        elif self.doubleSpinBoxComprimento.value() == 0.0:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText('Insira o comprimento do circuito condutor.')
            msg.setWindowTitle("Atenção - Inserir Comprimento")
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msg.exec_()
        elif self.comboBoxResistividadeSolo.currentText() == '':
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText('Escolha a resistividade térmica do solo.')
            msg.setWindowTitle("Atenção - Escolher Resistividade do Solo")
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msg.exec_()
        elif self.comboBoxFormaAgrupamento.currentText() == '':
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText('Escolha a forma de agrupamento do circuito.')
            msg.setWindowTitle("Atenção - Escolher Agrupamento")
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msg.exec_()
        elif self.comboBoxCircuitosAgrupados.currentText() == '':
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText('Escolha a quantidade de circuitos agrupados.')
            msg.setWindowTitle("Atenção - Escolher Quantidade de Circuitos Agrupados")
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msg.exec_()
        elif self.comboBoxCircuitosAgrupados.currentText() == '':
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText('Escolha a quantidade de circuitos agrupados.')
            msg.setWindowTitle("Atenção - Escolher Quantidade de Circuitos Agrupados")
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msg.exec_()
        elif self.comboBoxDistancia.isEnabled() and self.comboBoxDistancia.currentText() == '':
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText('Escolha a '+self.labelDistancia.text()+'.')
            msg.setWindowTitle("ffffAtenção - Escolher Quantidade de Circuitos Agrupados")
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msg.exec_()
        elif  self.comboBoxHarmonica.isEnabled() and self.comboBoxHarmonica.currentText() == '':
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText('Escolha a taxa de 3ª Harmônica.')
            msg.setWindowTitle("Atenção - Escolher 3ª Harmônica")
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msg.exec_()
        elif self.doubleSpinBoxCorrenteIB.isEnabled() and self.doubleSpinBoxCorrenteIB.value() == 0.0:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Warning)
            msg.setText('Insira a Corrente IB. CorrenteIB é a corrente definida pela raiz quadrada da soma do quadrado da corrente fundamental ao quadrado de suas harmônicas. Ela deve ser ao menos maior que a corrente nominal do projeto.')
            msg.setWindowTitle("Atenção - Insira a Corrente IB")
            msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
            msg.exec_()
        else:
            if self.comboBoxTipoLinha.currentText() in ['Canaleta fechada no piso, solo ou parede','Canaleta ventilada no piso ou solo', 'Canaleta ventilada no piso ou solo','Diretamente enterrado','Eletroduto enterrado no solo ou canaleta não ventilada no solo']:
                subterranea = 'Sim'
                resistividade_termica_solo = self.comboBoxResistividadeSolo.currentText()
                distancia_cabos_eletrodutos = self.comboBoxDistancia.currentText()
            else:
                subterranea = 'Não'
                resistividade_termica_solo = '2.5'
                distancia_cabos_eletrodutos = "Desconsiderada"
                
            if self.comboBoxHarmonica.currentText() == '':
                taxa3h = '-'
            else:
                taxa3h = self.comboBoxHarmonica.currentText()

            try:
                secao_cabo = funcoes.Dim_cabo_secao(self.comboBoxTipoCircuito.currentText(),self.doubleSpinBoxPotencia.value(),self.doubleSpinBoxFatorPotencia.value(),
                                                    self.doubleSpinBoxTensao.value(),self.comboBoxTipoSistema.currentText(),
                                                    self.comboBoxTipoLinha.currentText(),self.comboBoxTipoCondutor.currentText(),
                                                    self.comboBoxCondutoresCarregados.currentText(),self.comboBoxTempCondutor.currentText(),
                                                    subterranea,self.comboBoxTempAmbiente.currentText(),self.comboBoxTipoIsolamento.currentText(),
                                                    resistividade_termica_solo,self.comboBoxFormaAgrupamento.currentText(),
                                                    self.comboBoxCircuitosAgrupados.currentText(),distancia_cabos_eletrodutos,
                                                    self.comboBoxHarmonica.currentText(),self.doubleSpinBoxCorrenteIB.value()).calcula()
            
                self.resultado.append([self.lineEditNomeCircuito.text(),secao_cabo[0],secao_cabo[1],secao_cabo[2],secao_cabo[3],secao_cabo[4],
                                       secao_cabo[5],secao_cabo[6],
                                       str(self.doubleSpinBoxPotencia.value()),str(self.doubleSpinBoxTensao.value()),str(self.doubleSpinBoxFatorPotencia.value()),
                                       secao_cabo[7],secao_cabo[8],secao_cabo[9],secao_cabo[10],secao_cabo[11],self.comboBoxTipoSistema.currentText(),
                                       self.comboBoxCondutoresCarregados.currentText(),self.comboBoxTipoLinha.currentText(),self.comboBoxTipoCondutor.currentText(),
                                       secao_cabo[12],self.comboBoxTempCondutor.currentText(),subterranea,self.comboBoxTempAmbiente.currentText(),
                                       self.comboBoxTipoIsolamento.currentText(),resistividade_termica_solo,self.comboBoxFormaAgrupamento.currentText(),
                                       self.comboBoxCircuitosAgrupados.currentText(),distancia_cabos_eletrodutos,
                                       taxa3h,str(self.doubleSpinBoxCorrenteIB.value())])
                        
                self.tableWidget.insertRow(0)
                i = 0
                for item in self.resultado[-1]:
                    self.tableWidget.setItem(0,i, QTableWidgetItem(item))
                    i+=1

            except:
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Warning)
                msg.setText('Nosso programa não conseguiu especificar o erro. Verifique os dados de entrada. Caso o erro persista, envie-nos um email explicando o que ocorreu.')
                msg.setWindowTitle("Atenção - Erro Desconhecido")
                msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
                msg.exec_()
        
    def clicked_excluir_circuitos(self):
        if self.resultado:
            try:
                item = len(self.resultado)-1-self.tableWidget.currentRow()
                self.resultado.pop(item)
                self.tableWidget.removeRow(self.tableWidget.currentRow())
            except:
                msg = QtWidgets.QMessageBox()
                msg.setIcon(QtWidgets.QMessageBox.Warning)
                msg.setText('Escolha na Tabela de Cálculos o circuito a ser excluído.')
                msg.setWindowTitle("Atenção - Selecione uma Linha")
                msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
                msg.exec_()

    def clicked_salva_csv(self):
        filename = QFileDialog.getSaveFileName(None, 'Save File',os.getenv('HOME'))
        if filename and filename[0] != '':
            print(filename)
            saveLine = 'Circuito,Corrente Corrigida (A),Seção Nominal do Condutor Fase (mm²),Seção Nominal do Condutor Neutro (mm²),Seção Nominal do Condutor de Proteção (mm²),Corrente Máxima do Condutor Fase (A),Corrente Máxima do Condutor Neutro (A),Corrente Máxima do Condutor Proteção (A),Potência(W),Tensão (V),Fator de Potência,Corrente Não Corrigida,FC Temperatura,FC Resistividade Térmica do Solo,FC Agrupamento,F Harmônica,Fases,Condutores Carregados,Linha Elétrica,Condutor,Método de Instalação,Temp. Condutor (ºC),Linha Subterrânea,Temp. Ambiente (ºC),Isolamento,Resistividade Térmica do Solo,Agrupamento,Circuitos Agrupados,Distância,Taxa 3ª Harmônica,Corrente IB\n'
            saveFile = open(filename[0], 'a')
            saveFile.write(saveLine)
            saveFile.close()

            for linha in self.resultado:
                saveLine = ','.join(linha) +'\n'
                saveFile = open(filename[0], 'a')
                saveFile.write(saveLine)
                saveFile.close()
        
                
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
