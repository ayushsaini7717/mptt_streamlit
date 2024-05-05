import streamlit as s1
import pandas as pd
import numpy as np
import time
from PIL import Image
import plotly.graph_objects as px
# s1.markdown("""
#             <div class="hide">I am shown when someone hovers over the div above.</div>
            
#             """,unsafe_allow_html=True)
with open("main.css") as p:
    s1.markdown(f"<style>{p.read()}</style>",unsafe_allow_html=True)

choose=s1.sidebar.selectbox("Maximum Power Transfer Theorem",["Aim","Theory","Pretest","Simulation","Feedback"])
if(choose=="Aim"):
    s1.title(":black[To Study and Verify Maximum Power Transfer Theorem]")
    s1.divider()
    s1.write("To obtain maximum external power from a power source with internal resistance, the resistance of the load must equal the resistance of the source from its output terminals.")
elif(choose=="Pretest"):
    total_correct=0
    s1.title(":blue[To Study and Verify Maximum Power Transfer Theorem]")
    s1.divider()
    s1.write("1--The maximum power is delivered from a source to its load when the load resistance is ______ the source resistance.")
    s1.write("a) greater than")
    s1.write("b) less than")
    s1.write("c) equal to")
    s1.write("d) less than or equal to")
    p1,p11=s1.columns([1,3])
    with p1:
        ans1=s1.selectbox("Options are:",("None","a","b","c","d"),key=1)
    
    if(ans1=='c'):
        total_correct+=1
        s1.success("Correct answer...")
    elif(ans1=="None"):
        s1.write("Choose the correct option")
    else:
        s1.error("Incorrect answer...")
    s1.divider()
    s1.write("2--Maximum power transfer takes place at an efficiency of")
    s1.write("a) 25%")
    s1.write("b) 50%")
    s1.write("c) 75%")
    s1.write("d) 100%")
    p2,p22=s1.columns([1,3])
    with p2:
        ans2=s1.selectbox("Options are:",("None","a","b","c","d"),key=2)
    if(ans2=="b"):
        total_correct+=1
        s1.success("Correct answer...")
    elif(ans2=="None"):
        s1.write("choose the correct option")
    else:
        s1.error("Incorrect answer...")
    s1.divider()
    s1.write("3--The maximum power transfer theorem is used in")
    s1.write("a) electronic circuits")
    s1.write("b) power system")
    s1.write("c) home lighting system")
    s1.write("d) None of these")
    p3,p33=s1.columns([1,3])
    with p3:
        ans3=s1.selectbox("Options are:",("None","a","b","c","d"),key=3)
    if(ans3=="a"):
        total_correct+=1
        s1.success("Correct answer...")
    elif(ans3=="None"):
        s1.write("choose the correct option")
    else:
        s1.error("Incorrect answer...")
    s1.divider()
    s1.write("4--The Maximum Power Transfer Theorem is based on the concept of ____________________?")
    s1.write("a) voltage division")
    s1.write("b) current division")
    s1.write("c) superposition")
    s1.write("d) ohm's law")
    p4,p44=s1.columns([1,3])
    with p4:
        ans4=s1.selectbox("Options are:",("None","a","b","c","d"),key=4)
    if(ans4=="d"):
        total_correct+=1
        s1.success("Correct option...")
    elif(ans4=="None"):
        s1.write("choose the correct option")
    else:
        s1.error("Incorrect answer...")
    s1.divider()
    s1.write("5--Which alternative theorem is often preferred over the Maximum Power Transfer Theorem in practical circuit design?")
    s1.write("a) Norton's Theorem")
    s1.write("b) Thevenin's Theorem")
    s1.write("c) Superposition Theorem")
    s1.write("d) Mesh Current Analysis")
    p5,p55=s1.columns([1,3])
    with p5:
        ans5=s1.selectbox("Options are:",("None","a","b","c","d"),key=5)
    if(ans5=="b"):
        total_correct+=1
        s1.success("Correct answer...")
    elif(ans5=="None"):
        s1.write("choose the correct option")
    else:
        s1.error("Incorrect answer...")
    s1.divider()
    s1.divider()
    if(total_correct>=3):
        #s1.balloons()
        s1.write("You give ",total_correct," correct answer")
elif(choose=="Theory"):
    s1.title("Maximum power transfer theorem")
    s1.header(":violet[Introduction:-]")
    s1.write("According to Maximum power transfer theorem the condition for maximum power flow through load resistor can be achieved when the load resistor is equal to thevenin's equivalent resistor of circuit.")
    #s1.subheader(":violet[Proof:-]")
    image=Image.open("mptt.png")
    s1.image(image)
    s1.write("The Maximum Power Transfer Theorem aims to figure out the value RL, such that it consumes maximum power from the source.")
    s1.latex(r'''I=\left(\frac{V_{Th}}{R_{Th} + R_{L}}\right)''')
    s1.write("Power through load resistor")
    s1.latex(r'''P=I_{L}^2 R_{L}''')
    s1.write("P_{L} can be maximized by adjusting RL, therefore highest power can be generated when(dPL/dRL) =0")
    s1.latex(r'''\frac{dP_{L}}{dR_{L}} = \left[\frac{1}{(R_{Th} + R{L})^2}\right]^2\left[\left(R_{Th} + R{L}\right)^2\frac{d}{d R_{L}}\left(V_{Th}^2 R_{L}\right) - V_{Th}^2 R_{L}\frac{d}{d R_L}\left(R_{Th} + R_{L}\right)^2\right]''')
    s1.latex(r'''= \frac{1}{\left(R_{Th} + R_{L}\right)^4\left[\left(R_{Th} + R_{L}\right)^2 V_{Th}^2 - V_{Th}^2 R_{L} * 2\left(R_{Th} + R_{L}\right)\right]}''')
    s1.latex(r'''= \frac{V_{Th}\left(R_{Th} + R_{L} - 2R_{L}\right)}{\left(R_{Th} + R_{L}\right)^3} = \frac{V_{Th}^2\left(R_{Th} - R_{L}\right)}{\left(R_{Th} + R{L}\right)}''')
    s1.write("For Power to be Maximum")
    s1.latex(r'''\frac{dP_{L}}{dR_{L}} = 0''')
    s1.latex(r'''\frac{V_{Th}^2\left(R_{Th} - R_{L}\right)}{\left(R_{Th} + R_{L}\right)} = 0''')
    s1.latex(r'''\left(R_{Th} - R_{L}\right) = 0''')
    s1.latex(r'''R_{Th} = R_{L}''')
    s1.write("So, the highest power transmitted to the load resistance is: ")
    s1.latex(r'''P_{max} = \frac{V_{Th}^2}{4R_{Th}}''')
    s1.subheader(":violet[Efficiency:-]")
    s1.write("Since the total power generated by the source is PL+PS, the wasted internal power PS should be small compared to PL for efficient operation. Formally, we define the power-transfer efficiency as")
    s1.latex(r'''Efficiency=\frac{P_{L}}{P_{L}+P_{S}}''')
    s1.write("Which is often expressed as a percentage. If the load has been matched for maximum power transfer, then PS=PL, and so efficiency,")
    s1.latex(r'''Efficiency=\frac{P_{L}}{2P_{L}}''')
    s1.write("**Efficiency=50%**")
    s1.subheader(":violet[Advantages]")
    s1.write("* The main benefit of the maximum power transfer theorem is, it can analyze the performance at any point")
    s1.write("* It is applicable to ac and dc network.")
    s1.subheader(":violet[Disadvantages]")
    s1.write("* This is not applicable for nonlinear and unilateral networks.")
    s1.write("* The limitation of the maximum power transfer theorem is it not applicable in power systems, due to its 50% efficiency. So the main concern of this is efficiency.")
    s1.write("* Due to less efficiency, this cannot be accepted within power lines.")
    s1.subheader(":violet[Applications]")
    s1.write("* It’s used in solar cell applications, adjusting the electrical load on the cell to obtain maximum output power.")
    s1.write("* It also helps in making a circuit having maximum power dissipation correctly at the load of resistance.")
elif(choose=="Simulation"):
    s1.title("**Maximum Power Transfer Theorem**")
    with s1.sidebar:
        with s1.expander("**Instructions**"):
            s1.write("1. Enter the value of R1,R2,R3 and Voltage")
            s1.write("2. Enter the different values of load resistor")
            s1.write("3. Click on add button to show load resistor and power in table")
            s1.write("4. Click on plot button to plot the graph")
            s1.write("5. To reset the page, press reset button")
            s1.divider()
            s1.subheader("formulae")
            s1.latex(r'''R_{Th} = \frac{R1*R3}{R1+R3} + R2''')
            s1.latex(r'''V_{Th}=R3\left[\frac{V}{R1+R3}\right]''')
            s1.latex(r'''P=\left(\frac{V_{Th}}{R_{Th}+R_{L}}\right)^2*R_{L}''')
            
    if s1.session_state.get('clear'):
        s1.session_state['100']=1.0
        s1.session_state['101']=1.0
        s1.session_state['102']=1.0
        s1.session_state['103']=1.0
        s1.session_state['999']=1
        s1.session_state['12']=1
        
       
    #s1.divider()
    co1,co2=s1.columns(2)
    if "input1" not in s1.session_state:
        s1.session_state.input1=False
    def callback_input1():
        s1.session_state.input1=True
    
    if "input2" not in s1.session_state:
        s1.session_state.input2=False
    def callback_input2():
        s1.session_state.input2=True
    if "input3" not in s1.session_state:
        s1.session_state.input3=False
    def callback_input3():
        s1.session_state.input3=True
    if "input4" not in s1.session_state:
        s1.session_state.input4=False
    def callback_input4():
        s1.session_state.input4=True
    with s1.sidebar:
        r1=s1.number_input("Enter the value of R1: ",min_value=1.0,max_value=None,step=1.0,key=100,on_change=callback_input1)#max value of resistor is 500 mega ohm

    with s1.sidebar:
        r2=s1.number_input("Enter the value of R2: ",min_value=1.0,max_value=500000000.0,step=1.0,key=101,disabled=not s1.session_state.input1,on_change=callback_input2)
    with s1.sidebar:
        r3=s1.number_input("Enter the value of R3: ",min_value=1.0,max_value=500000000.0,step=1.0,key=102,disabled=not s1.session_state.input2,on_change=callback_input3)
    with s1.sidebar:
        v=s1.number_input("Enter the value of Voltage: ",min_value=1.0,max_value=282.0,step=1.0,key=103,disabled=not s1.session_state.input3,on_change=callback_input4) #max voltage in dc ckt is 282v
    
    #s1.divider()
    # col1,col2,col3,col4=s1.columns(4)
    # with col1:
    #     s1.write("R1 is:  ",r1)
    # with col2:
    #     s1.write("R2 is:  ",r2)
    # with col3:
    #     s1.write("R3 is:  ",r3)
    # with col4:
    #     s1.write("V is:  ",v)
    
    # with s1.sidebar:
    #     ninput=s1.number_input("Enter the number of different value of load resistor",min_value=1,max_value=100,step=1,key=999)
    # rl=list()
    if "slide" not in s1.session_state:
        s1.session_state.slide=False

    if "count" not in s1.session_state:
        s1.session_state.count=list()

    def callback_1():
        s1.session_state.slide=True
    if "input5" not in s1.session_state:
        s1.session_state.input5=False
    def callback_input5():
        s1.session_state.input5=not s1.session_state.input5
    with s1.sidebar:
        s=s1.slider("Enter the different values of Load Resistor",1,100,1,on_change=callback_1,key=12,disabled=not s1.session_state.input4)
        if s1.session_state.slide:
            s1.session_state.count.append(s)
    
    power=list()
    # with s1.sidebar:
    #     for i in range(0,ninput):
    #         rl.append(s1.slider("Enter the value of load resistor: ",0,100,0,key=i))
    rth=((r1*r3)/(r1+r3))+r2
    vth=r3*(v/(r1+r3))
    rth=round(rth,2)
    vth=round(vth,2)
    p1=list()
    rl=list()
    if s1.session_state.input4:
        rl=5
        rl=s1.session_state.count
    ninput=len(rl)
    for i in range(0,ninput):
        p1.append(pow(vth/(rth+rl[i]),2))
    for i in range(0,ninput):
        pw=p1[i]*rl[i]
        power.append(pw)
        
    
    
    
    c1,c2=s1.columns(2)
    
    
    plot=px.Figure(data=[px.Scatter(
        x=rl,
        y=power,
        mode="lines+markers",
        marker=dict(
            color='LightSkyBlue',
            size=12,
            line=dict(
                color='MediumPurple',
                width=2
            )
        ),
    )])
    plot.update_layout(
        title={
            'text' : 'Power V/s Load resistor',
            'x':0.5,
            'xanchor': 'center',
        },
        titlefont=dict(size=20),
        xaxis_title='Load resistor',
        yaxis_title='Power',
        hovermode="y unified",
        plot_bgcolor='#D3D3D3',
        showlegend=True,
        xaxis=dict(
        showgrid=True,
        
    )
    )
    plot.update_layout(shapes=[px.layout.Shape(
    type='rect',
    xref='paper',
    yref='paper',
    x0=-0.07,
    y0=-0.1,
    x1=1.06,
    y1=1.1,
    line={'width': 1, 'color': 'black'}
)])
    if "button_clicked" not in s1.session_state:
        s1.session_state.button_clicked=False
        
    def callback():
        s1.session_state.button_clicked=not s1.session_state.button_clicked
    
    # if "reset" not in s1.session_state:
    #     s1.session_state.reset=False
    # def callback_reset():
    #     s1.session_state.reset=not s1.session_state.reset
    with co1:
        image=Image.open("mxp.png")
        s1.image(image)
        col1,col2,col3=s1.columns(3)
        with col1:
            rset=s1.button('**Reset**',key='clear')
            if rset:
                rl.clear()
                s1.session_state.button_clicked=not s1.session_state.button_clicked
                s1.session_state.slide=not s1.session_state.slide
                # s1.session_state.input1=False
                # s1.session_state.input2=False
                # s1.session_state.input3=False
                # s1.session_state.input4=False
                #rl=[]
            with s1.container():
                s1.write("Rth is: ",rth)
        
        with col2:
            table=s1.button("**Add**",on_click=callback,disabled=not s1.session_state.slide)
            if table:
                rl.pop(ninput-1)
            with s1.container():
                s1.write("Vth is: ",vth)
        with col3:
            plot_button=s1.button("**Plot**",disabled=not s1.session_state.button_clicked)
            if plot_button:
                rl.pop(ninput-1)
        #if s1.session_state.input5:
        
        
        with co2:
            if s1.session_state.button_clicked:
                with s1.spinner("Please wait..."):
                    df=pd.DataFrame(list(zip(rl,power)),columns =['Load resistor(Rl) in ', 'Power(P) in Watt'])
                    df.index = np.arange(1, len(df) + 1)  #to start index from 1
                    if s1.session_state.button_clicked:
                        #time.sleep(2)
                        s1.table(df)
        if plot_button:
            s1.plotly_chart(plot)
    #s1.write(rl)
    
        
                
    #slider in graph

#     plot.update_layout(
#     xaxis=dict(
#         rangeselector=dict(
#             buttons=list([
#                 dict(
#                     count=1,
#                 )
#             ])
            
#             ),
#         rangeslider=dict(
#                 visible=True
#         )
#     )
# )
    
else:
    s1.write("Your opinion is valuable to us.Your feedback will help us make it better for you and other users. ")
    feedback=s1.text_input("Give your Feedback")
    if feedback:
        s1.success("Thanks for your time")
    
    