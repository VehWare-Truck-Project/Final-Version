# Senior Project Final Version - VehWare Truck Project

Team : Sinem Ozden - Selin Dinc - Ozan Emre Sayilir

Our project's aim is to reduce the trafic accidents and the deaths caused by it. 

Our code detects cars around a truck by using a camera footage and alarms the user if there is a car that is too close. By this way we try to cover up the blind spots of the long trucks and reduce the car accidents that caused by reckless drivers.

We use opticalFlow and Tensorflow for different angles of cameras. We chose Tensorflow to detect cars infront of the truck and the opticalFlow for the sides. We made this choice intentionally because the efficeny we got from different sides with different algorithms were significantly 
different. 

Because the camera for the sides were from fish angle Tensorflow had problems with the weird shaped cars but beacuse opticalFlow only detects the shifting pixels in two different frame it detecting well. But for the front the background changes were too much and for opticalFlow everything was moving. Thus, we chose to use Tensorflow. 

We also used PyQt5 to create the interface for the application.

You can see our working progress in our wiki:
http://www.cs.binghamton.edu/~steflik/wiki/index.php/Vehware_Truck_Camera_--_Sinem_OZDEN,_Ozan_SAYILIR,_Selin_Dinc,
