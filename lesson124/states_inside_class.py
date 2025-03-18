# Maintaining state inside the class
class Camera:
    def __init__(self, name, recording=False):
        self.name = name
        self.recording = recording

    def record(self):
        if self.recording:
            print(f'{self.name} is ALREADY recording...')
            return

        print(f'{self.name} is recording...')
        self.recording = True

    def stop_recording(self):
        if not self.recording:
            print(f'{self.name} is NOT recording...')
            return

        print(f'{self.name} is stopping the recording...')
        self.recording = False

    def take_photo(self):
        if self.recording:
            print(f'{self.name} cannot take a photo while recording')
            return

        print(f'{self.name} is taking a photo...')


c1 = Camera('Canon')
c2 = Camera('Sony')

c1.record()
c1.record()
c1.take_photo()
c1.stop_recording()
c1.take_photo()

print()

c2.stop_recording()
c2.record()
c2.record()
c2.take_photo()
c2.stop_recording()
c2.take_photo()
