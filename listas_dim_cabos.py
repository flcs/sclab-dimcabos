"""
Copyright (c) 2017 Guilherme Taborda Ribas.

Copyright (c) 2016 Riverbank Computing Limited.

Copyright (c) 2017 The Qt Company.


This file is part of DimCabos.

    DimCabos is free software: you can redistribute it and/or modify
    it under the terms of the GNU Lesser General Public License as published by
    the Free Software Foundation, either version 3 of the License, or any later version.

    DimCabos is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Lesser General Public License for more details.

    You should have received a copy of the GNU Lesser General Public License
    along with EletroCrom.  If not, see <http://www.gnu.org/licenses/>.

"""

lista_tipo_circuito = ['','Iluminação', 'Força', 'Sinalização', 'Controle']

lista_sistema = ['','Monofásico (F + N)', 'Monofásico com Terra (F + N + T)',
                 'Bifásico (2F)', 'Bifásico (2F + N)','Bifásico com Terra (2F + T)',
                 'Bifásico com Terra (2F + N + T)','Trifásico (3F)', 'Trifásico (3F + N)',
                 'Trifásico com Terra (3F + T)', 'Trifásico com Terra (3F + N + T)'
                 ]
#verificar se coloca corrente contínua, e o que muda.

lista_tipo_linha = ['','Afastado da parede ou suspenso por cabo de suporte (unipolar)',
                    'Afastado da parede ou suspenso por cabo de suporte (multipolar)',
                    'Bandejas não perfuradas ou prateleiras',
                    'Bandejas perfuradas (horizontal ou vertical)(unipolar)',
                    'Bandejas perfuradas (horizontal ou vertical)(multipolar)',
                    'Canaleta fechada no piso, solo ou parede',
                    'Canaleta ventilada no piso ou solo',
                    'Diretamente em espaço de construção - 1,5De ≤ V < 5De',
                    'Diretamente em espaço de construção - 5De ≤ V ≤ 50De',
                    'Diretamente enterrado', 'Eletrocalha', 'Eletroduto aparente',
                    'Eletroduto de seção não circular embutido em alvenaria',
                    'Eletroduto de seção não circular embutido em alvenaria - 1,5De ≤ V < 5De',
                    'Eletroduto de seção não circular embutido em alvenaria - 5De ≤ V < 50De',
                    'Eletroduto em canaleta fechada - 1,5De ≤ V < 20De',
                    'Eletroduto em canaleta fechada - V ≥ 20De',
                    'Eletroduto em canaleta ventilada no piso ou solo',
                    'Eletroduto em espaço de construção',
                    'Eletroduto em espaço de construção - 1,5De ≤ V < 20De',
                    'Eletroduto em espaço de construção - V ≥ 20De',
                    'Eletroduto embutido em alvenaria',
                    'Eletroduto embutido em caixilho de porta ou janela',
                    'Eletroduto embutido em parede isolante',
                    'Eletroduto enterrado no solo ou canaleta não ventilada no solo',
                    'Embutimento direto em alvenaria',
                    'Embutimento direto em caixilho de porta ou janela',
                    'Embutimento direto em parede isolante',
                    'Fixação direta à parede ou teto',
                    'Forro falso ou piso elevado - 1,5De ≤ V < 5De',
                    'Forro falso ou piso elevado - 5De ≤ V ≤ 50De',
                    'Leitos, suportes horizontais ou telas (unipolar)',
                    'Leitos, suportes horizontais ou telas (multipolar)',
                    'Moldura','Sobre isoladores',                                      
                    ]

lista_tipo_condutor = ['','Isolado', 'Unipolar', 'Multipolar']
"""
usar essa lista para link de ajuda na escolha da quantidade de condutores
lista_condutores_carregados = ['Monofásico a dois condutores (2 condutores carregados)',
                               'Monofásico a três condutores (2 condutores carregados)',
                               'Duas fases sem neutro (2 condutores carregados)',
                               'Duas fases com neutro (3 condutores carregados)',
                               'Trifásico sem neutro (3 condutores carregados)',
                               'Trifásico com neutro (3 condutores carregados)',
                               ]
"""
lista_condutores_carregados = ['','2 condutores carregados',
                               '3 condutores carregados',
                               '2 condutores carregados justapostos',
                               '3 condutores carregados em triófilo',
                               '3 condutores carregados no mesmo plano justapostos',
                               '3 condutores carragados no mesmo plano espaçados (Horizontal)',
                               '3 condutores carragados no mesmo plano espaçados (Vertical)'
                               ]
lista_tipo_isolamento = ['','PVC', 'EPR', 'XLPE']

lista_temperatura_condutor = ['','70', '90']

lista_temperatura = ['','10', '15', '20',
                     '25', '30', '35',
                     '40', '45', '50',
                     '55', '60', '65',
                     '70', '75', '80']

lista_resistividade_termica_solo = ['','1', '1.5', '2', '2.5', '3']

lista_cicuitos_agrupados = ['','1', '2', '3', '4', '5', '6',
                            '7', '8', '9 a 11', '12 a 15',
                            '16 a 19', 'mais que 20']

lista_distancia_cond_dutos = ['','Nula', 'Um diâmetro de de cabo', '0.125m',
                              '0.25m', '0.5m', '1.0m']

lista_forma_agrupamento = ['','Em feixe: ao ar livre ou sobre superfície; embutidos; em condutos fechados',
                           'Camada única sobre parede, piso ou em bandeja não perfurada ou prateleira',
                           'Camada única no teto',
                           'Camada única em bandeja perfurada',
                           'Camada única sobre leito, suporte, etc.',
                           'Duas camadas', 'Três camadas', 'Quatro ou cinco camadas',
                           'Seis a oito camadas', 'Nove ou mais camadas',
                           'Linhas com cabos diretamente enterrados',
                           'Linhas em eletrodutos diretamente enterrados']

lista_taxa_3_harmonica = ['','<= 15%', '16% a 33%', '33% a 35%',
                          '36% a 40%', '41% a 45%', '46% a 50%',
                          '51% a 55%', '56% a 60%', '61% a 65%',
                          '>= 66%']

resistividade_termica = {'1' : 1.18, '1.5' : 1.1,
                         '2' : 1.05, '2.5' : 1.0,
                         '3' : 0.96}

dict_tipo_linha = {'Afastado da parede ou suspenso por cabo de suporte (unipolar)' : 1,
                    'Afastado da parede ou suspenso por cabo de suporte (multipolar)' : 2,
                    'Bandejas não perfuradas ou prateleiras' : 3,
                    'Bandejas perfuradas (horizontal ou vertical)(unipolar)' : 4,
                    'Bandejas perfuradas (horizontal ou vertical)(multipolar)' : 5,
                    'Canaleta fechada no piso, solo ou parede' :6 ,
                    'Canaleta ventilada no piso ou solo' : 7,
                    'Diretamente em espaço de construção - 1,5De ≤ V < 5De' : 8,
                    'Diretamente em espaço de construção - 5De ≤ V ≤ 50De' : 9,
                    'Diretamente enterrado' : 10, 'Eletrocalha' : 11, 'Eletroduto aparente' : 12,
                    'Eletroduto de seção não circular embutido em alvenaria' : 13,
                    'Eletroduto de seção não circular embutido em alvenaria - 1,5De ≤ V < 5De' : 14,
                    'Eletroduto de seção não circular embutido em alvenaria - 5De ≤ V < 50De' : 15,
                    'Eletroduto em canaleta fechada - 1,5De ≤ V < 20De' : 16,
                    'Eletroduto em canaleta fechada - V ≥ 20De' : 17,
                    'Eletroduto em canaleta ventilada no piso ou solo' : 18,
                    'Eletroduto em espaço de construção' : 19,
                    'Eletroduto em espaço de construção - 1,5De ≤ V < 20De' : 20,
                    'Eletroduto em espaço de construção - V ≥ 20De' : 21,
                    'Eletroduto embutido em alvenaria' : 22,
                    'Eletroduto embutido em caixilho de porta ou janela' : 23,
                    'Eletroduto embutido em parede isolante' : 24,
                    'Eletroduto enterrado no solo ou canaleta não ventilada no solo' : 25,
                    'Embutimento direto em alvenaria' : 26,
                    'Embutimento direto em caixilho de porta ou janela' : 27,
                    'Embutimento direto em parede isolante' : 28,
                    'Fixação direta à parede ou teto' : 29,
                    'Forro falso ou piso elevado - 1,5De ≤ V < 5De' : 30,
                    'Forro falso ou piso elevado - 5De ≤ V ≤ 50De' : 31,
                    'Leitos, suportes horizontais ou telas (unipolar)' : 32,
                    'Leitos, suportes horizontais ou telas (multipolar)' : 33,
                    'Moldura' : 34,'Sobre isoladores' : 35,                                      
                    }

dict_condutores_carregados = {'2 condutores carregados' : 'dois_condutores',
                               '3 condutores carregados' : 'tres_condutores',
                               '2 condutores carregados justapostos' : 'dois_condutores_justapostos',
                               '3 condutores carregados em triófilo' : 'tres_condutores_triofilo',
                               '3 condutores carregados no mesmo plano justapostos' : 'tres_condutores_justapostos',
                               '3 condutores carragados no mesmo plano espaçados (Horizontal)' : 'horizontal',
                               '3 condutores carragados no mesmo plano espaçados (Vertical)' : 'vertical'
                               }

dict_forma_agrupamento = {'Em feixe: ao ar livre ou sobre superfície; embutidos; em condutos fechados':1,
                           'Camada única sobre parede, piso ou em bandeja não perfurada ou prateleira':2,
                           'Camada única no teto':3,
                           'Camada única em bandeja perfurada':4,
                           'Camada única sobre leito, suporte, etc.':5,
                           'Duas camadas':6, 'Três camadas':7, 'Quatro ou cinco camadas':8,
                           'Seis a oito camadas':9, 'Nove ou mais camadas':10,
                           'Linhas com cabos diretamente enterrados':11,
                           'Linhas em eletrodutos diretamente enterrados':12
                          }

dict_cicuitos_agrupados = {'1':'um_circuito', '2':'dois_circuitos', '3':'tres_circuitos',
                           '4':'quatro_circuitos', '5':'cinco_circuitos', '6':'seis_circuitos',
                            '7':'sete_circuitos', '8':'oito_circuitos', '9 a 11':'nove_a_onze_circuitos',
                           '12 a 15':'doze_a_quize_circuitos','16 a 19':'dezesseis_a_dezenove_circuitos',
                           'mais que 20':'mais_que_vinte_circuitos'
                           }

dict_cabos_diretamente_enterrados = {'Nula': 'nula', 'Um diâmetro de de cabo':'um_diametro_de_cabo',
                                     '0.125m':'um_dois_cinco','0.25m':'dois_cinco', '0.5m':'cinco'
                                     }
dict_cabos_eletroduto_enterrado = {'Nula': 'nula','0.25m':'dois_cinco', '0.5m':'cinco', '1.0m': 'um'}

dict_fch_neutro_bifasico = {'<= 15%':1, '16% a 33%':1, '33% a 35%':1.15,
                            '36% a 40%':1.19, '41% a 45%':1.23, '46% a 50%':1.27,
                          '51% a 55%':1.30, '56% a 60%':1.34, '61% a 65%':1.38,
                          '>= 66%':1.41
                            }

dict_fch_neutro_trifasico = {'16% a 33%':1, '33% a 35%':1.15, '36% a 40%':1.19,
                            '41% a 45%':1.24, '46% a 50%':1.35, '51% a 55%':1.45,
                            '56% a 60%':1.55, '61% a 65%':1.64, '>= 66%':1.73
                            }

dict_fch15_neutro_trifasico = {35:25, 50:25, 70:35, 95:50, 120:70, 150:70,
                               185:95, 240:120, 300:150, 400:185, 500:240,
                               630:400, 800:400, 1000:500
                               }

dict_cabos_protecao = {1.5:1.5, 2.5:2.5, 4:4, 6:6, 10:10,
                       16:16, 25:16, 35:16, 50:25, 70:35,
                       95:50, 120:70, 150:95, 185:95, 240:120,
                       300:150, 400:240, 500:240, 630:400,
                       800:400, 1000:500
                       }
