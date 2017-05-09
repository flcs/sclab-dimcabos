import math
import datetime
import sqlite3

from listas_dim_cabos import resistividade_termica, dict_tipo_linha, dict_condutores_carregados, dict_forma_agrupamento, dict_cicuitos_agrupados, dict_cabos_diretamente_enterrados,dict_cabos_eletroduto_enterrado,dict_fch_neutro_bifasico,dict_fch_neutro_trifasico,dict_fch15_neutro_trifasico,dict_cabos_protecao
from bd_execute import DatabaseManager

class Dim_cabo_secao():
    def __init__(self,tipo_circuito,potencia,fp, tensao,n_fases,tipo_linha,
                 tipo_condutor,condutores_carregados,temperatura_condutor,
                 linha_subterranea,temperatura_ambiente,tipo_isolamento,
                 resist_solo,forma_agrup,circ_agrup,dist_cabos_elet,
                 harmonica, correnteIB):

        self.tipo_circuito = tipo_circuito
        self.potencia = potencia
        self.tensao = tensao
        self.n_fases = n_fases
        self.tipo_linha = tipo_linha
        self.tipo_condutor = tipo_condutor
        self.condutores_carregados = condutores_carregados
        self.temperatura_condutor = temperatura_condutor
        self.linha_subterranea = linha_subterranea
        self.tipo_isolamento = tipo_isolamento
        self.temperatura_ambiente = temperatura_ambiente
        self.resist_solo = resist_solo
        self.forma_agrupamento = forma_agrup
        self.cicuitos_agrupados = circ_agrup
        self.distancia_cabos_eletrodutos = dist_cabos_elet
        self.fp = float(fp)
        self.harmonica = harmonica
        self.corrente_ib = correnteIB
        self.fcs = 0
        #self.fct = '' não declarei pos vai receber uma matriz do banco de dados 
        self.fca=''
        self.amb = ''
        self.tabela = ''
        self.sql = ''
        self.metodo = ''
        self.coluna = ''
        
        
    def calcula(self):
        
##        if self.n_fases in ['Monofásico (F + N)', 'Monofásico (2F)', 'Monofásico (2F + N)',
##                            'Monofásico com Terra (2F + T)', 'Monofásico com Terra (2F + N + T)',
##                            'Monofásico com Terra (F + N + T)']:
##            corrente_sc = float(self.potencia)/(float(self.tensao)*self.fp)
##        else:
##            corrente_sc = float(self.potencia)/(float(self.tensao)*self.fp*math.sqrt(3))
        
        corrente_sc = float(self.potencia)/(float(self.tensao)*self.fp)
        
        #determinar fator de correção de tempeatura e resistividade do solo
        if self.linha_subterranea == 'Sim':
            self.amb = 'solo'
            self.fcs = resistividade_termica[self.resist_solo]
        else:
            self.amb = 'ambiente'
            self.fcs = 1.0
            
        if self.tipo_isolamento == 'PVC':
            self.tabela = 'temperatura_pvc'
        else:
            self.tabela = 'temperatura_epr_xlpe'            

        self.dbmgr = DatabaseManager('tabelas_dim_cabos.db')    
        self.sql = 'SELECT ' + self.amb + ' FROM ' + self.tabela + ' WHERE temperatura = ' + str(self.temperatura_ambiente)
        self.fct = self.dbmgr.query(self.sql).fetchall()
            
        #correção pela temperatura
        corrente = corrente_sc/self.fct[0][0]

        #correção pela resistividade do solo.
        corrente = corrente/self.fcs       
        corrente = round(corrente, 2)
        
        #correção agrupamento
        if dict_forma_agrupamento[self.forma_agrupamento] in [1,2,3,4,5]:
            self.tabela = 'uma_camada'
            self.coluna = dict_cicuitos_agrupados[self.cicuitos_agrupados]
            self.linha = dict_forma_agrupamento[self.forma_agrupamento]
            self.sql = 'SELECT ' + self.coluna + ' FROM ' + self.tabela + ' WHERE n = ' + str(self.linha)
            
        elif dict_forma_agrupamento[self.forma_agrupamento] in [6,7,8,9,10]:
            self.tabela = 'mais_de_uma_camada'
            self.linha = dict_forma_agrupamento[self.forma_agrupamento]
            if dict_cicuitos_agrupados[self.cicuitos_agrupados] in ['nove_a_onze_circuitos','doze_a_quize_circuitos','dezesseis_a_dezenove_circuitos','mais_que_vinte_circuitos']:
                self.coluna = 'nove_ou_mais_circuitos'
            else:
                self.coluna = dict_cicuitos_agrupados[self.cicuitos_agrupados]
            self.sql = 'SELECT ' + self.coluna + ' FROM ' + self.tabela + ' WHERE n = ' + str(self.linha)
                    
        elif dict_forma_agrupamento[self.forma_agrupamento] == 11:
            self.tabela = 'cabos_diretamente_enterrados'
            self.coluna = dict_cabos_diretamente_enterrados[self.distancia_cabos_eletrodutos]
            self.linha = self.cicuitos_agrupados
            self.sql = 'SELECT ' + self.coluna + ' FROM ' + self.tabela + ' WHERE n = ' + str(self.linha)

        elif dict_forma_agrupamento[self.forma_agrupamento] == 12:
            if self.tipo_condutor == 'Multipolar':            
                self.tabela = 'multipolares_eletroduto_enterrado'                
                self.coluna = dict_cabos_eletroduto_enterrado[self.distancia_cabos_eletrodutos]
                self.linha = self.cicuitos_agrupados
                self.sql = 'SELECT ' + self.coluna + ' FROM ' + self.tabela + ' WHERE n = ' + str(self.linha)
            else:
                self.tabela = 'unipolares_eletroduto_enterrado'                
                self.coluna = dict_cabos_eletroduto_enterrado[self.distancia_cabos_eletrodutos]
                self.linha = self.cicuitos_agrupados
                self.sql = 'SELECT ' + self.coluna + ' FROM ' + self.tabela + ' WHERE n = ' + str(self.linha)
            
        
        self.fca = self.dbmgr.query(self.sql).fetchall()[0][0]

        corrente = corrente/self.fca              
        
        #correção 3ª harmônica Fase Trifásico 4 Fios
        if (self.harmonica != '<= 15%') and (self.n_fases in ['Trifásico (3F + N)','Trifásico com Terra (3F + N + T)']):
            corrente = corrente/0.86        

        corrente = round(corrente, 2)
        
        #Determinar método de instalçao
        #Utilizou-se o dicionário dict_tipo_linha pois o sqlite não reconhece ç ^ ~ etc.
        self.sql = 'SELECT ' + self.tipo_condutor + ' FROM metodo_instalacao WHERE n = ' + str(dict_tipo_linha[self.tipo_linha])
        self.metodo = self.dbmgr.query(self.sql).fetchall()
        self.metodo = self.metodo[0][0]
        
        #Determinar Tabela de seção
        self.tabela = 'cobre_' + self.temperatura_condutor + '_' + self.metodo + '_secao'
##        print(self.tabela)
        #Determinar coluna pesquisada
        self.coluna = dict_condutores_carregados[self.condutores_carregados]
##        print(self.coluna)
        #determinar cabos fase
        #colunas secao dois_condutores tres_condutores dois_condutores_justapostos tres_condutores_triofilo tres_condutores_justapostos horizontal vertical
        
        self.sql = 'SELECT min(secao) FROM ' + self.tabela + ' WHERE ' + self.coluna + ' IN (SELECT ' + self.coluna + ' FROM ' + self.tabela + ' WHERE ' + self.coluna + ' >= ' + str(corrente) + ')'
##        print(self.sql)
        self.secao_fase = self.dbmgr.query(self.sql).fetchall()        
        self.secao_fase = self.secao_fase[0][0]

        if self.tipo_circuito == 'Iluminação':
            if self.secao_fase < 1.5:
                self.secao_fase = 1.5
        elif self.tipo_circuito == 'Força':
            if self.secao_fase < 2.5:
                self.secao_fase = 2.5

        #Determinar Corrente máxima do cabo fase
        self.sql = 'SELECT ' + self.coluna + ' FROM ' + self.tabela + ' WHERE secao = ' + str(self.secao_fase)
        self.corrente_maxima_fase = self.dbmgr.query(self.sql).fetchall()
        self.corrente_maxima_fase = self.corrente_maxima_fase[0][0]

        #Determinar cabo neutro
        if self.n_fases in ['Monofásico (F + N)', 'Monofásico com Terra (F + N + T)']:
            self.secao_neutro = self.secao_fase
            self.corrente_maxima_neutro = self.corrente_maxima_fase
            self.fch = '-'

        elif self.n_fases in ['Bifásico (2F + N)','Bifásico com Terra (2F + N + T)']:
            if self.harmonica in ['<= 15%', '16% a 33%']:
                self.secao_neutro = self.secao_fase
                self.corrente_maxima_neutro = self.corrente_maxima_fase
                self.fch = '-'
            else:
                self.fch = dict_fch_neutro_bifasico[self.harmonica]
                corrente_neutro = dict_fch_neutro_bifasico[self.harmonica]*self.corrente_ib
                #seção neutro
                self.sql = 'SELECT min(secao) FROM ' + self.tabela + ' WHERE ' + self.coluna + ' IN (SELECT ' + self.coluna + ' FROM ' + self.tabela + ' WHERE ' + self.coluna + ' >= ' + str(corrente_neutro) + ')'
                self.secao_neutro = self.dbmgr.query(self.sql).fetchall()        
                self.secao_neutro = self.secao_neutro[0][0]
                #corrente máxima neutro
                self.sql = 'SELECT ' + self.coluna + ' FROM ' + self.tabela + ' WHERE secao = ' + str(self.secao_neutro)
                self.corrente_maxima_neutro = self.dbmgr.query(self.sql).fetchall()
                self.corrente_maxima_neutro = self.corrente_maxima_neutro[0][0]

        elif self.n_fases in ['Trifásico (3F + N)', 'Trifásico com Terra (3F + N + T)']:
            if self.harmonica == '<= 15%':
                self.fch = '-'
                if self.secao_fase <= 25:
                    self.secao_neutro = self.secao_fase
                    self.corrente_maxima_neutro = self.corrente_maxima_fase                    
                else:
                    self.secao_neutro = dict_fch15_neutro_trifasico[self.secao_fase]
                    #corrente máxima neutro
                    self.sql = 'SELECT ' + self.coluna + ' FROM ' + self.tabela + ' WHERE secao = ' + str(self.secao_neutro)
                    self.corrente_maxima_neutro = self.dbmgr.query(self.sql).fetchall()
                    self.corrente_maxima_neutro = self.corrente_maxima_neutro[0][0]
                
            elif self.harmonica == '16% a 33%':
                self.fch = '-'
                self.secao_neutro = self.secao_fase
                self.corrente_maxima_neutro = self.corrente_maxima_fase
            else:
                self.fch = dict_fch_neutro_trifasico[self.harmonica]
                corrente_neutro = dict_fch_neutro_trifasico[self.harmonica]*self.corrente_ib
                #seção neutro
                self.sql = 'SELECT min(secao) FROM ' + self.tabela + ' WHERE ' + self.coluna + ' IN (SELECT ' + self.coluna + ' FROM ' + self.tabela + ' WHERE ' + self.coluna + ' >= ' + str(corrente_neutro) + ')'
                self.secao_neutro = self.dbmgr.query(self.sql).fetchall()        
                self.secao_neutro = self.secao_neutro[0][0]
                #corrente máxima neutro
                self.sql = 'SELECT ' + self.coluna + ' FROM ' + self.tabela + ' WHERE secao = ' + str(self.secao_neutro)
                self.corrente_maxima_neutro = self.dbmgr.query(self.sql).fetchall()
                self.corrente_maxima_neutro = self.corrente_maxima_neutro[0][0]
                
        elif self.n_fases in ['Bifásico (2F)','Bifásico com Terra (2F + T)','Trifásico (3F)','Trifásico com Terra (3F + T)']:
            self.fch = '-'
            self.secao_neutro = '-'
            self.corrente_maxima_neutro = '-'

        #Determinar cabo proteção
        if self.n_fases in ['Monofásico (F + N)','Bifásico (2F)', 'Bifásico (2F + N)','Trifásico (3F)', 'Trifásico (3F + N)']:
            self.secao_protecao = '-'
            self.corrente_maxima_protecao = '-'
        else:
            if self.secao_fase <= 16:
                self.secao_protecao = self.secao_fase
            else:
                self.secao_protecao = dict_cabos_protecao[self.secao_fase]
            #corrente máxima neutro
            self.sql = 'SELECT ' + self.coluna + ' FROM ' + self.tabela + ' WHERE secao = ' + str(self.secao_protecao)
            self.corrente_maxima_protecao = self.dbmgr.query(self.sql).fetchall()
            self.corrente_maxima_protecao = self.corrente_maxima_protecao[0][0]

            
        return [str(corrente),  str(self.secao_fase), str(self.secao_neutro), str(self.secao_protecao),
                str(self.corrente_maxima_fase), str(self.corrente_maxima_neutro), str(self.corrente_maxima_protecao),str(round(corrente_sc, 2)),
                str(self.fct[0][0]), str(self.fcs), str(self.fca), str(self.fch), str(self.metodo)]
        
