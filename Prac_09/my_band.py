"""Band example with list of musicians."""
from band import Band
from musician import Musician
from guitar import Guitar


def main():
    band = Band("Extreme")
    nuno = Musician("Nuno Bettencourt")
    nuno.add(Guitar("Washburn N4", 1990, 2499.95))
    nuno.add(Guitar("Takamine acoustic", 1986, 1200.0))
    band.add(nuno)
    band.add(Musician("Gary Cherone"))
    pat = Musician("Pat Badger")
    pat.add(Guitar("Mouradian CS-74 Bass", 2009, 1500.0))
    band.add(pat)
    kevin = Musician("Kevin Figueiredo")
    band.add(kevin)

    print("band (str)")
    print(band)
    print("band.play()")
    print(band.play())
    """
    Output: 
    band (str)
    Extreme (Nuno Bettencourt ([Washburn N4 (1990) : $2,499.95, Takamine acoustic (1986) : $1,200.00]), Gary Cherone ([]), Pat Badger ([Mouradian CS-74 Bass (2009) : $1,500.00]), Kevin Figueiredo ([]))
    band.play()
    Nuno Bettencourt is playing: Washburn N4 (1990) : $2,499.95
    Gary Cherone needs an instrument!
    Pat Badger is playing: Mouradian CS-74 Bass (2009) : $1,500.00
    Kevin Figueiredo needs an instrument!
    """


main()