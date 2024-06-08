import streamlit as st

st.markdown(
    """<style>.block-container{max-width: 86rem !important;}</style>""",
    unsafe_allow_html=True,
)


def run_interface():

    st.write("---")

    # with open("texts/home_intro.md", "r") as file:
    #     intro = file.read()
    #
    # st.markdown(intro)

    st.markdown(
"""
## MÉTODOS QUANTITATIVOS 

	- [ ] 1.1 Valor do Dinheiro no Tempo
		- [ ] a. Interpretar taxas de juros como taxas de retorno ou de desconto e entender sua relação com o conceito de custo de oportunidade.
		- [ ] b. Calcular taxas anuais efetivas de juros, dada uma frequência de capitalização semestral, trimestral, mensal, diária ou contínua.
		- [ ] c. Calcular e interpretar o valor presente e o valor futuro de um único fluxo de caixa, de uma anuidade e de uma perpetuidade (apenas valor presente), bem como de uma série de fluxos de caixa irregulares.
	- [ ] 1.2 Conceitos Básicos de Estatística
		- [ ] a. Calcular e interpretar medidas de tendência central de uma amostra ou população: média, mediana e moda.
		- [ ] b. Calcular e interpretar quantis (quartis, quintis, decis e percentis).
		- [ ] c. Calcular e interpretar medidas de dispersão de uma amostra ou população: variância e desvio-padrão.
		- [ ] d. Calcular e interpretar a covariância e o coeficiente de correlação entre duas variáveis.
		- [ ] e. Entender e interpretar as propriedades de um conjunto de dados apresentados sob forma gráfica.
	- [ ] 1.3 Conceitos Básicos de Probabilidade
		- [ ] a. Definir e calcular o valor esperado de uma variável aleatória e do retorno de uma carteira de investimentos.
		- [ ] b. Calcular e interpretar a variância e o desvio-padrão de uma variável aleatória e do retorno de uma carteira de investimentos.
		- [ ] c. Entender, definir e distinguir entre variáveis aleatórias discretas e contínuas.
		- [ ] d. Definir uma distribuição de probabilidade.
		- [ ] e. Entender e distinguir as distribuições de probabilidade uniforme, binomial, normal e lognormal.
		- [ ] f. Definir uma distribuição normal padrão, bem como calcular e interpretar probabilidades utilizando tal distribuição.
		- [ ] g. Entender e explicar a utilização da distribuição lognormal na modelagem de preços de ativos.
	- [ ] 1.4 Amostragem, Estimação e Testes de Hipótese
		- [ ] a. Distinguir entre população e amostra e definir amostragem aleatória.
		- [ ] b. Calcular a variância e o erro-padrão da média amostral.
		- [ ] c. Definir e distinguir entre estimativa por ponto e por intervalo de confiança.
		- [ ] d. Calcular e interpretar o intervalo de confiança da média populacional, dada uma distribuição normal.
		- [ ] e. Entender e explicar a formulação de um teste de hipóteses.
		- [ ] f. Entender e formular a hipótese nula e a hipótese alternativa de um teste de hipóteses.
		- [ ] g. Definir e diferenciar os erros tipo I e tipo II, bem como entender e interpretar o nível de significância de um teste de hipóteses.
		- [ ] h. Distinguir entre testes de hipóteses unicaudais ou bicaudais.
	- [ ] 1.5 Regressão Linear e Múltipla
		- [ ] a. Entender e interpretar um modelo de regressão simples e múltipla.
		- [ ] b. Definir e entender variável dependente, variável independente, intercepto, termo aleatório e coeficiente de determinação (R2).
		- [ ] c. Dado um modelo de regressão e o valor da variável independente, calcular o valor estimado de uma variável dependente, assim como calcular e interpretar um intervalo de confiança para este valor.
		- [ ] d. Analisar um teste t para um coeficiente de regressão e calcular seu nível de significância.
		- [ ] e. Interpretar o coeficiente de regressão e calcular intervalos de confiança para essa estatística.
		- [ ] f. Formular hipóteses nulas e alternativas sobre o valor de um coeficiente de regressão de uma população, determinar qual o teste estatístico apropriado e se a hipótese nula será rejeitada a determinado intervalo de confiança.
		- [ ] g. Interpretar os resultados de uma regressão.
		- [ ] h. Explicar o uso de análise de variância (ANOVA) na análise de regressão e interpretar seus resultados.
		- [ ] i. Analisar as limitações de análise de regressão.
"""
            )

def init_setup():
    pass


def main():
    init_setup()
    run_interface()


if __name__ == "__main__":
    main()

