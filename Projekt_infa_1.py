import sys 
from math import sin, cos, sqrt, atan, atan2, degrees, radians, pi
import numpy as np

o = object()

class Transformacje:
    def __init__(self, model: str = "wgs84"):
        """
        Parametry elipsoid:
            a - duża półoś elipsoidy - promień równikowy
            b - mała półoś elipsoidy - promień południkowy
            flat - spłaszczenie
            ecc2 - mimośród^2
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
        elif model == "mars":
            self.a = 3396900.0
            self.b = 3376097.80585952
        else:
            raise NotImplementedError(f"{model} model not implemented")
        self.flat = (self.a - self.b) / self.a
        self.ecc = sqrt(2 * self.flat - self.flat ** 2) # eccentricity  WGS84:0.0818191910428 
        self.ecc2 = (2 * self.flat - self.flat ** 2) # eccentricity**2


    
    def xyz2plh(self, X, Y, Z, output = 'dec_degree'):
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
        output [STR] - optional, defoulf 
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
        if output == "dec_degree":
            return degrees(lat), degrees(lon), h 
        elif output == "dms":
            lat = self.deg2dms(degrees(lat))
            lon = self.deg2dms(degrees(lon))
            return f"{lat[0]:02d}:{lat[1]:02d}:{lat[2]:.2f}", f"{lon[0]:02d}:{lon[1]:02d}:{lon[2]:.2f}", f"{h:.3f}"
        else:
            raise NotImplementedError(f"{output} - output format not defined")
            
    def plh2xyz(self, phi, lam, h):
        phi = radians(phi)
        lam = radians(lam)
        
        Rn = self.a/sqrt(1-self.ecc2*sin(phi)**2)
        q = Rn *self.ecc2 *sin(phi)
        x = (Rn + h)*cos(phi)*cos(lam)
        y = (Rn + h)*cos(phi)*sin(lam)
        z = (Rn + h)*sin(phi)-q
        return x,y,z
    
    
    def lambda0_l(lam):
        
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
            
        return(lam0,numer)
    
    def sigma(self, phi):
        
        A0 = 1 - self.ecc2/4 - (3*self.ecc2**2) /64 - (5*self.ecc2**3) /256
        A2 = 3/8 * (self.ecc2 + (self.ecc2**2) /4 + (15*self.ecc2**3) /128)
        A4 = 15/256 * (self.ecc2**2 + (3*self.ecc2**3) /4)
        A6 = (35*self.ecc2**3) /3072
        
        sigma = self.a*(A0*phi - A2*sin(2*phi) + A4*sin(4*phi) - A6*sin(6*phi))    
        
        return(sigma)
    
    
    def Np(self, phi):
        
        N = self.a / sqrt(1 - self.ecc2 * sin(phi)**2)
        
        return(N)


    def f1(self,xGK): #!!!
        
        A0 = 1 - self.ecc2/4 - (3*self.ecc2**2) /64 - (5*self.ecc2**3) /256
        fj = xGK/(self.a*A0)
        
        while True:
            
            fi = fj
            sig = self.sigma(phi)
            
            fj = fi + (xGK - sig)/(self.a*A0)
            
            if np.abs(fj - fi) <(0.000001 / 206265):
                break
        
        return(fj)



if __name__ == "__main__":
    # utworzenie obiektu
    geo = Transformacje(model = "wgs84")
    print("To jest argv: ", sys.argv)
    # dane XYZ geocentryczne
    # X = 3664940.500; Y = 1409153.590; Z = 5009571.170
    # phi, lam, h = geo.xyz2plh(X, Y, Z)
    # print(phi, lam, h)
    # phi, lam, h = geo.xyz2plh2(X, Y, Z)
    # print(phi, lam, h)
    


    input_file_path = sys.argv
    
    if '--xyz2plh' in sys.argv and '--plh2xyz' in sys.argv:
        print('możesz podać tylko jedną flagę')
    elif '--xyz2plh' in sys.argv:
        
    
        with open(input_file_path[2],'r') as f:
            dane = f.readlines()
            dane = dane[4:]
            
            
            plh = []
            for d in dane:
            
                d = d.strip()
                x,y,z = d.split(',')
                x,y,z = (float(x),float(y),float(z))
                p,l,h = geo.xyz2plh(x,y,z)
                plh.append([p,l,h])
            
        with open('wyniki_xyz2plh.txt','w') as f:
            f.write('phi[deg], lam[deg], h[m] \n')
            for coords in plh:
                coords_plh_line = ','.join([str(coord) for coord in coords])
                f.write(coords_plh_line + '\n')
        
    
    elif '--plh2xyz' in sys.argv:
    
        with open(input_file_path[2],'r') as f:
            dane = f.readlines()
            dane = dane[1:]
            
            
            xyz = []
            for d in dane:
            
                d = d.strip()
                phi_str,lam_str,h_str = d.split(',')
                phi,lam,h = (float(phi_str),float(lam_str),float(h_str))
                x,y,z = geo.plh2xyz(phi,lam,h)
                xyz.append([x,y,z])
            
        with open('wyniki_plh2xyz.txt','w') as f:
            f.write('X[m], Y[m], Z[m] \n')
            for coords in xyz:
                coords_xyz_line = ','.join([str(coord) for coord in coords])
                f.write(coords_xyz_line + '\n')