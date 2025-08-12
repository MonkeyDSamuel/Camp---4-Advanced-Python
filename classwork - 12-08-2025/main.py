#from lib.menu

from models.RBI import RBI
from models.SBI import SBI
from models.UBI import UBI

if __name__ == '__main__':
    sbi = SBI()
    print(sbi.mudra_loan)
    print(sbi.display_rate_of_interest())

    ubi = UBI()
    print(ubi.display_rate_of_interest())