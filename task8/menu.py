import data_bace
import view
import phone_book as pb

def choise_menu(choise):
    match choise:
        case 1:
            view.print_phone_book()
        case 2:
            data_bace.load_contact()
        case 3:
            data_bace.save_contact()
        case 4:
            pb.add_contact()
        case 5:
            pb.replase_contact()
        case 6:
            pb.remove_contact()
        case 7:
            pb.search_contact()
        case 0:
            return True
        
while True:
    choise = view.main_menu()
    if choise_menu(choise):
        break

