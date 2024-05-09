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
