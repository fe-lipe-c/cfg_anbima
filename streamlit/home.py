import pandas as pd
import streamlit as st
import pyield as pyd
import config as cfg

st.markdown(
    """<style>.block-container{max-width: 86rem !important;}</style>""",
    unsafe_allow_html=True,
)


def run_interface():


    st.title("Certificação de Fundamentos em Gestão")
    st.write("---")

    # with open("texts/home_intro.md", "r") as file:
    #     intro = file.read()
    #
    # st.markdown(intro)

    st.markdown(
"""
## CFG - Certificação de Fundamentos em Gestão

### Programa

- [ ] 1 MÉTODOS QUANTITATIVOS
- [ ] 2. ECONOMIA
	- [ ] 2.1 Microeconomia
		- [ ] 2.1.1 Oferta e Demanda
			- [ ] a. Entender e explicar os princípios de oferta e demanda.
			- [ ] b. Descrever causas e efeitos do movimento ao longo das curvas de oferta e demanda.
			- [ ] c. Descrever causas e efeitos do deslocamento das curvas de oferta e demanda.
			- [ ] d. Calcular e interpretar funções de demanda e de oferta, bem como suas formas inversas.
			- [ ] e. Calcular o preço e a quantidade de equilíbrio em um mercado, dadas as funções de demanda e de oferta.
			- [ ] f. Calcular e determinar a existência de excesso de demanda ou excesso de oferta em um mercado, dadas as curvas de oferta e demanda e o preço do bem.
			- [ ] g. Explicar e calcular o excedente do consumidor, o excedente do produtor e o excedente total.
			- [ ] h. Definir e calcular a elasticidade-preço da oferta e da demanda, bem como analisar os diferentes fatores que a influenciam.
			- [ ] i. Explicar e calcular a elasticidade cruzada da demanda.
			- [ ] j. Explicar e calcular a elasticidade-renda da demanda
			- [ ] k. Entender o impacto da regulação governamental (limites de preço, quotas, impostos e subsídios) e interpretar seus efeitos sobre o equilíbrio de mercado.
		- [ ] 2.1.2 Demanda do Consumidor
			- [ ] a. Calcular e interpretar a restrição orçamentária, bem como descrever seu uso no processo de escolha do consumidor.
			- [ ] b. Entender e interpretar uma função de utilidade.
			- [ ] c. Descrever o uso de curvas de indiferença na escolha do consumidor.
			- [ ] d. Definir e comparar bens normais e bens inferiores
			- [ ] e. Definir e comparar bens substitutos e bens complementares
			- [ ] f. Entender e interpretar o efeito renda e o efeito substituição
		- [ ] 2.1.3 Produção, Custos e Lucro da Firma
			- [ ] a. Identificar e descrever os fatores de produção da firma.
			- [ ] b. Calcular e interpretar funções de produção.
			- [ ] c. Calcular, interpretar e comparar o produto total, o produto médio e o produto marginal da firma.
			- [ ] d. Entender e interpretar a existência de retornos marginais decrescentes.
			- [ ] e. Calcular e interpretar o custo fixo e o custo variável de produção.
			- [ ] f. Calcular, interpretar e comparar o custo total, o custo médio e o custo marginal de produção.
			- [ ] g. Descrever e determinar os pontos de break-even e de encerramento de produção.
			- [ ] h. Entender economias e deseconomias de escala e sua relação com o custo médio de produção.
			- [ ] i. Calcular, interpretar e comparar a receita total, a receita média e a receita marginal da firma.
			- [ ] j. Entender e diferenciar o lucro normal e o lucro econômico.
			- [ ] k. Entender a condição de maximização de lucro e determinar a quantidade que maximiza o lucro da firma.
		- [ ] 2.1.4 Estruturas de Mercado
			- [ ] a. Descrever as características de um mercado em competição perfeita e explicar por que empresas em tais mercados são tomadoras de preço, analisando a relação entre demanda, preço e receita.
			- [ ] b. Explicar como uma empresa maximiza lucros em um mercado em competição perfeita, relacionando custo e receita marginal e o conceito de lucro econômico.
			- [ ] c. Distinguir entre a curva de demanda de mercado e a curva de demanda vista pela firma em competição perfeita.
			- [ ] d. Explicar a relação entre custo marginal, receita marginal e preço para uma empresa que se encontra em um mercado perfeitamente competitivo e produz a quantidade que maximiza seus lucros.
			- [ ] e. Descrever as principais características dos monopólios, explicar os motivos para seu surgimento e identificar suas estratégias de preços.
			- [ ] f. Explicar a relação entre preço, receita marginal e custo marginal no monopólio.
			- [ ] g. Distinguir monopólio de competição perfeita e explicar por que o monopólio pode estabelecer preços mais altos.
			- [ ] h. Explicar por que o monopólio é considerado ineficiente.
			- [ ] i. Analisar questões relacionadas à regulamentação de um monopólio natural e explicar o papel da economia de escala nessa categoria de monopólio.
			- [ ] j. Descrever as características de concorrência monopolística e identificar a existência de lucro econômico (ou perda econômica) no curto prazo.
			- [ ] k. Avaliar se a competição monopolística é uma estrutura de mercado eficiente.
			- [ ] l. Descrever as características do oligopólio e de seus modelos tradicionais.
			- [ ] m. Entender e interpretar os modelos de oligopólio de Cournot-Nash e de Bertrand.
			- [ ] n. Entender e interpretar o modelo de firma dominante.
			- [ ] o. Entender e interpretar o modelo de curva de demanda quebrada.
			- [ ] p. Calcular e interpretar medidas de concentração da indústria (Índice Herfindahl-Hirschman e Índice de Concentração), bem como descrever seu uso e suas limitações.
			- [ ] q. Descrever e indicar o Equilíbrio de Nash e entender o conceito de “dilema do prisioneiro” em Teoria dos Jogos.
			- [ ] r. Definir e descrever monopsônio e oligopsônio.
	- [ ] 2.2 Macroeconomia
		- [ ] 2.2.1 Indicadores Econômicos
			- [ ] a. Definir, interpretar e diferenciar Produto Interno Bruto (PIB) de Produto Nacional Bruto (PNB).
			- [ ] b. Analisar os fatores que determinam a demanda por moeda, bem como os efeitos sobre tal demanda causados por alterações no PIB real e inovações financeiras.
			- [ ] c. Avaliar o impacto de uma mudança em cada um dos principais indicadores econômicos (inflação, emprego e renda) sobre os investimentos em títulos de renda fixa, ações e taxas de câmbio.
			- [ ] d. Analisar o impacto de diferentes indicadores econômicos sobre os rumos da política econômica.
			- [ ] e. Explicar como a taxa de juros é determinada, sua influência no equilíbrio de mercado e a interação entre mudanças nas taxas de juros e a oferta monetária.
			- [ ] f. Caracterizar os indicadores de taxas de juros no mercado nacional (Taxa Selic, TLP, TBF, TR) e avaliar os impactos nos reajustes de contratos financeiros.
			- [ ] g. Caracterizar a Taxa DI, seu uso, formação e a dinâmica do mercado interfinanceiro.
			- [ ] h. Definir e explicar a construção de índices de preço (IGP-M, IGP-DI, IGP-10, INPC e IPCA), bem como identificar e explicar problemas associados à utilização de tais índices
		- [ ] 2.2.2 Sistema Financeiro Nacional (SFN)
			- [ ] a. Explicar as principais atribuições dos órgãos e agentes reguladores: Conselho Monetário Nacional (CMN), Banco Central do Brasil, Comissão de Valores Mobiliários (CVM).
			- [ ] b. Comparar e contrastar as diferentes instituições financeiras, suas funções econômicas, seus impactos na regulamentação, desregulamentação e inovações dos mercados financeiros (bancos múltiplos, bancos de investimento, distribuidoras e corretoras de títulos e valores mobiliários, de câmbio e de futuros).
			- [ ] c. Explicar como os bancos criam moeda e calcular a quantia de empréstimos que um banco pode gerar, dado um certo valor de depósitos e taxa de depósito compulsório.
			- [ ] d. Analisar os objetivos do Banco Central e os resultados do Balanço de Pagamentos. Comparar e contrastar as ferramentas de política econômica, bem como seus potenciais riscos se utilizadas incorretamente.
			- [ ] e. Explicar as funções, a estrutura e o funcionamento e Sistema de Pagamentos Brasileiro (SPB), incluindo as câmaras de compensação/liquidação atuantes no mercado brasileiro (Clearing B3 e SELIC).
		- [ ] 2.2.3 Política Fiscal e Governo
			- [ ] a. Entender e determinar a necessidade de financiamento do setor público, bem como explicar como esta afeta a política fiscal e a dívida pública.
			- [ ] b. Analisar as fontes de recursos para investimentos e a influência da política fiscal nos mercados de capitais.
			- [ ] c. Descrever e interpretar a Curva de Laffer.
			- [ ] d. Descrever o fenômeno de crowding-out e seu efeito sobre as taxas de juros e o investimento privado em uma economia.
			- [ ] e. Analisar os efeitos intergeracionais da política fiscal e entender como as decisões tomadas em uma geração podem afetar as gerações futuras.
			- [ ] f. Comparar e contrastar os efeitos dos multiplicadores de gastos do governo, de impostos e de orçamento equilibrado.
			- [ ] g. Explicar como uma política fiscal discricionária pode ajudar na estabilização do ciclo de negócios.
"""
            )

def init_setup():
    pass


def main():
    init_setup()
    run_interface()


if __name__ == "__main__":
    main()

