import streamlit as st
from math import sqrt
from PIL import Image
img1 = Image.open('cat.jpeg')
#from PIL import Image
#image = Image.open('me.png')
#st.set_page_config(page_title='tradingideas',page_icon=image)

#hide_menu_style = """
#        <style>
#        #MainMenu {visibility: hidden; }
#        footer {visibility: hidden;}
#        </style>
#        """
#st.markdown(hide_menu_style, unsafe_allow_html=True)

############## function sections ##########################################
@st.cache(allow_output_mutation=True)
def fib(n:int):
    '''
    @Fibonacci numbers solving in O(n) with Binet formula
    @n: input integer
    '''
    if n < 2:
        return n
    else:
       #Binet's formula
       first_term = pow((1+sqrt(5)),n)
       second_term = pow((1-sqrt(5)),n)
       f = (first_term - second_term)/(pow(2,n)*sqrt(5))
       return int(f) 
######################################################################
def main():
    st.title("FibMe")
    

    input = st.text_input("Write a number")
    if st.button("Submit"):
        
        output = fib(int(input))
        out = (str(output))
        st.success("Tadaaa")
        st.header(out)

        #butt = st.checkbox("Show me the trick!")
        #if (butt):
        st.image(img1,caption="Awwwww",width=None)
        st.balloons()

if __name__== "__main__":
    main()
