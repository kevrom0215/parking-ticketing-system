class vehicle():
    def __init__(self, plate_no, vehicle_type, paid,time_in, time_out=None) -> None:
        self.plate_no = plate_no
        self.time_in = time_in
        self.time_out = time_out
        self.vehicle_type = vehicle_type
        self.paid = paid
