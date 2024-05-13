1. Opis działania programu:
 
   TRANSFORMER jest programem służącym do transformacji współrzędnych między układami na elipsoidach odniesienia. Program umożliwia przeliczenie współrzędnych w układach: plh->xyz, xyz->plh, pl->PL1992, pl->PL2000, xyz->neu. Program 
   obsługuje 3 elipsoidy odniesienia: GRS80, WGS84 oraz elipsoide Krasowskiego.
   
   Program korzysta z:
   
   - python w wersji 3.11
     
   - bibliotek:
     
   -numpy
   
   -math
   
   Obsługiwane systemy:
   
   - Windows
     
3. Korzystanie z programu:
  
   Do działania programu konieczne jest utworzenie pliku ze współrzędnymi z rozszerzeniem txt. W pliku ze współrzędnymi muszą znajdować się współrzędne oddzielone przecinkiem, każdy kolejny punkt musi znajdować się w nowym 
   wierszu. W przypadku współrzędnych kartezjański. Format:"X,Y,Z" Wartości powinny być podawane w metrach, separator dziesiętny - kropka. W przypadku współrzędnych geodezyjnych. Format: "phi,lam,h" Wartości "phi" i 
   "lam" powinny być podawane w stopniach dziesiętnych, wartości "h" w metrach separator dziesiętny - kropka.

   W celu wywołania programu konieczne jest uruchomienie wiersza poleceń w lokalizacji, w której znajduje się program.
   
   Wywoływanie funkcji:
   
   W celu wywołania funkcji należy użyć komendy:
   >     python Projekt_infa_1.py nazwa_flagi nazwa_pliku.txt
  
   Jeśli użytkownik chce:
   
   - użyć konkretnej elipsoidy to komenda wygląda następująco:
     
     
   >     python Projekt_infa_1.py --model nazwa_elipsoidy --nazwa_flagi nazwa_pliku.txt
   
  
   - podać numer wiersz na którym kończy się nagłówek w pliku tekstowym:
     
     
   >     python Projekt_infa_1.py --header_lines liczba_wierszy  --nazwa_flagi nazwa_pliku.txt

   
   Powyższe flagi można używać naprzemienie i jednocześnie:
   
   >     python Projekt_infa_1.py --model nazwa_elipsoidy --header_lines liczba_wierszy --nazwa_flagi nazwa_pliku.txt
  
   Obsługiwane elipsoidy:
 
   -GRS80
 
   -WGS84
 
   -Krasowski

   Gdy użytkownik nie wybierze żadnej elipsoidy to domyślnie będzie model grs80.

   Domyślnie długość nagłówka w pliku.txt jest jeden.

    Nazwy obsługiwanych funkcji:

    - xyz2plh (przelicza współrzędne X, Y, Z na współrzędne phi, lam, h)

    - plh2xyz (przelicza współrzędne phi, lam, h na współrzędne X, Y, Z)

    - pl2000 (przelicza współrzędne phi, lam do układu PL2000)

    - pl92 (przelicza współrzędne phi, lam do układu PL1992)

    - neu (przelicza współrzędne geocentryczne odbiornika do współrzędnych topocentrycznych n, e, u na podstawie współrzędnych x,y,z odbiornika i satelitów)

    Przykładowe formaty plików.txt wraz z opisem kolejnych kolumn dla poszczególnych funckji:

- xyz2plh:
	- Współrzędna X punktu wyrażona w metrach
	- Współrzędna Y punktu wyrażona w metrach
	- Współrzędna Z punktu wyrażona w metrach		

	Przykładowy plik ze współrzędnymi:

    >	  3664940.500,1409153.590,5009571.170    
    >	  3664940.510,1409153.580,5009571.167

- plh2xyz:
	- Współrzędna phi punktu wyrażona w stopniach
	- Współrzędna lam punktu wyrażona w stopniach
	- Współrzędna h punktu wyrażona w metrach		

	Przykładowy plik ze współrzędnymi:

    >     52.09727222,21.03153333,141.399
    >     52.09727216,21.03153314,141.400
   
- pl2000:
	- Współrzędna phi punktu wyrażona w stopniach
	- Współrzędna lam punktu wyrażona w stopniach
   	- Wysokość punktu wyrażona w metrach
			

	Przykładowy plik ze współrzędnymi:
     >		52.09727222,21.03153333,141.399
     >		52.09727216,21.03153314,141.400 
   
- pl1992:
	- Współrzędna phi punktu wyrażona w stopniach
	- Współrzędna lam punktu wyrażona w stopniach
   	- Wysokość punktu wyrażona w metrach
			

	Przykładowy plik ze współrzędnymi:   
   >		52.09727222,21.03153333,141.399
   >		52.09727216,21.03153314,141.400      
   
- neu: 
	- Współrzędna X odbiornika wyrażona w metrach
	- Współrzędna Y odbiornika wyrażona w metrach
	- Współrzędna Z odbiornika wyrażona w metrach
   
         Przykładowy plik ze współrzędnymi:

   >	 3664940.500,1409153.590,5009571.170    
   >	 3664940.510,1409153.580,5009571.167

     Przykładowe wywołania fukcji wraz z przykładowym wyglądem pliku wynikowego współrzędnych po transformacji:

- xyz2plh:

   >		python Projekt_infa_1.py --model grs80 --header_lines 4 --xyz2plh wsp_inp.txt

     Wygląd pliku ze współrzędnymi po transformacji, gdzie w kolejnych kolumnach znajdują się:
   
	- Współrzędna phi punktu wyrażona w stopniach,
   
	- Współrzędna lam punktu wyrażona w stopniach,
   
	- Współrzędna h punktu wyrażona w metrach
 
     

   >     52.09727222,21.03153333,141.399
   >     52.09727216,21.03153314,141.400


 - plh2xyz:

   >		python Projekt_infa_1.py --model grs80 --header_lines 1 --plh2xyz wyniki_xyz2plh.txt

				
   Wygląd pliku ze współrzędnymi po transformacji, gdzie w kolejnych kolumnach oddzielonych spacjami znajdują się:
   
   
     - Współrzędna X punktu wyrażona w metrach,
    
  
     - Współrzędna Y punktu wyrażona w metrach,
    
  
     - Współrzędna Z punktu wyrażona w metrach

   
	

   >	 3664940.500,1409153.590,5009571.170
   >	 3664940.510,1409153.580,5009571.167 


 - pl2000:

   >		python Projekt_infa_1.py --model grs80 --header_lines 1 --pl2000 wyniki_xyz2plh.txt

				
    Wygląd pliku ze współrzędnymi po transformacji, gdzie w kolejnych kolumnach znajdują się:
   

      - Współrzędna X punktu w układzie 2000 wyrażona w metrach,
   
 
      - Współrzędna Y punktu w układzie 2000 wyrażona w metrach

    
 
   >		 5773722.721,7502160.783
   >		 5773722.714,7502160.770

 - pl1992:

   >		python Projekt_infa_1.py --model grs80 --header_lines 1 --pl1992 wyniki_xyz2plh.txt

				
    Wygląd pliku ze współrzędnymi po transformacji, gdzie w kolejnych kolumnach znajdują się:
   

      - Współrzędna X punktu w układzie 1992 wyrażona w metrach,
   
 
      - Współrzędna Y punktu w układzie 1992 wyrażona w metrach

    
 
   >		 472071.341,639114.491
   >		 472071.334,639114.478

- neu

   >		python Projekt_infa_1.py --model grs80 --header_lines 1 --xyz2neu 3664940.500 1409153.590 5009571.170 wsp_inp.txt


   lub


   >		python Projekt_infa_1.py --model grs80 --header_lines 1 --xyz2neu 3664940.500,1409153.590,5009571.170 wsp_inp.txt
		
        
  Wygląd pliku ze współrzędnymi po transformacji, gdzie w kolejnych kolumnach znajdują się:
  
     
    - Współrzędna N punktu wyrażona w metrach,
    
       
    - Współrzędna E punktu wyrażona w metrach,
    
       
    - Współrzędna U punktu wyrażona w metrach
    
 
   

   >   		0.000,    0.000,  0.000
   > 		-0.006,  -0.013,  0.001 

3. Znane błędy, które nie zostały naprawione:
   
   Transformacja Krasowski na Pl2000 i na Pl1992 nie powinna być używana ponieważ jest to elipsoida lokalna a nie globalna i podaje błędne wyniki.
