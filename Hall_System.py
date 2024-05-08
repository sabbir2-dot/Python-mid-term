"""
Mid exam project: Ticket Booking System by Sabbir

"""

class Star_Cinema:
    _hall_list = []

    @classmethod
    def entry_hall(cls, hall):
        cls._hall_list.append(hall)


class Hall(Star_Cinema):  
    def __init__(self, rows, cols, hall_no):
        super().__init__()  
        self._seats = {}  
        self._show_list = []  
        self._rows = rows
        self._cols = cols
        self._hall_no = hall_no

        for row in range(1, rows + 1):
            for col in range(1, cols + 1):
                seat_name = f"{row}-{col}"
                self._seats[seat_name] = None

        self._allocate_seats()

        Star_Cinema.entry_hall(self)

    def _allocate_seats(self):
        self._seats = {self._hall_no: [['free' for _ in range(self._cols)] for _ in range(self._rows)]}

    def entry_show(self, id, movie_name, time):
        show_info = (id, movie_name, time)
        self._show_list.append(show_info)

    def book_seats(self, show_id, seats):
        for show_info in self._show_list:
            if show_info[0] == show_id:
                for seat in seats:
                    row, col = seat
                    if 0 < row <= self._rows and 0 < col <= self._cols:
                        if self._seats[self._hall_no][row - 1][col - 1] == 'free':
                            self._seats[self._hall_no][row - 1][col - 1] = 'booked'
                            print(f'Your {seat} is booked now! Thanks')
                        else:
                            print(f"Seat {seat} is already booked.")
                    else:
                        print(f"Seat {seat} is invalid for this hall.")
                return
        print(f"Show with id {show_id} not found.")

    def Show_list(self):
        for show in self._show_list:
            print(f'ID: {show[0]}, Movie Name: {show[1]}, Time: {show[2]}')

    def view_available_seats(self, show_id):
        for show_info in self._show_list:
            if show_info[0] == show_id:
                print(f"Available seats for Show ID {show_id}:")
                for row_idx, row in enumerate(self._seats[self._hall_no], start=1):
                    for col_idx, seat_status in enumerate(row, start=1):
                        if seat_status == 'free':
                            print(f"{row_idx}, {col_idx}")
                return
        print(f"Show with ID {show_id} not found.")



hall = Hall(rows=5, cols=10, hall_no=1)


hall.entry_show(id='123', movie_name='Movie A', time='10:00 AM')

hall.book_seats(show_id='123', seats=[(1, 1), (2, 3), (3, 5)])

# hall.Show_list()

# hall.view_available_seats('123')

while True:
        print("\nOptions:")
        print("1. View all shows today")
        print("2. View available seats")
        print("3. Book Ticket")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            hall.Show_list()
        elif choice == '2':
            show_id = input("Enter the show ID: ")
            hall.view_available_seats((show_id))
        elif choice == '3':
            show_id = input("Enter the show ID: ")
            row_col_input = input("Enter row and column numbers with space: ")
            row, col = map(int, row_col_input.split())
            hall.book_seats(int(show_id), [(row, col)])
        elif choice == '4':
            break
        else:
            print("Invalid choice! try again.")
