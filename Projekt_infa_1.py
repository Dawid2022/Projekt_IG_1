import sys 
from math import sin, cos, sqrt, atan, degrees, radians, pi, tan
import numpy as np


class Transformacje:
    def __init__(self, model: str = "grs80"):
        """
        Parametry elipsoid:
            a - duża półoś elipsoidy - promień równikowy
            b - mała półoś elipsoidy - promień południkowy
            flat - spłaszczenie
            ecc2 - pierwszy mimośród^2
            eccp2 - drugi mimośród^2
        + WGS84: https://en.wikipedia.org/wiki/World_Geodetic_System#WGS84
        + Inne powierzchnie odniesienia: https://en.wikibooks.org/wiki/PROJ.4#Spheroid
        + Parametry planet: https://nssdc.gsfc.nasa.gov/planetary/factsheet/index.html
        """
        if model == "wgs84":
            self.a = 6378137.0 # semimajor_axis
            self.b = 6356752.31424518 # semiminor_axis
        elif model == "grs80":
            self.a = 6378137.0
            self.b = 6356752.31414036
        elif model == "krasowski":
            self.a = 6378245.000
            self.b = 6356863.018773
        else:
            print(f"elipsoida {model} nie została zaimplementowana")
            sys.exit()
            
        self.flat = (self.a - self.b) / self.a
        self.ecc = sqrt(2 * self.flat - self.flat ** 2) # first eccentricity  WGS84:0.0818191910428 
        self.ecc2 = (2 * self.flat - self.flat ** 2) # first eccentricity**2
        self.eccp = sqrt(self.ecc2 / (1 - self.ecc2)) # second eccentricity
        self.eccp2 = (self.ecc2 / (1 - self.ecc2)) # second eccentricity**2


    
    def xyz2plh(self, X, Y, Z, units = 'dec_degree'):
        """
        Algorytm Hirvonena - algorytm transformacji współrzędnych ortokartezjańskich (x, y, z)
        na współrzędne geodezyjne długość szerokość i wysokośc elipsoidalna (phi, lam, h). Jest to proces iteracyjny. 
        W wyniku 3-4-krotneej iteracji wyznaczenia wsp. phi można przeliczyć współrzędne z dokładnoscią ok 1 cm.     
        Parameters
        ----------
        X, Y, Z : FLOAT
             współrzędne w układzie orto-kartezjańskim, 

        Returns
        -------
        lat
            [stopnie dziesiętne] - szerokość geodezyjna
        lon
            [stopnie dziesiętne] - długośc geodezyjna.
        h : TYPE
            [metry] - wysokość elipsoidalna
        units [STR] - optional, defoulf 
            dec_degree - decimal degree
            dms - degree, minutes, sec
        """
        r   = sqrt(X**2 + Y**2)           # promień
        lat_prev = atan(Z / (r * (1 - self.ecc2)))    # pierwsze przybliilizenie
        lat = 0
        while abs(lat_prev - lat) > 0.000001/206265:    
            lat_prev = lat
            N = self.a / sqrt(1 - self.ecc2 * sin(lat_prev)**2)
            h = r / cos(lat_prev) - N
            lat = atan((Z/r) * (((1 - self.ecc2 * N/(N + h))**(-1))))
        lon = atan(Y/X)
        N = self.a / sqrt(1 - self.ecc2 * (sin(lat))**2);
        h = r / cos(lat) - N       
        
        if units == "dec_degree":
            return degrees(lat), degrees(lon), h 
        elif units == "dms":
            lat = self.deg2dms(lat)
            lon = self.deg2dms(lon)
            return f"{lat}", f"{lon}", f" {h:.3f}"
        else:
            print(f"{units} - nie ma takiego formatu jednostek")
            sys.exit()
            
    
    def plh2xyz(self, phi, lam, h,):
        """
        Odwrotny algorytm Hirvonena - algorytm transformacji współrzędnych geodezyjnych 
        długość szerokość i wysokość elipsoidalna(phi, lambda, h) na współrzędne ortokartezjańskie  (X, Y, Z).

        Parameters
        ----------
        phi, lam, h : FLOAT
            [dec_degree] współrzędne geodezyjne, 

        Returns
        -------
        X, Y, Z : FLOAT
            [metry] współrzędne ortokartezjańskie
        """ 
        
<<<<<<< HEAD
        
        
=======
        phi = radians(phi)
        lam = radians(lam)
>>>>>>> ea191935056e06688226811db3ac0da60d730ec5
        Rn = self.a/sqrt(1-self.ecc2*sin(phi)**2)
        q = Rn *self.ecc2 *sin(phi)
        X = (Rn + h)*cos(phi)*cos(lam)
        Y = (Rn + h)*cos(phi)*sin(lam)
        Z = (Rn + h)*sin(phi)-q

        return X,Y,Z


    def xyz2neu(self, X, Y, Z, X_0, Y_0, Z_0):
        """
        Macierz R w transformacji współrzędnych XYZ na NEU jest macierzą rotacji, która pozwala przeliczyć 
        współrzędne z układu kartezjańskiego na współrzędne związanego z Ziemią układu współrzędnych geodezyjnych NEU.
        Wykorzystujemy bibliotekę numpy.
        
        Parameters
        ----------
        phi, lam: FLOAT
            [dec_degree] współrzędne phi, lambda w układzie geodezyjnym, 
       
        Returns
        -------
        R : array
            [niemianowane] macierz rotacji
        """
       
        phi, lam, h = [radians(float(coord)) for coord in self.xyz2plh(X,Y,Z)]
                       
        R = np.array([[-sin(lam), -sin(phi)*cos(lam), cos(phi)*cos(lam)],
                     [  cos(lam), -sin(phi)*sin(lam), cos(phi)*sin(lam)],
                     [         0,            cos(phi),        sin(phi)]])
        """
        Transformacja XYZ -> NEU - algorytm transformacji współrzędnych wektora pomiędzy dwoma punktami w układzie współrzędnych 
        ortokartezjańskich (X, Y, Z) na współrzędne wektora pomiędzy dwoma punktami w układzie NEU: North, East, Up (N, E, U). 
        Wykorzystujemy bibliotekę numpy.


        Parameters
        ----------
        X, Y, Z : FLOAT
            [metry] współrzędne w układzie orto-kartezjańskim, 
        
        X_0, Y_0, Z_0 : FLOAT
            [metry] współrzędne punktu referencyjnego w układzie orto-kartezjańskim, 

        Returns
        -------
        N, E, U : FLOAT
            [metry] współrzędne w układzie NEU
        """                                        
                                              
        XYZ_t= np.array([[X -X_0],
                          [Y -Y_0],
                          [Z -Z_0]])
        
        [[E], [N], [U]] = R.T @ XYZ_t
    
        return N, E, U



    def pl92(self,phi,lam):
        """
        Transformacja phi,lam -> PL-1992 - algorytm transformacji współrzędnych elipsoidalnych (phi, lam)
        na współrzędne płaskie w układzie odniesienia PL-1992 (x1992, y1992). Najpierw są obliczane współrzędne 
        x i y w układzie Gaussa-Krügera, które obliczane są na podstawie złożonych równań uwzględniających różne 
        czynniki związane z kątem phi i lam. Ostatecznie współrzędne te są cechowane do układu PL-1992. 
        Parameters
        ----------
        phi, lam : FLOAT
            [dec_degree] współrzędne geodezyjne,

        Returns
        -------
        x1992, y1992 : FLOAT
            [metry] współrzędne płaskie w układzie PL-1992
        """
        phi = radians(phi)
        lam = radians(lam)
        
        lam0 = np.radians(19)
        N = self.a / sqrt(1 - self.ecc2 * sin(phi)**2)
        
        A0 = 1 - self.ecc2/4 - (3*self.ecc2**2) /64 - (5*self.ecc2**3) /256
        A2 = 3/8 * (self.ecc2 + (self.ecc2**2) /4 + (15*self.ecc2**3) /128)
        A4 = 15/256 * (self.ecc2**2 + (3*self.ecc2**3) /4)
        A6 = (35*self.ecc2**3) /3072
        sigma = self.a*(A0*phi - A2*sin(2*phi) + A4*sin(4*phi) - A6*sin(6*phi))    

        dlam = lam - lam0
        t = tan(phi)
        eta2 = self.eccp2 * (cos(phi)**2)
        
        xGK = sigma + ((dlam**2 * N*sin(phi)*cos(phi))/2) * (1 + ((dlam**2 /12) * cos(phi)**2) * (5 - t**2 + 9*eta2 + 4*eta2**2)
                + ((dlam**4/360) * (cos(phi)**4)) * (61 - 58*t**2 + t**4 + 270*eta2 - 330*eta2*t**2))
        yGK = (dlam*N*cos(phi)) * (1 + ((dlam**2 /6) * cos(phi)**2) * (1 - t**2 + eta2) 
                + ((dlam**4 /120) * cos(phi)**4) * (5 - 18*t**2 + t**4 + 14*eta2 - 58*eta2*t**2))
        
        x1992 = xGK * 0.9993 - 5300000
        y1992 = yGK * 0.9993 + 500000
        
        return x1992,y1992



    def pl2000(self,phi,lam):
        """
        Transformacja phi,lam -> PL-2000 - to algorytm transformacji współrzędnych elipsoidalnych (phi, lam)
        na współrzędne płaskie w układzie odniesienia PL-2000 (x2000, y2000). Najpierw jest okreslana strefa (5, 6, 7 lub 8) 
        oraz południk odwzorowaczy. Kolejno są obliczane współrzędne x i y w układzie Gaussa-Krügera, które wyznaczane 
        są na podstawie złożonych równań uwzględniających różne czynniki związane z kątem phi i lam. Ostatecznie 
        współrzędne te są cechowane do układu PL-2000. 

        Parameters
        ----------
        phi,lam : FLOAT
            [dec_degree] współrzędne geodezyjne, 

        Returns
        -------
        x2000, y2000 : FLOAT
            [metry] współrzędne płaskie w układzie PL-2000
        """        
        phi = radians(phi)
        lam = radians(lam)
        
        
        if lam <= (11*pi)/120:
            numer = 5
            lam0 = np.radians(15)
        elif lam <= (13*pi)/120 and lam > (11*pi)/120:
            numer = 6
            lam0 = np.radians(18)
        elif lam <= (15*pi)/120 and lam > (13*pi)/120:
            numer = 7
            lam0 = np.radians(21)
        elif lam > (15*pi)/120:
            numer = 8
            lam0 = np.radians(24)
        
        N = self.a / sqrt(1 - self.ecc2 * sin(phi)**2)
        A0 = 1 - self.ecc2/4 - (3*self.ecc2**2) /64 - (5*self.ecc2**3) /256
        A2 = 3/8 * (self.ecc2 + (self.ecc2**2) /4 + (15*self.ecc2**3) /128)
        A4 = 15/256 * (self.ecc2**2 + (3*self.ecc2**3) /4)
        A6 = (35*self.ecc2**3) /3072
        sigma = self.a*(A0*phi - A2*sin(2*phi) + A4*sin(4*phi) - A6*sin(6*phi))    
        
        dlam = lam - lam0
        t = tan(phi)
        eta2 = self.eccp2 * (cos(phi)**2)
        
        xGK = sigma + ((dlam**2 * N*sin(phi)*cos(phi))/2) * (1 + ((dlam**2 /12) * cos(phi)**2) * (5 - t**2 + 9*eta2 + 4*eta2**2)
                + ((dlam**4/360) * (cos(phi)**4)) * (61 - 58*t**2 + t**4 + 270*eta2 - 330*eta2*t**2))
        yGK = (dlam*N*cos(phi)) * (1 + ((dlam**2 /6) * cos(phi)**2) * (1 - t**2 + eta2) 
                + ((dlam**4 /120) * cos(phi)**4) * (5 - 18*t**2 + t**4 + 14*eta2 - 58*eta2*t**2))
        
        x2000 = xGK * 0.999923
        y2000 = yGK * 0.999923 + numer*1000000 + 500000
    
        return x2000,y2000

            

    def deg2dms(self, data):
        
        x = abs(data)
        x = x * 180 / pi
        d = int(x)
        m = int(60 * (x - d))
        s = (x - d - m/60) * 3600
        d = int(data * 180 / pi)
        
        if m<10:
            m = f'0{m:1d}'
        else:
            m = f'{m:2d}'
        
        if s<10:
            s = f'0{s:2.5f}'
        else:
            s = f'{s:2.5f}'
        
        return(f'{d:3d}:{m}:{s}')
        
        




if __name__ == "__main__":

    geo = Transformacje(model = "grs80")
    header_lines = 1
    sys_line = [sys.argv[0]]
    
    for i in sys.argv[1:-1]:
        i = i.lower()
        sys_line.append(i)
    sys_line.append(sys.argv[-1])
    
    input_file_path = sys.argv[-1]
    immutable_flags = ['--header_lines','--model']
    units = 'dec_degree'
    
    
    I = []
    for i in sys_line:
        if i.startswith('--') and i not in immutable_flags:
            I.append(i)

    if len(I) > 1:
        print('Możesz podać tylko jedną flagę!!!')
        sys.exit()

    if '--header_lines' in sys_line:
        try:
            idx = sys_line.index('--header_lines')+1
            header_lines = abs(int(sys_line[idx]))
        except ValueError:
            print(f'{sys_line[idx]} nie jest liczbą całkowitą.')
            sys.exit()
            
    if '--model' in sys_line:
        
        model = sys_line[sys_line.index('--model')+1]
        geo = Transformacje(model)
        

    try:
        
        if '--xyz2plh' in sys_line:
            
            with open(input_file_path,'r') as f:
                dane = f.readlines()
                dane = dane[header_lines:]

                
                plh = []
                for d in dane:
                
                    d = d.strip()
                    x,y,z = d.split(',')
                    x,y,z = (float(x),float(y),float(z))
                    p,l,h = geo.xyz2plh(x,y,z,units)
                    plh.append([p,l,h])
                
            with open('wyniki_xyz2plh.txt','w') as f:
                f.write('phi[deg], lam[deg], h[m] \n')
                for coords in plh:
                    coords_plh_line = ','.join([str(coord) for coord in coords])
                    f.write(coords_plh_line + '\n')
            
        
        elif '--plh2xyz' in sys_line:
        
            with open(input_file_path,'r') as f:
                dane = f.readlines()
                dane = dane[header_lines:]
                
                xyz = []
                for d in dane:
                
                    d = d.strip()
                    phi_str,lam_str,h_str = d.split(',')
                    phi,lam,h = (float(phi_str),float(lam_str),float(h_str))
                    x,y,z = geo.plh2xyz(phi,lam,h,)
                    xyz.append([x,y,z])
                
            with open('wyniki_plh2xyz.txt','w') as f:
                f.write('X[m], Y[m], Z[m] \n')
                for coords in xyz:
                    coords_xyz_line = ','.join([f'{coord:.3f}' for coord in coords])
                    f.write(coords_xyz_line + '\n')
    
    
        elif '--xyz2neu' in sys_line:

            with open(input_file_path,'r') as f:
                 lines = f.readlines()
                 lines = lines[header_lines:]
                 
                 coords_neu = []
                 for line in lines:
                     line = line.strip()
                     x, y, z = line.split(',')
                     x, y, z = (float(x), float(y), float(z))
                     try:
                         x_0, y_0, z_0 = [float(coord) for coord in sys_line[sys_line.index('--xyz2neu')+1:-1]]
                     
                     except ValueError:
                         try:
                             
                             for coord in sys_line[sys_line.index('--xyz2neu')+1:-1]:
    
                                 coord = coord.strip()
                                 x_0, y_0, z_0 = coord.split(',')
                                 x_0, y_0, z_0 = (float(x_0), float(y_0), float(z_0))
                             
                         except ValueError:
                             print('Błędnie podałes współrzędne.')
                             sys.exit()
                  
                     n, e, u = geo.xyz2neu(x, y, z, x_0, y_0, z_0)
                     coords_neu.append([n, e, u])
                
            with open('wyniki_xyz2neu.txt','w') as f:
                 f.write('n[m], e[m], u[m] \n')
                 for coords in coords_neu:
                     coords_neu_line = ','.join([f'{coord:.3f}' for coord in coords])
                     f.write(coords_neu_line + '\n')  
    
        
        elif '--pl2000' in sys_line:
            
            with open(input_file_path,'r') as f:
                dane = f.readlines()
                dane = dane[header_lines:]
                
                xy = []
                for d in dane:
                    
                    d = d.strip()
                    phi_str,lam_str,_ = d.split(',')
                    phi,lam = (float(phi_str),float(lam_str))
                    x,y = geo.pl2000(phi,lam)
                    xy.append([x,y])
                
            with open('wyniki_pl2000.txt','w') as f:
                f.write('x2000[m], y2000[m] \n')
                for coords in xy:
                    coords_xy_line = ','.join([f'{coord:.3f}' for coord in coords])
                    f.write(coords_xy_line + '\n')
    
                    
        elif '--pl1992' in sys_line:
            
            with open(input_file_path,'r') as f:
                dane = f.readlines()
                dane = dane[header_lines:]
            
                xy = []
                for d in dane:
                    
                    d = d.strip()
                    phi_str,lam_str,_ = d.split(',')
                    phi,lam = (float(phi_str),float(lam_str))
                    x,y = geo.pl92(phi,lam)
                    xy.append([x,y])
                
            with open('wyniki_pl1992.txt','w') as f:
                f.write('x1992[m], y1992[m] \n')
                for coords in xy:
                    coords_xy_line = ','.join([f'{coord:.3f}' for coord in coords])
                    f.write(coords_xy_line + '\n')
    
    except UnicodeDecodeError:
        print('Plik {sys_line[-1]} ma inne rozszerzenie niż txt. Podaj prawidłowy plik.')
        sys.exit()
    except FileNotFoundError:
        print(f'Brak podanego pliku. {sys_line[-1]} nieznajduje się w folderze.')
        sys.exit()

