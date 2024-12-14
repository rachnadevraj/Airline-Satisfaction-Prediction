import streamlit as st
import pandas as pd
import numpy as np
from joblib import load

airlinemodel = load('airline.pkl')
#print ("loaded carsmodel")

def predict_satisfaction(Gender, 
                        Customer_Type,
                        Age, 
                        Type_of_Travel,
                        Class, 
                        Flight_Distance,
                        Inflight_wifi_service,
                        Departure_Arrival_time_convenient,
                        Ease_of_Online_booking,
                        Gate_location,
                        Food_and_drink,
                        Online_boarding,
                        Seat_comfort,
                        Inflight_entertainment,
                        On_board_service,
                        Leg_room_service,
                        Baggage_handling,
                        Checkin_service,
                        Inflight_service,
                        Cleanliness,
                        Departure_Delay_in_Minutes,
                        Arrival_Delay_in_Minutes):

  #  inputs_dict = {'KM_Driven' : float(kmDriven), 
  #                 'Fuel_Type': fuelType, 
  #                 'Age': float(age), 
  #                 'Transmission': transmission, 
  #                 'Owner_Type': ownerType, 
  #                 'Model': model.lower()}
inputs_dict = {'Gender' : gender,
               'Customer_Type' : customertype,
               'Age': float(age),
               'Type_of_Travel': traveltype,
               'Class': classtype,
               'Flight_Distance': int(distance),
               'Inflight_wifi_service': wifiservice,
               'Departure_Arrival_time_convenient': convenient,
               'Ease_of_Online_booking': easebooking,
               'Gate_location': gatelocation,
               'Food_and_drink': fooddrink,
               'Online_boarding': onlineboarding,
               'Seat_comfort': seatcomfort,
               'Inflight_entertainment': infltent,
               'On_board_service': onboardservice,
               'Leg_room_service': legroomservice,
               'Baggage_handling': baggagehandling,
               'Checkin_service': checkinservice,
               'Inflight_service': inflightservice,
               'Cleanliness': cleanliness,
               'Departure_Delay_in_Minutes': int(depduration),
               'Arrival_Delay_in_Minutes': int(arrduration)}
    
df = pd.DataFrame(inputs_dict,index=[0])

satisfaction = airlinemodel.predict(df)[0]
    return satisfaction 

 
#function to define the app_layout
def app_layout():
    
    st.title('Airline Satisfaction Prediction')
    st.header('Enter customer experience detail:')  
    
    ## Creating the user input fields 

    gender = st.selectbox('Gender:',
                          ['Male', 'Female'])

    customertype = st.selectbox('Customer Type:',
                                ['disloyal Customer', 'Loyal Customer'])

    age = st.number_input('Age:', 
                          min_value=1,
                          max_value=150, 
                          value=0)
    
    traveltype = st.selectbox('Type of Travel:',
                              ['Personal Travel', 'Business Travel'])

    classtype = st.selectbox('Class Type:',
                             ['Eco', 'Eco Plus', 'Business'])


    distance = st.number_input('Distance:',
                               min_value = 50,
                               max_value = 5000,
                               value = 50)

    wifiservice = st.selectbox('Wifi Service:',
                               ['0','1','2','3','4','5'])

    convenient = st.selectbox('Departure & Arrival Time Convenience:',
                               ['0','1','2','3','4','5'])

    easebooking = st.selectbox('Ease of Online Booking:',
                               ['0','1','2','3','4','5'])

    gatelocation = st.selectbox('Gate Location:',
                               ['0','1','2','3','4','5'])

    fooddrink = st.selectbox('Food & Drink:',
                               ['0','1','2','3','4','5'])

    onlineboarding = st.selectbox('Online Boarding:',
                               ['0','1','2','3','4','5'])

    seatcomfort = st.selectbox('Seat Comfort:',
                               ['0','1','2','3','4','5'])

    infltent = st.selectbox('Inflight Entertainment:',
                               ['0','1','2','3','4','5'])

    onboardservice = st.selectbox('Onboard Service:',
                               ['0','1','2','3','4','5'])

    legroomservice = st.selectbox('Legroom:',
                               ['0','1','2','3','4','5'])

    baggagehandling = st.selectbox('Baggage Handling:',
                               ['0','1','2','3','4','5'])

    checkinservice = st.selectbox('Checkin Service:',
                               ['0','1','2','3','4','5'])

    inflightservice = st.selectbox('Inflight Service:',
                               ['0','1','2','3','4','5'])

    cleanliness = st.selectbox('Cleanliness:',
                               ['0','1','2','3','4','5'])

    depduration = st.number_input('Delay of Deparature:',
                                  min_value=0,
                                  max_value=2000,
                                  value=0)

    arrduration = st.number_input('Delay of Arrival:',
                                  min_value=0,
                                  max_value=2000,
                                  value=0)
    
    if st.button('Predict Satisfaction'):
        satisfaction = predict_satisfaction(gender, 
                                            customertype, 
                                            age, 
                                            traveltype, 
                                            classtype, 
                                            distance,
                                            wifiservice,
                                            convenient,
                                            easebooking,
                                            gatelocation,
                                            fooddrink,
                                            onlineboarding,
                                            seatcomfort,
                                            infltent,
                                            onboardservice,
                                            legroomservice,
                                            baggagehandling,
                                            checkinservice,
                                            inflightservice,
                                            cleanliness,
                                            depduration,
                                            arrduration)
        st.success(f'Explected Customer Satisfaction is : {np.round(satisfaction, 2)}')
 
if __name__=='__main__':
  app_layout()
