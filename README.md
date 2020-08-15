# Final-Version
Our projects aim is to reduce the trafic accidents and the deaths caused by it. 
Our code detects cars around a truck by using an camera footage and alarms the user if there is a car that is too close. By this we try to cover up the blind spots of the long 
trucks and reduce the car accidents that caused by recless drivers. We use opticalFlow and Tensorflow for different angles of cameras. We choose Tensorflow to detect cars infront 
of the truck and the opticalFlow for the sides. We made this choise intentionally because the efficeny we got from different sides with different algorithms were significantly 
different. Bause the camera for the sides were from fish angle Tensorflow had problems with the wierd shaped cars but beczuse opticalFlow only detects the shifting pixels in two 
different frame it detecting well. But for the front the background changes were to much and for opticalFlow everything was moving so we choose to use Tensorflow. 
We also choose QTPy5 for creating the interface for the application.

You can see our working progress in wiki:
http://www.cs.binghamton.edu/~steflik/wiki/index.php/Vehware_Truck_Camera_--_Sinem_OZDEN,_Ozan_SAYILIR,_Selin_Dinc,
