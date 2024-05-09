1. Opis działania programu:
 
    TRANSFORMER jest programem służącym do transformacji współrzędnych między układami na elipsoidach odniesienia. Program umożliwia przeliczenie współrzędnych w układach: plh->xyz, xyz->plh, pl->PL1992, pl->PL2000, xyz->neu. Program obsługuje 3 elipsoidy odniesienia: GRS80, WGS84 oraz elipsoide Krasowskiego.
Program korzysta z:
- python w wersji 3.11
- bibliotek:
   -numpy
   -math
Obsługiwane systemy:
- Windows
2. Korzystanie z programu:
  
  Do działania programu konieczne jest utworzenie pliku ze współrzędnymi z rozszerzeniem txt. W      pliku ze współrzędnymi muszą znajdować się współrzędne oddzielone przecinkiem, każdy kolejny       punkt musi znajdować się w nowym wierszu. W przypadku współrzędnych kartezjański. Format:          "X;Y;Z" Wartości powinny być podawane w METRACH, separator dziesiętny - KROPKA. W przypadku        współrzędnych geodezyjnych. Format: "phi;lam;h" Wartości "phi" i "lam" powinny być podawane w      STOPNIACH DZIESIĘTNYCH, wartości "h" w METRACH separator dziesiętny - KROPKA.

  W celu wywołania programu konieczne jest uruchomienie wiersza poleceń w lokalizacji, w której      znajduje się program.
  Wywoływanie funkcji:
  W celu wywołania funkcji należy użyć komendy:
  >     python Projekt_infa_1.py nazwa_elipsoidy nazwa_funkcji nazwa_pliku.txt


 Obsługiwane elipsoidy:
 
 -GRS80
 
 -WGS84
 
 -Krasowski
 

 Nazwy obsługiwanych funkcji:

- plh2xyz (przelicza współrzędne phi, lam, h na współrzędne X, Y, Z)

- xyz2plh (przelicza współrzędne X, Y, Z na współrzędne phi, lam, h)

- pl92 (przelicza współrzędne phi, lam do układu PL1992)

- pl2000 (przelicza współrzędne phi, lam do układu PL2000)

- neu (przelicza współrzędne geocentryczne odbiornika do współrzędnych topocentrycznych n, e, u na podstawie współrzędnych x,y,z odbiornika i satelitów)

Przykładowe formaty plików txt wraz z opisem kolejnych kolumn dla poszczególnych funckji:
- plh2xyz:
	- Współrzędna phi punktu wyrażona w stopniach
	- Współrzędna lam punktu wyrażona w stopniach
	- Współrzędna h punktu wyrażona w metrach		

	Przykładowy plik ze współrzędnymi:

  >     3664940.5000000005,1409153.59,5009571.169999973
  >     3664940.51,1409153.58,5009571.166999972

- xyz2plh:
	- Współrzędna X punktu wyrażona w metrach
	- Współrzędna Y punktu wyrażona w metrach
	- Współrzędna Z punktu wyrażona w metrach		

	Przykładowy plik ze współrzędnymi:

   >	 3664940.500,1409153.590,5009571.170    
   >	 3664940.510,1409153.580,5009571.167
   
- neu: 
	- Współrzędna X odbiornika wyrażona w metrach
	- Współrzędna Y odbiornika wyrażona w metrach
	- Współrzędna Z odbiornika wyrażona w metrach
   
         Przykładowy plik ze współrzędnymi:

   >	 3664940.500,1409153.590,5009571.170    
   >	 3664940.510,1409153.580,5009571.167

  Przykładowe wywołania fukcji wraz z przykładowym wyglądem pliku wynikowego współrzędnych po transformacji:

  -plh2xyz:

   >		python Projekt_infa_1.py --plh2xyz wyniki_xyz2plh.txt 
				
Wygląd pliku ze współrzędnymi po transformacji, gdzie w kolejnych kolumnach oddzielonych spacjami znajdują się:
	- Współrzędna X punktu wyrażona w metrach,
	- Współrzędna Y punktu wyrażona w metrach,
	- Współrzędna Z punktu wyrażona w metrach
 
Przykładowy plik ze współrzędnymi:
	

   >	 3664940.500,1409153.590,5009571.170    
   >	 3664940.510,1409153.580,5009571.167

- xyz2plh:

   >		python Projekt_infa_1.py --xyz2plh wsp_inp.txt
				
Wygląd pliku ze współrzędnymi po transformacji, gdzie w kolejnych kolumnach znajdują się:
	- Współrzędna Fi punktu wyrażona w stopniach,
	- Współrzędna Lambda punktu wyrażona w stopniach,
	- Współrzędna h punktu wyrażona w metrach
 
Przykładowy plik ze współrzędnymi:

  >     3664940.5000000005,1409153.59,5009571.169999973
  >     3664940.51,1409153.58,5009571.166999972

-neu

   >		python Projekt_infa_1.py --xyz2neu 3664940.500 1409153.590 5009571.170  wsp_inp.txt
				
Wygląd pliku ze współrzędnymi po transformacji, gdzie w kolejnych kolumnach znajdują się:
	- Współrzędna N punktu wyrażona w metrach,
	- Współrzędna E punktu wyrażona w metrach,
	- Współrzędna U punktu wyrażona w metrach
 
 	

Przykładowy plik ze współrzędnymi:

   >   		0.000,      0.000,      0.000       
   > 		-0.006,     -0.013,      0.001
